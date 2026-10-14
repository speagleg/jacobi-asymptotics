# Rule R review: Plan 23 (PROOF.md §5.2, Theorem N″; Lemma H, Lemma Sat)

Reviewer: independent Rule R referee (adversarial). Target: branch plan-23-npp, commit dd441b1.

Read:
- AGENTS.md, VERIFICATION_POLICY.md (labels, Rule C, Rule N);
- PROOF.md §0 (status table and header), §1, §2 (Z1, Z1′), §3 (Z2, G3′-U steps 1–7), §5 (Prop N, Theorem N′ and its
  Remarks), §5.2 (all), the "G3′ status after N′" block;
- LOG.md Plan-23 entry; docs/superpowers/plans/2026-10-14-plan-23-npp.md; README.md status block;
- checks/check_npp.py and check_npp.out.

Numerics: I re-ran `.venv/bin/python research/G3prime/checks/check_npp.py` (1 min 25 s). The output is byte-identical
to `check_npp.out`. My own scratch scripts (mpmath, 50–800 digits) are described under "Independent checks".

## Verdict: ACCEPT WITH FIXES

The mathematics of Theorem N″ is correct. I re-derived Lemma H, Lemma Sat (including every Stirling-type step), the
collision-free reduction, the move map with all pair cases, the deletion gain and the constants, and found no error
that affects the conclusion. The constant c* = 0.239672… and θ* = 0.113062… are right. G3′ ⇒ d(E) = 0 follows, and
the residual case of N′ is closed.

The fixes are bookkeeping and framing: stale "residual GAP" text in five places (F1), an overstated "contains N′"
sentence (F2), Rule C for the three classical linear-algebra facts (F3), two unsupported numbers/claims in Remark
N″2 (F4), a hypothesis mismatch (strictly decreasing atoms vs ν's tied tail) in the preamble of the lemmas (F5),
and minor items F6–F10.

No major findings. Medium: F1, F2, F3, F4. Minor: F5–F8. Info: F9–F10.

## Checked and OK

### Lemma H (Review focus 1)
- **D_n vs Heine.** D_n(μ) = det(∫x^{i+j}dμ)_{i,j<n} equals Σ_{|S|=n}Π_{k∈S}w_k Π_{a<b∈S}(x_a − x_b)² (Cauchy–Binet),
  indexed by atom indices; equal atoms give zero terms, and summing over subsets with multiplicity equals the Hankel
  determinant of the merged measure. Checked numerically on a 7-atom measure with a tie (agreement to 20 digits). ✔
- **Gram identity.** With π_j monic orthogonal for μ, h_j = ‖π_j‖²_μ, p_j = π_j/√h_j, the change of basis from
  1, …, x^{n−1} to p_0, …, p_{n−1} is lower triangular with diagonal Π h_j^{−1/2}. So D_n(ν) = (Π h_j)·det G(ν) and
  D_n(μ) = Π h_j. This needs D_n(μ) > 0, i.e. μ has ≥ n support points; ν has infinitely many. D_n(μ ∖ E′) = 0 is
  allowed (then the inequality is trivial). ✔
- **G(μ∖E′) = I − VᵀV**, Sylvester det(I_n − VᵀV) = det(I_{E′} − VVᵀ), (VVᵀ)_{kl} = √(w_kw_l)K_n(x_k,x_l). ✔
- **PSD.** I − VᵀV is a Gram matrix of a nonnegative measure, so ‖V‖ ≤ 1 and I − VVᵀ ⪰ 0. Hadamard for PSD. ✔
- **ρ_n(k) = w_kK_n(x_k,x_k)** and 1 − ρ_n(k) = D_n(μ∖{k})/D_n(μ): checked numerically via a Cholesky construction of
  K_n (independent of the script's Stieltjes code), on a measure with tied tail atoms; agreement to 15 digits. ✔
  Ties do not matter for Lemma H: deleting index k removes only w_k.

### Lemma Sat (Review focus 2)
- **Christoffel.** Only the inequality 1/K_n(x_k,x_k) ≤ ∫P²dμ for deg P < n, P(x_k) = 1 is used; it is Cauchy–Schwarz
  in the p_j basis (see F3). ✔
- **Test polynomial.** Degree n − 1 < n, P(x_k) = 1, P(x_j) = 0 for j ≤ n, j ≠ k. 1 − ρ ≤ m/(w_k + m) ≤ m/w_k. ✔
- **Tail bound in the application to ν.** For l > n: n < l ≤ Mn gives G(l) = l⁻² < n⁻²; l > Mn gives
  0 < G(l) ≤ (Mn)⁻² < n⁻². So 0 < G(l) < G(j) for all j ≤ n and |G(l) − G(j)| ≤ G(j). Tail ties (k ∈ E, k > Mn) are
  harmless for this step (but see F5 for the stated hypothesis). ✔
- **Pure-power product.** x_j/|x_j − x_k| = k²/(|j − k|(j + k)) ≤ k²/(|j − k|max(j,k)). ✔
  - j < k: Π = k^{k−1}/(k−1)! = k^k/k! ≤ e^k (k! ≥ (k/e)^k). k = 1: empty product. ✔
  - j > k: log Π = 2(n−k)log k − log(n−k)! − Σ_{j=k+1}^n log j; Σ_{k+1}^n log j ≥ ∫_k^n log t dt (right-endpoint sum
    of an increasing function); log m! ≥ m log m − m for m ≥ 1 (and m = 0 trivially). ✔
  - Adding: log Π ≤ (2n − k)log k − n log n − (n − k)log(n − k) + 2n − k. The log n coefficient is
    (2n−k) − n − (n−k) = 0, and with k = θn this is exactly −n·g(θ). ✔
  - Exact check (mpmath, 50 digits) of log Π + n·g(k/n) ≤ 0 for all 1 ≤ k < n, 2 ≤ n < 200 and n ∈ {500, 1000}:
    max = −2.71 (at n = 2, k = 1). ✔
- **g decreasing.** g′(θ) = log(θ/(1−θ)) − 2/θ + 1. On (0, ½], log(θ/(1−θ)) ≤ 0 and 1 − 2/θ ≤ −3, so g′ ≤ −3. Only
  (0, ½] is used. ✔ Zero of g: θ₀ = 0.31538.

### Theorem N″ (Review focus 3)
- **(a) Collision terms.** σ indexed with multiplicity; k ∈ E means x_{k−1} = x_k, so a set containing {k−1, k} has a
  zero factor. ✔
- **(b) G3′-U step 4 is termwise.** Steps 2–3 bound every pair (head, cross, tail) of every index set S of size n,
  with a cost O(n log²n) uniform in S (uses only k_i ≥ i). Z2 is trivially true when γ_a = γ_b. The weights of σ and
  ν are the same w_k. So term_σ(S) ≤ e^{O(n log²n)}Λ^{n(n−1)}term_ν(S) for every S. ✔
- **(c) Move map.**
  - Well defined: k − 1 ∉ S (collision-free, k ∈ E′ ⊂ E), k − 1 ∉ E′ (no consecutive elements), images distinct, so
    |S′| = n and S′ ∩ E′ = ∅. ✔ Multiplicity ≥ 3 (k−2, k−1, k all equal atoms) causes no problem: S ∋ k−2, k is still
    "collision-free" in the stated sense, but its σ-term is 0 anyway and the ν-bound is only an upper bound. ✔
  - Preimages ≤ 2^{|E′|}. ✔
  - Weight: w_k = w_{k−1} exactly, since x_k = x_{k−1} (the text's "≤ C (Z1′)" is true but weaker; F8). ✔
  - Pair cases (f(t) = t⁻²):
    - moved k, larger unmoved head/tail partner b: f(k−1) − G(b) > f(k) − G(b). ✔
    - moved k, larger moved partner b ≥ k + 2: f(k−1) − f(b−1) ≥ f(k) − f(b) since t ↦ f(t) − f(t+m) decreases. ✔
    - moved k, smaller unmoved j ≤ k − 2: ratio (f(j) − f(k))/(f(j) − f(k−1)) ≤ 1 + 1/(k−1−j) by two mean-value
      bounds (2ξ⁻³ with ξ ∈ (k−1,k) vs ξ ∈ (j, k−1)). Over the distinct unmoved j < k − 1 this multiplies to at most
      Π_{m=1}^{k−2}(1 + 1/m)² = (k−1)². ✔
    - unmoved–unmoved: unchanged. ✔
  - Interaction of many moved elements: each pair has a fixed type, and the only factors > 1 are (moved, smaller
    unmoved), charged to the moved element; no interference. Per-move cost ≤ 2 log(k − 1) exactly. ✔
  - Exact check (mpmath, 60 digits), ν-like measures with pure-power head, random tied tail, random E with runs,
    E′ = alternate elements, random collision-free S (≈ 600 × 50 trials, only sets with ≥ 1 move counted):
    max[log term(S) − log term(S′) − Σ_moved 2 log(k−1)] = −4.25 < 0. Structured worst case S = [1, k−2] ∪ {k}:
    2 log-ratio = 0.34, 1.03, 2.20, 4.26, 6.62 vs 2 log(k−1) = 1.39, 2.77, 4.39, 6.73, 9.19 (k = 3, 5, 10, 30, 100). ✔
- **(d) Deletion gain.** E′ ⊂ [2, K], K ≤ θ*n (n = ⌈K/θ*⌉); g(k/n) ≥ g(θ*) > 0. log(W_{>n}/w_k) ≤ log(total mass)
  + log(k²/c₁) = O(log n). |E′| ≥ η′K/2 and K > θ*(n − 1), so the gain is ≥ η′θ*g(θ*)n² − O(n log n). ✔
- **(e) Step 5.** H7's bound for D_n(ν) is valid for all large n (with M fixed), hence along the subsequence; Λ via
  H6 exactly as in G3′-U step 6. Order: η′ and the K-sequence first, M fixed, n → ∞ along n_K, then M → ∞, then
  η′ → η. The subsequence does not depend on M. ✔
- **Constants.** θ* = 0.1130621447, c* = θ*g(θ*) = 0.2396722411, g(θ*) = 2.11983 (mpmath, 50 digits). ✔
- **End-to-end sanity (NUMERICAL, not evidence for the asymptotic).** Pure power x_k = k⁻², w_k = 2x_k, merging
  x_k := x_{k−1} for k ∈ E: log D_n(merged) − log D_n(pure) = −414.79 (n = 30, E = {2,4}), −637.55 (n = 40, E = {2,4}),
  −651.51 (n = 40, E = {3,6,9}), identical at 400 and 800 digits. Deleting E instead gives exactly log 2 per merged
  atom more (−416.18, −638.94, −653.59), as the merged weight doubles. So merging costs what deletion costs, which is
  the mechanism of the proof.

### Conclusion and labels (Review focus 4)
- G3′ means lim (1/n²)[log D_n(σ) − Φ_n] = 0, so liminf = 0 > −c*η unless η = 0. Hence d̄(E) = 0, i.e. d(E) = 0. ✔
- Residual case (positive lower density, d_*(E) = 0) has d̄(E) > 0, so it is covered. ✔
- The dependencies are exactly those of G3′-U (Z1/Z1′/Z2 from (C1); H5, H6, H7; Theorem H) plus elementary linear
  algebra. PROVED-mod-cite (C1) + mod-input Theorem H is the right label once F3 is done. Novelty UNCHECKED is stated
  (N″3). ✔
- Framing (rule 3): the statement is conditional on G3′ and concerns the ordinate list as input; nothing about RH. ✔

### Numerics claims (Review focus 5)
- [1], [2], [3] of `check_npp.out` match the PROOF text. C(1, 24) = 243.86 → "243.9" ✔; C(12, 24) = 15.46 → "15.5" ✔.
- Lemma Sat's bound at n = 24: 206.00 (k = 1) vs true 243.86, consistent.

## Findings

**F1 (Medium; PROOF.md header l. 3–4, status row N′, §5 Remarks, "G3′ status" block, README.md l. 45). Stale "residual
GAP" text.** After N″ several places still say the residual case is open:
- header: "N′ is proved for d_*(E) > 0 …; the residual case is GAP";
- table row N′: "residual GAP: positive lower density with d_*(E) = 0";
- §5 Remarks, directly after "It is closed by Theorem N″": "Whether the law fails there is not known either way.
  *(Heuristic:* it would need a thinning law for oscillating densities …)" — now contradicts the previous sentence;
- "G3′ status" block: "Hence |E ∩ [1, K]| ≤ 0.5925K(1 + o(1)), which does not exclude d_*(E) > 0"; "G3′ closes as: …
  necessity of d_*(E) = 0 by N′"; "no surveyed source states 'd_*(E) = 0' as open in this form";
- README.md: the residual N′ case is listed as Open; (N′) bullet not updated.
*Fix:* update all to d̄(E)/d(E) and N″ (after Rule R); delete the stale "not known either way" sentence and its
heuristic; in the status block write "does not exclude d̄(E) > 0" and "necessity of d(E) = 0 by N″".

**F2 (Medium; §5.2 after the theorem). "This contains Theorem N′'s conclusion, since d̄(E) ≥ d_*(E)."** True only
qualitatively (G3′ fails). N′ gives limsup ≤ 2 log(1 − d_*(E)), a statement about limsup with a larger constant
(2|log(1−d)| ≥ 2d > 0.24d); N″ gives only a liminf bound with c* = 0.2397. N″ does not imply N′'s inequality.
*Fix:* "This contains N′'s qualitative conclusion (G3′ fails when d_*(E) > 0), though not its quantitative limsup
bound, which N″ does not reproduce." Same for "subsumes N′" anywhere (LOG/status row are fine as written).

**F3 (Medium; Lemma H, Lemma Sat; Rule C(3)). Classical facts used without citation or proof.** Sylvester's
determinant identity, Hadamard's inequality for PSD matrices and the Christoffel variational formula are invoked by
name. Rule C(3): "standard" is not a citation. G2/CITATIONS.md has a "Classical facts … proved inline" section with
Hadamard, but G3prime/CITATIONS.md has none. *Fix:* add one-line inline proofs (each is two lines):
- Christoffel (only the needed direction): P = Σc_jp_j, ∫P²dμ = |c|², 1 = P(x_k) = c·v with v_j = p_j(x_k), so
  1 ≤ |c|²|v|² by Cauchy–Schwarz, i.e. ∫P² ≥ 1/K_n(x_k,x_k);
- Sylvester: nonzero eigenvalues of VᵀV and VVᵀ coincide with multiplicity;
- Hadamard for PSD A with a_ii > 0: det(D^{−1/2}AD^{−1/2}) ≤ (trace/n)^n = 1 by AM–GM; if some a_ii = 0 the row is
  zero.
and list them in G3prime/CITATIONS.md under "classical facts, proved inline".

**F4 (Medium; Remark N″2). Two unsupported claims.**
- "the indices k ≲ 0.55n are *saturated*: ρ_n(k) is exponentially close to 1." Lemma Sat proves saturation only
  where g > 0, i.e. k < 0.3154n (g(0.55) = −0.94). The recorded numerics go only to k = n/2 (C(12,24) = 15.5). The
  value 0.55 is not in any recorded output. *Fix:* "Lemma Sat proves ρ_n(k) ≥ 1 − e^{−2n g(k/n) + O(log n)} for
  k < 0.315n; numerically (check_npp [2]) C(n/2, n) is still ≈ 15 at n = 24", or record the source of 0.55 as
  NUMERICAL.
- "so o(n) deletions in the head can already cost order n²." Not proved and likely false. The Law-P heuristic for
  deleting the first m atoms gives cost ≈ 4nm log(n/m), which is o(n²) when m = o(n) (e.g. m = n/log n gives
  ≍ n² log log n/log n). What Lemma Sat does give is: εn deletions in [1, θn] cost ≥ 2g(θ)εn², and εn deletions at
  the smallest indices cost ≍ ε log(1/ε)n², i.e. the cost per deletion is n log(n/k), not O(1). *Fix:* replace by
  "so εn deletions in the head cost order n² (≥ 2g(θ)εn² if they lie in [1, θn]), rather than O(n)".
- Also in N″1: "The gap between them is exactly the small positive gaps" overstates; it is a heuristic. Mark it
  *(Heuristic)* like the twin-pair ρ ≈ ½ remark.

**F5 (Minor; preamble of Lemmas H and Sat). Hypothesis "x_1 > x_2 > … > 0" is not satisfied by ν.** ν's tail atoms
G(k) = x_k/λ (k > Mn) tie whenever k ∈ E. The proofs never use strict decrease: Lemma H needs only D_n(μ) > 0
(≥ n support points) and Lemma Sat needs only x_1, …, x_n distinct and 0 ≤ x_l ≤ x_j for l > n, j ≤ n (in fact
0 ≤ x_l ≤ 2x_j suffices for |x_l − x_j| ≤ x_j). *Fix:* state these hypotheses, and in step 4 say "0 < G(l) < G(n) for
l > n (tail ties allowed)".

**F6 (Minor; Lemma H, Gram bullet). Normalisation stated loosely.** "(unitriangular up to the factor Π h_j)" — write
h_j := ‖π_j‖²_μ for the monic orthogonal π_j, note D_n(μ) = Π_{j<n}h_j > 0 because μ has ≥ n atoms, and that
D_n(ν) = Π h_j · det G(ν) follows from the triangular change of basis. Also state that D_n(μ∖E′) = 0 is allowed.

**F7 (Minor; Lemma Sat statement). "For 1 ≤ k ≤ n" vs "θ := k/n < 1".** The general bound is stated for k ≤ n,
the pure-power bound only for θ < 1. *Fix:* state the pure-power bound for 1 ≤ k < n explicitly (that is all that is
used).

**F8 (Minor; proof step 3).** "The weight factor w_k/w_{k−1} ≤ C (Z1′)": in fact w_k = w_{k−1} exactly for k ∈ E
(x_k = x_{k−1}), so the factor is 1. Also the per-move bound can be stated sharply as (k−1)²:
Π_{m=1}^{k−2}(1 + 1/m)² = (k−1)². Optional, but it makes the "O(log k) per move, no interference" point explicit:
every factor > 1 comes from a (moved, smaller unmoved) pair and is charged to the moved element.

**F9 (Info; check_npp.py [3]).** The reported "max … = 0.000" is an artifact: `worst` is initialised to 0 and sets with
no moved element contribute exactly 0, so the line cannot show a negative maximum. The check also uses pure-power
weights 2/k² (not w_k = w_{k−1}), S ⊂ [1, 3n) with no tail, and the bound 2(log k + 2) + log 4 rather than the
proof's. *Fix:* initialise to −∞, skip sets with no move, report the actual max (my analogue: −4.25 against
2 log(k−1)). Cosmetic: [2] prints k = 8 twice at n = 16.

**F10 (Info; LOG.md). "Hadamard's inequality … shows that deletion costs add up."** It shows they are superadditive
(the joint cost is ≥ the sum). Suggest "at least add up". The Rule A entry could also list the adversarial cases
tried for the move map (multiplicity ≥ 3, tail ties, dense S near k).

## Recommended labels
- **Lemma H:** PROVED (after F3/F6), REVIEWED.
- **Lemma Sat:** PROVED (after F3/F5/F7), REVIEWED.
- **Theorem N″:** PROVED-mod-cite (C1) + mod-input Theorem H (via G3′-U steps 1–5, item 11 H5–H7); REVIEWED after
  F1–F4 are applied (re-check needed only for the edited text). Novelty: UNCHECKED.
- **Theorem N′ row:** drop "residual GAP"; add "residual case closed by N″ (qualitatively)".
- **G3′ sandwich:** "necessity of d(E) = 0 (N″)".
