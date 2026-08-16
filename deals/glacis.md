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
