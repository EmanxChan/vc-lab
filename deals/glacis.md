---
name: Glacis
status: diligence
stage: pre-seed
source: Plug and Play Seattle · Batch 3
url: https://glacis.io
fit: 4/5
one_liner: A flight recorder for enterprise AI — tamper-proof records of what a model actually did.
reason: Tamper-proof records of what an AI actually did — accountability infrastructure for a world where nobody can verify model behavior. Closest fit in the batch, genuinely pre-seed at $575K, Seattle. Strongest candidate for a full memo.
raised: $575,000
first_seen: 2026-08-14
---

## 1. The one-liner

Runtime assurance for AI systems that act. Glacis sits at the inference boundary and produces a
cryptographically signed receipt for every governed action — "the evidence layer under the AI you
already run."

Existing monitoring answers *did it work?* Glacis answers *did it follow our rules?*, and produces
proof a third party can verify without trusting either the vendor or the system that generated it.

## 2. Why now

Three things changed inside about eighteen months.

**Agents started taking actions.** Observability tooling was built for models that return text. Once
a system books, refunds, files, or triages, "the output looked fine" stops being an adequate record.

**The regulatory surface got real and got fragmented.** Enterprises in healthcare, hiring, and
insurance now have to show what an AI did and under what policy — to auditors, to counterparties,
and increasingly across jurisdictions that disagree with each other.

**Verification became cheap enough to run inline.** Signed receipts with an external witness are
only viable if they add negligible latency at the inference boundary. That is a recent engineering
possibility, not a 2021 one.

## 3. Team

- **Joe Braidwood** — co-founder. Previously chief strategy officer at Vektor Medical, co-founder of
  Scener, CMO at SwiftKey. Has taken deep technology into regulated markets before.
- **Dr. Jennifer Shannon** — co-founder. Nearly two decades as a psychiatrist, adjunct professor at
  the University of Washington, former medical director at Cognoa. Clinical credibility in exactly
  the market where AI accountability is hardest.
- **Rohit Tatachar** — co-founder and CTO, joined April 2026. Nineteen years at Microsoft, most
  recently a VP-level product leader on the Azure AI Foundry team.

A clinician and an enterprise-AI platform leader on the same founding team is an unusual pairing,
and it maps directly onto the buyer.

## 4. Market

The buyer is an enterprise already running agentic AI in a regulated workflow — contact centre
operations, clinical AI and ambient scribes, hiring, insurance evidence exchange. The budget exists
today and sits with compliance and risk rather than with the AI team, which matters: it is not a
budget that has to be created.

Distribution is unusually strong for the stage. Partners include nVoq, CHAI, DiMe Society,
ScaleHealth, and Cloudflare; the company is in Cloudflare's Launchpad and Plug and Play's third
Seattle cohort. **OVERT 1.0** is published as an open standard with an open-source Python SDK, which
is a standards-adoption play rather than a pure product play — if OVERT becomes the format auditors
ask for, the category forms around them.

Raised **$575K** from Geoff Ralston's Safe Artificial Intelligence Fund, Mighty Capital, Sourdough
Ventures, Lionheart Ventures, AI House, and AI2 Incubator. Seed planned for later in 2026.

## Update — 2026-10-28

Three things moved between 2026-08-14 and today, and all three land on open questions in
sections 5 and 8 below. Facts only; the judgement calls are still his.

**A state regulator now requires OVERT receipts.** Glacis signed a memorandum of understanding
with Utah's Office of Artificial Intelligence Policy on 2026-08-10, announced 2026-10-05. Signed
receipts are a condition of initial and continued participation in Utah's AI Learning Laboratory
for vendors and systems OAIP designates, with a receipt required for each covered inference or
safety-control evaluation. Twelve-month term. Glacis is also one of six outside evaluators Utah
named for its health-AI sandbox. Caveat: nearly all of the detail comes from the company's own
release, and OAIP's evaluator page confirms the MOU and its term but not the terms themselves.

**OVERT is moving out of Glacis's control, on purpose.** Announced 2026-09-21: CHAI (the Coalition
for Health AI, 3,000+ members) and the Seattle nonprofit AIGovOps Foundation will jointly steward
the standard, with Glacis as a **non-voting editor** still maintaining the spec and running the
registry. Not yet in effect — it starts on a commencement certificate signed by all three.
Braidwood: "We built it for everyone to use, our competitors included." The spec is at OVERT 1.1,
published June 2026.

**Lloyd's Lab.** Glacis was selected as one of ten companies in the latest Lloyd's Lab accelerator
cohort — insurance-side validation of one of the four buyers named in section 4.

Two open items from this check:

- **No seed announced.** Section 4 said "seed planned for later in 2026." Still the case as of
  today; no round has been made public. The site lists Plug and Play itself among the backers now,
  which was not in the August read.
- **Rohit Tatachar is not on the team page.** glacis.io/about currently lists two founders —
  Braidwood and Shannon — plus six advisors, and no CTO. That may be a stale page rather than a
  departure, and it is not something to infer from a website. Ask directly; section 8's last
  bullet is exactly this question.

**Name collision to avoid.** "Glacis Labs" is an unrelated New York crypto company that raised a
$6.8M seed led by Lightspeed Faction in July 2026. Any search for Glacis funding will surface it.

Sources: [Utah MOU release](https://www.prnewswire.com/news-releases/glacis-announces-utah-agreement-to-require-verifiable-ai-receipts-for-designated-sandbox-systems-302898065.html)
· [OVERT stewardship release](https://www.prnewswire.com/news-releases/glacis-to-place-overt-its-open-standard-for-verifying-ai-safeguards-under-chai-and-aigovops-foundation-stewardship-302884276.html)
· [glacis.io/about](https://www.glacis.io/about) · [unite.ai on the Utah requirement](https://www.unite.ai/utah-ai-office-requires-signed-receipts-for-designated-sandbox-systems/)


## 5. Thesis fit

_Mine to write. The case to test: the thesis is AI that rebuilds human trust. Glacis does not
connect people to each other — it makes machine behaviour verifiable so institutions and the people
they serve can rely on it. Is that the thesis, or is it infrastructure adjacent to the thesis? The
patient whose scribe is audited never meets this product. Decide whether that distance disqualifies
it._

## 6. The bet

_Mine to write. One sentence, the single thing that has to be true._

## 7. Terms and ownership

_Unknown — no conversation with the company yet. Needs instrument, cap, check size, resulting
ownership, and whether pro rata is available. Until this is filled in, this is a diligence memo
rather than an investment memo._

## 8. The anti-memo

_Mine to write. The strongest case against, honestly. Starting points worth attacking:_

- _Is this a feature? Cloud providers and model vendors have every incentive to ship attestation
  natively, and Tatachar came from the team that would build it at Azure._
- _Standards plays either win the category or become a footnote. OVERT has no adoption commitment
  from an auditor or regulator yet — what would one look like, and what happens without it?_
- _Compliance budget exists, but does it get spent before an enforcement action makes it urgent?_
- _Two of three founders are non-technical; the CTO joined recently. What breaks if he leaves?_

---

**Sources.** [glacis.io](https://www.glacis.io/) · [OVERT 1.0 standard](https://overt.is/) ·
[GeekWire, "Seattle startup Glacis brings longtime Microsoft leader aboard"](https://www.geekwire.com/2026/seattle-startup-glacis-brings-longtime-microsoft-leader-aboard-to-target-ais-biggest-blind-spot/)
· Plug and Play Seattle Batch 3.
