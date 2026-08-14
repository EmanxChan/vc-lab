# VC Glossary

Venture capital in plain English, with a concrete example for every term. Written for how I
learn — no jargon defined using more jargon, and a real number or a short story attached to
everything so it sticks.

Every term reads at two depths. The definition and its **Picture this** example are the quick
answer. Click into a term for the deep dive: why it matters, what it looks like in practice, where
it goes wrong, and where the term came from. Those live in [`profiles/`](profiles/), one file per
term.

Separate from my engineering [tech-glossary](https://github.com/EmanxChan/tech-glossary) —
different vocabulary, different job.

**Live version:** https://vc-lab.vercel.app/glossary.html

---

## 1. The rounds — how money arrives

### Angel investor
A person investing their own money, usually the first check a company ever takes.
**Picture this:** a founder you met through Grid110 needs $50K to build a prototype. No fund is
going to write that check. You do, personally. That's angel investing — and it's what I'm doing
now.

### Pre-seed
The earliest institutional round, usually before real revenue exists. Money to build the first
version and hire two or three people.
**Picture this:** two founders, a demo that works on a good day, twelve users who love it.
They raise $750K to spend a year finding out whether anyone will pay.

### Seed
The round that funds the search for product-market fit. There's usually a product and some
early customers, but the business model isn't proven.
**Picture this:** same company a year later — $8K a month in revenue, 40 paying customers.
They raise $3M to figure out if that becomes $80K a month.

### Series A
The first big round. You're no longer proving the thing works; you're proving it scales.
**Picture this:** $150K a month in revenue growing 15% monthly. They raise $12M to hire a
sales team and find out if growth survives contact with a real go-to-market motion.

### Series B, C, and beyond
Progressively larger rounds for expansion — new markets, new products, sometimes preparing to
go public. Series C can run into the hundreds of millions.
**Picture this:** the average US unicorn raises **more than six VC rounds** before it gets there.
Nobody arrives in one jump.

### Bridge round
A small round to get a company from where it is to its next real round or milestone. Usually on
a SAFE or note rather than a priced round.
**Picture this:** a company has five months of cash and needs nine to hit the metrics that
justify a Series A. Existing investors put in $1M to bridge the gap.

### Down round
Raising at a lower valuation than the previous round. Painful, and the moment anti-dilution
clauses come alive.
**Picture this:** a company raised at $40M in 2021. In 2023 the best offer is $18M. Everyone
who invested at $40M just watched their stake shrink in value — and if they had ratchet
protection, everyone *else's* stake shrinks in size to compensate.

### Accelerator
A program that gives small checks, mentorship, and a demo day in exchange for equity.
**Picture this:** Y Combinator writes $500K and takes about 1 in 100 applicants — roughly
150–200 companies out of 10,000+ applications. Plug and Play, Grid110, and Material Change are
accelerators I came through.

### Lead investor
The investor who sets the terms, does the deepest diligence, and usually takes the board seat.
Everyone else follows their price.
**Picture this:** a $3M seed round where one fund puts in $2M and negotiates the term sheet.
Six angels put in the rest at the same terms without negotiating anything.

### Syndicate
A group investing together in one deal, usually organized by one person.
**Picture this:** an angel finds a deal, can only write $25K, but brings twelve friends who add
$300K. The company gets one line on its cap table instead of thirteen.

---

## 2. The paperwork — how the money is structured

### Term sheet
A short, non-binding document laying out the deal: how much, at what price, and what rights the
investor gets. The blueprint the lawyers build from.
**Picture this:** two pages that say $2M at a $10M pre-money valuation, 1x liquidation
preference, one board seat, pro rata rights. Nobody's committed yet, but everyone now knows the
shape of the deal.

### SAFE
*Simple Agreement for Future Equity.* You give money now and get shares later, when the company
raises a priced round. No valuation is set today, which is why it's fast and cheap.
**Picture this:** you wire $50K on a SAFE. Eighteen months later the company raises a Series A
and your SAFE converts into actual shares at that point — not before.

### Valuation cap
The maximum company value at which your SAFE converts. It protects you from the company getting
so valuable that your early risk buys almost nothing.
**Picture this:** you invest $500K on a SAFE with a $10M post-money cap. The Series A prices the
company at $40M. Without the cap you'd get 1.25% of the company. With it, you get **5%** —
because your conversion is calculated as if the company were worth $10M.

### Post-money vs pre-money SAFE
On a **post-money** SAFE, your percentage is locked and later SAFEs dilute the founders, not
you. On a **pre-money** SAFE, later SAFEs dilute you too.
**Picture this:** post-money is the modern standard and the one founders most often
underestimate — a common mistake is modeling dilution with pre-money math, signing a post-money
SAFE, and discovering 5–10% more dilution than expected.

### Discount
A percentage off the next round's price, as thanks for going early.
**Picture this:** a 20% discount means when the Series A prices at $10M, you convert as if it
were $8M. If your SAFE has both a cap and a discount, you get whichever is better for you.

### Convertible note
Like a SAFE, but technically a loan — it has an interest rate and a maturity date. Mostly
replaced by SAFEs at pre-seed because it's more complicated.

### Priced round
A round where the company's value is actually set and you buy shares at a real per-share price.
Slower and more expensive than a SAFE because everything gets negotiated.

### Incorporation and the 83(b) election
Setting the company up as a corporation, issuing founder stock, and filing the 83(b) election
within 30 days so tax is assessed at today's near-zero value.
**Picture this:** two founders issue themselves 8,000,000 shares at $0.0001 — worth $800 total. They file 83(b)
within 30 days and pay tax on $800. Miss the deadline and they are taxed on the value at each
vesting date instead, which for a company that works can be a career-defining bill.

### Delaware C-Corp vs. LLC
The two common US structures. Venture-backed companies are almost always Delaware C-Corps; LLCs
are for businesses that will not raise institutional equity.
**Picture this:** an LLC with a great product tries to raise a seed round. The fund's LPs cannot hold pass-through
income without tax consequences, so the deal requires converting first — weeks of legal work and
a tax event, at exactly the moment speed mattered.

### NVCA model documents
The industry-standard set of venture financing templates, published free by the National Venture
Capital Association.
**Picture this:** a seed round on NVCA docs with a short list of negotiated terms closes in three weeks. The same
round on a lawyer's bespoke paper generates two extra rounds of redlines and $40,000 in fees
arguing about clauses everyone would have accepted as standard.

### IP assignment agreement
The document transferring ownership of work product from a founder, employee, or contractor to
the company.
**Picture this:** a contractor built the original prototype in 2023 and was paid, but never signed an assignment.
At Series A diligence it emerges that he still owns the core code. He now has enormous leverage
and knows it.

### Qualified Small Business Stock (QSBS)
A US tax provision that can exclude a large share of capital gains on qualifying C-Corp stock
held long enough — Section 1202.
**Picture this:** a founder holds qualifying stock for the required period and sells. A meaningful portion of the
gain comes out federally tax-free. The same outcome through an LLC, or sold too early, is taxed
in full.

---

## 3. Ownership — who owns what, and how it shrinks

### Pre-money valuation
What the company is worth *before* the new money goes in.

### Post-money valuation
Pre-money plus the new money.
**Picture this:** $8M pre-money, $2M invested → $10M post-money. The investor owns
$2M ÷ $10M = **20%**. Always check which number someone means; the difference is real money.

### Cap table
The spreadsheet of who owns what. Founders, employees, investors, and everyone's percentage.

### Dilution
Your percentage shrinking because new shares were created. It isn't theft — it's the cost of
the company being worth more.
**Picture this:** you own 10% of a company worth $10M ($1M). They raise at $50M, and you're
diluted to 8%. Your 8% is worth $4M. You own less of something much bigger.

### Fully diluted shares
The total share count if every option, warrant, and SAFE converted today. The honest
denominator — always ask for percentages on a fully diluted basis.

### Option pool
Shares set aside for future employees. Usually 10–20%.
**Picture this:** the "option pool shuffle" — an investor asks for a 15% pool to be created
*before* the money goes in, which means it comes out of the founders' share, not the
investor's. Standard practice, and worth knowing it's a negotiation, not a law of nature.

### Pro rata rights
The right to invest again later to keep your percentage from shrinking.
**Picture this:** you own 5% after a seed round. At Series A you'd drop to 3.5%. Pro rata lets
you write another check at the new price to stay at 5%. This is how a small early check keeps
mattering in a company that works.

### Ownership target
The percentage you're deliberately aiming to hold after investing. The discipline that connects
your check size to the math.
**Picture this:** if you want 8% and the company is raising at a $12M post-money, your check
needs to be about $960K. If you can only write $100K, you're not getting 8% — so either the
target or the deal has to change.

### Vesting and the cliff
Equity earned over time rather than granted outright. The cliff is the initial period where
nothing vests at all, then a chunk vests at once.
**Picture this:** the standard is four years with a one-year cliff. Leave at month eleven and you own nothing.
Stay to month twelve and 25% vests that day, with the rest arriving monthly for three more
years.

### Vesting acceleration
Vesting speeding up on a trigger. Single trigger fires on a change of control; double trigger
requires both an acquisition and the person being let go.
**Picture this:** a founder with double-trigger acceleration is acquired and kept on — vesting continues as
normal. Acquired and terminated within the window — the balance vests immediately. Single
trigger would have vested everything the day the deal closed.

### Co-founder equity split
How founding equity is divided between the people starting the company.
**Picture this:** an equal split decided in week two, before anyone knows who will still be here in year three.
Two years later one founder is running the company and the other left for a job, still holding a
third of it because nobody set up vesting.

### Advisor equity grants
Small equity grants to advisors in exchange for ongoing help — typically a fraction of a
percent, vesting over one to two years.
**Picture this:** 0.25% over two years for monthly calls and warm introductions. The advisor makes two
introductions in month one, then stops responding. Without vesting, they'd have kept the whole
grant.

### 409A valuation
An independent appraisal of a company's common stock, used to set option strike prices at fair
market value.
**Picture this:** the preferred sold at $2.40 in the seed round. The 409A comes back at $0.61 for common, because
common lacks the preference and the protective rights. Employee options get struck at $0.61.

---

## 4. The protective terms — what investors ask for

### Liquidation preference
Who gets paid first when the company sells, and how much before anyone else sees a dollar.
**Picture this:** an investor puts in $5M with a **1x** preference. Company sells for $20M —
they take $5M off the top, then $15M is split among everyone. With a **2x** preference they
take $10M first, and only $10M is left for the founders and team.

### Participating preferred ("double dip")
The investor takes their preference *and then also* shares in what's left.
**Picture this:** $5M invested, 1x participating, 25% ownership, $20M exit. They take $5M,
then 25% of the remaining $15M ($3.75M) — $8.75M total instead of $5M. Founders feel this one.

### Anti-dilution
Protection if the company later raises at a lower price. Two flavors, very different in
severity.
**Picture this:** **full ratchet** re-prices all your old shares down to the new low price — the
harshest version. **Weighted average** adjusts partially, based on how big the down round was.
Weighted average is normal; full ratchet is a red flag worth pushing back on.

### Board seat
A formal seat on the board of directors, with a vote on major decisions. Usually goes to the
lead investor.

### Drag-along rights
If enough shareholders agree to sell, they can force the rest to sell too. Stops one small
holder from blocking an acquisition.

### Tag-along rights
If big shareholders sell, small ones can join on the same terms. The mirror image of
drag-along, protecting the little guy.

### Pay-to-play
If you don't participate in the next round, you lose your preferred protections and get converted
down to common. It punishes investors who go quiet when things get hard.
**Picture this:** appears in roughly 10% of deals. It's founder-friendly and a real signal — an
investor who accepts it is telling you they intend to keep supporting the company, not just ride
the first check.

### Cram down
A round priced so low, with terms so aggressive, that it effectively wipes out existing holders.
Usually happens when a company needs cash and has no leverage.
**Picture this:** a company that raised at $60M can't raise again. A new investor offers $8M
post-money with a 3x preference and full ratchet. Existing investors and employees are left with
almost nothing. Technically a financing, functionally a reset.

### No-shop
A promise not to use your term sheet to shop for a better one. Standard, but the duration matters.
**Picture this:** 30–60 days is normal and fair. A 120-day no-shop with no obligation on the
investor's side is a founder agreeing to stop fundraising while someone decides at leisure.

### Right of First Refusal (ROFR)
If a shareholder wants to sell, the company or its investors get first option to buy at that price.
It controls who ends up on the cap table.

### Redemption rights
The right to force the company to buy back shares after some period. Rare and aggressive at
pre-seed — it converts equity into something closer to debt.

### Side letter
A separate agreement giving one investor terms the others don't have — extra reporting, fee
breaks, co-investment rights.
**Picture this:** side letters are why distributions are complicated. Before paying anyone, the
fund has to check what it privately promised each LP.

### Information rights
The right to get regular financials and updates. Sounds procedural, but it's the difference
between knowing a company is in trouble and finding out at the wake.

### Protective provisions
A list of things the company cannot do without preferred shareholder approval, regardless of who
controls the board.
**Picture this:** investors hold 18% and no board majority. They still get a veto on selling the company, raising
a senior round, changing the charter, or issuing new preferred. Minority economics, real control
over specific decisions.

### Conversion rights
The right of preferred shareholders to convert into common stock — voluntarily at any time, or
automatically on a qualifying event.
**Picture this:** at a $400M exit, holding a $10M preference on 25% ownership means taking $10M or converting and
taking $100M. Everyone converts. The preference was insurance that expired unused.

### Voting agreement
The agreement binding shareholders to vote their shares a particular way — most importantly on
who sits on the board.
**Picture this:** the agreement says the board is five: two elected by common, two by preferred, one independent
agreed by both. Everyone contractually votes that way, so board composition is settled years in
advance rather than fought over annually.

### Investor Rights Agreement (IRA)
The agreement bundling the ongoing rights investors get after closing — information,
registration, pro rata, and inspection.
**Picture this:** the term sheet is two pages about price. The IRA is thirty pages about what happens every
quarter for the next decade — what gets reported, who can demand an IPO registration, and who
has the right to keep buying.

### Most Favored Nation (MFN) clause
A promise that if someone later gets better terms, this investor gets them too.
**Picture this:** an angel invests on a SAFE with MFN and no cap. Six months later the company sells SAFEs at a
$8M cap. The MFN investor automatically gets the $8M cap without negotiating for it.

### Warrant coverage
The right to buy additional shares at a set price later, usually expressed as a percentage of
the amount invested.
**Picture this:** a $2M investment with 20% warrant coverage carries the right to buy another $400,000 of stock at
the round price. If the company does well, that's cheap stock bought years later at an old
valuation.

### Deemed liquidation event
The definition of what counts as a liquidation for the purpose of paying out preferences —
usually including an acquisition, not just a winding up.
**Picture this:** the company is acquired for $80M. Nobody is liquidating anything, but the charter deems the sale
a liquidation, so the preference stack pays out first exactly as it would in a wind-down.

### Board observer seat
The right to attend board meetings and receive materials, without a vote.
**Picture this:** a seed fund that owns 6% gets an observer seat. They see everything, ask questions, and can't
vote. For an investor without the ownership to justify a full seat, it's most of the value at
none of the governance cost.

---

## 5. The payout stack — who actually gets paid first

This is the part almost nobody explains, and it's where founder outcomes are decided.

### Common stock
Plain ownership. Every share gets an equal slice. Founders and employees hold this. It gets paid
**last**.

### Convertible preferred stock
What investors actually buy. It gives the holder a *choice* at exit: take the liquidation
preference, or convert to common and take their percentage — whichever pays more.
**Picture this:** over **99%** of VC preferred stock is convertible, and nearly 100% of modern
unicorn financings use it. It's not an exotic instrument; it's the default.

### Series preferred
Each round issues its own named class — Series A, Series B, Series C. They are *not*
interchangeable. Each can carry different rights, and that's what determines the payout order.

### Original Issue Price (OIP)
The per-share price an investor actually paid. Investment amount ÷ shares received. This is the
number liquidation preferences are calculated from.

### Par value
A nominal legal value in the corporate charter, usually $0.001. Economically meaningless — don't
confuse it with OIP.

### Seniority
Later rounds usually get paid **before** earlier ones. Being first in is not being first paid.
**Picture this:** when Kabbage sold, Series F took $161M first, then Series E ($166M), then D
($50M), then C ($31M). Only $22M was left for Series A and B — even though common shareholders
still held roughly 28% of the company.

### Pari passu
Latin for "equal footing." Classes share proceeds in proportion to their preferences instead of
one going first.
**Picture this:** two 1x series — Series A put in $10M, Series B put in $15M, $25M of preferences
total. The company sells for only $5M. Series A gets (10÷25) × $5M = **$2M**; Series B gets
(15÷25) × $5M = **$3M**. Founders get nothing.

### Stacked preferences
Preferences piling up round after round, so the amount owed before common sees a dollar keeps
growing.
**Picture this:** same company, but Series B negotiated **2x** instead of 1x on its $15M. Total
preferences jump from $25M to **$40M**. Any exit under $40M now returns literally nothing to the
founders and team.

### Conversion point
The exit value at which an investor stops preferring their liquidation preference and would
rather convert to common. Below it, take the preference. Above it, convert.
**Picture this:** Series A put in $10M for 25%. On its own, it converts at a $40M exit. Then
Series B invests $15M — and now at $40M, Series B takes its $15M first, leaving $25M, of which
Series A's 25% is only $6.25M. Worse than its $10M preference. **Series A's conversion point just
moved from $40M to $55M** because someone else joined the stack.

### Conversion price per share
Liquidation preference divided by fully diluted shares. The shortcut for working out who converts
first without trial and error — **lowest converts first.**
**Picture this:** Series A at $4.00, Series B at $6.50, Series C at $9.75. A converts, then B,
then C. With six or twelve series in a mature company, this ordering rule is the only sane way
through.

### Disagreement range
The band of exit values where different investors want opposite things, and every extra round
widens it.
**Picture this:** between $55M and $80M, Series A wants to convert and Series B doesn't — a $25M
band of conflict. Add Series C and the band stretches to $65M wide ($85M–$150M). Higher
multiples and participation rights widen it further. This is the machinery behind board fights
about whether to sell.

### Mandatory / automatic conversion
A clause forcing preferred shareholders to convert to common when conditions are met — usually a
qualifying IPO. It wipes out their liquidation preference.
**Picture this:** Palantir's charter required net IPO proceeds of at least **$150M** *and* a
valuation of at least **$5B** to trigger automatic conversion.

### The hold-up problem
When one investor class blocks something everyone else wants — like an IPO — because converting
would pay them less than their preference.
**Picture this:** Series B paid $15M for 18.75%. A $65M sale pays them their full $15M
preference. A $70M IPO — a *higher* valuation — forces conversion and pays them 18.75% × $70M =
**$13.1M**. They lose $1.9M by the company doing better, so they rationally block the IPO. That
is why mandatory conversion clauses exist.

### IPO ratchet
A guarantee that an investor receives a minimum per-share value at IPO, regardless of the actual
price.
**Picture this:** Square's Series E investors were guaranteed **$18.56 per share**. Square went
public at **$9**. The company had to issue them additional shares to make up the difference.

---

## 6. How a fund is built

### Limited Partner (LP)
The investor *in* a fund. Family offices, funds of funds, pension funds, exited founders,
wealthy individuals. They commit money and don't pick companies. "Limited" refers to their
liability, not their influence.

### General Partner (GP)
The entity that makes the investment decisions and carries unlimited liability for them. Earns
carry.

### Management Company (ManCo)
The operating business — brand, staff, vendors, office. Paid by the management fee. The thing
you'd actually go to work at.

### The Fund
A limited partnership that holds the money and the shares. No employees. Most firms run several
at once.
**Picture this:** all three exist so fee income, profit share, and investor capital sit in three
different pockets. A firm can't quietly fund payroll out of investor money.

### LPA (Limited Partnership Agreement)
The contract between the GP and the LPs. Fund life, fees, carry, what the fund may and may not
invest in.

### LPAC (Advisory Committee)
A small group of LPs who advise the GP and vote on conflicts of interest.

### Capital call
The fund asking LPs to actually send money they've already committed. Capital is drawn down over
years, not paid upfront.
**Picture this:** an LP commits $500K. Year one the fund calls $100K. The other $400K stays in
the LP's account until needed — which is exactly why a capital call notice period (usually 15
days) is in the LPA.

### Committed capital
What LPs have legally promised the fund over its life. Not money in the bank — a binding IOU the
fund is allowed to draw on. "A $100M fund" always means $100M *committed*.
**Picture this:** you hold a final close at $100M. The bank account might have $8M in it that
morning. The other $92M is a promise you'll collect over five years, one capital call at a time.

### Contributed capital (paid-in)
The share of committed capital LPs have actually sent. This is the number performance metrics
divide by, and the number the waterfall has to pay back before anyone earns a profit share.
**Picture this:** three years in, your $100M fund has called $60M. Committed is still $100M;
contributed is $60M. Return $30M tomorrow and DPI is 0.5x — half of the $60M paid in, not half of
the $100M promised. Mixing these two up is the most common beginner error in fund math.

### First close
The point where enough has been committed to start investing. Typically 10–25% of the target.
**Picture this:** VC Lab's rule of thumb is you can form the fund at 10% of target or $1M
committed, whichever comes first.

### PACT
A non-binding commitment letter used in VC Lab methodology. Signing it "hard circles" an LP as
serious and moves them out of polite conversation.

### GP commit
The GP's own money in the fund — usually about 1%. Skin in the game.
**Picture this:** on a $10M fund, the GP is expected to put in around $100K of their own. LPs
ask about this early.

### Key person clause
If named individuals leave, the fund stops making new investments until LPs agree otherwise.
LPs invested in *those people*.

### Dry powder
Committed money not yet invested.

### Fund duration / investment period
A fund typically lives **10 years**, with new investments made only in the first **3–5**. The
rest of the life is spent supporting companies and waiting for exits.

### SPV (Special Purpose Vehicle)
A one-deal fund. Pools money from several people into a single investment.
**Picture this:** you find a great deal but don't have a fund. You form an SPV, raise $400K from
eight people, and the SPV writes one check. One line on the cap table.

### Venture builder (studio)
A firm that starts companies itself instead of investing in other people's. It supplies the idea,
the founding team, and the first money, and keeps a large stake because it was there on day zero.
**Picture this:** a traditional fund might own 8% of a company after a pre-seed check. A venture
builder that hired the founders and named the company holds 30–50% — but it is now running the
business, not backing it. Different job, different risk, different hours.

---

## 7. How a fund makes money

Read this one top to bottom the first time — it builds in order: the words you need, then what the GP earns, then the tiers money runs down on its way out, then the safety nets that decide whether the GP keeps any of it. One fund runs through every example so the numbers stay comparable.

### Distribution
Cash — or sometimes shares — actually leaving the fund and landing with LPs. Not a valuation, not
a markup. Money out the door.
**Picture this:** a portfolio company is acquired and $60M wires into the fund. That is not a
distribution yet. It becomes one when the fund passes it onward. Every rule in this section is a
rule about how each distribution gets sliced on its way out.

### Realized vs. unrealized
**Realized** means it's over: the fund sold, got acquired out, or wrote the position to zero.
**Unrealized** means you still hold it and are estimating what it's worth.
**Picture this:** carry is only ever paid on realized gains. A portfolio marked at $400M pays the
GP exactly $0. This is the entire reason a fund manager can look rich on paper for eight years and
still not have been paid.

### Cost basis
What the fund paid for a position. It has to come back before a single dollar counts as profit.
**Picture this:** the fund puts $10M into a company that exits for $60M. Cost basis $10M, gain
$50M. Carry is calculated on the $50M, never on the $60M. On this one deal that distinction is
worth $2M.

### Write-off
Marking a position to zero because the company died. It counts as realized — it just realizes a
loss instead of a gain.
**Picture this:** in venture this is the *normal* outcome, not the exception. Whether those zeros
get subtracted before the GP takes carry on the winners is the single biggest variable in this
whole section.

### The ten-check fund (our running example)
One fund, reused for every calculation below so the numbers stay comparable. **$100M raised, ten
$10M investments.** Fees are set aside for clarity — a real $100M fund invests about $80M and
spends the rest on a decade of management fee.

| Company | What happens | Back to the fund |
|---|---|---|
| A | Exits year 4 | $60M |
| B, C, D | Die | $0 |
| E–I | Limp along, small exits | $2M each = $10M |
| J | Exits year 9 | $50M |
| **Total** | | **$120M** |

**Picture this:** $120M back on $100M in. **Profit: $20M. Carry genuinely earned at 20%: $4M.**
That $4M is the honest answer every structure below is trying to reach. Watch how far some of them
wander from it.

### Management fee
An annual charge to run the firm — roughly **2%** of committed capital. Pays salaries, travel,
legal, diligence.
**Picture this:** the ten-check fund charges $2M a year. Over ten years that's $20M — a fifth of
the fund, gone before a single investment is made. Which is why LPs care so much about fund size.

### Carried interest ("carry")
The GP's cut of the fund's *profit*, usually **20%**. Not 20% of the money returned — 20% of
what's left over after every dollar LPs paid in has already gone home.
**Picture this:** the ten-check fund returns $120M. Profit is $20M, so carry is $4M and LPs keep
$116M. Notice how small $4M looks beside a "$120M returned" headline. Carry is still what makes a
fund manager wealthy; fees just keep the lights on.

### 2 and 20
The standard package: 2% annual fee, 20% of profits.
**The tension:** fees are paid whether or not the fund performs. A big fund can pay its GPs well
while returning nothing. That's why a serious emerging manager points at carry, not fees.

### Carry pool
The fund's total carry, divided among the people at the firm. The GP entity earns it; individuals
hold points in it.
**Picture this:** the ten-check fund's $4M is the pool. Two founding partners take 40% each, and
the last 20% is spread across a principal, an associate and a platform hire. The principal's 5%
comes to $200K — before vesting, and nine years after they started working on it.

### Distribution waterfall
The rules for splitting up each distribution, applied in a fixed order. Picture four buckets
stacked vertically: money fills the top one completely before a single dollar spills into the one
below. Carry lives in the bottom bucket.

| Tier | Who gets it | Until |
|---|---|---|
| 1. Return of capital | 100% LP | LPs have every dollar they paid in back |
| 2. Preferred return | 100% LP | LPs have earned the hurdle, usually 8%/yr |
| 3. GP catch-up | 100% GP | GP holds 20% of the profit paid so far |
| 4. The split | 80% LP / 20% GP | Forever after |

Most venture funds only run tiers 1 and 4 — capital back, then straight 80/20. Tiers 2 and 3 are
private-equity furniture that shows up in VC mainly when a large institutional LP asks for them.
**Picture this:** the ten-check fund returns $120M. Tier 1 sends the first $100M straight to LPs.
The $20M sitting above it is profit: LPs $16M, GP $4M. That's the whole idea. Every remaining term
in this section is an argument about *when* the GP gets that $4M and *what it was calculated on*.

### Return of capital
Tier one, and the tier that decides everything above it. LPs get back every dollar they paid in
before profit is said to exist. The fight is over what counts as "paid in."
**Picture this:** a real $100M fund invests about $80M and spends $20M on ten years of management
fee. Narrow reading — LPs are whole once $80M comes back, and the GP starts earning carry there.
Proper reading, and the market standard — LPs are whole at **$100M**, fees included. On a fund
returning $120M that one definition is the difference between $8M of carry and **$4M**. It's the
first clause a serious LP turns to.

### Hurdle rate / preferred return
Tier two. A minimum annual return LPs must receive before the GP earns any carry — usually **8%**,
compounding, on the capital actually drawn.
**Picture this:** most venture LPAs skip it entirely. An 8% hurdle is either irrelevant (a 3x fund
sails past it) or unreachable (a 0.9x fund was never getting there), so the clause does most of
its real work in private equity. The ten-check fund at 1.2x never clears it. When a hurdle *does*
show up in a VC fund, the fight that follows is always about the catch-up.

### GP catch-up
Tier three, and the one nobody explains. Once LPs have their capital and their preferred return,
the GP takes **100% of the next dollars** — not 20%, all of them — until they're holding 20% of
all the profit paid out so far. Only then does the 80/20 split start.

The ten-check fund never reaches this tier, so take a stronger one: $100M in, $200M out, with
$20M of preferred return accrued.
**Picture this:** LPs take $100M (capital), then $20M (pref). Profit paid so far: $20M, every
dollar of it to LPs. Now the GP catches up — they take the next **$5M** at 100%, which makes
profit $25M with $5M to the GP: exactly 20%. The final $75M splits 80/20 → LPs $60M, GP $15M.
**GP total: $20M, precisely 20% of the fund's $100M profit.** The hurdle delayed the GP's money.
With a full catch-up, it never cost them a dollar of it.

### Hard hurdle vs. soft hurdle
A **soft** hurdle pairs the preferred return with a full catch-up, so once the fund clears the bar
the GP still earns 20% of *all* profit. A **hard** hurdle has no catch-up — the GP earns carry only
on profit *above* the hurdle, and never gets that first slice back.
**Picture this:** the $200M-on-$100M fund again. Soft hurdle: the GP ends at $20M. Hard hurdle: LPs
keep $120M off the top and the GP splits only the remaining $80M → **$16M.** Same fund, same "20%"
headline, $4M apart. So when a term sheet says "8% preferred return," the next question is always
"with catch-up?"

### European waterfall (whole-of-fund)
Carry is worked out on the fund as one single pot. Everything LPs paid in comes back first — every
investment, plus fees, plus expenses — before the GP sees a cent. The default today, and
effectively mandatory for a first-time manager.
**Picture this:** the ten-check fund, year by year. **Year 4** — Company A returns $60M, all of it
to LPs, who are still $40M short of whole. Carry: **$0.** **Years 5–8** — three companies die, five
return $2M each, LPs reach $70M. Carry: **$0.** **Year 9** — Company J returns $50M. The first $30M
finishes paying LPs back; the last $20M is the fund's profit and splits 80/20. **GP carry: $4M,
first dollar received in year 9.** Exactly what was earned, nine years after the work started.

### American waterfall (deal-by-deal)
Carry is worked out one investment at a time. A company exits, LPs get that deal's cost back, and
the gain splits 80/20 immediately. The GP gets paid years earlier — and can end up holding carry
the fund never earned.
**Picture this:** same fund, same ten companies, same outcomes. **Year 4** — Company A returns
$60M: hand LPs back the $10M cost, split the $50M gain → **GP takes $10M.** **Years 5–8** — the
write-offs and small exits pay no carry, but nothing takes the year-4 money back either. **Year 9**
— Company J returns $50M: return the $10M cost, split the $40M gain → **GP takes another $8M.**
Final tally: **$18M of carry paid out by a fund that made $20M of profit.** They earned $4M. They
are holding $18M.

### The same fund, both ways
The comparison worth memorizing. Identical fund, identical companies, identical outcomes — only
the waterfall clause changes.

| | European | American (deal-by-deal) |
|---|---|---|
| Carry paid in year 4 | $0 | $10M |
| Carry paid in year 9 | $4M | $8M |
| **Total carry taken** | **$4M** | **$18M** |
| Carry actually earned | $4M | $4M |
| Owed back at wind-down | $0 | $14M |
| GP's first dollar | Year 9 | Year 4 |

**Picture this:** the headline split is 20% in both columns. The dollars are 4.5x apart and the
timing is five years apart. Every term that follows — loss carryforward, clawback, escrow, interim
tests, tax — exists to answer one question: does that $14M actually come back?

### Loss carryforward
The clause that decides how brutal an American waterfall really is. Before the GP takes carry on a
winner, the LPA may require that losses already realized on *other* deals be paid back to LPs
first. Three flavors, GP-friendly to LP-friendly: pure deal-by-deal (only that deal's cost comes
back), deal-by-deal with loss carryforward (realized write-offs come back too), and whole-of-fund
— which is just European by another name.
**Picture this:** rerun year 9 of the ten-check fund with a loss carryforward. $70M of losses are
on the books by then — three write-offs, plus five companies that returned $2M on $10M each.
Company J's $50M can't cover them, so the GP's year-9 carry drops from $8M to **$0** and total
carry taken falls from $18M to $10M. Whether your losses land before or after your wins quietly
decides how much carry you ever touch.

### The float
The advantage that survives even a perfect clawback: the GP had the money for years, and you never
get that back.
**Picture this:** the deal-by-deal GP held $10M from year 4 to year 9. Five years of use on that
money is worth roughly $4M at 7%. Even if every dollar of the $14M is returned on schedule and in
full, the two structures were never actually equal.

### Clawback
The provision forcing a GP to hand back carry they were paid too early. It's the thing that makes
an American waterfall defensible in theory: whatever happened deal by deal, the fund trues up to
whole-fund math at the end and the GP repays the difference.
**Picture this:** the deal-by-deal GP took $18M from the ten-check fund and earned $4M, so the
clawback says $14M goes back. Whether it actually does comes down to three clauses nobody reads:
whether it's tested before wind-down, whether any of the carry sat in escrow, and whether it's
owed gross or net of tax. The next three terms are those three clauses.

### Wind-down
The end of a fund's life. Remaining positions are sold or written off, the final waterfall is run,
escrow is released, any clawback is collected, and the partnership dissolves.
**Picture this:** this is when a clawback finally gets tested in most LPAs — year 10 or later. A GP
who took carry in year 4 has had six years to spend it, change firms, or become someone you'd have
to sue. That gap is the entire reason interim tests and escrow exist.

### Interim clawback test
A mid-life true-up. Instead of waiting for wind-down, the LPA reruns the whole-fund math on a
schedule — often every two or three years, or at the end of the investment period — and makes the
GP return any excess then.
**Picture this:** the deal-by-deal GP took $10M in year 4. A year-6 test reruns the numbers: the
fund has returned $70M against $100M in, so earned carry is $0 and $10M goes back six years before
the fund closes. Without an interim test, LPs spend a decade as unsecured creditors of a person.

### Escrow (carry holdback)
The slice of every carry distribution the fund withholds against a future clawback — typically
**20–30%**, released at wind-down.
**Picture this:** the GP's $10M of year-4 carry arrives as $7M in the bank and $3M sitting in
escrow. Which is why "the fund paid carry" and "the GP got the money" are two different sentences.

### Net-of-tax clawback
The clause that turns a timing difference into a permanent dollar difference. Most clawbacks are
capped at what the GP kept **after paying tax** on the carry — so when the money goes back, the
tax already paid to the IRS does not come with it. LPs absorb that.
**Picture this:** the deal-by-deal GP took $18M and owes $14M back. At roughly 35% combined federal
and California tax they kept $11.7M, and a net-of-tax clawback caps the repayment there. **LPs are
permanently short $2.3M** — 11.5% of the fund's entire profit — under a structure that was supposed
to be economically identical to European.

### Carry vesting
Carry belongs to the firm; your personal slice of the carry pool vests over time — commonly **four
to six years**, often with a one-year cliff, and usually per-fund rather than per-person.
**Picture this:** you join the ten-check fund as a principal holding 5% of the pool, and you leave
in year 3 of a four-year vest. You keep 75% of your 5% — which is 3.75% of $4M, or **$150K** — on a
fund that won't distribute carry until year 9. You will be waiting six years after you left to
find out what it was worth.

### Distribution in kind
Paying LPs in shares instead of cash, usually once a portfolio company is public and the lockup has
expired. Carry is computed on the share price the day the shares go out.
**Picture this:** the fund holds 2M shares of a newly public company at $30. Rather than sell into
the market, it distributes the stock. The waterfall treats it as $60M returned — and every LP
carries their own price risk from that morning forward.

### The three-year hold (Section 1061)
Carry is taxed as capital gain, but since 2017 the underlying asset has to be held **more than
three years** or the GP's carry on it is recharacterized as short-term and taxed at ordinary rates.
**Picture this:** a company you funded 26 months ago gets acquired. The LPs are thrilled; your
carry on that exit is taxed near 37% instead of near 20%. Venture holding periods usually clear
three years without trying, which is exactly why the rule bites private equity and hedge funds
harder than it bites us.

### Recycling
Reinvesting early returns instead of distributing them, so more than 100% of the fund gets
deployed. Usually capped, and often zero for new managers.

---

## 8. Keeping score

### MOIC
*Multiple on Invested Capital.* The raw multiple. $1M in, $3M out = 3x. Ignores time completely.

### TVPI
*Total Value to Paid-In.* Everything distributed **plus** what's still held, divided by money in.
The headline number.
**Picture this:** $1M invested, $500K already returned, $1.5M still in the portfolio →
TVPI = **2.0x**.

### DPI
*Distributed to Paid-In.* Cash actually returned. The number nobody can argue with.
**Picture this:** in that same fund, DPI = 0.5x. TVPI says 2.0x, but only half your money has
genuinely come home. When a fund brags about TVPI and goes quiet about DPI, that's the tell.

### RVPI
*Residual Value to Paid-In.* What's still in the ground — paper value, self-reported.

### IRR
*Internal Rate of Return.* The annualized return, accounting for timing.
**Picture this:** 3x over 3 years is a much better IRR than 3x over 12 years. IRR is also the
most gameable number in venture — early markups inflate it — so read it beside DPI, never alone.

### Markup
Writing a company's value up because a later round priced it higher. Real signal, imaginary
money.
**Picture this:** you invest at $10M. Two years later they raise at $60M. Your stake is marked up
6x. You have not received a dollar.

### The Power Law
One investment returns more than all the others combined. Not a quirk — the organizing principle
of the whole asset class.
**Picture this:** 30 investments. 20 die. 8 return roughly the money. 1 returns 2x. And 1 returns
50x and pays for everything. The job isn't avoiding the 20 — it's guaranteeing you're in the 1.

---

## 9. Doing the work

### Deal flow
The total number of opportunities you see per unit of time. Quality of deal flow is most of the
job.
**Picture this:** an active early-stage firm sees roughly **1,000 opportunities a year.**

### The dealflow process
Six steps, and they're a pipeline you manage rather than a thing that happens to you:
**sourcing → filtering → diligence → decision → closing → follow-up.**
**Picture this:** most people entering venture think the job is step 3. It's mostly steps 1 and 2,
and the funds that beat you are usually beating you at sourcing, not at analysis.

### First-level filter
The fast, mechanical pass: sector, stage, geography, valuation range. Anything outside the thesis
exits immediately, in seconds, without guilt.
**Picture this:** mine is — is it AI, does it touch trust or community, is it pre-seed, is it US?
Four questions. If any is no, it's out, however much I like the founder.

### Second-level filter
The slower judgment pass on what survives: founder quality, traction, defensibility,
differentiation. What your thesis tells you to *weight*, not just what it lets in.
**Picture this:** first-level is a gate anyone could operate from a written rule. Second-level is
where your actual taste lives, and it's the thing a fund is really hiring when it hires you.

### Anti-portfolio
The deals you passed on that went on to win. Kept deliberately by good investors.
**Picture this:** Bessemer publishes theirs. The point isn't self-flagellation — it's that your
passes are data about your filter, and reviewing them is the only way to find out your filter is
miscalibrated.

### Inbound vs. outbound
Inbound arrives because someone sent it to you. Outbound is what you went and found.
**Picture this:** tracking the split is the honest measure of whether your network is real. An
investor whose dealflow is 95% outbound doesn't have an edge yet — they have effort.

### Pipeline
The set of companies you're actively tracking, with a stage attached to each. The difference
between an investor and an enthusiast is that one of them can tell you what's in their pipeline
this week.

### Conviction
The point at which you'd defend a company in a room of people who disagree. Distinct from
interest, excitement, or liking the founder.
**Picture this:** the test I'd use — can I write the single sentence that must be true for this to
work, and do I believe it? If I can only say "the team is great and the space is hot," that's
interest, not conviction.

### Sourcing
Actively finding companies rather than waiting.
**Picture this:** roughly **60%** of venture deals come through networks. Which is precisely why
my alumni relationships across Plug and Play, Grid110, and Material Change are the asset, not a
line on a bio.

### Form D
The short filing a company sends the SEC within 15 days of its first sale of securities in a
private round. It names the company, its officers and directors, the total amount being offered,
and how much has sold so far. Free and public on EDGAR, which makes it the one sourcing signal
that doesn't depend on anyone telling you anything.
**Picture this:** a Seattle company files a Form D showing a **$1.5M offering with $900,000 sold.**
That says two things at once — the round opened in the last couple of weeks, and roughly $600,000
is still open. That gap is the window an angel check can still fit through, and it closes fast.

### Due diligence
Investigating before investing — team, market, product, numbers, references.
**Picture this:** at pre-seed there's often no revenue to diligence. So you're mostly diligencing
the founder: do they see reality clearly, and do people who've worked with them want to again?

### The deal funnel
The filtering ratio from lead to check. The average VC reviews about **101 startups per
investment** — 150 for IT-focused firms, 120 for early stage, 78 for healthcare.
**Picture this — what happens to 100 startups:**
1. **~70 are gone within minutes**, usually with no meeting at all
2. **~30** get an informal coffee or video call
3. **~10** survive to a partner meeting with a written memo
4. **fewer than 2 in 5** of those completing diligence get a term sheet
5. and it takes **1.7 term sheets to produce 1 investment** — roughly 40% of offers get declined
   or lost to a competing offer

Conviction isn't the bottleneck. Volume at the top is.

### Term sheet conversion
The fact that issuing a term sheet isn't winning the deal. At the term sheet, leverage flips to
the founder.

### Elimination by aspects
How investors actually read pitches: hunting for a fatal flaw so they can stop reading. Not
looking for reasons to say yes — looking for a reason to stop.
**Picture this:** of 100 companies that reach investors, about **70 disappear without ever
getting a meeting.** Which is why naming your weakness early works — it removes the flaw they
were scanning for and signals self-awareness.

### Cold outreach
Contacting an investor with no introduction. Works better than founders assume.
**Picture this:** research on 80,000+ cold emails to 28,000 investors found nearly **10% replied
with interest** — and the best-written pitches got **13–17%**. Plain language describing what you
actually built beat polished marketing language.

### Evidence over projections
Investors weight what already happened above what you forecast.
**Picture this:** "we have 40 customers paying $200/month" beats "our TAM is $8 billion" every
single time. And yet: about **40% of YC-funded companies arrive as ideas with no revenue** — so
"too early" is rarely the real objection.

### Deal memo
Your written case for an investment: what they do, why now, why these founders, the one thing
that must be true, and an honest anti-memo arguing against.

### Investment committee (IC)
The group that approves investments. For a solo angel, the IC is you — which makes writing the
memo the only check on your own enthusiasm.

### Follow-on
Investing again in a company you already own.

### Reserves
Money held back from the start for follow-ons.
**Picture this:** a fund that deploys 100% into first checks has nothing left when its best
company raises again — and gets diluted out of its winner exactly when the winner is proving
itself.

### Unicorn
A company valued at $1B or more. The unit of measurement for whether an early investor got it
right.

### Operator-angel
An angel who built or ran something before writing checks. The dominant profile at the top.
**Picture this:** the power law among angels is brutal — only **181 individuals have backed 5+
unicorns**, about 50 have reached 10, and just **6 have backed 20 or more.** Peter Thiel leads at
27. And the currently-active list looks different from the all-time list: **114 of the most
active recent angels don't appear in the lifetime top 100** at all. Being active now matters more
than having been early once.

### Concentration
Venture returns and venture *careers* both follow a power law.
**Picture this:** roughly **5% of venture capitalists have generated about 90% of the industry's
profits.** And 70% of the top-100 individual angels are in California, 50 in San Francisco alone
— which is a real headwind to name honestly for anyone investing from Seattle.

### Valuation overstatement
Headline private valuations are inflated because preferred stock carries protections common
stock doesn't. A "$1B company" is not worth $1B to everyone on the cap table.
**Picture this:** serious rankings discount stated unicorn valuations by roughly **50%** to get
to a common-share-equivalent value. When you read "valued at $2B," the honest number is closer
to $1B.

### Human capital decay
A track record ages. Recent wins say more about an investor than old ones.
**Picture this:** the Strebulaev–Jackson ranking applies a **three-year half-life** — a 2022
investment counts fully, 2019 counts 25%, 2016 counts 12.5%. Which is exactly why "114 of the
most active recent angels aren't in the lifetime top 100" matters more than it sounds.

### Value add
The measurable version of "we're helpful": taking a board seat, or leading the round rather than
following.
**Picture this:** the ranking awards explicit bonus points for board seats and lead positions,
because those are the two places involvement is actually observable.

### Net profits (vs. gross)
Returns after subtracting what you paid to get them. It penalizes deploying enormous capital to
find a few winners.
**Picture this:** two investors both return $500M. One deployed $100M, the other $2B. Gross
returns look similar; net profit says they're not remotely the same investor.

### Warm introduction
Being introduced to an investor by someone they already trust, rather than arriving cold.
**Picture this:** a founder emails a partner directly and gets no reply. A portfolio founder forwards the same
deck with two sentences of endorsement and the meeting happens that week. Same company, same
deck.

### Partner meeting
The meeting where a fund's partners decide together whether to invest, usually the last step
before a term sheet.
**Picture this:** the founder has met one partner three times and thinks the deal is close. The partner meeting is
where six people who have spent forty minutes on it each ask the questions that decide it.

### Pitch deck
The ten-to-fifteen slide document that gets a meeting and structures the conversation once you
have one.
**Picture this:** the deck's job is not to explain the company completely. It's to make someone want a
conversation. A deck that answers everything usually gets read instead of discussed, which is
worse.

### Investor update
The regular written update to existing investors — usually monthly or quarterly — covering
metrics, progress, problems, and asks.
**Picture this:** a founder sends a short update on the fifth of every month for two years. When they raise the
next round, the investors already know the story, and two of them make introductions without
being asked.

### Fundraising process
Running a raise as a time-boxed process with parallel conversations, rather than a sequence of
individual approaches.
**Picture this:** twenty-five first meetings compressed into three weeks. Everyone is at the same stage, so a term
sheet from one creates real urgency for the others. Spread the same meetings over five months
and every conversation happens in isolation.

### Round sizing
Deciding how much to raise — set by the milestones that make the next round possible, not by
what's available.
**Picture this:** the right question is never "how much can we get?" It's "what has to be true for a Series A, how
long does that take, and what does that cost?" Then add margin, because it always takes longer.

### Investor objections
The recurring reasons investors say no — market size, defensibility, team gaps, timing, traction
— and how a founder handles them.
**Picture this:** the fourth investor in a row asks how you stop a large incumbent from shipping this. That's not
four opinions, it's one unanswered question in the pitch.

### Market timing ("why now")
The argument for why this company is possible and necessary now, when it wasn't three years ago
and won't be novel in three more.
**Picture this:** the same idea failed in 2015 because the model wasn't good enough and the data wasn't digitised.
Both changed in the last eighteen months. That's a why-now — a specific thing that shifted, with
a date attached.

### Founder story
The account of why this particular person is building this particular thing — the connection
between their history and the problem.
**Picture this:** "I spent six years as a nurse practitioner watching claims get denied for reasons nobody could
explain, and I built the spreadsheet that fixed it for my clinic" does more work than any market
slide.

---

## 10. How companies are judged

### Traction
Evidence that people want the thing. Users, revenue, retention, usage.

### Burn rate
How much cash a company spends per month.

### Runway
How many months until the money runs out.
**Picture this:** $600K in the bank, burning $50K a month = **12 months of runway.** Fundraising
takes about six, so this company should already be raising.

### Lifestyle business
A company that makes real money for its owners but has no path to becoming enormous. Nothing is
wrong with it — it is just not what venture capital is built to fund.
**Picture this:** an agency doing $2M a year, throwing off $400K in profit to two founders,
growing 10% a year. A wonderful outcome for them and a terrible one for a fund, because a 10%
grower cannot return the fund no matter how well it is run. This is the most common reason a good
company gets a pass, and saying it plainly is kinder than inventing a flaw.

### Product-market fit
The point where the market pulls the product out of the company instead of the company pushing
it out.

### TAM
*Total Addressable Market.* The whole revenue opportunity if you won everything.
**Picture this:** treat a $10B TAM slide as a claim to check, not a fact. At pre-seed it's the
least informative number in the deck.

### KPI
The handful of metrics a company actually steers by.

### Retention / churn
Whether people who started using it are still using it. The least gameable number a young company
has.
**Picture this:** growth can be bought. Retention can't. A company adding 40% more users monthly
while losing 30% of last month's is not growing, it's leaking — and at pre-seed, retention is
usually the only real evidence product-market fit is coming.

### Net revenue retention (NRR)
What last year's customers are worth this year, including expansion, minus churn. Above 100% means
the existing base grows without adding anyone.
**Picture this:** 120% NRR means a company that signed zero new customers would still grow 20%.
That's the number that makes enterprise investors lean in.

### Default alive / default dead
Whether a company reaches profitability on current cash and current growth, without raising again.
**Picture this:** Paul Graham's framing, and the most useful question to ask a founder at pre-seed
— not "how much runway do you have" but "does your current trajectory get you to safety, or does
it require me and someone after me?"

### Founder-market fit
Whether *these specific people* are the right ones for this problem. At pre-seed, where there's
little else to underwrite, this is most of the decision.

### Prior shared experience
Whether co-founders knew each other before starting. The single strongest team signal in the
unicorn data.
**Picture this:** of 1,377 multi-founder unicorns, **68.6% had co-founders who previously worked
or studied together** — 57.8% same employer, 33.3% same university. Working together beats
studying together. "We met at a hackathon last month" is a real risk factor.

### Odds ratio
How overrepresented a background is among winners, compared to how common it is among all
VC-backed founders. Above 1.0 means it predicts something; below means it doesn't.
**Picture this:** Facebook/Meta alumni sit at **4.0x**, Google at **2.9x**, the Israel Defense
Forces at **2.6x**. Harvard is **0.89 — below parity.** Prestige and predictive power are
different things, and this number tells them apart.

### Talent factory
A company whose alumni disproportionately go on to found winners — and the fact that these
decay.
**Picture this:** the PayPal Mafia's odds ratio collapsed from **12.0 before 2016 to 1.7 after.**
Meanwhile Google rose from 4.4% to 9.1% of unicorn founders, Facebook from 0.9% to 5.3%, and
OpenAI went from zero to 1.8% — **21 unicorn founders since 2016.** Where talent comes from is a
moving target; today's edge is watching the current factories, not the famous old one.

### University signal
Which schools actually overproduce unicorn founders, by volume and by rate.
**Picture this:** Stanford leads on raw count (113 unicorns), then MIT (89) and Harvard (76). But
by odds ratio the leader is **University of Utah at 3.72x**, then **University of Washington at
2.57x**. Michigan and Penn are top-13 by count yet *below* 1.0 by odds. Only Stanford and MIT
lead on both — and the Seattle note is that UW is second in the country on rate.

### Unit economics
Whether a single customer makes or loses money, once you count what it cost to get them and what
it costs to serve them.
**Picture this:** $1,800 to acquire, $60 a month in revenue, $14 a month to serve. You're profitable on that
customer in month 40 — assuming they stay that long, which they don't.

### Gross margin
Revenue minus the direct cost of delivering it, as a percentage — what's left to fund everything
else.
**Picture this:** $100 of revenue costs $38 in inference, hosting, and support. Gross margin is 62%. That 62% is
what has to cover engineering, sales, and everything else before there's a profit.

### ARR, MRR, and ACV
Annual recurring revenue, monthly recurring revenue, and average contract value — three views of
the same subscription base.
**Picture this:** MRR of $84,000 means ARR of about $1M. If that's spread over 40 customers, ACV is $25,000 — a
mid-market business. Over 4 customers, ACV is $250,000 and it's an enterprise one with
concentration risk.

### Customer acquisition cost (CAC)
Everything spent to win a customer, divided by the number of customers won.
**Picture this:** $60,000 on marketing and sales in a quarter — including the salaries — produced 30 customers.
CAC is $2,000. Counting only ad spend would have said $700, and every decision built on that
number would be wrong.

### CAC payback period
How long it takes for a customer's gross profit to repay what it cost to acquire them.
**Picture this:** CAC of $2,400, gross profit of $200 a month. Payback is 12 months. Every customer is a twelve-
month loan the company makes to itself, funded by the last round.

### Lifetime value (LTV)
The total gross profit expected from a customer across the whole relationship. A projection, not
a measurement.
**Picture this:** $200 a month gross profit and an average life of 30 months gives an LTV of $6,000. Against a CAC
of $2,000 that's a 3:1 ratio — entirely dependent on a 30-month assumption that a two-year-old
company cannot have observed.

### Gross burn vs. net burn
Gross burn is total cash going out. Net burn is that minus cash coming in — what actually
shortens the runway.
**Picture this:** $420,000 out and $180,000 in each month. Gross burn is $420K, net burn is $240K. Runway is
calculated on the $240K, but a revenue stumble moves you toward the $420K fast.

### Runway extension levers
The specific moves available to buy more time — cutting cost, accelerating collections, raising
a bridge, or growing revenue.
**Picture this:** seven months of runway. Cutting discretionary spend buys one month. Moving customers to annual
prepay buys two. A bridge from existing investors buys six. Each has a different cost and a
different signal.

### Cohort retention
Tracking each group of customers who started in the same period separately, so you can see
whether retention is improving.
**Picture this:** the January cohort is at 34% after six months. The June cohort is at 61% at the same age. The
product got better, and only cohort analysis shows it — the blended number hides it completely.

### North Star metric
The single number that best captures the value customers get, used to align what everyone works
on.
**Picture this:** not signups, and not revenue. Something like "weekly active teams completing at least one
workflow" — a number that only goes up when the product is genuinely being used for its purpose.

### TAM, SAM, and SOM
Total addressable market, serviceable addressable market, and serviceable obtainable market —
the market, the slice you could actually sell to, and the slice you could realistically win.
**Picture this:** TAM: everyone with this problem. SAM: those in your geography, segment, and price band. SOM:
what you could win in five years given a real sales motion. The third number is the only one
that constrains anything.

### Bottom-up market sizing
Building the market number from actual units — how many customers exist, and what each would pay
— instead of taking a share of an industry total.
**Picture this:** 28,000 US clinics of the right size, times $14,000 a year, is a $392M market. Every input is
checkable and arguable, which is exactly what makes it credible.

### First ten hires
The first employees after the founders — the hires that set the culture and determine what the
company can execute.
**Picture this:** hire ten generalists who can each do three jobs badly, and you get a company that ships slowly.
Hire ten specialists too early and you get a company that can't change direction. Both mistakes
are expensive at this size.

---

## 11. Getting out

### Exit
The event that turns shares into money: acquisition, IPO, or secondary sale.

### Liquidity event
Any moment shareholders can convert equity to cash.

### M&A
Another company buys this one. The most common exit by far.

### IPO
The company lists publicly. Rare, slow, and the outcome everyone talks about.

### Secondary sale
Selling your existing shares to another investor without the company raising anything.
**Picture this:** you invested at $10M. Five years later the company is worth $400M but nowhere
near an IPO. You sell part of your stake to a growth fund and take real money off the table.

### Lock-up period
After an IPO, insiders can't sell for a set window — typically 90–180 days.

### Acqui-hire
An acquisition made mostly for the team, where the product is usually shut down.
**Picture this:** a company that raised $6M and didn't find a market sells for $9M. The engineers get retention
packages worth more than the shareholders receive. Investors get their money back, and not much
more.

### Letter of intent (LOI)
A mostly non-binding document setting out the shape of an acquisition before the definitive
agreements are drafted.
**Picture this:** the LOI says $60M, subject to diligence, with 45 days of exclusivity. The price is non-binding
and the exclusivity is binding — which is the part that actually changes the company's position.

### Asset sale vs. stock sale
Whether the buyer purchases the company's assets or its shares. It changes who keeps the
liabilities and how everyone is taxed.
**Picture this:** in a stock sale the buyer takes the whole company, history and liabilities included. In an asset
sale they take the parts they want, leave the rest behind, and the selling entity has to be
wound up afterwards.

### Earnout
Part of the purchase price paid later, contingent on the business hitting agreed targets after
the acquisition.
**Picture this:** $40M at close, plus $20M if revenue doubles within two years. The founders no longer control the
budget, the sales team, or the roadmap — but the $20M depends on all three.

### Tender offer (employee liquidity)
A company-organised process letting employees and early shareholders sell some shares to
investors, without an exit.
**Picture this:** at Series D the company runs a tender: employees with vested shares can sell up to 20% of their
holding to the incoming investor. People who've been there six years get to buy a house without
waiting for an IPO.

---

## 12. Who the customer is

Everything above is about money and structure. This is the part that decides whether any of it
was worth doing — who the company is actually for, and how you tell whether the founder knows.

### Ideal Customer Profile (ICP)
A description of the customer a product serves best — specific enough that you can look at any
company and say yes or no.
**Picture this:** not "mid-market SaaS companies." More like: "US healthcare practices with 8–40 clinicians, no
in-house IT, already paying for a scheduling tool they complain about." The first one is a
category. The second one is a list you can actually build.

### Segment vs. persona
A segment is the kind of company you sell to. A persona is the individual human inside it you
have to convince.
**Picture this:** the segment is "dental practices with 5–15 chairs." The personas are the practice owner who
signs, the office manager who uses it daily, and the hygienist who will quietly refuse to log
in. Three different pitches, one segment.

### Jobs to Be Done (JTBD)
The framing that people don't buy products, they hire them to make progress on something. The
job is the progress, not the product.
**Picture this:** the classic study: a fast-food chain wanted to sell more milkshakes. Nearly half were bought
before 9am by solo commuters. The job wasn't dessert — it was a one-handed thing that lasts the
whole drive and stops you being hungry until lunch. The real competition was bananas and bagels,
not other milkshakes.

### Painkiller vs. vitamin
Whether the product solves a problem that already hurts, or offers an improvement that is nice
to have.
**Picture this:** payroll compliance software is a painkiller — get it wrong and you're fined. A tool that makes
team retros 20% more engaging is a vitamin. In a good year both sell. In a budget freeze only
one survives, and it isn't the vitamin.

### Design partner
An early customer who commits to building alongside you — real usage and real feedback, in
exchange for influence over the product and usually favourable terms.
**Picture this:** a pre-seed company signs three hospitals as design partners. They pay a reduced rate, get weekly
calls with the founders, and shape the roadmap. In return the company gets something no amount
of user research buys: a real workflow to build against, and three logos that become references.

### Early adopter
The customer who buys before the product is finished, because their problem is bad enough that
an unpolished solution still beats what they have.
**Picture this:** the first buyers of a compliance tool are usually the teams that just failed an audit. They will
tolerate bugs, missing features, and a founder doing implementation personally — because the
alternative is failing the next one.

### Customer discovery interview
A structured conversation about what someone actually does today — run to learn, not to sell or
to get validation.
**Picture this:** a founder asks thirty people "would you use a tool that does X?" and gets twenty-six yeses. Zero
of them buy. The question that would have worked: "what did you do the last time this came up,
and how long did it take?"

### Leading questions
Questions that carry the answer inside them, so the response confirms what you already hoped
rather than telling you anything.
**Picture this:** "Wouldn't it be useful if this took five minutes instead of an hour?" Of course. Everyone says
yes. You have learned nothing except that faster is better than slower.

### Problem validation vs. solution validation
Two different questions: does this problem actually hurt enough that someone will pay to fix it,
and does this particular fix work?
**Picture this:** a team spends four months building a beautiful scheduling tool. It works perfectly. Nobody buys,
because the scheduling was annoying but never expensive enough to justify a purchase order.
Solution validated, problem never was.

### Switching costs
Everything it costs a customer to move off what they use now — migration, retraining,
integrations, contracts, and the risk of it going wrong.
**Picture this:** a hospital's scheduling system is bad, everybody complains, and it will not be replaced. Twelve
years of data live in it, four other systems read from it, and the person who would own the
migration is already at capacity. Your product being better is not the obstacle.

### Pilot vs. paid contract
A pilot is a time-boxed trial with an exit. A paid contract is a commitment. They look similar
on a slide and mean completely different things.
**Picture this:** "we're in pilot with three enterprises" can mean three signed six-figure deals with a proof
period, or three free trials with a friendly manager who hasn't told procurement. Ask which, and
the meeting changes.

---

## 13. How the company makes money

A revenue model is how the cash arrives. A business model is the whole machine. Founders
conflate them constantly, and the conflation hides whether the thing can actually work at scale.

### Business model vs. revenue model
The revenue model is how cash arrives. The business model is the whole machine — who you serve,
what you deliver, what it costs, and why the economics hold.
**Picture this:** "subscription" is a revenue model. The business model is: mid-size clinics pay $800 a month, we
acquire them for $2,400 through partner referrals, they stay four years, and gross margin is 78%
because support is self-serve.

### Subscription business model
Customers pay a recurring fee for continued access, usually monthly or annually.
**Picture this:** $500/month per clinic, billed annually with a 15% discount. Predictable revenue, but you have to
earn it again every renewal — and the annual discount means you find out about problems twelve
months late.

### Two-sided marketplace
A business that creates value by connecting two distinct groups who need each other, and takes a
cut of what happens between them.
**Picture this:** riders and drivers, guests and hosts, patients and clinicians. The product isn't the app — it's
the fact that when one side shows up, the other side is already there.

### Transaction fee (take rate)
The platform takes a percentage of each transaction it enables, rather than charging for access.
**Picture this:** a booking platform charges 12% of every job. A $400 job earns $48. Revenue only exists when the
customer succeeds — which is either beautifully aligned or brutally exposed, depending on the
week.

### Freemium
A free tier that's genuinely useful, with paid tiers for the users who need more.
**Picture this:** the free plan handles three projects. It's real, people use it for years, and it costs you
money. The bet is that enough of them hit four projects — and that the free users bring the
paying ones in.

### Platform vs. pipeline
A pipeline business creates value and sells it. A platform lets others create value and takes a
cut of the exchange.
**Picture this:** a studio that makes films is a pipeline. A service where anyone can publish and viewers choose
is a platform. Same industry, completely different cost structures, growth curves, and
defensibility.

### B2B2C
Selling to a business that puts your product in front of its own consumers, so the business pays
and the consumer uses.
**Picture this:** a benefits tool sells to employers; employees use it. One signature reaches four thousand users
— and if that employer leaves, four thousand users leave with them.

### Direct-to-consumer (D2C)
Selling straight to the end customer, skipping retailers and distributors.
**Picture this:** a mattress brand sells online, owns the customer relationship, keeps the retail margin — and
pays for every single customer through ads, which is the part that got expensive.

### Licensing
Charging others to use your technology, brand, or IP inside their own product, rather than
selling a product yourself.
**Picture this:** a speech-recognition company licenses its engine to four device makers. It never touches an end
user, has almost no support burden, and lives entirely on the commercial health of four
partners.

### Advertising-supported
The product is free to users, and revenue comes from selling their attention to advertisers.
**Picture this:** a news app with two million monthly readers earning $8 per thousand impressions. The reader is
not the customer — the advertiser is, and the reader is the inventory.

### On-demand (gig)
Connecting customers who want something now with independent workers who deliver it,
coordinating supply in real time.
**Picture this:** a delivery app at 7pm on a Friday. Demand triples, and the whole business is whether enough
couriers chose to be online in that specific neighbourhood in that specific hour.

### Pay-for-performance (results-as-a-service)
Charging for the outcome rather than the tool — a share of savings, a fee per result, a cut of
recovered revenue.
**Picture this:** a claims-recovery product takes 25% of what it recovers. The hospital pays nothing up front and
can't really say no, because the alternative is recovering nothing.

### Pricing models
The structure of the charge — per seat, per usage, flat tier, per outcome — as distinct from how
much it costs.
**Picture this:** the same $50,000 a year can be 100 seats at $500, 5 million API calls at a cent, or a flat
platform fee. Identical revenue, completely different incentives about whether the customer lets
more people use it.

### Value-based pricing
Setting price from what the outcome is worth to the customer, rather than from what it costs you
to deliver or what competitors charge.
**Picture this:** the software costs $4 a month to run. It saves a mid-size firm 60 hours of paralegal time a
month. Cost-plus says charge $20. Value-based says the conversation starts far higher, and the
customer will still be delighted.

### Willingness to pay
The most a specific customer would actually hand over, discovered through behaviour rather than
asked in a survey.
**Picture this:** "would you pay $200 a month for this?" gets a yes from eight out of ten. An invoice for $200
gets paid by one. The survey measured politeness.

---

## 14. How it reaches customers

Go-to-market is where good products go to die quietly. These are the terms for how a company
finds its first customers and whether that motion can be repeated by someone who is not the
founder.

### Wedge
The narrow first thing you do so well that a customer will tolerate switching, from which you
expand into everything else.
**Picture this:** a company that eventually wants to run all of a clinic's back office starts with one thing:
chasing unpaid insurance claims. Small, painful, measurable, and nobody else wants to own it.
That's the way in.

### Beachhead market
The first narrow market you take completely, chosen because winning it gives you the credibility
and cash to take the next one.
**Picture this:** not "legal tech." More like "immigration law firms with 5–20 attorneys in California." Small
enough to dominate, connected enough that the reference travels, adjacent to the next segment
you want.

### Founder-led sales
The founders doing the selling themselves, before there's a repeatable motion to hand to anyone
else.
**Picture this:** the CEO runs every demo for the first forty customers. It doesn't scale, and that isn't the
point — the point is that she hears every objection first-hand and changes the product on
Monday.

### Product-led vs. sales-led growth
Whether the product acquires and converts users on its own, or people do it through a sales
process.
**Picture this:** one company's users sign up, get value in ten minutes, and hit a paywall on day nine. The other
runs a six-week evaluation with three stakeholders and a security review. Both can work. Running
the wrong one for your price point doesn't.

### Land and expand
Start with a small deal in one team, prove it works, then grow into the rest of the
organisation.
**Picture this:** $12,000 with one department in March. By the following March it's $140,000 across six
departments, and nobody ran a new sales process — the first team did the selling internally.

### Channel strategy
Which routes you use to reach customers — direct, partners, resellers, marketplaces — and what
each one costs you.
**Picture this:** a company sells direct at 100% of revenue and through a cloud marketplace at 80%. The
marketplace deals close twice as fast because the budget is already approved. Whether that 20%
is worth it is the entire question.

### User, buyer, and champion
Three distinct roles in a B2B sale: the person who uses it, the person who pays for it, and the
person inside who fights for it.
**Picture this:** the nurse uses it, the CFO signs it, and the clinic operations lead is the one forwarding your
email at 11pm because the current system just broke again. Lose the third and the deal dies
quietly.

### Sales pipeline stages
The named steps a deal moves through from first contact to closed, each with a definition of
what has to be true to advance.
**Picture this:** not "interested / very interested / really interested." More like: discovery call held, problem
confirmed by the buyer, pricing shared, security review passed, contract out. Each one either
happened or it didn't.

### SQL vs. MQL
A marketing qualified lead has shown interest. A sales qualified lead has been verified as
someone who could actually buy.
**Picture this:** four hundred people downloaded the whitepaper (MQLs). Eleven of them have the problem, a budget,
and authority (SQLs). Reporting the four hundred as pipeline is how forecasts go wrong.

### Customer reference
An existing customer willing to tell a prospect, in their own words, that this works.
**Picture this:** a hospital CIO takes a fifteen-minute call with another hospital CIO. That call closes more
deals than any amount of marketing, and it's the asset that took eighteen months to earn.

---

## 15. What makes it defensible

Every deck claims a moat. Most describe a head start. These terms separate the two, and give you
the vocabulary to ask the follow-up question.

### Competitive moat
The structural reason a competitor with money and talent still can't take your customers.
**Picture this:** not "our tech is better." More like: every customer's four years of data lives here, three other
systems read from it, and the person who'd own a migration already said no twice.

### Differentiation
The specific thing you do that competitors don't, stated concretely enough that a customer could
repeat it.
**Picture this:** "we're faster and more intuitive" is not differentiation — every competitor says it. "We're the
only one that reads handwritten intake forms" is, because it's checkable and it's either true or
it isn't.

### Unfair advantage
Something this specific team or company has that a competitor can't simply decide to acquire —
access, data, a relationship, hard-won expertise.
**Picture this:** two founders spent nine years inside hospital revenue cycle teams. They know which twelve people
to call, what the workflow actually looks like at 2am, and why the last three vendors failed. A
well-funded competitor can hire engineers. It can't hire that.

### Category creation
Defining a new kind of product rather than competing inside an existing one, so buyers evaluate
you on terms you set.
**Picture this:** instead of being the twelfth CRM, you name the thing you do something nobody sells yet. Now
there's no feature comparison — but there's also no budget line, and someone has to create one.

### Substitute vs. direct competitor
A direct competitor sells something like yours. A substitute is whatever the customer uses
instead — including a spreadsheet, an intern, or nothing.
**Picture this:** the competitive slide lists four funded startups. The deals are actually lost to Excel and
"we'll revisit next year." Those two win more often than all four combined.

### Win-loss analysis
Systematically asking why deals were won or lost, from the buyer rather than from the
salesperson.
**Picture this:** the team believes they lose on price. Six buyer interviews later, the real answer is that the
security questionnaire took eleven days and a competitor answered in two.

### Positioning
The place your product occupies in the buyer's head — what kind of thing it is, who it's for,
and what it's better than.
**Picture this:** the same analytics tool positioned as "business intelligence for enterprises" competes with
entrenched incumbents and loses. Positioned as "the reporting layer for Shopify stores doing
$1M+" it's the obvious choice, at the same price.

### Messaging vs. positioning
Positioning is the strategic decision about what you are and who you're for. Messaging is the
words you use to say it.
**Picture this:** the positioning is "the reporting layer for mid-size Shopify stores." The messaging is the
headline, the cold email, and the first line of the demo. Change the words weekly if you like —
changing the position weekly means nobody knows what you sell.

### Tagline vs. value proposition
A tagline is short and memorable. A value proposition explains what you do and why it's worth
it. Confusing them costs you the buyer's first ten seconds.
**Picture this:** "Work, simplified." tells a visitor nothing. "Cut month-end close from nine days to two" tells
them whether to keep reading. One is a mood; the other is a claim.

---

## 16. Building the thing

The product side of judgment — what got built, how the team decides what to build next, and
which numbers tell you whether it is working.

### Minimum viable product (MVP)
The smallest thing you can build that produces a real answer to the riskiest question you have.
**Picture this:** the MVP for a marketplace was a spreadsheet and two founders manually matching people over
WhatsApp. It answered the only question that mattered — will both sides show up — without a line
of product code.

### Prototype vs. MVP
A prototype demonstrates an idea to people. An MVP is used by real customers to do real work.
**Picture this:** the Figma flow that gets nods in a meeting is a prototype. The rough version that a clinic used
to process actual claims last Tuesday is an MVP. Only one of them generated evidence.

### Activation
The moment a new user first gets real value — and the share of signups who reach it.
**Picture this:** for a document tool, activation might be "invited a teammate and edited a real file within seven
days." Users who cross that line retain at 60%. Those who don't, retain at 4%.

### Feature prioritization
Deciding what to build next, and — more importantly — what not to build.
**Picture this:** the roadmap has forty items. Engineering capacity is four per quarter. The decision isn't which
four are good ideas; thirty of them are good ideas. It's which four move the one number that
matters.

### Product roadmap vs. backlog
A roadmap is the sequence of outcomes you're pursuing. A backlog is the list of specific work
items waiting to be done.
**Picture this:** the roadmap says "cut time-to-first-value below ten minutes this quarter." The backlog holds the
forty tickets that might contribute. Showing a customer the backlog is how you accidentally make
forty promises.

### Technical debt
The future cost of a shortcut taken now — code that works today and makes tomorrow slower.
**Picture this:** hardcoding one customer's business rules ships the deal in a week. Two years and eleven
customers later, every new rule takes four days and touches nine files.

### Net Promoter Score (NPS)
One question — how likely are you to recommend this — scored 0–10, with promoters minus
detractors giving a number from -100 to +100.
**Picture this:** 40% score 9–10, 20% score 0–6. NPS is +20. It's a fine trend line and a terrible decision-making
tool on its own.

### OKRs
A goal-setting structure: an ambitious Objective, with a few measurable Key Results that say
what would have to be true to hit it.
**Picture this:** Objective: make onboarding effortless. Key results: activation from 22% to 45%, time-to-first-
value under ten minutes, support tickets per new account down by half. Not a task list — a set
of outcomes.

---

## Where this came from

- **[VC Lab / GoVCLab](https://govclab.com)** — the Venture Institute curriculum, fund mechanics,
  and [VC terms reference](https://govclab.com/2023/07/23/venture-capital-terms/)
- **[Ilya Strebulaev (Stanford GSB)](https://ilyastrebulaev.substack.com)** — most of the hard
  numbers here are his. Full archive read: the payout stack and pari passu, conversion decisions
  across rounds, the hold-up problem and mandatory conversion, the deal funnel, cold-pitch
  experiments, the YC filter, angel power-law rankings, unicorn founder backgrounds, university
  odds ratios, the VC 101 series, and the 2026 Strebulaev–Jackson ranking methodology.
- **[Foundersuite's 150-term glossary](https://blog.foundersuite.com/venture-capital-glossary-founders-vcs/)**
  and **[GoingVC](https://www.goingvc.com/post/90-essential-venture-capital-terms-a-comprehensive-glossary)** — deal terms and traction vocabulary
- **[Carta](https://carta.com/learn/private-funds/management/distribution-waterfall/)** and
  **[AngelList](https://www.angellist.com/learn/distributions)** — waterfall and distribution mechanics
- **[Y Combinator's post-money SAFE primer](https://www.ycombinator.com/documents)** — SAFE conversion math
- **[Lev Learn](https://getlev.co/learn)** — the founder-side vocabulary. Their concept library is
  what prompted sections 12–16 here, and it shaped which terms I decided were worth knowing from
  the other side of the table. The deep dives on this site are my own writing, not theirs — read
  their pages for their version.
- **[NVCA model documents](https://nvca.org/model-legal-documents/)** and
  **[ILPA principles](https://ilpa.org/principles-3-0/)** — the standard paper for financings and
  for LP/GP terms
- Primary sources cited on individual terms: Brad Feld on term sheets, Marc Andreessen on
  product-market fit, Paul Graham on default alive, Clayton Christensen on jobs to be done,
  Geoffrey Moore on beachheads, Ward Cunningham on technical debt.

Definitions and deep dives are written in my own words. Where a specific figure or case is cited,
it comes from the sources above.
