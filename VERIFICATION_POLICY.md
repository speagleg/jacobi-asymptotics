> Adapted from math-pursuits VERIFICATION_POLICY.md (commit f5f6aef). Changes for this repo: the label
> PROVED-mod-input (proved modulo a named Lean/structure input listed in lean/JacobiAsym/Inputs.lean) is added;
> "item" means a research problem under research/ (G3prime, G2, G1) or a toolkit module.

# Verification policy — math-pursuits

Adopted 2026-10-07. Replaces the 8-section audit used in the source repos, whose failure modes
are documented in `reviews/`. Each rule below exists because the old pipeline let a specific
error through.

## Labels
| Label | Meaning | Required evidence |
|---|---|---|
| PROVED | Complete proof, every step checked | Written proof; every external theorem quoted with hypotheses (rule C); adversarial pass logged (rule A); second-reader review |
| CERTIFIED | Finite computation with rigorous error control | Interval/ball arithmetic over every operation, explicit truncation/tail bounds, no hard-coded flags, reproducible script (rule N) |
| NUMERICAL | Strong numerical evidence | High-precision computation, precision-doubling stability, stated precision |
| CONJECTURE | Supported pattern | State the evidence and its limits |
| KNOWN | Already in the literature | Reference to the exact statement |
| RETRACTED | Found false | Counterexample or identified error |

Novelty is a separate field: NEW / POSSIBLY-NEW / KNOWN / UNCHECKED. Default is UNCHECKED.

**Labels used in this repo (Plan 37, 2026-10-14).** Sources: PROVED-mod-cite from the G2 PROOF.md header; CONDITIONAL
and GAP from the G1 PROOF.md header; PROVED-mod-input from the note at the top of this file; REVIEWED from Rule R below;
the remaining rows describe how the labels are used in research/ (revised after Rule R, G2/review/REVIEW_Plan37.md F8).
| Label | Meaning |
|---|---|
| PROVED-mod-cite (X) | Proved from explicitly cited external results X, each read and quoted with its hypotheses in a CITATIONS.md (rule C); the hypotheses are checked in the application. (G2 header; item 11's convention.) |
| PROVED-mod-input (X) | Proved modulo a named input X listed in `lean/JacobiAsym/Inputs.lean` (e.g. `TheoremHPure`; see the note at the top of this file). Usage note: G3′ also writes "mod-input" for stated hypotheses on the zeros ((SG), (LG*), PCC, SPC_ℂ⁺, RH, (V), (V⁺), (D∞), (SG*)); G1 calls results of that kind CONDITIONAL. |
| CONDITIONAL | Proved assuming a stated hypothesis that is not a named Lean input. (G1 header.) |
| GAP | A precise unproved statement, with no claim about its difficulty. (G1 header.) |
| REVIEWED | Rule R done: an independent second reader re-derived the key steps and the fixes were applied. Combined with the labels above (e.g. "PROVED-mod-cite + REVIEWED"); it does not upgrade them. |
| PROVED-mod-G2 | Proved using a result of research/G2 as an internal input (RH_zeta E1); inherits G2's labels. |
| PROOF SKETCH / DRAFT | A written argument that is not a proof (steps missing or rejected by review); never cited as a proof (e.g. RH.md, RH_proof.md). |
| REFUTED | A conjectured or hoped-for statement shown false in the stated generality (e.g. (T3) for rough weights, by Theorem R). RETRACTED is reserved for a claim of this repo that was found false. |
| SUPERSEDED | Still valid, but contained in a later result, or replaced by a later construction; the file says by which. |
| HYPOTHESIS | A named assumption (e.g. (SG), (NA), (V⁺)), stated precisely and not proved; results using it are mod-input / CONDITIONAL. |
| OBSTRUCTION | A recorded reason why a specific proof route fails; heuristic unless stated otherwise, and not a claim about all routes. |
| HEURISTIC | An argument or explanation that is not a proof and is not used as one. |
| sorry-free | A Lean declaration whose proof contains no `sorry` and passes `lean/check.sh` (axioms audit: only `propext`, `Quot.sound`, `Classical.choice`). PROVED-mod-input Lean theorems are sorry-free modulo their named-input hypotheses. |

## Rule C — citations
1. Quote each external theorem verbatim (or precisely paraphrased), with every hypothesis, plus
   source and theorem number, from a source the agent has actually read.
2. Check that each hypothesis holds in the application, explicitly.
3. "Classical", "well known" and "standard" are not citations.
4. Watchlist of previously misused results: Hutchinson; Pólya 1918/1926; Newman 1976; Karlin TP₂;
   Prékopa–Leindler; Laguerre–Pólya / Pólya–Jensen criterion (all degrees, all shifts, using
   γ_k = k!·a_k); Griffin–Ono–Rolen–Zagier (fixed d, large n); Chasse 2013; Calegari–Geraghty;
   Kim–Shahidi / Gelbart–Jacquet / Newton–Thorne; Montgomery 1988; Liouville's approximation theorem;
   Mineyev–Yu / Kadison–Kaplansky; Ostrik rank-2 classification; Freedman–Larsen–Wang.

## Rule N — numerics
1. "Certified" requires enclosures (Arb, `mpmath.iv`, Mathematica `Interval[]`, exact PARI). A
   difference between two precisions is not an error bound.
2. Finite checks of a universally quantified statement are NUMERICAL, unless an analytic bound
   covers the rest and that bound is itself proved with explicit constants.
3. Pass/fail values must be computed, never typed into an export.
4. Saddle-point and asymptotic arguments must state the saddle equation exactly and give explicit
   error bounds. (A wrong saddle produced errors of 10³–10³⁷⁰ in the source corpus.)
5. Normalisations must be written out (k! vs (2k)! vs γ_k; Γ_R(s)=π^{−s/2}Γ(s/2), Γ_C(s)=2(2π)^{−s}Γ(s)).

## Rule A — adversarial pass
Before PROVED, for each lemma: try to construct a counterexample (small cases, degenerate
parameters, two-point measures, step functions); test the converse if it is used; check every
"by symmetry" and "the cross term vanishes". Log attempts.

## Rule X — circularity
Inputs that presuppose the conclusion (zeros placed on the line; PSLQ fitted to the formula being
tested; identities that are the definition rewritten) cannot be evidence. State the data provenance.

## Rule L — literature
Before NEW or POSSIBLY-NEW: check all item README §4 references, search arXiv/MathSciNet-style for
the precise statement, and record queries and findings in LOG.md. One web search is not a check.

## Rule R — review
DONE requires REVIEWED: a human or a second independent agent re-derives the key steps from the
write-up alone and re-runs the checks. LLM self-review does not count as the second reader.

## Optional — formalisation
For short statements, write a Lean 4 / Mathlib statement in the style of the openai/math "comparator
challenges": a small human-audited statement file, the proof kept separately, allowed axioms
`propext`, `Quot.sound`, `Classical.choice`. Lean is not installed yet; installing it needs human approval.
*(Stale — Plan 37 note, 2026-10-14: in this repo Lean 4.34.1 + Mathlib are installed and used; see AGENTS.md
"Environment" and lean/README.md.)*
