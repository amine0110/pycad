# Cold outreach messaging: dental CBCT (Path A)

Drafts for Nour to review before anything is sent. Nothing here has been sent or published.

- Sender: Nour Islam Mokhtari, founder, PYCAD (pycad.co)
- Product scope in all copy: **Path A only. View, measure, share.**
- Live viewer: https://dental.pycad.co (Google sign-in)
- Public demo page: https://pycad.co/demos/dental-dicom-viewer/
- Source brief: Marketer, "ICPs and messaging", 2026-09-28

Contents

1. Free offers (what to lead with and why)
2. ICP 1 sequence: dental imaging / radiology hubs
3. ICP 2 sequence: dental teleradiology / remote reading centers
4. OEM / platform embed (short sequence)
5. LinkedIn DM variants
6. Merge fields
7. Reply snippets for common questions
8. Do / don't claim checklist
9. Personalization tips
10. Appendix: "Browser CBCT review checklist" (content for the free PDF)

---

## 1. Free offers

Four offers, ranked. Each one is something Nour can deliver today with the live viewer and his own time. None of them promise white-label, regulatory paperwork, AI reporting, or anything outside view / measure / share.

### Offer A (primary, Email 1): "Your scan, in a browser, in a private workspace"

The prospect sends one de-identified CBCT (and a pan if they have it). Nour loads it into a private workspace on dental.pycad.co and sends login steps. They open their own study in a browser and judge it on their own data.

Fallback for anyone who can't send data: the same private workspace with a sample CBCT already loaded.

Why this leads:
- It's concrete and specific to them. "Your own scan" beats "a demo" every time.
- Low effort to say yes: one reply, one file.
- It qualifies. Someone who sends a study is a real conversation. Someone who asks for the sample case is still warm.
- It shows the product instead of describing it, which keeps copy short and claim-safe.

Delivery steps for Nour (per prospect):
1. Ask for a **de-identified** study only. Before uploading, check DICOM tags for anything identifying (PatientName, PatientID, BirthDate, InstitutionName, ReferringPhysicianName). PYCAD's own `DicomAnonymizer` (`docs/preprocessing/dicom_anonymization.md`) can do this if they send something un-scrubbed. If anything identifying arrives, don't upload it; scrub it or ask them to resend.
2. Upload, then open it yourself: confirm the slices load, the pan and cross-sections render for that study, and measurements behave. If a view doesn't work on their scanner's export, say so honestly in the reply rather than sending a broken link.
3. Send login steps (Google sign-in; fresh Google accounts work). Offer a 15–20 minute walkthrough, or let them explore on their own.
4. Only mention sharing if you have tested the share link end to end on a fresh account for that workspace. Otherwise: "happy to walk you through sharing on a short call."

### Offer B (Email 2): Free handoff teardown, 20 minutes

On a call, they show how a scan currently gets from them to the person who needs to look at it (referring dentist for hubs, reader for teleradiology). Nour opens the same kind of study in the browser side by side. They keep the notes whether or not they buy.

Why: it's about their workflow, not our product. It gives people who won't send data a reason to talk. It surfaces the real buying pain (install friction, USB/download handoff, reader setup) in their own words.

### Offer C (Email 3): One-page "Browser CBCT review checklist"

A vendor-neutral, no-pitch checklist of what to check before putting any browser CBCT viewer in front of referring dentists or readers. Content is drafted in the Appendix (section 10). **Only offer it once the PDF exists.** Until then, Email 3 can offer "I'll send you the list" and Nour pastes the text into the reply.

Why: it's a reply-to-receive asset ("want it?"), which gets replies from people who aren't ready to talk. It positions Nour as someone who knows the problem. It's educational and Path A by design.

### Offer D (later, Nour must approve terms): Limited free pilot

Don't use in Email 1. Use only as an optional line in Email 3 or after a reply, once Nour sets the terms. Draft options for Nour to pick from (all numbers are placeholders, nothing is set):

- **D1, study-count pilot:** up to [N] de-identified studies over [N] weeks, free, for [N] of their people. Ends with a 20-minute review call.
- **D2, one-group pilot (hubs):** one referring clinic or dentist group gets browser access to their scans from the hub for [N] weeks.
- **D3, reader pilot (teleradiology):** [N] readers open their normal CBCT/pan studies in the viewer for [N] weeks. Reporting stays in their system.

Pilot guardrails: say "free pilot" only once terms are set. Don't promise storage limits, SLAs, uptime, hosting region, or compliance terms inside a pilot offer.

### Offer sequencing

| Touch | Primary offer | Backup inside the same email |
|---|---|---|
| Email 1 | A: their scan in a private workspace | A-fallback: sample case login |
| Email 2 | B: 20-min handoff teardown | demo page link |
| Email 3 | C: checklist (reply to receive) | [optional] D pilot line, if approved |
| Email 4 | A restated, one-word reply ("scan") | ask who else owns this |

---

## 2. ICP 1 sequence: dental imaging / radiology hubs

Who: multi-dentist / multi-clinic imaging centers that take the scan and send it on to referring dentists. Pattern: CIR Brazil.

Pain we speak to: referring dentists get the CBCT on a USB, a download, or a desktop viewer they have to install, and a lot of them don't open it.

Cadence: Email 1 on day 0. Email 2 three to five business days later. Email 3 seven to ten business days after Email 1. Email 4 about a week after Email 3. Send 2–4 as replies in the same thread unless noted.

Deliverability: no links in Email 1. One link at most in later emails. Plain text, no images, no tracking-heavy signature.

### Email 1 (day 0)

Subject variants:
- a {{Company}} scan in a browser
- your referring dentists + CBCT files
- one of your CBCTs, free workspace
- quick offer for {{Company}}
- no install for your referrers

Body:

```
Hi {{FirstName}},

{{PersonalLine}}

I'm Nour, I run PYCAD. We built a browser viewer for dental CBCT. You open the scan, scroll the slices, look at the pan and cross-sections, take measurements. Nothing to install on the dentist's side.

Here's the offer: send me one de-identified CBCT from {{Company}} and I'll set it up in a private workspace for you, free. You log in, click around on your own scan, and decide if it's worth a conversation.

If you'd rather not send data, I can give you a login with a sample case already loaded.

Want me to set one up?

Nour
Founder, PYCAD
pycad.co
```

Fallback if you have no `{{PersonalLine}}`: delete the line. Don't replace it with a generic compliment.

### Email 2 (day 3–5 business days, same thread)

Subject variants (only if starting a new thread):
- how do your referrers open scans?
- 20 minutes on your scan handoff
- {{Company}} to referring dentist
- the step after the scan

Body:

```
Hi {{FirstName}},

Different angle, in case sending a scan is a step too far right now.

When a referring dentist gets a CBCT from {{Company}} today, how do they open it?

If you're up for 20 minutes, show me how a scan gets from you to a referring dentist, and I'll open the same kind of case in the browser next to it. You keep the notes either way. No slides.

This is what the viewer looks like, if you want to see it first:
https://pycad.co/demos/dental-dicom-viewer/

Nour
```

### Email 3 (day 7–10 business days after Email 1, same thread)

Subject variants (new thread only):
- checklist for browser CBCT review
- what to check before your referrers use a web viewer
- a one-page list for {{Company}}
- before you pick a CBCT viewer

Body:

```
Hi {{FirstName}},

I put together a one-page checklist for imaging centers thinking about browser CBCT review for their referring dentists. What to test before rolling it out: which views you need, how measurements are calibrated, how sharing and access work, where the data lives.

It's vendor-neutral. No pitch inside, our viewer isn't in it.

Want me to send it?

Nour
```

Optional line, add only after Nour approves pilot terms (see Offer D). Place before the sign-off:

```
And if you'd rather test with real cases, I can open a free pilot for one of your referring clinics for [N] weeks.
```

### Email 4, break-up (about a week after Email 3, same thread)

Subject variants (new thread only):
- closing the loop
- last one from me
- should I stop?

Body:

```
Hi {{FirstName}},

I'll stop here so I'm not filling your inbox.

If browser review for your referring dentists comes up later, the offer stands: one de-identified scan, a private workspace, free. Reply "scan" and I'll set it up.

And if someone else at {{Company}} handles this, I'd be grateful for their name.

Nour
```

### PT-BR adaptation for Brazilian hubs (Email 1 and break-up)

Get a native speaker to check this before sending. Don't say or imply that the viewer interface is in Portuguese.

Email 1, subject variants:
- uma tomografia da {{Company}} no navegador
- seus dentistas parceiros + arquivos de CBCT
- proposta rápida para a {{Company}}

```
Olá {{FirstName}},

{{PersonalLine}}

Sou o Nour, fundador da PYCAD. Fizemos um visualizador de tomografia odontológica (CBCT) que roda no navegador. Você abre o exame, navega pelos cortes, vê a panorâmica e os cortes transversais, faz medições. O dentista não precisa instalar nada.

A proposta: me envie uma tomografia anonimizada da {{Company}} e eu monto um espaço privado para vocês, sem custo. Vocês entram, testam com o próprio exame e decidem se vale uma conversa.

Se preferir não enviar dados, posso liberar um acesso com um caso de exemplo já carregado.

Quer que eu prepare?

Nour
Fundador, PYCAD
pycad.co
```

Break-up:

```
Olá {{FirstName}},

Vou parar por aqui para não lotar sua caixa de entrada.

Se a visualização no navegador para seus dentistas parceiros voltar a ser assunto, a proposta continua de pé: uma tomografia anonimizada, um espaço privado, sem custo. É só responder "exame" que eu preparo.

E se outra pessoa na {{Company}} cuida disso, agradeço se puder me indicar.

Nour
```

---

## 3. ICP 2 sequence: dental teleradiology / remote reading centers

Who: remote CBCT and dental reading services with radiologists reading at volume. Pattern: Diagnoshare / OMF radiology practices.

What they told us (Diagnoshare): they want CBCT and pan viewing, not implant planning. Reading and reporting are their job, and they don't want AI replacing the radiologist's report. The copy repeats that back to them. Being clear about what the viewer doesn't do is the hook here.

Cadence and deliverability: same as ICP 1.

Wording rule for this ICP: say "open", "view", "review", "measure". Don't say "diagnose", "diagnostic", "read for diagnosis", or anything about the viewer's role in the report.

### Email 1 (day 0)

Subject variants:
- CBCT + pan in a browser, nothing else
- a viewer for {{Company}}'s readers
- your reports stay yours
- one study, private workspace, free
- for your reading team

Body:

```
Hi {{FirstName}},

{{PersonalLine}}

I'm Nour, founder of PYCAD. We make a browser viewer for dental CBCT and panoramic images. Open the study, scroll the slices, cross-sections, measure. That's the whole scope.

No implant planning module. No AI writing reports. Reading and reporting stay with your radiologists, which I think is how it should be.

The offer: send me one de-identified study and I'll set it up in a private workspace for your team, free. One of your readers opens it in a browser and tells me what's missing. If you can't send data, I'll give you a login with a sample case instead.

Worth setting up?

Nour
Founder, PYCAD
pycad.co
```

### Email 2 (day 3–5 business days, same thread)

Subject variants (new thread only):
- opening CBCTs at volume
- 15 minutes, one of your studies
- where your readers lose time
- {{Company}} reader setup

Body:

```
Hi {{FirstName}},

Quick follow-up with a different offer.

When your readers work through a queue of CBCTs, the time spent getting each study open (download, import, a desktop app per machine) adds up before anyone reads anything.

If you have 15 minutes, share your screen and open one study the way your team does today. Then open the same type of study in our viewer. You drive, I watch where it slows you down. Useful for you even if we never work together.

What it looks like:
https://pycad.co/demos/dental-dicom-viewer/

Nour
```

### Email 3 (day 7–10 business days after Email 1, same thread)

Subject variants (new thread only):
- checklist for a reader-side CBCT viewer
- what your readers should test first
- one-page list for {{Company}}

Body:

```
Hi {{FirstName}},

I wrote a one-page checklist for reading centers looking at browser CBCT viewers: which views your readers need, how measurements are calibrated, what happens with large studies, how access and sharing work, where the data sits, and how to keep reporting fully in your own system.

It's vendor-neutral, not a brochure.

Want a copy?

Nour
```

Optional line, add only after Nour approves pilot terms (see Offer D3). Place before the sign-off:

```
If it's easier to judge on real work, I can set up a free pilot for [N] of your readers for [N] weeks. Reporting stays in your system the whole time.
```

### Email 4, break-up (about a week after Email 3, same thread)

Subject variants (new thread only):
- closing the loop
- last note on CBCT viewing
- should I stop?

Body:

```
Hi {{FirstName}},

Last one from me.

If a simpler way for your readers to open CBCT and pan studies ever comes up, reply "study" and I'll set up a private workspace with one of your de-identified cases. Free, no call required.

If someone else runs reader tools at {{Company}}, a name would help a lot.

Nour
```

---

## 4. OEM / platform embed (short sequence)

Who: dental software platforms that might license a viewer to put inside their product (SKU B pattern). Fewer accounts, bigger deals, so write each one by hand. A direct call CTA is fine here because these are buyers with intent.

Don't mention pricing in email. Don't describe an SDK, API, or embed method as shipped. Talk about the viewer and offer a technical conversation.

### OEM Email 1

Subject variants:
- CBCT viewing inside {{Company}}
- a browser CBCT viewer for {{Company}}'s users
- licensing a dental DICOM viewer

```
Hi {{FirstName}},

{{PersonalLine}}

I'm Nour, founder of PYCAD. We built a browser viewer for dental CBCT: slices, pan, cross-sections, measurements, sharing. We license it to platforms that would rather not build and maintain a viewer themselves.

Two ways to look at it, both free:
1. Send me one de-identified study exported from {{Company}} and I'll load it in a private workspace so your team can judge the viewer on your own data.
2. A 30-minute technical call with me on how it could sit inside your product, and straight answers on licensing.

Which is more useful?

Nour
Founder, PYCAD
pycad.co
```

### OEM Email 2 (4–6 business days, same thread)

```
Hi {{FirstName}},

One thing I'd ask any viewer vendor, including us: does it open the files your users actually have, from the scanners they actually use?

Easiest way to find out is one exported study from {{Company}}. I'll load it and tell you honestly what works and what doesn't.

Demo, if you'd like a look first:
https://pycad.co/demos/dental-dicom-viewer/

Nour
```

### OEM Email 3, break-up (about a week later, same thread)

```
Hi {{FirstName}},

I'll leave it here. If a built-in CBCT viewer lands on the {{Company}} roadmap, reply and I'll set up a workspace with one of your exported studies.

Nour
```

---

## 5. LinkedIn DM variants

Connection notes must be under 300 characters. No links in the connection note.

### ICP 1: hubs

Connection note:

```
Hi {{FirstName}}, I'm Nour, founder of PYCAD. We built a browser viewer for dental CBCT so referring dentists don't have to install anything. Would like to connect.
```

After they accept:

```
Thanks for connecting, {{FirstName}}. Straight offer: send me one de-identified CBCT from {{Company}} and I'll set it up in a private browser workspace for you, free. You try it on your own scan. Interested?
```

Follow-up (about 5 business days, no reply):

```
Or if sending a scan is too much, I can give you a login with a sample case loaded. Takes you two minutes to see if it's relevant.
```

### ICP 2: teleradiology

Connection note:

```
Hi {{FirstName}}, Nour here, founder of PYCAD. We make a browser viewer for dental CBCT and pan. No implant planning, no AI reports, just viewing and measuring. Happy to connect.
```

After they accept:

```
Thanks, {{FirstName}}. If it's useful: send one de-identified study and I'll set up a private workspace so one of your readers can open it in a browser and tell me what's missing. Free. Reporting stays entirely with you.
```

Follow-up:

```
No pressure. If a 15-minute screen share on one of your studies is easier, I'm happy to do that instead.
```

### OEM

Connection note:

```
Hi {{FirstName}}, I'm Nour, founder of PYCAD. We license a browser dental CBCT viewer to software platforms. Would like to connect.
```

After they accept:

```
Thanks for connecting. If a CBCT viewer inside {{Company}} is ever on the table, I'll load one of your exported studies into a private workspace so your team can judge it on real data. Free.
```

---

## 6. Merge fields

| Field | What goes in it | Fallback if empty |
|---|---|---|
| `{{FirstName}}` | First name only | "Hi there," (better: don't send) |
| `{{Company}}` | Short, spoken company name ("CIR", not "CIR Centro de Imagem Radiológica Ltda.") | "your team" |
| `{{Role}}` | Their title. Used to choose the ICP and angle, not pasted into copy. | n/a |
| `{{PersonalLine}}` | One true, specific sentence about them (see section 9) | Delete the line |
| `{{Country}}` | Decides EN vs PT-BR version and whether hosting questions are likely | n/a |
| `{{ScannerHint}}` | Scanner brand/model if public. Use only in a hand-written reply, never in the template body. | n/a |
| `{{CurrentHandoff}}` | How they deliver scans today, if known (portal, download, USB). Use only in a hand-written `{{PersonalLine}}`. | n/a |

Rules:
- Never send with a broken or empty merge tag. Preview every row.
- `{{PersonalLine}}` has to be something a human noticed: a post they wrote, a new location, a service page, a talk. Not "I love what you're doing at {{Company}}."

---

## 7. Reply snippets for common questions

Short, honest answers for when a prospect replies with a question. Edit them to fit, but don't expand the claims.

**Where is the data hosted?**

```
Cases are hosted on Google Cloud in the US (us-central1), not in Brazil. If that's a problem for your data policy, tell me now and we'll work out whether this fits, rather than find out later.
```

**Is it FDA / ANVISA / MDR cleared?**

```
No, and I don't claim it is. It's a viewer for opening, measuring and sharing scans. Reading and reporting stay with your team. If your use needs a cleared device, let's talk about what exactly you need so I can give you a straight answer on fit.
```

**Does it do HU / bone density?**

```
No, not in this viewer. It's for viewing, measuring and sharing.
```

**Does it do implant planning?**

```
Not as a planning product. Some testers use basic implant placement, but that's not what I'm offering you. The viewer I'm pitching is for viewing, measuring and sharing.
```

**Can we put our logo on it / white label?**

```
Not today. If branding for your referring dentists matters, tell me what you'd need and I'll tell you honestly whether and when we could do it.
```

**Does it have AI / auto segmentation?**

```
I'd rather show you than describe it. Happy to walk you through it on a short call.
```

**Can referring dentists / other readers open a shared case?**

```
Yes, that's part of what the viewer is for. I'll walk you through sharing on a short call so you see exactly how it works for the other person.
```
(Only send this after you've tested share end to end on a fresh account. Before that, use: "Happy to walk you through sharing on a short call.")

**Is there a mobile app?**

```
No native app. It runs in the browser.
```

**What does it cost?**

```
Depends on number of clinics, seats and storage, so I'd rather understand your volume before I throw a number at you. Can you tell me roughly how many studies a month and how many people need access?
```
(Nour: add a range here if you decide to share one. Don't let anyone else invent a number.)

**HIPAA / LGPD / BAA / DPA?**

Nour answers these personally. No template, no compliance claims in writing until confirmed.

---

## 8. Do / don't claim checklist

Run every email, DM and reply through this before sending.

### Do say

- Browser viewer for dental CBCT (and pan)
- View, scroll slices, panoramic, cross-sections, measure
- Share with a referring dentist or colleague, but soft: "happy to walk you through sharing on a short call" until share is tested end to end on a fresh account
- Nothing to install; Google sign-in
- Reading and reporting stay with your team
- No implant planning module (for ICP 2 this is a selling point)
- Free private workspace with their de-identified study or a sample case
- De-identified data only
- Hosting is Google Cloud US (us-central1). Only say this when asked, and always honestly.

### Don't say (ever, in cold copy)

- HU, Hounsfield, bone density, density measurements
- Implant planning as the pitch, fixture collision, surgical guides, ortho planning
- AI that writes the report or laudo, "AI-assisted reading", "automated findings"
- FDA, ANVISA, MDR, CE, "cleared", "approved", "certified", "medical-grade", "diagnostic-grade", "for diagnosis"
- HIPAA/LGPD "compliant", "fully secure", "bank-level security", or offering a BAA
- Native mobile app
- White-label, your branding, PT-BR interface, hub assign/routing features as shipped
- Root segmentation or auto-segmentation as ready
- Specific load times, speed multiples, uptime or accuracy numbers
- Pricing, pilot sizes or free terms that Nour hasn't set
- Customer names or logos (including Diagnoshare or CIR) without permission
- Any competitor or other product name (viewers, DICOM libraries, portals)
- The Diagnoshare call date or any other prospect's details

### Voice check

- First person, Nour. Short sentences. One ask per email.
- Cut on sight: "I hope this finds you well", "leverage", "cutting-edge", "game-changer", "delve", "seamless", "streamline", "robust", "unlock", "empower", "revolutionize", "state-of-the-art", "just checking in", "circling back", "touching base".
- No bullet lists, bold or emojis in cold emails. No fake "Re:" subjects.
- If a sentence would fit any company's cold email, delete it.

---

## 9. Personalization tips

**ICP 1, hubs.** Look at their site for how they deliver results to dentists (a portal login, "download your exam", a viewer to install, "we deliver on USB"). Reference that in one line: "Saw that {{Company}} sends CBCTs to dentists as a download with a viewer." Also worth a line: number of locations, a new unit opening, or a scanner upgrade they announced.

**ICP 2, teleradiology.** Anchor on their scope and their radiologists. Mention a reader by name if they post about cases, their turnaround promise, or that they read CBCT for referring general dentists. Put the "reporting stays yours" line near the top for anyone who has posted skepticism about AI reporting.

**OEM.** Name the specific place in their product where a CBCT viewer would sit (patient record, case sharing, treatment view). One sentence showing you used their product is worth more than a paragraph about ours.

---

## 10. Appendix: "Browser CBCT review checklist" (content for the free PDF)

Draft text for Offer C. Vendor-neutral, and PYCAD isn't mentioned in the body. Nour to review and turn into a one-page PDF before offering it as an attachment. Until then, paste the text into a reply.

---

**Browser CBCT review: what to check before your dentists or readers use it**

A one-page checklist for dental imaging centers and reading services. Test each item on your own studies, not the vendor's sample case.

**1. Opening your studies**
- Does it open CBCT exports from every scanner model you use, including older units?
- How long does your largest typical study take to open on a normal clinic internet connection?
- What happens with incomplete or unusual series: a clear error, or a silent partial load?

**2. Views you actually need**
- Axial, coronal and sagittal, linked to each other?
- A panoramic reconstruction, and can the curve be adjusted?
- Cross-sections along the arch, with visible slice position and spacing?
- If you also send 2D pans, do they open in the same place?

**3. Measurement**
- Do measurements use the pixel spacing in the DICOM file, and are the units shown?
- Can the person on the other end see a measurement you made?
- Is it clear what the tool does not measure, so nobody treats it as more than it is?

**4. Sharing and access**
- How does a referring dentist or reader get to a case: a link, an account, both?
- Can you revoke access or set an expiry?
- Does the recipient need to install anything or create an account?
- Can you see who opened what?

**5. Data**
- Where are studies hosted (country / region)? Does that fit your data policy?
- What is retained, for how long, and how do you delete a case?
- Is there a clear way to send de-identified studies for testing?

**6. Workflow fit**
- Does reporting stay in your own system, in your own format?
- Does the viewer add steps for your team, or remove them?
- Does it work on the browsers and machines your people already use? If someone will use a tablet, test that specifically.

**7. Scope and claims**
- Is the vendor clear about what the viewer is for and what it isn't?
- Are any regulatory or clinical claims backed by documents you can read?

**8. Support**
- Who do you contact when a study won't open, and how fast do they respond?
- Will they look at a problem study with you?

---
