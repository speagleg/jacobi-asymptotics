# G3′ log

## 2026-10-13: Plan 7 execution

- **Setup.** Workspace created. Added the toolkit helper `merge_repeats`, with tests. `DiscreteMeasure.from_atoms`
  rejects duplicate atoms, so the checks merge equal atoms and add their weights first (Ruling, Plan 7 Task 1).
- **Sensitivity probe** (`checks/check_merge.out`, NUMERICAL).
  - [1] Making a fraction φ of the indices into double values shifts S_n by −0.17, −0.47 and −1.13
    (φ = 0.1, 0.25, 0.5; n = 4000). The predicted values are 2 log(1−φ) = −0.21, −0.58 and −1.39. The shifts still
    drift toward these slowly, like the O(1/log n) drift of S_n itself. The heuristic is not refuted, so Task 5 goes
    ahead.
  - [2] A defect confined to the index window [1000, 2000) is invisible for n ≤ 1500 and appears for n ≥ 2000. Only
    indices up to about n affect D_n at the n² scale.
  - [3] True zeros: see `.out`.
- **Citations.** (C1) Trudgian's Corollary 1 was read from the arXiv PDF and quoted. (C3) was read from
  arXiv:2501.14545 §1, which surveys simple-zero proportions; the best unconditional result quoted is > 40.75%.
  (C4) was ruled unnecessary (CITATIONS.md).
- **Z1, Z2, G3′-U** written. Rule A pass:
  - No step uses a lower bound on any γ_b − γ_a, checked line by line in §3.
  - The log γ̃_b factor of Z2 appears only for b ≤ Mn. Tail pairs are rescaled exactly.
  - H7 tolerates ties in G on the tail: its proof uses only 0 < G ≤ (Mn)⁻² there (item 11 §7b steps 2–3).
  - A potential issue checked: Z1 is proved only for γ_k ≥ 10⁶ (k ≥ k₁). The finitely many smaller indices are
    handled by the constant B (Z2, "small indices") and by c in Z1′. Both are positive and finite, so they cost O(n).
  - Numerical ratio check: `checks/check_ratio.out`.
- **G3′-L** written under (SG). Rule A pass:
  - *Danger: tail subsets.* The far-pair losses carry a log γ̃_a factor, so they are unbounded for deep indices. A
    pairwise uniform comparison (as in the H_L lower bound) therefore fails. This was resolved by turning the losses
    into weights a^{−C log n} and proving Lemma W: item 11's log-convexity weight step loses only (s−3)·K n log n,
    uniformly in s. With s_n ≍ log n the loss is O(n log² n).
  - Lemma S checked numerically: `checks/check_shift.out` (min ratio 1.0005 ≥ 1).
  - (SG) gives π(j) ≤ (1+2η)j eventually: yes, since #bad ≤ ηK.
- **Proposition N.** A rigorous obstruction (mod Theorem H): smooth ordinates with every m-th value doubled have the
  same counting information, yet the law fails by 2 log(1 − 1/m). The general converse (GAP N′) needs a deletion lemma
  for clustered index sets; it is not proved.

## Stop: the unconditional lower bound needs inputs beyond (C1) (Prop N); hardness not established (GAP N′)

The unconditional lower bound of G3′ needs information that the counting function does not give (Prop N), for example
about multiplicities or small gaps. The sufficient input (SG) implies that almost all ordinates are simple values
(horizontal multiplicity 1, (C3) §1.3). In the
literature read (CITATIONS.md (C3)), the best unconditional simple-zero proportion is > 40.75%, and no surveyed
result, conditional or not, reaches proportion one. G3′ is therefore closed in the following form:

- **G3′-U:** unconditional (PROVED-mod-cite (C1) on top of item 11).
- **G3′-L:** PROVED-mod-input (SG).
- **Prop N:** counting information is insufficient (PROVED-mod-input Theorem H).
- **GAP N′:** general deletion. It would make density-zero repeated ordinates necessary. Together with (SG) being
  sufficient, this sandwiches G3′; it is not an equivalence.

- **Rule R (2026-10-13):** ACCEPT WITH FIXES (`review/REVIEW_G3prime.md`). Fixes applied the same day: Z1 (2E bound,
  analytic C₀, all-k form); Z2 (small indices for all b > a); G3′-L (ℓ_n bound with the (1+log n)² term and the
  min(n−1, ·) near count, e^{−C(1+log n)²} weights, π(j) ≤ C_η j, lower sum/denominator factors, far-partner case
  split); N ((log h)′ proof, sup domain, |π − ψ| ≤ 1); N′ and stop-condition framing corrected.

## 2026-10-13: G3′* (own-atom normalization)

- **Probes** (`star/`, NUMERICAL).
  - Thinning with convergent density keeps the own-normalized law.
  - Log-periodic holes break it, with a shift that does not decay.
  - Near-duplicates down to 10⁻⁵ of the spacing are harmless.
- **Theorem T** (thinning, convergent density), **G3′*-U** under (D∞), **G3′*-L** under (D∞) + (SG*): §7.
- **Rule R, first pass** (`review/REVIEW_T.md`). Accept with fixes for everything except G3′*-L, which was rejected
  for an order-of-limits gap. Repaired with a two-scale near-pair split (Lemma K at M₁ and M₂).
- **Rule R, re-review.** G3′*-L: ACCEPT WITH FIXES (editorial: J′-rank indexing, L_{y′} vs L_{E′} normalization, the
  C_θ constant, status rows). Applied, so all of §6–§7 is REVIEWED.
- **Outcome.** No unconditional proof. The obstruction is relocated from "density-one simplicity" (SG) to
  (D∞) + (SG*), which allow multiple zeros and off-line symmetric pairs at any convergent density. Neither (D∞) nor
  (SG*) is supplied by the literature read; (C3) gives only liminf N_d/N ≥ 0.4075.

## 2026-10-14 — Plan 17 (unconditional bounded defect; PCC ⇒ G3′)
- **Inputs read:** GLSS arXiv:2503.15449v4 ((6.1), PCC, Theorems 1–2), and Lamzouri arXiv:2609.02882v2 (Theorem 1.1;
  context). Fujii's second moment is quoted from GLSS (secondary).
- **Rule A (adversarial pass, before the write-up).**
  - Pairs of off-line zeros make BGST's complex-weighted pair sums indefinite. This rules out counting close pairs
    among critical zeros via Lamzouri's Hilbert-space identity. Ruling: use GLSS's vertical-distance formula (6.1), all
    of whose terms are nonnegative.
  - Fujii's O-constant is not explicit. Ruling: θ₀ / C is not explicit.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan17.md).
  - F1 (major): Caro–Wei sets need not have a convergent density, so the Theorem T route has a gap. Repaired by
    Fix A: run the §4 G3′-L proof on the separated subset, with Lemma S at a constant C.
  - F2–F9 (minor) applied. Re-check: ACCEPT (N1–N2 wording applied). Theorems B, C REVIEWED.
- **Outcome:**
  - unconditionally, D := liminf (1/n²)[log D_n − Φ_n] ∈ [−3 log C, 0];
  - G3′ ⇐ PCC (no RH);
  - G3′ ⇒ d_*(repeats) = 0 (N′).

## 2026-10-14 — Plan 19 (RH-free route to G3′: Theorem S)
- **Inputs read:**
  - (C3) BGST arXiv:2501.14545v3: §2.1 multiset Z(T); §3 MT (3.1)–(3.2), corrected errors, dyadic window;
    positivity (3.6)–(3.7).
  - (C6) Lamzouri arXiv:2609.02882v2: Prop 2.1 and its proof; §3 Lemmas 3.1–3.2 and (3.2)–(3.3).
- **First draft (stalled).**
  - Approach: restrict Goldston's Thm-4 argument to critical–critical pairs, with off-line pairs bounded by a local
    zero-density "Lemma A′".
  - Rule A: kernel growth T^{2M|β−½|} beats Selberg-type density for M ≥ ⅛, which is a recollection, not cited. So the
    route stalls.
- **Rule A ruling reversed.** Plan 17's Rule A ruled that indefinite complex-weighted sums prevent counting close
  pairs via Lamzouri's identity. That ruling is superseded for *upper-bound* counting:
  - individual terms are never used;
  - Lamzouri's operator A has tr A = N and ‖A‖²_HS = S, so Σ(μ − 1)² = S − 2N + N_d;
  - near pairs force small Gram eigenvalues (Lemma G, deterministic).
  Lemma PC bounds S above under the one-sided SPC_ℂ⁺ (exact weight removal, any support).
- **Rule A pass on Lemma G (before the review):**
  - Weyl perturbation bound for intervals (2·rank);
  - zero-eigenvalue bookkeeping;
  - chain factor 2;
  - numerics `rhfree/checks/check_spectral_sg.py`.
  The Rule R reviewer's adversarial search (3000 configurations) found no violation.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan19.md). No major findings. F1–F8 and N1–N2 applied (N3 at promotion). Re-check: ACCEPT (R1–R2 wording applied). REVIEWED. Fixes:
  - dyadic-SPC wording;
  - §4 retitled (quasi-RH at most, not RH);
  - Step 1 made self-contained;
  - quotes added;
  - Theorem S(b) details.
- **Outcome:** SPC_ℂ⁺ (upper half of the dyadic complex-weighted SPC, bounded range per tolerance; no RH) ⇒
  100% simple critical zeros, small gaps ≪ δ³, (SG), G3′ (mod Theorem H). Novelty UNCHECKED.

## 2026-10-14 — Plan 20 (open questions after Theorem S)
- **Inputs read:**
  - (C3): (3.5), the "two changes" remark, and the Lemma-1 remark.
  - (C8) §9: Theorem 7 and its proof, (9.7)–(9.9).
  - [BGSTB24] and Goldston–Montgomery [18] were NOT read.
- **Results:**
  - Theorem S′ (full window; on RH, the upper half of Montgomery's SPC suffices).
  - Lemma N (Sylvester inertia + Ky Fan): E ≥ k + 4Σ m_z dist(h_z, V)².
  - Proposition Q: SPC_ℂ⁺ + (NA) ⇒ quasi-RH. (NA) is a hypothesis: synthetic numerics only, vacuous on RH.
  - Prime side: the Theorem 7 route loses a constant C > 1 (heuristic), and Lemma G needs C → 1. Reduced to a
    weighted Lemma G (OPEN).
- **Rule A.**
  - Full-window positivity was sourced only through an unread lemma. It is now self-contained via a residue identity
    (numerically 2e-31).
  - (NA) for λ ≤ ½ fails numerically (near-completeness). So Proposition Q uses λ_j → ∞.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan20.md). No major findings. F1–F12 applied. Re-check: ACCEPT (R1 quote x²; R2 applied). REVIEWED.

## 2026-10-14 — Plan 21 (RH + one-sided prime variance ⇒ G3′)
- **Inputs read:** (C8) (4.1)–(4.4) and §9, (9.4)–(9.9) (raw re-extraction confirms the error terms); (C3) (3.5).
  [18] was NOT read.
- **Idea.** Keep Goldston's Fejér weight on the zero side, with G = R/(2xκ²) and Ψ ∈ [0, 1], so there is no
  Tauberian step. On RH, K² ≥ 0, so counting needs positivity only.
- **Rule A.** The sinc² oscillation breaks a naive Stieltjes integration by parts at infinity. Fixed by truncating at
  ΛT = T log²T, with dyadic variation bounds.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan21.md). F1 (medium: main-term error near α = 1) fixed. F2
  (medium: P1 depends on a sketched (9.9)) relabelled; a self-contained proof is OPEN (V5). F3–F12 applied. Re-check: ACCEPT (R1 quote added; R2, R3 applied). REVIEWED.

## 2026-10-14 — Plan 22 (self-contained (9.7) and (9.9))
- **Inputs read:** (C8) PDF pp. 4–7 (Prop. 1, (3.4), (3.11)–(3.14)) and pp. 19–20 ((9.4)–(9.9)).
- **Lemma 9.7*:** G_κ = FT of κ⁻¹Δ(e^{s−κ/2}), then Plancherel, then Prop. 1. This gives L = R + O(log²T/T).
- **Lemma 9.9*:** Δ = a_y D + R with |R| ≪ κa_y√y log²y; the exact by-parts identity gives the main term; Cauchy–Schwarz
  gives a full-range error.
- **Numerics:** `rhfree/checks/check_99`, on actual primes.
- **Effect:** Theorem V⁺ no longer depends on statements that are only sketched in (C8).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan22.md). F1–F9 applied; RHPRIME P1 body rewritten (F2). Re-check: ACCEPT (R1–R3 applied). REVIEWED.

## 2026-10-14 — Plan 23 (residual N′ case closed: Theorem N″)
- **Idea.** The Heine index sets of σ that contain a collision pair vanish.
  - A move map plus the pure-power head of G3′-U's comparison measure ν turns this into a deletion bound.
  - Hadamard's inequality on det(I − K_E) shows that deletion costs are superadditive (they at least add up).
  - A Lagrange test polynomial (Christoffel) shows that head atoms are saturated, at cost ≥ 2n·g(k/n).
  - Result: d̄(E) > 0 ⇒ liminf ≤ −0.2397·d̄(E). Hence G3′ ⇒ d(E) = 0.
- **Rule A.** Long-double deletion numerics disagreed with 300-digit values by up to about 20%. All recorded evidence
  is now exact mp (`checks/check_npp`).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan23.md). F1–F10 applied (in the plan-24 worktree, together with the N‴ θ₀ fix). Re-check: ACCEPT (R1–R3 applied). REVIEWED.

## 2026-10-14 — Plan 24 (Theorem N‴; the sufficiency obstruction)
- **N‴.** Gaps ≤ e^{−βk} at positive upper density break G3′.
  - Proof: twin pair factor ε_k ≲ (log k)²g_k in G3′-U, then the expansion Π(ε_k² + avoidance).
  - The avoidance term uses the §5.2 move map plus Hadamard plus saturation.
- **Attempted (route via G3′-L step 6 only):** weaken (SG) to "d(E) = 0 + Σ log⁺(1/g) = o(K²/log K)" in G3′-L. This failed.
  - G3′-L folds near costs into weights compared with j^{−s_n} (s_n ~ log n). A per-element cost A log²a is not
    dominated for a ≫ n^{O(1)}.
  - Truncating the comparison measure at N needs Σ_{l>N}w_l·D_{n−1}/D_n ≪ 1, i.e. log N ≳ n log n, which
    reintroduces the cost. (Superseded by Plan 25's Lemma Tr.)
  - Recorded at the time as OPEN (N‴1). Later superseded by Plan 25's Lemma Tr.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan24.md). F1–F9 applied. Re-check: ACCEPT (R1–R3 applied). REVIEWED.

## 2026-10-14 — Plan 25 (Theorem L′: log-gap sufficiency)
- **Idea.** In G3′-L, restrict the Heine sum to the window [1, Mn] and bound the near-twin costs directly, by
  C log n·Σ log⁺(1/g), instead of folding them into weights.
- **Lemma Tr.** Truncating the pure-power comparison at Mn costs only O(n²/log M), via det(I − K_A).
  - Lagrange on n nodes in (n, 2n] gives the spectral gap e^{−O(n)}.
  - Convexity of −log(1 − λ), and Lemma K bounds E#tail.
- **Result:** (LG*) ⇒ G3′. (LG*) contains (SG), and also "d(E) = 0 + Σ log⁺(1/g) = o(K²/log K)".
- **Remaining:** gap sequences satisfying neither (LG*) nor N‴'s condition. These are not ordered "between".
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan25.md). F1 (the false "O(1) truncation" remark), F2 (the
  convexity step rewritten), F3–F9 applied. Re-check: ACCEPT (R1: Lemma Tr is PROVED-mod-input Theorem H; R2, R3 applied). REVIEWED.

## 2026-10-14 — Plan 26 (Theorem Ch: exact characterization)
- **Observation.** The earlier log-K losses were bookkeeping. The cost is pair energy, capped by drop costs.
- **Necessity.** Group the Heine sets by T = S ∩ W, W = [k₂, ⌊θn⌋]. Each group is ≤ e^{−2P_ε(T)}·D_n(ν ∖ (W ∖ T)), and Hadamard plus
  saturation charge ≥ 2n·g(θ) per drop. Summing over 2^{θn} choices costs e^{O(n)}. No move map is needed.
- **Sufficiency.** Run the L′ argument on the optimal T for each n. It drops o(n) indices, so the index shift costs
  o(n²); then Lemma Tr.
- **Result:** G3′ ⟺ 𝒞(K) = o(K²). N″, N‴ and L′ are corollaries; the former sliver example satisfies G3′.
- **Numerics:** `checks/check_clusters` (exact) shows m² pair-energy scaling and capping.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan26.md). F1–F12 applied. Re-check: ACCEPT (R1 applied). REVIEWED.

## 2026-10-14 — Plan 31 (Ch's criterion on the zeta zeros; NUMERICAL)
- On 2M Odlyzko zeros, P(K)/K → 0.227, approaching c_GUE = 0.241. So 𝒞(K)/K² ≲ 0.23/K: about 1.1·10⁻⁷ at K = 2·10⁶.
- The smallest normalized gap is 5.45·10⁻³. There are 255 gaps < 0.05, against the GUE proxy ≈ 274.

## 2026-10-14 — Plan 43 (D1: positioning G3′; PROOF.md §5.6)
- **Sources read (PDFs, arXiv):** GLSS 2503.15449v4 (abstract, §§1–3, §7, §8 head); Lamzouri 2609.02882v2 (abstract,
  §1 to Remark 1.2); Goldston math/0412313 (§5 Theorem 2 and after, §6 (6.8)–(6.11)). Quotes added as CITATIONS (C5),
  (C6), (C8) Plan 43 addenda.
- **Proved (§5.6):**
  - Lemma L (off-line zeros pair on one ordinate, from GLSS §2) and Lemma CI:
    N − N_dist ≤ N − N₀ˢ ≤ N − A ≤ 2(N − N_dist), with |E ∩ [1, N(T)]| = N − N_dist.
  - Proposition I: ½δ_sc ≤ d̄(E) ≤ δ_sc, so d(E) = 0 ⟺ 100% of zeros simple and on the critical line.
  - Corollary Lz: d̄(E) ≤ 1 − C_Lz = 0.32749… unconditionally, from (C6) Thm 1.1 ((C6)'s "C0", renamed in PROOF;
    arXiv v2 preprint). It replaces §5.5's 0.5925. The novelty note in research/program/novelty_G3p.md is corrected:
    the update comes from C_Lz, not from 83.62% distinct zeros, which count zeros, not ordinates.
  - Lemma D: 𝒞(K) = 𝒞_dist(K) + K·|E ∩ (k₂, K]| exactly (pairs at normalized distance < 1 are automatically near).
    Hence Theorem Sp: G3′ ⟺ d(E) = 0 ∧ 𝒞_dist(K) = o(K²).
  - Corollary Pos: G3′ ⇒ 100% simple and critical.
- **Stop condition (AGENTS.md, "a step is as hard as an open problem").** An unconditional proof of G3′ would prove
  (100%-SC). The sources read obtain (100%-SC) only under hypotheses: PCC or HMH (GLSS Theorems 1–2), RH + SPC
  ((C8) Thm 4 via SZC); see also this repo's Theorem S (SPC_ℂ⁺) and Corollary P (RH + (V)). They quote Montgomery's
  conjecture for its simplicity part (GLSS abstract). Their best unconditional proportion is C_Lz = 0.6725 ((C6),
  preprint).
  Goldston (C8, 2004) writes, on simplicity, "a major advance … even on RH". Recommendation (outline §1.5), pending
  Rule R: close the main line of G3′ at U unconditional, B bounded defect, exact characterization Ch/Sp, and
  positioning Pos. This is a statement about
  difficulty only; nothing here is evidence about RH or about (100%-SC).
- **Correction to research/program/outline_D_G3p.md §1.2 (a [derived here] claim):**
  - "d(E) = 0 ⟺ HMH" is false as an elementary deduction. Only HMH ⇒ d(E) = 0 holds (GLSS Thm 2 + Prop I).
  - A partial converse holds: |E ∩ [1, K]| = o(K/log K) ⇒ HMH (Lemma CI(iii)).
  - G3′ ⇒ HMH and G3′ ⇒ SZC are NOT established (GAP).
- **Rule A (attempts logged):**
  - (1) Can two distinct critical zeros share an ordinate? No: they would be the same point.
  - (2) Off-line ρ with 1 − ρ̄ = ρ? Only if β = ½.
  - (3) Could nontrivial zeros on Re s ∈ {0, 1} make (C6)'s N(T) differ from (C1)'s? No, by GLSS §2's strip statement.
  - (4) Lines straddling the boundary k₂ or K: handled by R_K := ([k₂, K] ∖ E) ∪ {k₂} and by counting at T = γ_K
    (whole lines).
  - (5) Near-ness in 𝒞 depends on indices (through γ̃), not values. Resolved: for indices ≥ k₂, d_ab < 1 forces near,
    by Z1 and γ ≥ 10⁶.
  - (6) Sharpness of the factors 1 and 2 in CI(ii): examples H = 3 (simple critical zero plus an off-line pair) and
    H = 2 (an off-line pair).
  - (7) Converse d(E) = 0 ⇒ HMH: counterexample at the level of counting (lines of multiplicity h_T → ∞), recorded.
- **Numerics (sanity, toy configurations, not zeta data):** `checks/check_positioning` → `.out` [1]–[3].
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan43.md). Fixes applied:
  - F1: "only from PCC or HMH" became "only under hypotheses" (adds (C8) Thm 4, Theorem S, Cor P).
  - F2: dated correction notes in research/program/outline_D_G3p.md and RESEARCH_PROGRAM.md §D (separate docs:
    commit).
  - F3: Lamzouri's constant renamed C_Lz.
  - F4: dated qualifier on §5.5's "not claimed" sentence.
  - F5: this entry ("corrected").
  - F6: (C6) preprint status noted at Cor Lz and in the §0 row.
  - F7: Lemma CI relabelled; H(v) ≤ 2E(v) cited from (C1) directly.
  - F8: P3 reworded around the quotes.
  - F9: optimality remark at Cor Lz.
  - F10: sharpness of the middle inequality; counting example rephrased.
  Re-check ACCEPT — REVIEWED.
