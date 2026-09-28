# Cold outreach messaging: dental CBCT (Path A)

Drafts for Nour to review before anything is sent. Nothing here has been sent or published.

- Sender: Nour Islam Mokhtari, founder, PYCAD (pycad.co)
- Product scope in all copy: **Path A only. View, measure, share.**
- Live viewer: https://dental.pycad.co (Google sign-in)
- Public demo page: https://pycad.co/demos/dental-dicom-viewer/
- Source brief: Marketer, "ICPs and messaging", 2026-09-28
- Revision 2: rewritten after Nour's feedback. The emails now sound more like Nour typing, and every touch in a sequence makes the same ask.

Contents

1. The one offer
2. ICP 1 sequence: dental imaging / radiology hubs
3. ICP 2 sequence: dental teleradiology / remote reading centers
4. OEM / platform embed (short sequence)
5. LinkedIn DM variants
6. Merge fields
7. Reply snippets for common questions
8. Do / don't claim checklist, voice rules
9. Personalization tips
10. Appendix A: reply tools for after they engage (teardown call, checklist, pilot)
11. Appendix B: "Browser CBCT review checklist" text

---

## 1. The one offer

Every cold touch in every sequence asks for the same thing:

> **Send me one de-identified study. I'll load it into a private workspace on our viewer, free, so you can open your own scan in a browser.**
> Fallback (same offer, different data): if they can't send a study, I load a sample CBCT into the workspace instead.

Follow-ups don't add new offers. Each one pushes the same ask from a different angle:

| Touch | Same ask, but... |
|---|---|
| Email 1 | the ask itself, short |
| Email 2 | why their *own* scan (every unit exports differently) |
| Email 3 | lowers the bar: sample case if sending data is the problem |
| Email 4 | leave the door open, one-word reply, or who else to ask |

The teardown call, the checklist and the pilot aren't cold CTAs anymore. They live in Appendix A and get used only after someone has replied.

Why this offer:
- It's about their data. "Your scan in a browser" is more interesting than "a demo".
- Saying yes takes one reply and one file.
- It qualifies. Someone who sends a study is a real conversation, and someone who asks for the sample is still warm.
- The product shows itself, so the emails can stay short and make almost no claims.

Delivery steps for Nour (per prospect):
1. Ask for a **de-identified** study only. Before uploading, check DICOM tags for anything identifying (PatientName, PatientID, BirthDate, InstitutionName, ReferringPhysicianName). PYCAD's own `DicomAnonymizer` (`docs/preprocessing/dicom_anonymization.md`) can scrub it. If something identifying arrives, don't upload it; scrub it or ask them to resend.
2. Upload it, then open it yourself: confirm the slices load, the pan and cross-sections render for that study, and measurements behave. If something doesn't work on their scanner's export, tell them straight rather than sending a broken link.
3. Send login steps (Google sign-in; fresh Google accounts work). Offer to walk them through it if they want; otherwise let them explore.
4. Only mention sharing if you've tested the share link end to end on a fresh account for that workspace. Otherwise: "happy to walk you through sharing on a short call."

---

## 2. ICP 1 sequence: dental imaging / radiology hubs

Who: multi-dentist / multi-clinic imaging centers that take the scan and send it on to referring dentists. Pattern: CIR Brazil.

Cadence: Email 1 on day 0. Email 2 three to five business days later. Email 3 about a week after Email 2. Email 4 about a week after that. Send 2–4 as replies in the same thread.

Deliverability: no links in any of these. The ask is a reply, so a link only adds risk. Plain text, short signature.

### Email 1 (day 0)

Subject variants (lowercase on purpose):
- your cbct scans in a browser
- {{Company}} + referring dentists
- one of your scans
- quick question

```
Hi {{FirstName}},

{{PersonalLine}}

I'm Nour, I run PYCAD. We built a CBCT viewer that works in the browser, so a referring dentist can open the scan, go through the slices and the pan, take a measurement, without installing anything.

Would you send me one de-identified CBCT from {{Company}}? I'll load it into a private workspace for you, free. Easier to judge on your own scan than on my description.

Nour
PYCAD
```

If you have no real `{{PersonalLine}}`, delete the line. Don't fill it with a compliment.

### Email 2 (3–5 business days, same thread)

New-thread subjects if needed: "your scans, again" / "re: cbct in the browser"

```
Hi {{FirstName}},

Bumping this in case it got buried.

The reason I ask for one of your scans instead of just sending a demo: every CBCT unit exports a bit differently, and if our viewer has trouble with your files you should find that out on day one, not after a sales call.

Any de-identified case is fine. I set it up myself.

Nour
```

### Email 3 (about a week after Email 2, same thread)

New-thread subjects if needed: "sample case instead?" / "no scan needed"

```
Hi {{FirstName}},

If sending a patient scan out is the hassle here (fair enough, even anonymized), I can load a sample CBCT into the workspace instead and send you the login.

Not the same as seeing your own, but you'd get a feel for it in a few minutes. Want that?

Nour
```

### Email 4, break-up (about a week after Email 3, same thread)

New-thread subjects if needed: "leaving this here" / "last one"

```
Hi {{FirstName}},

I'll stop here.

If you want to see a {{Company}} scan in the browser at some point, just reply "scan" and I'll set it up. Or if someone else looks after how your referring dentists get their images, a name would help.

Thanks,
Nour
```

### PT-BR version for Brazilian hubs

Same four touches, same ask. Get a native speaker to check before sending. Don't imply the viewer interface is in Portuguese.

Email 1. Subjects: "suas tomografias no navegador" / "{{Company}} + dentistas parceiros" / "uma pergunta rápida"

```
Olá {{FirstName}},

{{PersonalLine}}

Sou o Nour, da PYCAD. A gente fez um visualizador de tomografia (CBCT) que roda no navegador. O dentista parceiro abre o exame, passa pelos cortes e pela panorâmica, faz uma medição, sem instalar nada.

Você me mandaria uma tomografia anonimizada da {{Company}}? Eu coloco num espaço privado pra vocês, sem custo. É mais fácil avaliar com um exame de vocês do que pela minha descrição.

Nour
PYCAD
```

Email 2:

```
Olá {{FirstName}},

Voltando nesse assunto caso tenha se perdido.

Peço um exame de vocês em vez de só mandar uma demo porque cada tomógrafo exporta de um jeito um pouco diferente. Se o nosso visualizador tiver problema com os arquivos de vocês, melhor saber logo de cara.

Qualquer caso anonimizado serve. Eu mesmo configuro.

Nour
```

Email 3:

```
Olá {{FirstName}},

Se o problema é enviar exame de paciente (entendo, mesmo anonimizado), posso colocar uma tomografia de exemplo no espaço e te mandar o acesso.

Não é igual a ver um exame de vocês, mas em poucos minutos dá pra ter uma ideia. Quer?

Nour
```

Email 4:

```
Olá {{FirstName}},

Vou parar por aqui.

Se em algum momento quiser ver um exame da {{Company}} no navegador, é só responder "exame" que eu preparo. E se outra pessoa cuida de como os dentistas parceiros recebem as imagens, me indica?

Obrigado,
Nour
```

---

## 3. ICP 2 sequence: dental teleradiology / remote reading centers

Who: remote CBCT and dental reading services with radiologists reading at volume. Pattern: Diagnoshare / OMF radiology practices.

What they told us (Diagnoshare): they want CBCT and pan viewing, not implant planning. Reading and reporting are their job, and they don't want AI replacing the radiologist's report. Email 1 repeats that back in plain words.

Wording rule for this ICP: "open", "view", "go through", "measure". Never "diagnose", "diagnostic", or anything suggesting the viewer takes part in the report.

Cadence and deliverability: same as ICP 1.

### Email 1 (day 0)

Subject variants:
- cbct + pan viewer, nothing else
- viewer for your readers
- one of your studies
- quick question

```
Hi {{FirstName}},

{{PersonalLine}}

I'm Nour from PYCAD. We make a browser viewer for dental CBCT and pans. It's just a viewer. You go through the volume, cross-sections, measure. There's no implant planning in it and it doesn't write reports. Your radiologists read and report exactly the way they do now.

Could you send me one de-identified study? I'll put it in a private workspace for your team, free, and one of your readers can open it in a browser and tell me what's missing.

Nour
PYCAD
```

### Email 2 (3–5 business days, same thread)

New-thread subjects if needed: "one study" / "re: cbct viewer"

```
Hi {{FirstName}},

Following up on this.

What I'd really like is for one of your readers to open a real study from your queue in the browser and tell me if it's quicker or slower than what they use now. That's hard to judge from a demo with a clean sample, and it's the only opinion that matters.

Still happy to set it up, free. Any de-identified CBCT or pan.

Nour
```

### Email 3 (about a week after Email 2, same thread)

New-thread subjects if needed: "sample case instead?" / "no data needed"

```
Hi {{FirstName}},

I know sending studies out isn't simple, even de-identified.

If that's what's in the way, I can set up the workspace with a sample CBCT instead and your readers can look at it whenever they have a minute. Want the login?

Nour
```

### Email 4, break-up (about a week after Email 3, same thread)

New-thread subjects if needed: "leaving this here" / "last one"

```
Hi {{FirstName}},

Last note from me.

If you want to try it on one of your studies later, reply "study" and I'll set it up. And if someone else at {{Company}} looks after the tools your readers use, I'd appreciate the name.

Thanks,
Nour
```

---

## 4. OEM / platform embed (short sequence)

Who: dental software platforms that might license a viewer to put inside their product (SKU B pattern). Few accounts, big deals, so edit each one by hand.

Same idea as the other sequences: one ask (one exported study from their platform, loaded into a private workspace). Hold the technical and licensing call until they reply. Don't mention pricing, and don't describe an SDK, API or embed method as shipped.

### OEM Email 1

Subjects: "cbct viewer inside {{Company}}" / "one of your exports" / "quick question"

```
Hi {{FirstName}},

{{PersonalLine}}

I'm Nour, founder of PYCAD. We built a browser viewer for dental CBCT and we license it to platforms that would rather not build and maintain one themselves.

Would you send me one de-identified study exported from {{Company}}? I'll load it into a private workspace so your team can judge the viewer on your own data. Free, and if it goes well we can talk licensing after.

Nour
PYCAD
```

### OEM Email 2 (4–6 business days, same thread)

```
Hi {{FirstName}},

Bumping this. The first thing I'd check with any viewer vendor, us included, is whether it opens the files your users actually have. One exported study answers that, and I'll tell you honestly what works and what doesn't.

Nour
```

### OEM Email 3, break-up (about a week later, same thread)

```
Hi {{FirstName}},

I'll leave it here. If a built-in CBCT viewer ends up on the {{Company}} roadmap, send me an export and I'll set up the workspace.

Nour
```

---

## 5. LinkedIn DM variants

Same single offer as the emails. Connection notes under 300 characters, no links.

### ICP 1: hubs

Connection note:

```
Hi {{FirstName}}, Nour from PYCAD here. We built a browser CBCT viewer for referring dentists, nothing to install. Would be good to connect.
```

After they accept:

```
Thanks for connecting {{FirstName}}. If you're up for it, send me one de-identified CBCT from {{Company}} and I'll load it into a private workspace for you, free. Easier to judge on your own scan.
```

Follow-up (about 5 business days, no reply):

```
If sending a scan is a pain I can load a sample case instead and send you the login.
```

### ICP 2: teleradiology

Connection note:

```
Hi {{FirstName}}, Nour from PYCAD. We make a browser viewer for dental CBCT and pans. Just a viewer, no implant planning, no AI reports. Would be good to connect.
```

After they accept:

```
Thanks {{FirstName}}. If it's useful, send one de-identified study and I'll put it in a private workspace so one of your readers can open it in a browser and tell me what's missing. Free. Reporting stays with you.
```

Follow-up:

```
If sending studies out is the issue, I can load a sample CBCT instead. Happy to send the login.
```

### OEM

Connection note:

```
Hi {{FirstName}}, I'm Nour, founder of PYCAD. We license a browser dental CBCT viewer to software platforms. Would like to connect.
```

After they accept:

```
Thanks for connecting. If a CBCT viewer inside {{Company}} is ever on the table, send me one exported study and I'll load it into a private workspace so your team can judge it on real data. Free.
```

---

## 6. Merge fields

| Field | What goes in it | Fallback if empty |
|---|---|---|
| `{{FirstName}}` | First name only | Don't send |
| `{{Company}}` | Short, spoken company name ("CIR", not "CIR Centro de Imagem Radiológica Ltda.") | "your team" |
| `{{Role}}` | Their title. Used to choose the ICP, not pasted into copy. | n/a |
| `{{PersonalLine}}` | One true, specific sentence about them (see section 9) | Delete the line |
| `{{Country}}` | Decides EN vs PT-BR version and whether hosting questions are likely | n/a |
| `{{ScannerHint}}` | Scanner brand/model if public. Use only in a hand-written reply, never in the template body. | n/a |
| `{{CurrentHandoff}}` | How they deliver scans today, if known (portal, download, USB). Use only inside a hand-written `{{PersonalLine}}`. | n/a |

Rules:
- Never send with a broken or empty merge tag. Preview every row.
- `{{PersonalLine}}` has to be something a person actually noticed. Examples of the right register:
  - "Saw you opened a second unit in Campinas."
  - "Your site says results go out as a download with a viewer, which is partly why I'm writing."
  - "Read your post about CBCT referrals from general dentists."
- Not: "I love what you're doing at {{Company}}."

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

## 8. Do / don't claim checklist, voice rules

Run every email, DM and reply through this before sending.

### Do say

- Browser viewer for dental CBCT (and pan)
- Slices, panoramic, cross-sections, measure
- Share with a referring dentist or colleague, but soft: "happy to walk you through sharing on a short call" until share is tested end to end on a fresh account
- Nothing to install; Google sign-in
- Reading and reporting stay with your team
- No implant planning module (a selling point for ICP 2)
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

### One-offer rule

- Every cold touch asks for the same thing: one de-identified study into a private workspace, with the sample case as the fallback.
- A follow-up never introduces a new offer, asset, call type or pilot.
- The teardown call, checklist and pilot are only used after a reply (Appendix A).

### Voice rules (so it reads like Nour, not a template)

- Write it the way you'd type a quick email to someone you respect but don't know. Contractions. Plain words.
- Keep lengths uneven. Email 1 can be 80–100 words; the follow-ups get shorter. Not every email needs the same structure.
- One question per email, near the end.
- No neat three-part lists ("fast, simple, secure"), no "Here's the offer:" or "The short version:" lead-ins, no punchy fragment chains ("No slides. No pitch. Just…").
- No bullets, bold, emojis or links in cold emails. No fake "Re:" subjects.
- Subjects are lowercase and plain, like something typed quickly.
- Cut on sight: "I hope this finds you well", "leverage", "cutting-edge", "game-changer", "delve", "seamless", "streamline", "robust", "unlock", "empower", "revolutionize", "state-of-the-art", "just checking in", "circling back", "touching base", "I'd love to", "at your convenience".
- If a sentence could go in any company's cold email, delete it.
- Read it out loud. If Nour wouldn't say it to someone across a table, rewrite it.

---

## 9. Personalization tips

**ICP 1, hubs.** Check their site for how results reach dentists (a portal login, "download your exam", a viewer to install, "delivered on USB"). One line about that is the best `{{PersonalLine}}`. Second best: a new location or a scanner upgrade they announced.

**ICP 2, teleradiology.** Anchor on their scope and their radiologists. Mention a reader who posts cases, their turnaround promise, or who they read for (general dentists, oral surgeons). If they've posted skepticism about AI reporting, their Email 1 already covers it with "doesn't write reports".

**OEM.** Name the specific place in their product where a CBCT viewer would sit (patient record, case sharing, treatment view). One sentence showing you actually used their product beats anything about ours.

---

## 10. Appendix A: reply tools for after they engage

These are **not** cold CTAs. Use them only in a reply thread, once a prospect has answered, and only when they fit what the person said.

**Handoff teardown call (20 min).** For a hub that replies with "interesting, but how would our dentists use it?" They show how a scan gets from them to a referring dentist today, and Nour opens the same kind of study in the browser next to it. Reply line:

```
Happy to show you on a call. Share your screen and walk me through how a dentist gets a scan from you today, and I'll open the same kind of case in the browser next to it. 20 minutes.
```

**Reader screen share (15 min).** The ICP 2 version, for a reading center that replies but still won't send data. Reply line:

```
If it's easier, we can do it live. One of your readers shares their screen and opens a study the usual way, then opens the sample in our viewer. 15 minutes.
```

**Browser CBCT review checklist.** For a prospect who says they're comparing viewers or "not ready yet". Send the text from Appendix B (or the PDF once it exists). Reply line:

```
Makes sense. I wrote a one-page list of what to test in any browser CBCT viewer before rolling it out. It doesn't mention us. Pasting it below in case it helps.
```

**Free pilot (Nour must set terms first).** Only for a prospect who has already opened a workspace and wants to try it on real work. Draft shapes for Nour to pick from (all numbers are placeholders, nothing is set):

- Study-count pilot: up to [N] de-identified studies over [N] weeks, for [N] of their people, ending with a short review call.
- One-group pilot (hubs): one referring clinic or dentist group gets browser access to their scans from the hub for [N] weeks.
- Reader pilot (teleradiology): [N] readers open their normal CBCT/pan studies in the viewer for [N] weeks. Reporting stays in their system.

Pilot guardrails: say "free pilot" only once terms are set. Don't promise storage limits, SLAs, uptime, hosting region or compliance terms inside a pilot.

---

## 11. Appendix B: "Browser CBCT review checklist" text

Draft text for the checklist in Appendix A. Vendor-neutral, and PYCAD isn't mentioned in the body. Nour to review and turn into a one-page PDF. Until then, paste the text into a reply.

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
