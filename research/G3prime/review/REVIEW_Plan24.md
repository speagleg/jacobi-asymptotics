# Rule R review: Plan 24 (PROOF.md §5.3, Theorem N‴; Remark N‴1; check_twins)

Reviewer: independent Rule R referee (adversarial). Target: worktree ja-plan24, branch plan-24-nppp, commit 9a10b30
(N‴ content from 08edf11, θ < θ₀ edit from 953ac5a).

Read:
- AGENTS.md; PROOF.md §0 (N‴ row), §1, §2 (Z1, Z1′), §3 (Z2, G3′-U steps 1–7), §4 (definition of g_k; G3′-L step 6),
  §5 (E, N′), §5.2 (Lemma H, Lemma Sat, N″ proof, reviewed in REVIEW_Plan23.md), §5.3 (all), "G3′ status after N′";
- LOG.md Plan-24 entry; README.md diff (HEAD~3..HEAD); docs/superpowers/plans/2026-10-14-plan-24-nppp.md;
- checks/check_twins.py and check_twins.out.

Numerics: I re-ran `.venv/bin/python ../ja-plan24/research/G3prime/checks/check_twins.py` from jacobi-asymptotics
(9 s, not 10–30 min). The output is byte-identical to `check_twins.out`. Scratch scripts (exact rationals / mpmath)
are described under "Independent checks".

## Verdict: ACCEPT WITH FIXES

Theorem N‴ is correct as stated, with the stated constant. I re-derived every step (twin pair factor, its insertion
into G3′-U, the expansion inequality, the (k+1 → k) move map with all pair cases, the application of Lemma H + Lemma
Sat to ν ∖ (F+1), the product, the parameters and the order of limits) and found no error affecting the conclusion
G3′ ⇒ d(T_β) = 0 for every β > 0. The fixes are an index slip in the T_β ⊇ E claim, presentation gaps in steps 1, 2
and 4, wording of Remark N‴1 (the obstruction is to one route, and the "sharp condition" is heuristic with a
redundant clause), and the numerical illustration (script docstring and printed column do not match what is computed;
the "≈ min(2 log(1/g), C(k,n))" heuristic holds only for increments and with cap C(k+1, n)).

No major findings. Medium: F1, F2, F3, F4. Minor: F5–F9. Info: F10–F11.

## Checked and OK

### Step 1 (scales)
- |T_β ∩ [1, θ₁K/θ)| < θ₁K/θ = η′K/2, so |T_β ∩ [θ₁K/θ, K]| ≥ η′K/2. ✔
- Keeping every third element of the enumerated set gives consecutive kept elements at distance ≥ 3 and
  |T′| ≥ ⌈(η′K/2)/3⌉ ≥ η′K/6. ✔ (Distance ≥ 2 already suffices, see F10.)
- n := ⌈(K+1)/θ⌉ gives θn ≥ K + 1, so k + 1 ≤ θn for k ∈ T′, and K ≥ θ(n−1) − 1, so |T′|/n ≥ η′θ/6 − O(1/n). Lower
  end: θ₁n ≤ θ₁((K+1)/θ + 1) = η′K/2 + O(1), so k ≥ θ₁n − O(1) (see F5). ✔
- For K large, every k ∈ T′ is ≥ η′K/2 ≥ max(k₂, 2). ✔

### Step 2 (twin pair factor) — Review focus 1
- x_k − x_{k+1} = (γ_{k+1} − γ_k)(γ_{k+1} + γ_k)/((γ_k² + ¼)(γ_{k+1}² + ¼)) ≤ (γ_{k+1} − γ_k)·2γ_{k+1}/(γ_k²γ_{k+1}²)
  = 2(γ_{k+1} − γ_k)/(γ_k²γ_{k+1}) ≤ 2(γ_{k+1} − γ_k)/γ_k³. So the stated constant 4 holds, and γ_{k+1} ≤ 2γ_k is not
  even needed. With γ_{k+1} − γ_k = 2πg_k/log(γ_k/2π) (γ_k > 2π for all k) this is ≤ 8πg_k/(γ_k³ log(γ_k/2π)). ✔
- G(k) − G(k+1) = (2k+1)/(k²(k+1)²) ≥ k⁻³ ⇔ k² − k − 1 ≥ 0, true for k ≥ 2; both k, k+1 ≤ θn < Mn, so G is the pure
  power there. ✔
- Λ = max(L(Mn), λ) ≥ L(Mn) ≥ L(1) > 0 (L nondecreasing, §1). ✔
- ε_k := (x_k − x_{k+1})/(Λ(G(k) − G(k+1))) ≤ 8πk³g_k/(L(1)γ_k³ log(γ_k/2π)) ≤ C(log k)²g_k (γ_k ≍ k/log k by Z1),
  so (log k)³ is a valid over-estimate. Repeats give ε_k = 0, consistent with term_σ = 0. ✔
- **Insertion (head pair? termwise?).** k + 1 ≤ K + 1 ≤ θn < Mn, so {k, k+1} ⊂ S is always a head pair. G3′-U step 3
  bounds Σ_{pairs}2 log ρ* ≤ O(n log²n) *uniformly in S*, and every summand is ≥ 0 (ρ* ≥ 1). Replacing the factor
  (ρ*Λ)² of the pairs {k, k+1} ⊂ S by (ε_kΛ)² removes nonnegative summands, so the remaining aggregate is still
  ≤ O(n log²n) and the Λ-count n(n−1) is unchanged. The weight factor is identical (ν carries σ's weights). Hence
  term_σ(S) ≤ e^{O(n log²n)}Λ^{n(n−1)}term_ν(S)Π_{k∈T′}ε_k^{2X_k(S)} for every S, with the same O-constant. ✔ (F3:
  say this in the text.)

### Step 3 (expansion) — Review focus 2
- For fixed S let A := {k ∈ T′ : X_k(S) = 1}. The right side counts term_ν(S) once for each U ⊃ A with weight
  Π_{k∈U}ε_k² ≥ 0; the U = A summand alone is Π_{A}ε_k² term_ν(S). All other summands are ≥ 0. Infinite sums of
  nonnegative terms, so rearrangement is free. ✔ (Valid whether or not ε_k < 1.)

### Step 4 (move map, deletion) — Review focus 3
- **Well-definedness.** If k+1 ∈ S and k ∈ F, then k ∉ S (S avoids F-pairs), so the image k is free. Two moved
  elements k+1, k′+1 have distinct images. An image k cannot coincide with another moved original k′+1 (would need
  |k − k′| = 1). Hence S′ is an n-set. ✔
- **S′ ∩ (F+1) = ∅.** Every element of S ∩ (F+1) is moved; images lie in F, and F ∩ (F+1) = ∅ since spacing ≥ 2. ✔
- **Preimages.** Given S′, a preimage is fixed by choosing, for each k ∈ F ∩ S′, whether it was k or k+1: ≤ 2^{|F|}. ✔
- **Per-move cost ≤ k².** term_ν(S)/term_ν(S′), attributed to the moved elements:
  - weight w_{k+1}/w_k = x_{k+1}/x_k ≤ 1 (x nonincreasing; here x_{k+1} ≤ x_k, typically strictly). ✔
  - larger partner b (unmoved head, or tail with G(b) ≤ (Mn)⁻² ≤ G(k+1)): moving to the larger atom G(k) increases
    the distance, ratio ≤ 1. ✔
  - two moved elements k+1 < k′+1: both shift by −1; t ↦ t⁻² − (t+m)⁻² decreasing gives ratio ≤ 1. ✔
  - smaller unmoved partner j ≤ k − 1 (j ≠ k since k ∉ S): ratio = 1 + (G(k) − G(k+1))/(G(j) − G(k)) ≤ 1 + 1/(k − j),
    since G(k) − G(k+1) ≤ 2/k³ and G(j) − G(k) ≥ 2(k − j)/k³ (MVT, f′ = −2t⁻³ decreasing in absolute value). Squared
    and multiplied over j = 1, …, k−1: Π_{m=1}^{k−1}(1 + 1/m)² = k². ✔
- So Σ_{S avoiding F-pairs}term_ν(S) ≤ 2^{|F|}Π_{k∈F}k²·D_n(ν ∖ (F+1)) ≤ e^{O(|F| log n)}D_n(ν ∖ (F+1)). ✔
- **Lemma H + Lemma Sat on ν.** Head atoms G(j) = j⁻², j ≤ n, distinct; every l > n has 0 < G(l) < n⁻² (l ≤ Mn: l⁻²;
  l > Mn: ≤ (Mn)⁻²); tail ties allowed (F5 of Plan 23). Index k + 1 < n since k + 1 ≤ θn < n. Lemma H gives
  D_n(ν ∖ (F+1))/D_n(ν) ≤ Π_{k∈F}(1 − ρ_n(k+1)); Lemma Sat gives 1 − ρ_n(k+1) ≤ exp(−2n·g((k+1)/n) +
  log(W_{>n}/w_{k+1})), with W_{>n} ≤ Σ_l 2x_l < ∞ and w_{k+1} = 2x_{k+1} ≫ (log n)²n⁻², so the log is O(log n)
  uniformly in k ≤ n. g is decreasing on (0, ½] (g′ ≤ −3) and (k+1)/n ≤ θ < θ₀ < ½, so g((k+1)/n) ≥ g(θ) > 0. ✔

### Step 5 (product)
- With F = T′ ∖ U: Σ_U Π_Uε_k²·Π_{k∈T′∖U}e^{−2ng(θ)+O(log n)} = Π_{k∈T′}(ε_k² + e^{−2ng(θ)+O(log n)}) (binomial
  identity; the move cost e^{O(|F| log n)} is absorbed per factor). ✔
- ε_k² ≤ C²(log k)⁶e^{−2βk} ≤ e^{−2βθ₁n + O(log n)} using k ≥ θ₁n − O(1); a + b ≤ 2max(a, b) gives each factor
  ≤ e^{−min(2βθ₁, 2g(θ))n + O(log n)}, and 2βθ₁ = βθη′. ✔

### Step 6 (conclusion, order of limits)
- log D_n(σ) ≤ n(n−1)log Λ + log D_n(ν) − |T′|·n·min(βθη′, 2g(θ)) + O(|T′| log n) + O(n log²n). With G3′-U steps 5–7
  (H7 for D_n(ν) at fixed M, H6 for Λ) along the subsequence n_K = ⌈(K+1)/θ⌉ → ∞:
  (1/n²)[log D_n(σ) − Φ_n] ≤ A₂²/(8 log M) − (η′θ/6)min(βθη′, 2g(θ)) + o(1). liminf over all n ≤ limit along the
  subsequence; then M → ∞ (the left side does not depend on M), then η′ ↑ η. Final constant −(ηθ/6)min(βθη, 2g(θ))
  matches the statement. ✔
- "Hence G3′ ⇒ d(T_β) = 0": G3′ forces liminf = 0, so η = d̄(T_β) = 0. ✔

### Labels
- PROVED-mod-cite (C1) + mod-input Theorem H, depending on §5.2 (Lemma H, Lemma Sat, move map — REVIEWED) and G3′-U
  steps 1–5: appropriate. Nothing beyond (C1) about the zeros is used (Z1 for γ_k ≍ k/log k and k₂; Z1′ for (Hw) via
  G3′-U). ✔

## Independent checks (scratch: scratchpad/p24rev/)

1. **check_twins re-run:** byte-identical to `check_twins.out`.
2. **What the saturated value is** (`twins2.py`, mpmath, n = 20, 800 atoms): for ε → 0 the moved atom k+1 merges into
   atom k, so the limit loss is log D_n(μ) − log D_n(μ ∖ {k+1} with w_{k+1} added to atom k). Computed:

   | k | printed C(k,n) | C(k+1,n) | merged deletion of k+1 | saturated loss (ε = 1e−80) |
   |---|---|---|---|---|
   | 3 | 100.89 | 78.13 | 77.68 | 77.68 |
   | 6 | 47.28 | 36.24 | 35.69 | 35.69 |
   | 10 | 13.64 | 8.75 | 8.15 | 8.15 |

   So the text's "77.7 for k = 3 and 35.7 for k = 6 (the cost of losing the slot)" is accurate, but the slot lost is
   k + 1, not the k whose C(k,n) the script prints next to it (F6).
3. **Move map, exact rationals** (`move.py`): ν with head j⁻² (16 atoms, one tail tie), nonincreasing weights, n = 5,
   random F ⊂ [2, 10] with spacing ≥ 2; all 4368 5-subsets enumerated (300 random draws of F, those with spacing < 2 skipped). Per-S ratio term(S)/term(S′) ≤ Π_{moved}k², and
   Σ_{S avoiding F-pairs}term(S) ≤ 2^{|F|}Π_{F}k²·D_n(ν ∖ (F+1)). Both held exactly on
   every sampled F (max of ratio/bound = 1, attained only when nothing moves).

## Findings

**F1 (Medium; §5.3 preamble "T_β contains every repeated index (g_k = 0)"; also N‴1 and status block).** Index slip.
E (§5) is {k ≥ 2 : γ_k = γ_{k−1}}, while g_k = 0 means γ_{k+1} = γ_k. So T_β ⊇ E − 1, not E. Densities agree
(d̄(E − 1) = d̄(E)), so nothing downstream breaks, but the sentence is false as written.
*Fix:* "T_β contains E − 1 = {k : γ_{k+1} = γ_k} (g_k = 0), so d̄(T_β) ≥ d̄(E)."

**F2 (Medium; Remark N‴1, bullet "A proof of the sufficiency direction meets a truncation obstacle").** Overstated
scope. What was shown (LOG) is that *the G3′-L route* (fold near costs into weights compared with j^{−s_n}, then
truncate) fails; nothing says every proof meets it. The LOG entry also tested a different condition
("Σ log⁺(1/g) = o(K²/log K)") from the heuristic "sharp condition" in N‴1 (o(K²) with a cap K).
*Fix:* "The route of G3′-L step 6 meets a truncation obstacle … (LOG, Plan 24, attempted with
Σ_{k≤K}log⁺(1/g_k) = o(K²/log K)). This is an obstacle to that route only." Also the LOG's "log N ≳ n" understates
the requirement (D_{n−1}/D_n = 1/h_{n−1} = e^{(4+o(1))n log n}, so log N ≳ n log n); harmless but correct it or write
"log N ≫ n".

**F3 (Medium; §5.3 step 2, insertion into G3′-U).** The proof says "this replaces the factor ρ*(k,k+1) ≥ 1" but does
not say why the aggregated e^{O(n log²n)} survives. It does (uniform-in-S bound on a sum of nonnegative terms; one
term per twin pair is removed; k+1 ≤ θn < Mn so the pair is a head pair), but this is the Review-focus point and should
be in the text.
*Fix:* add "Since k+1 ≤ θn < Mn, {k, k+1} is a head pair; G3′-U step 3 bounds Σ 2 log ρ* ≥ 0 uniformly in S, so
dropping these summands keeps the e^{O(n log²n)} factor."

**F4 (Medium; N‴1 heuristic and numerical illustration).** The heuristic "a near-twin pair costs ≈ min(2 log(1/g),
C(k,n))" is not what `check_twins.out` shows, and the text reads as if the numerics support it:
- the absolute loss is far from 2 log(1/ε): −13.10 vs 9.2 (k = 3, ε = 10⁻²; the loss is *negative*), 14.19 vs 36.8
  (k = 3, ε = 10⁻⁸). Only the *increment* matches: 14.19 − (−13.10) = 27.29 vs 27.63 (k = 3), 27.35 (k = 6). Two
  points per k.
- the cap is the merged deletion cost of index k+1 (≈ C(k+1,n) − 0.5), not C(k,n) (e.g. 77.68 vs 100.89 at k = 3).
- the relative atom gap ε is not the normalized gap g (they differ by polylog factors in k; harmless for the heuristic
  but should be said).
*Fix:* "the loss increases by ≈ 2Δlog(1/ε) between ε = 10⁻² and 10⁻⁸ (27.3 vs 27.6), starting from a negative value,
and saturates at the cost of deleting index k+1 with its weight merged into k (77.7 for k = 3, vs C(4,20) = 78.1)".
Restate the heuristic as "≈ min(2 log(1/g) + O(1), C(k+1,n))" or "cost of order min(log(1/g), n)", and keep it
labelled Heuristic.

**F5 (Minor; step 1, "θ₁n ≤ k ≤ θn − 1 for k ∈ T′ (up to rounding)").** The lower end is k ≥ θ₁n − O(1) (from
k ≥ η′K/2 and n ≤ (K+1)/θ + 1); the upper end k ≤ K ≤ θn − 1 is exact. *Fix:* write "θ₁n − 1 ≤ k ≤ θn − 1" and note
this costs e^{O(1)} in ε_k².

**F6 (Minor; checks/check_twins.py docstring and printed column).** The docstring describes experiments that the code
does not run (a twin "added" with "a copy kept at x_k", "T(k,ε)", "log D_n(μ ∖ {k} + {twin})"). The code moves atom
k+1 to x_k(1−ε) (so slot k+1 is vacated, weight w_{k+1} kept), and prints C(k,n) for deleting index k, which is the
wrong comparison for the saturation value. *Fix:* rewrite the docstring to describe what is computed; print
C(k+1,n) and the merged-deletion value (check 2 above) next to the saturated loss; regenerate the .out.

**F7 (Minor; heuristic "sharp condition" in N‴1).** "d(E) = 0 and Σ_{k≤K}min(log⁺(1/g_k), K) = o(K²)": the first
clause is implied by the second (g_k = 0 contributes K, so d̄(E) > 0 gives Σ ≥ c K²). Also the heuristic uses the cap
K for all k ≤ K, whereas saturation (C ≍ n) is proved only for k < θ₀n (N″2). *Fix:* drop "d(E) = 0 and" (or say
"equivalently includes"), and note that the cap for k ≥ θ₀n is unestablished; keep "Heuristic" and
"would make … sharp" conditional (it is not claimed proved; good).

**F8 (Minor; §0 N‴ row and §5.3 heading).** Novelty UNCHECKED appears only in N‴2; N″'s row/heading carries it.
Dependencies list "N″, Z2" but the proof uses Lemma H, Lemma Sat and the move map of §5.2 and G3′-U steps 1–5 (and
Z1 for γ_k ≍ k/log k). *Fix:* row: "PROVED-mod-cite (C1) + mod-input Theorem H; depends on §5.2 (Lemma H, Lemma
Sat, move map) and G3′-U; novelty UNCHECKED" | "Lemma H, Lemma Sat, G3′-U, Z1".

**F9 (Minor; Remark N‴0).** "Since g ≤ 0 on [θ₀, ½], the restriction θ < θ₀ is needed" — needed for *this* bound to
be nontrivial (Lemma Sat gives no gain), not shown necessary for the theorem. *Fix:* "is needed for Lemma Sat to give
a gain".

**F10 (Info; step 1 constant).** Spacing ≥ 2 suffices for the move map (well-definedness and S′ ∩ (F+1) = ∅ only use
F ∩ (F+1) = ∅ and |k − k′| ≠ 1; checked exactly in check 3). Keeping every other element gives |T′| ≥ η′K/4 − 1 and the
constant (ηθ/4)·min(βθη, 2g(θ)). Optional.

**F11 (Info; README, plan doc, LOG).** README bullet ("N‴ in review") and the "Sufficiency gap" line are accurate.
Plan T4 open as expected. LOG says "Rule R: pending; depends on Plan 23 (§5.2) review" — Plan 23 is now REVIEWED;
update when this review is processed. check_twins runtime is ~9 s, not 10–30 min.

## Recommended labels

After F1–F9 (F10–F11 optional):
- Theorem N‴: **PROVED-mod-cite (C1) + mod-input Theorem H; depends on §5.2 (REVIEWED) and G3′-U; Rule R ACCEPT WITH
  FIXES (review/REVIEW_Plan24.md); novelty UNCHECKED.** REVIEWED once the fixes are applied and re-checked.
- Remark N‴1: the necessity/sufficiency summary is PROVED (N″, N‴, G3′-L); the near-twin cost and the "sharp condition"
  stay **Heuristic**; the sufficiency obstruction is an **obstacle to the G3′-L route** (LOG), not a no-go result.
- check_twins: **NUMERICAL (exact mpmath, 300 digits)**, illustration only.

## Re-check (commit 831394a, worktree ja-plan24, branch plan-24-nppp)

Scope: §5.3 (all), the §0 N‴ row, LOG Plan-24 entry, README N‴ lines, checks/check_twins.py and .out. I re-ran
`check_twins.py` from jacobi-asymptotics. The output is byte-identical to the committed `.out`, and its numbers
match my scratch values (C(k+1,n) = 78.13, 36.24, 8.75; saturation 77.68, 35.69, 8.15).

| # | Status | Note |
|---|---|---|
| F1 | RESOLVED | "T_β ⊇ E − 1 = {k : γ_{k+1} = γ_k}, same density as E". Correct. |
| F2 | RESOLVED (see R1) | N‴1 now says the obstacle is to the G3′-L step-6 route only. The LOG labels the attempt "route via G3′-L step 6 only" and corrects the requirement to log N ≳ n log n. |
| F3 | RESOLVED | New bullets: the uniform-in-S bound on a sum of nonnegative 2 log ρ* terms survives, and k+1 ≤ θn < Mn makes {k, k+1} a head pair. Matches my derivation. |
| F4 | RESOLVED (R3 nit) | The text now uses increments (27.3 vs 27.6 at k = 3), saturation = merged deletion of k+1 (77.68 / 35.69 vs C(k+1,n) = 78.13 / 36.24), and says ε ≠ g. All checked against the .out. |
| F5 | RESOLVED | θ₁n − O(1) ≤ k ≤ θn − 1. |
| F6 | RESOLVED | The docstring describes what the code computes, and C(k+1,n) is printed. One stale inline comment remains ("twin: atom k+... inserted"); harmless. |
| F7 | RESOLVED | The "sharp condition" no longer has the redundant clause, says it implies d(E) = 0, and is marked "Not proved". The cap ≳ n is stated only for k < θ₀n. |
| F8 | RESOLVED | Row and heading: PROVED-mod-cite (C1) + mod-input Theorem H; depends on §5.2 (REVIEWED) and G3′-U; novelty UNCHECKED. Depends-on column: N″ (Lemma H, Lemma Sat, move map), G3′-U, Z1, Z2. |
| F9 | RESOLVED | N‴0: "needed for Lemma Sat to give a gain; not claimed necessary for the theorem". F10 is noted as unused. Fine. |

Twin factor with coefficient 2: x_k − x_{k+1} ≤ 2(γ_{k+1} − γ_k)/γ_k³ = 2·2πg_k/(γ_k³ log(γ_k/2π)) = 4πg_k/(γ_k³
log(γ_k/2π)). ✔ ε_k ≤ C(log k)²g_k. ✔ The rest of the proof (steps 3–6, constants) is unchanged from the version
reviewed above.

### Residual items
- **R1 (Minor; but blocking for merge order; N‴1 bullets "Sufficient … (LG*) (Theorem L′, §4.1, Plan 25)" and
  "History … Plan 25's Lemma Tr (§4.1) removes it"; LOG "(Superseded by Plan 25's Lemma Tr.)").** §4.1, Theorem L′,
  (LG*) and Lemma Tr do not exist in this worktree (PROOF.md has §4 only), and they are unreviewed. As written, N‴1
  states "(LG*) is sufficient" as a fact. *Fix:* either merge Plan 25 first, or tag these sentences "(Plan 25, Rule R
  pending)" until L′ is REVIEWED. I did not assess L′ or Lemma Tr; this re-check accepts nothing about them.
- **R2 (Nit; LOG Plan-24 entry).** It still says "ε_k ≲ (log k)³g_k" (valid but inconsistent with §5.3's (log k)²) and
  "Recorded as OPEN (N‴1)", while N‴1 now says the obstacle is superseded. Also the LOG Rule R line needs updating to
  the re-check outcome. README l. 46 ("gaps between e^{−o(k)} and δ") predates the new N‴1 wording ("the window
  between those two conditions"); align once Plan 25 lands.
- **R3 (Nit; N‴1 numerics).** "At ε = 10⁻², moving the atom up even *gains*" holds for k = 3, 6 (loss −13.10, −3.18)
  but not k = 10 (+1.83). Add "for k = 3, 6".

### Re-check verdict: ACCEPT

The F1–F9 fixes are correct, and the mathematics of Theorem N‴ was already correct. R1 is about cross-references to
unreviewed Plan 25 material, not about N‴. R2 and R3 are nits.

Final labels:
- **Theorem N‴ (§5.3): PROVED-mod-cite (C1) + mod-input Theorem H; depends on §5.2 (REVIEWED) and G3′-U; Rule R
  ACCEPT WITH FIXES (review/REVIEW_Plan24.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED.**
- Remark N‴1: necessity part PROVED (N″, N‴); the near-twin cost and the sharp condition are **Heuristic**; the
  references to (LG*)/Theorem L′/Lemma Tr carry **Plan 25's** status, not this review's (R1).
- check_twins: **NUMERICAL (exact mpmath, 300 digits), illustration only.**
