/**
 * Bow & Arrow Studio LLC — House-Rules Acknowledgment Endpoint
 * ==============================================================
 *
 * Deployed as a Google Apps Script web app on bowandarrowstudiollc@gmail.com.
 * Receives signed house-rules acknowledgments from /house-rules.html, appends
 * an audit row to a Google Sheet, generates a PDF with the embedded signature,
 * and emails the PDF to both the guest and Adam.
 *
 * Architecture: TIER-LOW (per CLAUDE_CODE_HANDOFF_booking-site.md §6.3).
 * Compliance:  ESIGN Act (15 U.S.C. § 7001) + Va. UETA (Va. Code § 59.1-479
 *              et seq.) consent flag captured + retained.
 *
 *
 * DEPLOYMENT — Adam does this (Claude Code wrote the code; Apps Script
 * deployment is an account-bound action and stays in your hands):
 *
 *   1. Create the audit Google Sheet first
 *      ─────────────────────────────────────
 *      a. https://sheets.google.com → New Sheet
 *      b. Name it "Bow & Arrow — House Rules Acknowledgments — Audit Log"
 *      c. From the URL bar copy the long ID between /d/ and /edit:
 *         https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit
 *         You'll paste it in step 4 as AUDIT_SHEET_ID.
 *      d. Sheet should be PRIVATE — do NOT share with anyone. The web app
 *         (running as you) writes into it; you read it directly when you
 *         want to audit.
 *
 *   2. Create the Apps Script project
 *      ──────────────────────────────
 *      a. https://script.google.com → New project
 *      b. Name it "Bow & Arrow — House Rules Signature Endpoint"
 *      c. Delete the default Code.gs contents and paste this entire file
 *      d. Save (Ctrl/Cmd-S)
 *
 *   3. Set Script Properties (where the SHEET_ID and HOST_EMAIL live —
 *      not committed to git for safety)
 *      ─────────────────────────────────────────
 *      a. Project Settings (gear icon, left sidebar) → Script Properties
 *      b. Add Script Property:
 *           Name:  AUDIT_SHEET_ID
 *           Value: <the long ID you copied in step 1c>
 *      c. Add Script Property:
 *           Name:  HOST_EMAIL
 *           Value: bowandarrowstudiollc@gmail.com
 *      d. Add Script Property (optional — defaults to "Acknowledgments" tab):
 *           Name:  AUDIT_SHEET_TAB
 *           Value: Acknowledgments
 *      e. Save.
 *
 *   4. Deploy as Web App
 *      ──────────────────
 *      a. Top-right "Deploy" → "New deployment"
 *      b. Type: Web app (the gear icon next to "Select type")
 *      c. Description: "House rules acknowledgment endpoint v1"
 *      d. Execute as: Me (bowandarrowstudiollc@gmail.com)
 *      e. Who has access: Anyone
 *           ⚠️  This is REQUIRED so the public web page can POST to it.
 *               The endpoint validates the consent flag server-side; only
 *               valid acknowledgments persist. The Sheet stays private.
 *      f. Deploy
 *      g. Authorize the scopes when prompted (Drive, Gmail, Sheets — all on
 *         your own account, fine)
 *      h. Copy the "Web app URL" — it looks like
 *           https://script.google.com/macros/s/AKfycb…/exec
 *
 *   5. Tell Claude Code the URL
 *      ─────────────────────────
 *      Paste the Web app URL into the chat. Claude will:
 *      a. Replace `APPS_SCRIPT_URL` in /house-rules.html with the real URL
 *      b. Commit + push, you merge PR 2, deploy
 *      c. Run an end-to-end smoke test together (one real signature
 *         submission, verify the PDF arrives in your inbox)
 *
 *   6. Future upgrades to this script
 *      ──────────────────────────────
 *      "Deploy" → "Manage deployments" → click pencil on the existing
 *      deployment → New version. The /exec URL stays the same.
 *      DO NOT pick "New deployment" again — that creates a SECOND endpoint
 *      and your frontend points at the old one.
 */

// ───────────────────────────────────────────────────────────────────────────
// Script Properties — read at runtime, never committed to source
// ───────────────────────────────────────────────────────────────────────────

const PROPS = PropertiesService.getScriptProperties();

function getProp_(name, fallback) {
  const v = PROPS.getProperty(name);
  if (v && v.trim().length > 0) return v.trim();
  if (typeof fallback !== 'undefined') return fallback;
  throw new Error('Missing required Script Property: ' + name + '. Set it under Project Settings → Script Properties.');
}

// ───────────────────────────────────────────────────────────────────────────
// Sheet schema
// ───────────────────────────────────────────────────────────────────────────

const SHEET_HEADERS = [
  'TimestampUTC',        // server-side time of receipt
  'RecordID',            // unique identifier returned to the frontend
  'Flow',                // "house_rules_acknowledgment" (Flow 1) or future flow IDs
  'DocumentID',
  'DocumentVersion',
  'FullName',
  'Email',
  'Property',
  'CheckInDate',
  'AirbnbConfirmationCode',
  'ConsentHouseRules',
  'UserAgent',
  'BrowserLanguage',
  'TimezoneOffsetMinutes',
  'ClientSubmittedAt',   // from the browser
  'SignaturePngByteLen', // we don't store the PNG in the Sheet — just confirm one was provided
  'PdfDriveFileId'       // ID of the archived PDF in Drive (Adam's account)
];

function ensureSheetReady_() {
  const sheetId = getProp_('AUDIT_SHEET_ID');
  const tabName = getProp_('AUDIT_SHEET_TAB', 'Acknowledgments');
  const ss = SpreadsheetApp.openById(sheetId);
  let sheet = ss.getSheetByName(tabName);
  if (!sheet) {
    sheet = ss.insertSheet(tabName);
    sheet.getRange(1, 1, 1, SHEET_HEADERS.length).setValues([SHEET_HEADERS]);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, SHEET_HEADERS.length).setFontWeight('bold');
  } else if (sheet.getRange(1, 1).getValue() === '') {
    sheet.getRange(1, 1, 1, SHEET_HEADERS.length).setValues([SHEET_HEADERS]);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, SHEET_HEADERS.length).setFontWeight('bold');
  }
  return sheet;
}

// ───────────────────────────────────────────────────────────────────────────
// Web app entrypoint
// ───────────────────────────────────────────────────────────────────────────

function doPost(e) {
  try {
    // 1. Parse payload (sent as text/plain; we JSON.parse manually to bypass CORS preflight)
    const rawBody = (e && e.postData && e.postData.contents) || '';
    if (!rawBody) return jsonResponse_(400, { ok: false, error: 'Empty request body.' });
    let payload;
    try {
      payload = JSON.parse(rawBody);
    } catch (err) {
      return jsonResponse_(400, { ok: false, error: 'Body was not valid JSON.' });
    }

    // 2. Validate required fields + consent flag (the legal gate)
    const required = ['flow', 'document_id', 'full_name', 'email', 'signature_png_data_url'];
    for (const k of required) {
      if (!payload[k] || String(payload[k]).trim() === '') {
        return jsonResponse_(400, { ok: false, error: 'Missing required field: ' + k });
      }
    }
    if (payload.flow !== 'house_rules_acknowledgment') {
      return jsonResponse_(400, { ok: false, error: 'Unsupported flow: ' + payload.flow });
    }
    if (payload.consent_house_rules !== true) {
      return jsonResponse_(400, { ok: false, error: 'House-rules consent checkbox must be ticked (ESIGN intent gate).' });
    }
    if (!isValidEmail_(payload.email)) {
      return jsonResponse_(400, { ok: false, error: 'Email address is not valid.' });
    }
    if (!isValidSignaturePng_(payload.signature_png_data_url)) {
      return jsonResponse_(400, { ok: false, error: 'Signature image is missing or malformed.' });
    }

    // 3. Generate a unique record ID (also returned to the frontend)
    const recordId = 'HRA-' + Utilities.formatDate(new Date(), 'UTC', 'yyyyMMdd-HHmmss') + '-' + randomToken_(6);

    // 4. Build the signed-acknowledgment PDF (embeds the signature PNG)
    const pdfHtml = buildAckHtml_(payload, recordId);
    const pdfBlob = htmlToPdf_(pdfHtml, recordId + '.pdf');

    // 5. Archive the PDF in the script-owner's Drive (Adam's account)
    const archivedFile = DriveApp.createFile(pdfBlob).setName('HouseRulesAck — ' + payload.full_name + ' — ' + recordId + '.pdf');
    const pdfFileId = archivedFile.getId();

    // 6. Append the audit row
    const sheet = ensureSheetReady_();
    sheet.appendRow([
      new Date().toISOString(),
      recordId,
      payload.flow,
      payload.document_id,
      payload.document_version || '',
      payload.full_name,
      payload.email,
      payload.property || '',
      payload.check_in || '',
      payload.airbnb_confirmation_code || '',
      payload.consent_house_rules ? 'TRUE' : 'FALSE',
      payload.user_agent || '',
      payload.browser_language || '',
      typeof payload.timezone_offset_minutes === 'number' ? payload.timezone_offset_minutes : '',
      payload.submitted_at_iso || '',
      estimatePngByteLen_(payload.signature_png_data_url),
      pdfFileId
    ]);

    // 7. Email PDF to guest + host
    const hostEmail = getProp_('HOST_EMAIL');
    sendAckEmails_(payload, recordId, pdfBlob, hostEmail);

    // 8. Success
    return jsonResponse_(200, { ok: true, record_id: recordId });
  } catch (err) {
    // Surface the verbatim error to the frontend AND log to the script's
    // Execution log (Apps Script "Executions" tab) so Adam can debug.
    console.error('doPost failed', err);
    return jsonResponse_(500, { ok: false, error: 'Server error: ' + (err && err.message ? err.message : String(err)) });
  }
}

// ───────────────────────────────────────────────────────────────────────────
// Helpers — PDF + email
// ───────────────────────────────────────────────────────────────────────────

function buildAckHtml_(p, recordId) {
  const sigSrc = escapeAttr_(p.signature_png_data_url);
  const safe = {
    full_name: escapeHtml_(p.full_name),
    email: escapeHtml_(p.email),
    property: escapeHtml_(p.property || '— not specified —'),
    check_in: escapeHtml_(p.check_in || '— not specified —'),
    airbnb_code: escapeHtml_(p.airbnb_confirmation_code || '— not provided —'),
    user_agent: escapeHtml_(p.user_agent || ''),
    submitted_at: escapeHtml_(p.submitted_at_iso || ''),
    browser_lang: escapeHtml_(p.browser_language || ''),
    document_id: escapeHtml_(p.document_id),
    document_version: escapeHtml_(p.document_version || '1.0')
  };
  const receivedAt = new Date().toISOString();

  return '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>House Rules Acknowledgment — ' + escapeHtml_(recordId) + '</title>' +
    '<style>' +
      'body{font-family:Helvetica,Arial,sans-serif;color:#222;margin:0;padding:24px 28px;font-size:11pt;line-height:1.5}' +
      'h1{font-size:18pt;margin:0 0 4pt;color:#0a0a0a}' +
      'h2{font-size:13pt;margin:18pt 0 6pt;color:#333;border-bottom:0.5pt solid #999;padding-bottom:2pt}' +
      'h3{font-size:11pt;margin:10pt 0 4pt}' +
      '.meta-block{background:#f5f5f5;border:0.5pt solid #ccc;padding:10pt 12pt;margin:10pt 0;font-size:10pt}' +
      '.meta-block table{border-collapse:collapse;width:100%}' +
      '.meta-block td{padding:2pt 6pt;vertical-align:top}' +
      '.meta-block td:first-child{font-weight:bold;width:35%;color:#555}' +
      'ol.rules{counter-reset:rule;list-style:none;padding-left:0}' +
      'ol.rules li{counter-increment:rule;padding:6pt 0 6pt 26pt;position:relative;border-bottom:0.25pt solid #eee}' +
      'ol.rules li::before{content:counter(rule) ".";position:absolute;left:0;top:6pt;font-weight:bold;color:#999;width:22pt;text-align:right}' +
      'ol.rules li strong{display:block;margin-bottom:2pt}' +
      '.signature-block{margin-top:14pt;padding:12pt;border:1pt solid #999;background:#fafafa}' +
      '.signature-block img{display:block;max-width:360pt;max-height:120pt;margin:6pt 0}' +
      '.consent-quote{background:#fff8e1;border-left:3pt solid #d4a017;padding:8pt 12pt;margin:10pt 0;font-style:italic;color:#444}' +
      '.legal{font-size:8.5pt;color:#666;margin-top:14pt;line-height:1.6}' +
      '.legal strong{color:#333}' +
    '</style></head><body>' +
    '<h1>House Rules Acknowledgment</h1>' +
    '<p style="margin:0;color:#666;font-size:10pt">Bow &amp; Arrow Studio LLC · 501 Caroline Street, Fredericksburg, VA 22401 · Record ' + escapeHtml_(recordId) + '</p>' +
    '<div class="meta-block"><table>' +
      '<tr><td>Full legal name</td><td>' + safe.full_name + '</td></tr>' +
      '<tr><td>Email</td><td>' + safe.email + '</td></tr>' +
      '<tr><td>Property booked</td><td>' + safe.property + '</td></tr>' +
      '<tr><td>Check-in date</td><td>' + safe.check_in + '</td></tr>' +
      '<tr><td>Airbnb confirmation</td><td>' + safe.airbnb_code + '</td></tr>' +
      '<tr><td>Document ID</td><td>' + safe.document_id + ' (v' + safe.document_version + ')</td></tr>' +
      '<tr><td>Server received at (UTC)</td><td>' + escapeHtml_(receivedAt) + '</td></tr>' +
      '<tr><td>Client submitted at</td><td>' + safe.submitted_at + '</td></tr>' +
      '<tr><td>Browser</td><td>' + safe.user_agent + '</td></tr>' +
    '</table></div>' +

    '<h2>The Eight Standards</h2>' +
    '<ol class="rules">' +
      '<li><strong>No Smoking or Vaping.</strong> Inside or on the porches. Smoking on the property is grounds for forfeiture of the full security deposit plus deep-cleaning costs.</li>' +
      '<li><strong>No Pets.</strong> None of these homes are pet-friendly. Service animals as defined by the ADA are welcome with prior notice. ESAs are not service animals under federal law.</li>' +
      '<li><strong>Occupancy Limit Enforced.</strong> The "up to N" count on each property is the max overnight occupancy. Day-time visitors welcome — sustained over-occupancy is grounds for cancellation.</li>' +
      '<li><strong>No Parties or Events.</strong> These are family homes in a residential historic district. No parties, no commercial events, no gatherings beyond the listed occupancy. The neighbors will tell us, and we will end the stay.</li>' +
      '<li><strong>Exterior Video Doorbells.</strong> Each property has a Google Nest video doorbell at the entry only — for safety, package monitoring, and check-in coordination. There are no cameras inside the home.</li>' +
      '<li><strong>Booking Guest Must Be 25+.</strong> The reserving guest must be at least 25 years of age and present for the duration of the stay. Younger guests welcome under their oversight.</li>' +
      '<li><strong>Insurance &amp; Liability.</strong> Your personal belongings are not insured by Bow &amp; Arrow Studio LLC. Bring renter\'s or traveler\'s insurance for valuables. The home is insured separately by the landlord.</li>' +
      '<li><strong>Questions Welcome.</strong> Special-circumstance request? Service-dog accommodation? Mobility considerations? Reach out before booking and we will work with you in writing.</li>' +
    '</ol>' +

    '<div class="consent-quote">' +
      '<strong>Consent affirmation:</strong> "I have read all eight house rules above and agree to abide by them for the entire duration of my stay. I understand violations may result in cancellation, forfeiture of the security deposit, or other remedies described in the rules." (Checkbox value: <strong>TRUE</strong>.)' +
    '</div>' +

    '<div class="signature-block">' +
      '<strong>Signature of ' + safe.full_name + ':</strong>' +
      '<img src="' + sigSrc + '" alt="Signature">' +
      '<div style="font-size:9pt;color:#666;margin-top:4pt">Signed on ' + escapeHtml_(p.signed_date || '') + ' · captured electronically via canvas; PNG embedded above is the verbatim mark drawn at submission.</div>' +
    '</div>' +

    '<div class="legal">' +
      '<strong>Electronic Records &amp; Signatures Notice.</strong> This acknowledgment was executed electronically in compliance with the federal Electronic Signatures in Global and National Commerce Act (E-SIGN Act, 15 U.S.C. § 7001 et seq.) and the Virginia Uniform Electronic Transactions Act (Va. Code § 59.1-479 et seq.). The signer affirmatively consented to do business electronically by ticking the consent checkbox and submitting this form. A copy of this signed acknowledgment is being delivered to the signer\'s email address of record (' + safe.email + ') simultaneously with this archive. Both parties retain the right to receive paper copies on request to Bow &amp; Arrow Studio LLC at the address above.' +
    '</div>' +

    '</body></html>';
}

/**
 * Convert HTML to PDF using Drive's built-in HTML-to-PDF rendering.
 * Drive accepts an HTML blob and serves the corresponding PDF representation.
 * The temp HTML file is trashed after conversion so Drive doesn't fill with junk.
 */
function htmlToPdf_(html, pdfName) {
  const htmlBlob = Utilities.newBlob(html, MimeType.HTML, pdfName.replace(/\.pdf$/i, '.html'));
  const tempHtmlFile = DriveApp.createFile(htmlBlob);
  try {
    const pdfBlob = tempHtmlFile.getAs(MimeType.PDF).setName(pdfName);
    return pdfBlob;
  } finally {
    tempHtmlFile.setTrashed(true);
  }
}

function sendAckEmails_(p, recordId, pdfBlob, hostEmail) {
  const subjectGuest = 'Your House Rules Acknowledgment — Bow & Arrow Studio LLC (' + recordId + ')';
  const subjectHost = 'House Rules ACK signed — ' + p.full_name + ' — ' + recordId;

  const guestBodyHtml =
    '<p>Hi ' + escapeHtml_(p.full_name) + ',</p>' +
    '<p>Thanks for taking a moment to read and acknowledge our house rules. Attached is the signed PDF for your records — please keep it for the duration of your stay.</p>' +
    '<p>If anything in those rules surprised you, or you have a special-circumstance request, reply to this email or text <strong>(832) 721-4228</strong>. We&rsquo;d much rather work it out in writing before you check in than discover a mismatch mid-stay.</p>' +
    '<p>Looking forward to hosting you.</p>' +
    '<p>— Adam &amp; Maria<br>Bow &amp; Arrow Studio LLC<br><a href="https://usmcmin.com/direct-booking.html">usmcmin.com/direct-booking</a></p>' +
    '<hr><p style="font-size:0.85em;color:#666">Record ID: ' + escapeHtml_(recordId) + ' · Property: ' + escapeHtml_(p.property || 'unspecified') + '</p>';

  const hostBodyHtml =
    '<p><strong>House Rules Acknowledgment signed.</strong></p>' +
    '<table style="border-collapse:collapse;font-size:14px">' +
      '<tr><td style="padding:4px 12px 4px 0;color:#555">Record</td><td>' + escapeHtml_(recordId) + '</td></tr>' +
      '<tr><td style="padding:4px 12px 4px 0;color:#555">Guest</td><td>' + escapeHtml_(p.full_name) + ' &lt;' + escapeHtml_(p.email) + '&gt;</td></tr>' +
      '<tr><td style="padding:4px 12px 4px 0;color:#555">Property</td><td>' + escapeHtml_(p.property || '— not specified —') + '</td></tr>' +
      '<tr><td style="padding:4px 12px 4px 0;color:#555">Check-in</td><td>' + escapeHtml_(p.check_in || '— not specified —') + '</td></tr>' +
      '<tr><td style="padding:4px 12px 4px 0;color:#555">Airbnb code</td><td>' + escapeHtml_(p.airbnb_confirmation_code || '— not provided —') + '</td></tr>' +
      '<tr><td style="padding:4px 12px 4px 0;color:#555">Consent</td><td>TRUE (gate enforced server-side)</td></tr>' +
    '</table>' +
    '<p style="font-size:0.85em;color:#666;margin-top:14px">Audit Sheet row appended. PDF archived in Drive (file ID returned in Sheet column N).</p>';

  // Send to guest (with PDF attached)
  GmailApp.sendEmail(p.email, subjectGuest, fallbackPlain_(guestBodyHtml), {
    htmlBody: guestBodyHtml,
    attachments: [pdfBlob],
    name: 'Bow & Arrow Studio LLC',
    replyTo: hostEmail
  });

  // Send to host (also with PDF attached — easier to forward later if needed)
  GmailApp.sendEmail(hostEmail, subjectHost, fallbackPlain_(hostBodyHtml), {
    htmlBody: hostBodyHtml,
    attachments: [pdfBlob],
    name: 'Bow & Arrow Studio LLC',
    replyTo: p.email
  });
}

// ───────────────────────────────────────────────────────────────────────────
// Utilities
// ───────────────────────────────────────────────────────────────────────────

function jsonResponse_(httpStatus, obj) {
  // Apps Script doesn't expose HTTP status codes for ContentService output, but
  // we set the status field inside the JSON body so the frontend can branch on it.
  obj._http_status = httpStatus;
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function isValidEmail_(s) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(s).trim());
}

function isValidSignaturePng_(dataUrl) {
  return typeof dataUrl === 'string' && dataUrl.indexOf('data:image/png;base64,') === 0 && dataUrl.length > 80;
}

function estimatePngByteLen_(dataUrl) {
  if (!dataUrl) return 0;
  const b64 = dataUrl.split(',')[1] || '';
  // Base64 expands by ~4/3; subtract padding.
  return Math.floor(b64.length * 3 / 4);
}

function randomToken_(n) {
  const alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let out = '';
  for (let i = 0; i < n; i++) out += alphabet[Math.floor(Math.random() * alphabet.length)];
  return out;
}

function escapeHtml_(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function escapeAttr_(s) {
  // For data: URLs in src="…" attributes — Drive's HTML→PDF tolerates them as-is.
  return String(s == null ? '' : s).replace(/"/g, '&quot;');
}

function fallbackPlain_(html) {
  return String(html)
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/<\/p>/gi, '\n\n')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'")
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

// ───────────────────────────────────────────────────────────────────────────
// One-off helper Adam can run from the Apps Script editor for sanity checks
// ───────────────────────────────────────────────────────────────────────────

/**
 * Run this from the Apps Script editor (function picker → "selfTest") to
 * verify your Script Properties are set + the audit Sheet is reachable.
 * Does NOT send any email or write any test rows; pure read.
 */
function selfTest() {
  console.log('--- Self-test ---');
  try {
    const sheetId = getProp_('AUDIT_SHEET_ID');
    console.log('AUDIT_SHEET_ID: ' + sheetId);
    const hostEmail = getProp_('HOST_EMAIL');
    console.log('HOST_EMAIL: ' + hostEmail);
    const tabName = getProp_('AUDIT_SHEET_TAB', 'Acknowledgments');
    console.log('AUDIT_SHEET_TAB: ' + tabName);
    const sheet = ensureSheetReady_();
    console.log('Sheet "' + sheet.getName() + '" reachable, ' + sheet.getLastRow() + ' rows.');
    console.log('Self-test OK.');
  } catch (err) {
    console.error('Self-test FAILED: ' + (err && err.message ? err.message : err));
    throw err;
  }
}
