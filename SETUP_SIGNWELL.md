# SignWell Setup — Mid-Term Rental Lease

**One-time setup** to wire e-signature into `mid-term-rental.html`.
Total time: ~15 minutes.
Cost: **$0/year** (1-2 leases/year fits the free tier indefinitely).

---

## Why SignWell

- **Free tier:** 3 documents/month, 1 saved template, unlimited signers.
- **No account needed for the signer** — they get a link, sign on phone or laptop, done.
- **Template Links** = one URL anyone can click to get their own signable copy. Perfect for a public lease page where the same lease text goes out 1-2× per year.
- **Legal weight:** typed signatures are binding under the federal E-SIGN Act and Virginia's UETA — language already in clause 53 of the lease.

---

## Setup steps

### 1. Generate the lease PDF

The lease body of `mid-term-rental.html` is your source of truth. To generate the PDF for SignWell:

1. Open https://usmcmin.com/mid-term-rental.html in Chrome (after deploy)
2. Press **Cmd-P** → Destination: **Save as PDF** → click **Save**
3. The page's `@media print` rules strip the nav, sign-block, and theme — you get a clean black-on-white lease document.

Save the file as `1405-Sunken-Rd-Lease.pdf`.

### 2. Create your SignWell account

1. Go to https://signwell.com → **Sign Up Free**
2. Use `bowandarrowstudiollc@gmail.com` (so executed leases land in the LLC inbox)
3. Verify the email

### 3. Upload the lease as a Document, then save as a Template

1. Dashboard → **Upload Document** → select `1405-Sunken-Rd-Lease.pdf`
2. SignWell shows the PDF with a field-placement editor.
3. Drag these fields onto the document where they belong (most of them go on the snapshot table early in the lease, plus the signature block at the end):

   | Field type | Label | Required? | Notes |
   |---|---|---|---|
   | Text | Tenant Full Name | Yes | Top of lease + signature line |
   | Text | Tenant Email | Yes | Snapshot section |
   | Text | Tenant Phone | Yes | Snapshot section |
   | Date | Term Start | Yes | Clause 8 |
   | Date | Term End | Yes | Clause 8 |
   | Text | Monthly Rent ($) | Yes | Snapshot table |
   | Text | Security Deposit ($) | Yes | Snapshot table |
   | Text | Forwarding Address (move-out) | No | Clause 19 |
   | Signature | Tenant Signature | Yes | Final page |
   | Date | Tenant Signature Date | Yes | Final page |
   | Signature | Landlord Signature (you) | Yes | Final page — you sign after tenant |
   | Date | Landlord Date | Yes | Final page |
   | Checkbox | Mold Disclosure Acknowledged | Yes | After Mold Disclosure section |
   | Checkbox | Video Doorbell Disclosure Acknowledged | Yes | After clause 40 |

4. Click **Save as Template** in the top right. Name it: `1405 Sunken Rd MTR Lease v1`.

### 4. Get the Template Link

1. From the Template view, click **Share** → **Template Link**
2. SignWell generates a public URL like `https://www.signwell.com/sign/abc123...`
3. Copy it.

### 5. Wire it into the page

Open `mid-term-rental.html` and find this block (around line 380):

```html
<a href="mailto:bowandarrowstudiollc@gmail.com?subject=..."
   class="sign-cta disabled"
   title="SignWell template link not yet configured...">
  ✏️ Sign with SignWell → <span style="font-size:0.7rem;opacity:0.8;">(setup pending)</span>
</a>
```

Replace with:

```html
<a href="https://www.signwell.com/sign/YOUR-TEMPLATE-LINK-HERE"
   class="sign-cta"
   target="_blank"
   rel="noopener">
  ✏️ Sign with SignWell →
</a>
```

(Drop the `disabled` class, drop the warning span, drop the title attribute. Keep `target="_blank"` so the lease opens in a new tab.)

Commit and push.

---

## What happens when a tenant signs

1. Tenant clicks **Sign with SignWell** on the public page
2. SignWell opens a fresh signable copy of the template
3. Tenant fills in their name, email, dates, rent (you can pre-fill rent for them via a quote email), security deposit
4. Tenant types/draws signature, checks the disclosure boxes, clicks Submit
5. SignWell auto-routes to YOU as the second signer
6. You get an email — open the link, type your signature, submit
7. SignWell emails the **fully executed PDF** to both parties
8. The signed PDF lives in your SignWell dashboard forever

---

## When you need to update the lease

If you need to change rent caps, adjust late fees, add a clause, etc.:

1. Edit `mid-term-rental.html` (the source of truth)
2. Re-export the PDF (Print → Save as PDF)
3. In SignWell: Templates → your template → **Replace File** → upload the new PDF
4. SignWell preserves your field placements where it can; re-anchor any that drifted
5. Save → existing Template Link still works, now points at the new version

---

## Renew the City Landlord License annually

Reminder unrelated to SignWell: per the City of Fredericksburg landlord license application on file, the license **must be renewed annually**. The license is calculated on gross rental receipts. Default fee is $25/year minimum.

Contact: City of Fredericksburg Commissioner of the Revenue, 540-372-1004.

---

## Future hardening (when you have time)

- **Inspection report:** Build a `/inspection-report.html` that's printable, mirroring this same pattern. Per clause 20 of the lease, you and the tenant complete one at move-in and move-out.
- **Background check:** SignWell free tier doesn't include this. If you want one, add a "Tenant Application" step before the lease using a free service like RentSpree or pull a soft credit/criminal report via TurboTenant ($55-$75 per applicant, paid by the tenant).
- **Rent payment:** Lease accepts cash/check/Venmo/Zelle. If volume grows, consider Avail (free tier for 1 unit) for online rent collection with auto late-fee assessment.
- **Photos for 1405 Sunken Rd:** the property card on `direct-booking.html` and the hero on `mid-term-rental.html` both currently show placeholders. Replace `.photo-placeholder` blocks with `<img>` tags pointing at `assets/img/properties/sunken-rd-*.jpg` once shoots are done.
