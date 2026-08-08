#!/usr/bin/env node
/**
 * render_explainer.js — turn a slide plan into a U.S.M.C. branded MP4.
 *
 * Reads the JSON plan emitted by bin/make-explainer-video.py --emit-plan,
 * renders each frame to PNG with Playwright, narrates each with Piper, and
 * muxes them with ffmpeg so every slide is held exactly as long as its own
 * narration. Brand cards get a fixed hold since they have no narration.
 *
 * Everything runs on this Mac — no cloud, no NotebookLM.
 *
 * Usage: node bin/render_explainer.js /tmp/plan.json /tmp/out.mp4
 */
const { chromium } = require('/Users/moop_bot_pro/Scripts/cdp-tmc/node_modules/playwright-core');
const { execFileSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const PIPER = path.join(os.homedir(), '.piper-venv/bin/piper');
const VOICES = path.join(os.homedir(), '.piper-voices');
const CARD_HOLD = 3.0;   // seconds a brand card stays up
const W = 1920, H = 1080;

async function main() {
  const [planPath, outPath] = process.argv.slice(2);
  if (!planPath || !outPath) { console.error('usage: render_explainer.js <plan.json> <out.mp4>'); process.exit(2); }
  const plan = JSON.parse(fs.readFileSync(planPath, 'utf8'));
  const model = path.join(VOICES, `${plan.voice}.onnx`);
  if (!fs.existsSync(model)) { console.error('voice missing:', model); process.exit(1); }

  const work = fs.mkdtempSync(path.join(os.tmpdir(), 'explainer-'));
  const b = await chromium.launch({ headless: true });
  const page = await b.newPage({ viewport: { width: W, height: H } });

  const segments = [];
  for (const s of plan.slides) {
    const i = String(s.index).padStart(3, '0');
    const png = path.join(work, `f${i}.png`);
    await page.setContent(s.html, { waitUntil: 'load' });
    await page.screenshot({ path: png });

    let dur = CARD_HOLD;
    let wav = null;
    if (s.narration && s.narration.trim()) {
      wav = path.join(work, `f${i}.wav`);
      execFileSync(PIPER, ['-m', model, '-f', wav], { input: s.narration, stdio: ['pipe','ignore','ignore'] });
      dur = Number(execFileSync('ffprobe',
        ['-v','error','-show_entries','format=duration','-of','csv=p=0', wav],
        { encoding: 'utf8' }).trim()) + 0.45;   // a beat of silence after each slide
    }
    segments.push({ png, wav, dur });
    process.stdout.write(`  frame ${s.index + 1}/${plan.slides.length}  ${dur.toFixed(1)}s\r`);
  }
  await b.close();
  console.log('\nrendered', segments.length, 'frames');

  // Per-segment MP4s, then concat. Simpler and far more robust than one giant
  // filtergraph, and a failure localises to a single slide.
  const parts = [];
  segments.forEach((s, n) => {
    const part = path.join(work, `p${String(n).padStart(3,'0')}.mp4`);
    const args = ['-y','-loop','1','-framerate','30','-i', s.png];
    if (s.wav) args.push('-i', s.wav);
    else args.push('-f','lavfi','-i','anullsrc=r=24000:cl=mono');
    args.push('-c:v','libx264','-pix_fmt','yuv420p','-r','30',
              '-c:a','aac','-b:a','128k','-ar','24000','-ac','1',
              '-t', s.dur.toFixed(3), '-shortest', part);
    execFileSync('ffmpeg', args, { stdio: 'ignore' });
    parts.push(part);
  });

  const list = path.join(work, 'list.txt');
  fs.writeFileSync(list, parts.map(p => `file '${p}'`).join('\n'));
  execFileSync('ffmpeg', ['-y','-f','concat','-safe','0','-i', list, '-c','copy', outPath], { stdio: 'ignore' });

  const total = segments.reduce((a, s) => a + s.dur, 0);
  const kb = Math.round(fs.statSync(outPath).size / 1024);
  console.log(`wrote ${outPath}  (${Math.floor(total/60)}m ${Math.round(total%60)}s, ${kb} KB)`);
  fs.rmSync(work, { recursive: true, force: true });
}
main().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
