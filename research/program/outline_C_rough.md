# Problem C — rough sandwiched weights w = k^{−s}e^{f}, |f| ≤ ε: research-program outline

Source state read: jacobi-asymptotics AGENTS.md, THEOREMS.md (H4), research/G1/PROOF.md §0, §3.2 (FV, Conj R),
§3.6 (Thm R, R1, R2), §3.7 (TC, T3-avg), §3.8 (TV, LP, L, T3-all, remark L2′), §4. Nothing in the repo was modified.
Numerics for this outline: `scratchpad/program/{bessel_check,window_check}.py` and their `.out` files (NUMERICAL,
float64 Lanczos with full reorthogonalisation, as in G1 `checks/check_t3_rough.py`; p = s = 2 unless noted).

Setting and notation as in G1 §3.6–3.8: x_k = k^{−p} (p > 0), v = k^{−s} (s > 1), w = v e^{f}, q_j = √w p_j,
μ_n = q_n², D_n := μ_n − μ_{n−1}, Δ²μ_N := μ_N − 2μ_{N−1} + μ_{N−2}, F_N := log(b_N²/b_{N−1}²),
L_n^{u}(f) := ⟨f, D_n^{u}⟩ (the first-variation functional at the measure u), β_n := n^p b_n/c(p). The arcsine
law ν on y = n^p x ∈ [0, 4c(p)] is parametrised as y = 2c(p)(1 + cos θ), with θ uniform on (0, π) (Lemma LP).

---------------------------------------------------------------------------------------------------------------

## 0. The organising heuristic (new, and checked numerically)

**Phase model.** In the band (atoms with y_k = n^p x_k ∈ (0, 4c)), the rows of J near n are close to the free matrix
c(2 + S + S*), so on a window of rows |n′ − n| ≤ L

  q_{n′}(k) ≈ R_k sin(n′θ_k + φ_k),  θ_k := θ(y_k),  R_k²/2 ≈ ν-mass carried by atom k.

From this:
- D_n(k) ≈ −R_k² sin θ_k sin(2nθ_k + 2φ_k − θ_k), and Δ²μ_N(k) ≈ −2R_k² sin²θ_k cos(2Nθ_k + 2φ_k − 2θ_k).
- With the phases ψ_k := 2Nθ_k + 2φ_k equidistributed over the atoms (the phase moves by an O(1), slowly varying
  amount from one atom to the next), this gives **universal limits**:
  - ‖D_N‖₁ → 8/π² ≈ 0.8106, i.e. TV(μ_N, μ_{N−1}) → 4/π², the Chebyshev value quoted in §3.2 F2;
  - ‖Δ²μ_N‖₁ → 4/π ≈ 1.2732;
  - restricted to an index window W, ‖Δ²μ_N|_W‖₁ → η_W := (8/π)∫_{θ: y(θ)^{−1/p} ∈ W} sin²θ dθ/π.
- L_n(f) is a **chirp coefficient**: a weighted exponential sum Σ_k f_k c_k e^{2inθ_k}, with |c_k| ≈ ν-mass·sinθ_k.
  The phase advances by about πρ(k/n) per atom, a frequency that sweeps (0, 1) across the band. So f breaks the law at
  n only if it tracks this chirp coherently over a window of length ≍ n. Random f and periodic f (for example parity)
  give stationary-phase size n^{−1/2}. This matches §3.2 [4], where the parity and random jumps decay like n^{−1/2}.
- **Bessel / large sieve.** Different n give almost orthogonal chirps (a Fejér kernel in n). So
  Σ_{n∈[N,2N]} L_n(f)² ≤ C_B‖f‖²_∞, with C_B independent of N. At most C_Bε²/δ² values of n per dyadic block can have
  |L_n| > δ. Theorem R's one spike per scale is therefore essentially the worst possible pattern.

**Numerical support (new; `bessel_check.out`, `window_check.out`).**

| quantity | prediction | observed |
|---|---|---|
| ‖D_n‖₁, p = 2, n = 240…247 | 8/π² = 0.811 | 0.78–0.86 |
| mean ‖Δ²μ_n‖₁, p = 2 | 4/π = 1.273 | 1.286 |
| mean ‖Δ²μ_n‖₁, p = 1 | 4/π = 1.273 | 1.275 (universal in p) |
| ‖Δ²μ_N\|_{[0.6N,1.6N]}‖₁ | 1.144 | 1.09–1.18 |
| ‖Δ²μ_N\|_{[0.6N,4N]}‖₁ | 1.265 | 1.21–1.30 |
| ‖Δ²μ_N\|_{[N,2N]}‖₁ | 0.416 | 0.411–0.416 |
| Bessel constant S(N) := max_{\|f\|≤1} Σ_{n∈[N,2N]} L_n² (sign power-iteration lower bound), N = 50, 100, 200 | O(1) | 2.07, 1.90, 1.91 (bounded) |
| same sum for random ±1 f | O(1) | 0.77, 0.73, 0.74 |
| nonlinear check at ε = 0.1 with the S-maximising f: Σ_n δ_n², δ_n := log b_n²(w) − log b_n²(v) | linear value εL_n | agrees with Σ(εL_n)² to 0.5%; corr(δ, εL) = 0.999 |

At ε = 0.1 the maximiser gives max|δ_n| of 0.067, 0.038 and 0.028 at N = 50, 100 and 200, which decays. The fraction
of n with |δ_n| > 0.02 is 14/51, 15/101 and 8/201. Even the worst f cannot keep many n bad. The data are consistent
with a density-one law for every rough f, with no spike train denser than O(1) per block at size ≍ ε.

---------------------------------------------------------------------------------------------------------------

## 1. Target theorems, ranked (tractability × interest)

| # | Target | Answers | Tractability | Interest | P(success) | Effort (plans) |
|---|---|---|---|---|---|---|
| T1 | **Thm RW**: Conjecture R in window form, f supported on ∪[aN_i, bN_i] (any a < u-edge < b, e.g. [0.6, 1.6]), N_{i+1}/N_i → ∞ | C1 | high | medium | 90% | 1 |
| T2 | **Thm LR + SOC**: linear response with a 2ε² remainder; sharp oscillation constants 8/π² (log b_n²) and 4/π (ratio F_N) | C4, C5 (first order) | high (LR) / medium (SOC) | high | 95% / 65% | 0.5 / 2 |
| T3 | **Thm Ra**: the pointwise a-law fails for some \|f\| ≤ ε (Toda form of FVa) | C3 (negative) | high | medium | 85% | 1 |
| T4 | **Thm D1**: density-one Law P *up to 2ε²*: for every \|f\| ≤ ε and δ > 0, #{n ≤ Y : \|log β_n²(w)\| > 2ε² + δ} = o(Y) | C2 (weak) | medium | high | 70% | 2 |
| T5 | **Thm D**: density-one Law P (b and a) for EVERY bounded f (any sandwich, no smallness) | C2 (full) | medium-low | very high | 50% | 3–4 |
| T6 | **Thm R1-sharp**: Lemma R1 with explicit constants: window-averaged η → 4/π; η_W as above; ε₀ = (4/π − o(1))/16 | C4 | medium | medium | 70% | (inside T2/SOC) |
| T7 | **Law-set theorems**: (a) positive classes (periodic/almost-periodic + slowly varying ⇒ law, rate n^{−1/2}); (b) a "chirp-free ⟺ law" characterisation à la Theorem Ch | C5 | low | very high | (a) 35%, (b) 15% | 3–6 |
| T8 | Fixed-ratio window form (ratio R(p) explicit; ratio 4 as in §3.2 [3]) | C1 (strong) | medium (R(p)) / low (ratio 4) | low | 60% / 30% | 1 / 2 |

Recommended order: T2(LR) → T1 → T3 → [Lemma PH] → T6/SOC → T4 → T5 → T7(a). T5 is the headline. T1–T3 are cheap and
safe.

---------------------------------------------------------------------------------------------------------------

## 2. Lemma chains (precise statements)

### 2.1 Cheap, essentially in hand

**Lemma R2b (second-order control of log b_n²).** Along w(t) = ve^{tf}, |(d²/dt²) log b_n²| ≤ 4‖f − c‖²_∞ for every
constant c, every n and every v.
*Proof.* This is the R2 proof one difference lower. (d²/dt²) log b_n² = (V_{n+1} − V_n) − (V_n − V_{n−1}), and each
V_{m+1} − V_m = A + B lies in [−2, 2]‖f‖²_∞ (R2: A ∈ [−2‖f‖², 0], B ∈ [0, 2‖f‖²]). Replacing f by f − c changes
neither Var_m nor ⟨f, D_n⟩.
Reuses: R2 steps 1–3, FV. Status: one paragraph; PROVED-ready.

**Theorem LR (linear response).** Let ε := ½ osc(f). Then for every n,
|log b_n²(w) − log b_n²(v) − L_n^v(f)| ≤ 2ε², and |F_N(w) − F_N(v) − ⟨f, Δ²μ_N^v⟩| ≤ 8ε² (R2 sharp form).
Consequence: limsup_n |log β_n²(w)| and limsup_n |L_n^v(f)| differ by at most 2ε². To accuracy ε², the law set is
exactly {f : L_n^v(f) → 0}, a condition on f against the pure-power kernel alone.
Numerics: Σδ² matches the linear value to 0.5% at ε = 0.1.

**Lemma R1W (window non-degeneracy).** Let 0 < a < b ≤ ∞ with (a, b) meeting the band
{u > (4c(p))^{−1/p}}, and W_N := [aN, bN]. There are δ_W > 0 and J (explicit given δ_W) such that every large N has
some m ∈ [N − J, N] with ‖Δ²μ_m^v|_{W_N}‖₁ ≥ η_W⁰ := δ_W/J².
*Proof.* Run R1 steps 1–3 with every sum restricted to W_N. The telescoping in step 1 and the pointwise recurrence in
step 3 both localise. Replace step 4 (moments) by **LP weak convergence**: ⟨dist(y, Z)²1_{W_N}, μ_{N−1}⟩ →
∫_{W′} dist(y, {−2, 0, 2})² dν_{[−2,2]} > 0, because W′ (the image of W_N) is a ν-continuity set of positive measure.
- This is simpler than the moment argument and gives δ_W explicitly. For W = ℕ, E_ν dist² ≈ 0.26 gives δ ≈ 0.016,
  J = 125 and η ≈ 10⁻⁶ (crude but explicit).
Reuses: R1, LP. Status: easy.

**Theorem RW (C1).** For every ε ≤ ε₀(W) := η_W⁰/16 and every sequence N_i with N_{i+1}/N_i → ∞, f := Σ_i
ε·sign(Δ²μ_{m_i}^v)·1_{W_{N_i}} (with m_i ∈ [N_i − J, N_i] from R1W) gives limsup_n |F_n(w)| ≥ εη_W⁰/2.
*Proof.* As in Theorem R, with three changes:
- (i) Windows below W_{N_i} lie in [1, bN_{i−1}] ⊂ head(θN_i) because N_i/N_{i−1} → ∞. Sat_p⁺ makes them
  exponentially small, as before.
- (ii) Windows above lie in (aN_{i+1}, ∞) ⊂ (MN_i, ∞) for every fixed M eventually. **Lemma TV** with g := f_far
  (supported off Mid) gives ‖g q_m‖ ≤ ε√y. Grönwall then gives y(t) ≤ e^{Cε}y(0) along the path ve^{f_i} → w, *with
  no additive ε term*.
  - The base ve^{f_i} itself has tail mass ≤ e^{2ε}(√F_p(M) + ε)² by TV along v → ve^{f_i} (this is the "O(ε) in √μ"
    of remark L2′).
  - So the cross-window error is ≤ 4ε·O(F_p(M) + ε²) → O(ε³), below the 8ε² already paid.
- (iii) The gain is ε‖Δ²μ|_W‖₁ ≥ εη_W⁰ by R1W.
This proves Conjecture R's window form with "sufficiently sparse" meaning N_{i+1}/N_i → ∞. Polynomial separation is no
longer needed.
Reuses: R, R2, R1W, TV, LP, Sat_p⁺. Hardest step: bookkeeping of (ii). Status: 1 plan.

**Theorem Ra (C3, negative).** Lemma FVa together with the recurrence (x − a_n)q_n = b_{n+1}q_{n+1} + b_nq_{n−1} gives
the **Toda form**

  (d/dt) a_n = ⟨f, b_{n+1}q_nq_{n+1} − b_nq_{n−1}q_n⟩ = ⟨f, ΔE_n⟩,  E_n := b_{n+1}q_nq_{n+1}.

(It follows from FVa by one line; check it numerically, as in L5[1].) The statement needs three ingredients:
- **R2a**: |d²a_n/dt²| ≤ C‖f‖²_∞·max_{|j−n|≤2} b_j. Differentiate E_n using q̇_m = ½fq_m − K_m(fq_m) − ½⟨fq_m, q_m⟩q_m
  (TV proof) and FV for ḃ.
- **R1a**: ‖n^pΔE_n^v‖₁ ≥ η_a on some m ∈ [N − J, N]. Prove it by contradiction exactly as in R1/R1W.
  - The phase model predicts n^pΔE_n → c·sin θ_k·(oscillation), with a limit ‖·‖₁ ≍ c(p)·const. So it is
    non-degenerate.
- **Construction**: then the Theorem R construction gives limsup_n n^p|a_n(w) − 2c(p)| ≥ c′ε.
Status: 1 plan; risk is only R2a algebra.

### 2.2 The new engine: local phase lemma (needed for T4, T5, T6, SOC)

**Lemma PH (local phase representation).** Let u be a weight sequence on the nodes k^{−p}. Assume its Jacobi
coefficients are *locally free* on the window I = [n − L, n + L]:
  max_{j∈I} |j^p b_j(u) − c(p)| + |j^p a_j(u) − 2c(p)| ≤ τ.
For η > 0 let B_η := {k : y_k := n^p x_k ∈ [η, 4c − η]} (band atoms, away from the edges). Then there are R_k ≥ 0 and
φ_k ∈ ℝ with

  Σ_{k∈B_η} sup_{n′∈I} |q_{n′}(k) − R_k sin(n′θ_k + φ_k)|² ≤ C(η, L)·(τ + 1/n)·Σ_{k∈B_η}(q_n(k)² + q_{n−1}(k)²),

and Σ_{k: y_k∈Y} R_k²/2 = ν_n(Y) + O_η(τ + L⁻¹) for intervals Y ⊂ [η, 4c − η], where ν_n is the image of
(1/(2L+1))Σ_{n′∈I}μ_{n′}.
*Proof plan.*
- (a) **Transfer matrices.** At energy x_k the vector (q_{n′}(k), q_{n′−1}(k)) obeys the three-term recurrence. On I
  the scaled matrices T_{n′}(y_k) differ from the free rotation (angle θ_k) by O(τ + L/n), uniformly for y_k ∈ B_η,
  where the free matrix is elliptic with |sin θ| ≥ c(η). A product of 2L such matrices differs from the free product by
  O_η(L(τ + L/n)).
  - Define (R_k, φ_k) from (q_n(k), q_{n−1}(k)) by the free rotation's eigen-decomposition.
- (b) **Amplitudes.** Averaging sin²(n′θ_k + φ_k) over n′ ∈ I gives ½ + O(1/(L|sin θ_k|)). LP weak convergence then
  gives the ν-mass statement.
For the pure power v, τ → 0 by RH_px / RH₁(r) / RH_plt1b, at every n. For rough u it holds on whatever n are locally
free.
Reuses: pure-power laws, LP, the T3a step-1 bounds (n^pa_n, n^pb_n ≤ C_p). Status: standard (discrete WKB on finite
windows). This is the **key new lemma**, 1 plan.

**Lemma FJ (Fejér decorrelation).** In the setting of PH, for any |g| ≤ 1 supported in B_η,

  Σ_{n′∈I} ⟨g, D_{n′}⟩² ≤ C(η)·(log L + L(τ + 1/n)^{1/2}·L).

Hence the average of ⟨g, D_{n′}⟩² over I is ≤ C(η)(log L)/L + o(1) as n → ∞ with L fixed.
*Proof.* Insert PH:
- ⟨g, D_{n′}⟩ = −Σ_k g_k R_k² sin θ_k Im(e^{i(2n′θ_k + 2φ_k − θ_k)}) + error.
- Expanding the square gives Σ_{k,k′} |c_k c_{k′}|·|Σ_{n′∈I} e^{2in′(θ_k − θ_{k′})}| ≤ Σ_{k,k′}|c_kc_{k′}|
  min(2L + 1, 1/‖(θ_k − θ_{k′})/π‖).
- The weights |c_k| ≲ ν-mass of atom k form a measure with bounded density in θ. So the double sum is
  ≲ ∫∫ min(L, 1/|θ − θ′|) dθdθ′ ≍ log L. (This is the elementary large-sieve/Fejér bound. It does not need the
  atom-spacing condition, because only the weight distribution matters.)
Edge and tail atoms (outside B_η, or k > Mn) are bounded trivially by ε·mass: O(√η) by the arcsine edge, and F_p(M) by
LP.
Status: elementary given PH.

### 2.3 Density-one theorems

**Theorem D1 (C2 up to ε²).** For every |f| ≤ ε and δ > 0, the set E := {n : |log β_n²(w)| > 2ε² + δ} has density
zero. The same holds for n^p|a_n(w) − 2c(p)| with a C(p)ε² threshold.
*Proof.*
- LR reduces the claim to {n : |L_n^v(f)| > δ} having density zero.
- PH (with v, τ → 0 at every n) and FJ show that on every window of length L the average of L_{n′}² is ≤ C(η)ε² log L/L
  + C√η ε² + CF_p(M)²ε² + o(1).
- Tile [N, 2N] by such windows and apply Chebyshev. Then let L, M → ∞ and η → 0.
Reuses: LR, PH, FJ, LP, Sat_p⁺. Effort: 2 plans including PH. P ≈ 70%.

**Theorem D (C2 full; headline).** For every bounded f (any sandwich e^{±G}), there is J ⊂ ℕ of density one with
n^pb_n(w) → c(p) and n^pa_n(w) → 2c(p) along J.
*Proof plan (continuity method in t; no smallness of f needed).* Take the path w(t) = ve^{tf} and steps t_i = ih,
i ≤ 1/h. Induction hypothesis H(i): the law (both coefficients) holds along a density-one set J_i for w(t_i).
- (1) H(i) ⇒ local freeness. If bad n have density zero, then for fixed L the set of n whose whole window
  [n − L, n + L] lies in J_i also has density one. On it τ → 0.
- (2) Local freeness ⇒ local LP. Lemma LP's method of moments only uses the J-entries within distance j of n. So on
  those n, μ_n^{(t_i)} → arcsine weakly. This gives the tail mass F_p(M) *without* the Grönwall factor e^{4G}, and
  PH/FJ apply to w(t_i).
- (3) Step. log b_n²(w(t_{i+1})) − log b_n²(w(t_i)) = hL_n^{(t_i)}(f) + r_n with |r_n| ≤ 2h²G² (LR at base w(t_i)).
  By FJ the first term is ≤ hδ outside a density-zero set. The same holds for a_n with FVa (Toda form) and R2a.
- (4) Accumulating over the 1/h steps: on ∩_i J_i (still density one), |log b_n²(w) − log b_n²(v)| ≤ δ + 2hG². The
  diagonal argument of T3-avg step 6 over h, δ → 0 finishes.
Hardest step: **(2)+(3) uniformity.** PH needs the window to be locally free for *both* a and b at w(t_i). FJ's o(1)
must be uniform over the density-one set (it is: all errors are explicit in τ, L, η). Also needed: a density-one *a-law*
at each step, hence R2a. Main risk: a hidden need for pointwise (not density) local freeness in the amplitude step (b) of
PH, through μ_n's mass on atoms whose y lies near the band edges at nearby n. Excising edges costs O(√η) uniformly, so
this seems controllable.
Status: 3–4 plans. P ≈ 50%. Payoff: the **dichotomy "pointwise law can fail (R), density-one law always holds (D)"**
for all rough sandwiched weights, extending T3-avg from slowly varying Ψ to arbitrary bounded Ψ.
- Novelty check required. This is a "Cesàro–Nevai"-type phenomenon. Possible prior art (recollection only, unverified,
  must pass the citation gate): Golinskii–Khrushchev (Cesàro asymptotics, OPUC); Simon, *OPUC* Vol. 1 Cesàro–Nevai
  class; Breuer–Last–Simon on the Nevai condition. None of these treats nodes accumulating at 0 with power-law
  coefficients.

### 2.4 Sharp constants (C4)

**Theorem R1-sharp / SOC.**
- (i) For v: lim_{L→∞} limsup_N |(1/L)Σ_{m∈[N−L,N]}‖Δ²μ_m^v‖₁ − 4/π| = 0. The same holds with 8/π² for ‖D_m‖₁ and
  with η_W for windows. *Proof:* PH plus the average of |cos(ψ − 2mθ)| over m, which tends to 2/π for θ/π outside a
  set of small ν-measure.
- (ii) Hence R1 holds with η = 4/π − δ and J = J(δ). Theorem R holds with ε₀ = (4/π)/16 − o(1) ≈ 0.08 and
  limsup|F_N(w)| ≥ (4/π)ε − 8ε² − o(1).
- (iii) (SOC, upper half) sup_{|f|≤ε} limsup_N |F_N(w)| ≤ (4/π)ε + 8ε², and similarly 8/π² for log b_n².
  - This needs **pointwise** (every N) phase equidistribution of ψ_k = 2Nθ_k + 2φ_k over the band atoms, i.e. a global
    Plancherel–Rotach phase φ_k(N). That is the hard part.
  - Candidate source: extract the band ("lens") asymptotics from RH_px/RH_plt1b, where φ is the equilibrium phase
    πn∫ρ. Numerically ‖D_n‖₁ fluctuates ±5% at n = 240, and the max over [N, 2N] falls 0.92 → 0.88 → 0.86 as N grows,
    so convergence is slow.
- Lower halves need only (i). P: (i)–(ii) 70%, (iii) 45%.

### 2.5 The law set (C5)

- **Proven-level statement available now:** LR gives "law ⟺ L_n^v(f) → 0" to accuracy 2ε², with L_n^v a fixed linear
  functional built from the pure power alone.
- **Positive classes (T7a).** Conjecture: f = g + h with g slowly varying (G1 §3.8 sense) and h in the Wiener algebra
  of almost-periodic sequences (Σ|ĥ_j| < ∞) ⇒ the full pointwise law, with |β_n − 1| = O(n^{−1/2}) when g ≡ 0.
  - Heuristic: each frequency α is hit by the chirp at the single band point where ρ(u) ≡ ±α (mod 1). Stationary phase
    gives n^{−1/2}. This matches §3.2 [4]: parity n^{−1/2} decay of the mean jump.
  - Needs the global phase (as in SOC (iii)) and a continuity method in pointwise form, which requires local freeness
    at *all* n, inducted along t. P ≈ 35%.
- **Characterisation (T7b, stretch).** Conjecture ChR: for bounded f, Law P holds pointwise ⟺ 𝒞_n(f) → 0, where
  𝒞_n(f) := Σ_k f_k ν_n(k) sin θ_k e^{2iΘ_n(k)} and Θ_n is the explicit pure-power phase.
  - Obstacle: along the path the phase Θ_n^{(t)} of w(t) may drift from Θ_n by O(1) (zero-counting functions of
    sandwiched perturbations are not controlled). So the condition may have to be stated with w's own phase, which is
    circular.
  - The honest fallback is the ε² version (LR) plus "for |f| ≤ ε ≤ ε₁, the law holds iff 𝒞_n(f) → 0 at every order",
    proved by showing that the second-order term is itself a bilinear chirp form controlled by sup_m |𝒞_m(f)|.
  - Analogy with Theorem Ch: Ch replaced an energy condition by an exact combinatorial one (𝒞(K) = o(K²)). Here the
    analogous exact quantity is the chirp maximal function, and Bessel (FJ) plays the role of Ch's counting bound.
    P ≈ 15%.
- Not a Cesàro condition on f. Slowly varying (Cesàro-type) behaviour is sufficient but far from necessary: periodic
  and random f also satisfy the law. Failure is purely coherent fine-scale (index scale 1) structure phase-locked to
  the OP oscillation.

---------------------------------------------------------------------------------------------------------------

## 3. Hardest steps (ranked)

1. **D step (2)–(3):** propagating local freeness through the continuity method uniformly on density-one sets (T5).
2. **Global phase / pointwise equidistribution** of 2Nθ_k + 2φ_k over band atoms (SOC upper half, T7). This needs
   Plancherel–Rotach band asymptotics from the RH analyses. They exist in principle (lens region) but nobody has
   extracted them.
3. **Lemma PH** near the band edges (θ → 0, π). Handled by excision at O(√η) cost. The saturated edge
   u = (4c)^{−1/p} sits inside [0.6N, 1.6N] for p = 2 (edge 2/π = 0.637), so windows straddle it. Harmless for R1W
   (weak convergence) but needs care in FJ.

## 4. Numerics still worth running (cheap, to de-risk)

- (N1) PH directly: fit q_{n′}(k) = R_k sin(n′θ_k + φ_k) on n′ ∈ [n − 10, n + 10] for v and for a rough w (ε = 0.2,
  random and adversarial). Report the weighted residual. This tests PH, including for rough u.
- (N2) The density-one law at ε = 0.5–1 (beyond LR's regime): adversarial f from sign power-iteration on [N, 2N],
  N ≤ 400. Track the fraction of n with |log β_n²(w)| > 0.05 as N doubles. T5 predicts that it → 0.
- (N3) Parity and almost-periodic f: |β_n − 1|·n^{1/2} bounded? (T7a rate.) Long-double RKPW up to n ≈ 4000, as in
  §3.2 [4].
- (N4) The Toda form of ȧ_n vs a finite difference (the identity check for T3).
- (N5) Fixed ratio 4 in the window construction (T8). Check the incoherence of far-window signs:
  ⟨sign(Δ²μ_{4N})1_{W_{4N}}, Δ²μ_N⟩ ≈ O(N^{−1/2})?

## 5. Effort and probabilities (summary)

- **Safe block, ~3 plans, P ≈ 85–95%:** LR, R1W, RW (C1), Ra (C3 negative).
- **Engine, ~1 plan, P ≈ 80%:** PH + FJ.
- **Middle block, ~3 plans, P ≈ 70%:** D1 (C2 up to ε²); R1-sharp lower halves (C4: η → 4/π, ε₀ ≈ 0.08).
- **Headline, ~3–4 plans, P ≈ 50%:** Theorem D (C2 full; density-one a- and b-laws for every bounded rough f).
- **Stretch, ≥ 4 plans, P ≈ 15–45%:** SOC upper half, positive law classes, and characterisation ChR (C5).

## 6. Publishable partial results

- **Paper A (safe):** "Bounded roughness and pointwise ratio asymptotics for discrete measures accumulating at 0":
  Theorems R + RW + Ra + LR. The dichotomy with T3-all is already REVIEWED in the repo.
- **Paper B (if T5 lands):** "Pointwise failure, density-one validity". Theorem D plus the Bessel/Fejér mechanism, and
  Theorem R as sharpness (one spike per scale is optimal up to constants: at most C_Bε²/δ² spikes per dyadic block).
- **Note C:** universal oscillation constants 4/π and 8/π² for ‖Δ²μ_N‖₁ and ‖D_N‖₁ (window-averaged version
  rigorous via PH). It is a clean statement and is independent of the rest.
