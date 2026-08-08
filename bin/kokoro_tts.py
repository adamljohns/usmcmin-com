#!/usr/bin/env python3
"""kokoro_tts.py — narrate one text chunk with Kokoro via mlx-audio.

Called by bin/render_explainer.js. Kokoro is the house voice engine (am_onyx
narrates 38 of the site's audio books), so explainer videos use it rather than
Piper — the narration should sound like the rest of usmcmin.org.

Model load is the expensive part, so this reads a JSON job list on stdin and
renders every chunk in one process.
  stdin : {"voice":"am_onyx","lang":"a","jobs":[{"text":"...","out":"/x.wav"}]}
"""
import sys, os, glob, json, tempfile, shutil
from mlx_audio.tts.generate import generate_audio
from mlx_audio.tts.utils import load_model

def main():
    spec = json.load(sys.stdin)
    voice = spec.get("voice", "am_onyx")
    lang = spec.get("lang", "a")
    model = load_model("mlx-community/Kokoro-82M-bf16")
    done = 0
    for j in spec["jobs"]:
        with tempfile.TemporaryDirectory(prefix="kok-") as tmp:
            generate_audio(text=j["text"], model=model, voice=voice,
                           lang_code=lang, output_path=tmp, file_prefix="seg",
                           join_audio=True, audio_format="wav", verbose=False)
            w = sorted(glob.glob(os.path.join(tmp, "*.wav")))
            if not w:
                print(json.dumps({"error": "no wav", "out": j["out"]}), file=sys.stderr)
                continue
            shutil.move(w[0], j["out"])
            done += 1
    print(json.dumps({"rendered": done}))

if __name__ == "__main__":
    main()
