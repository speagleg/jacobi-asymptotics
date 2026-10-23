# JZC SHIFT: the index-shift law of the multi-time layers is the dispersionless limit of the Toda flow

Status (2026-10-23, after Rule R review A): **REVIEWED** — research/G1/review/REVIEW_JZC_TODA_SHIFT_A.md (reviewer A, independent
second reader: re-derived Lemmas LB, D, R, H, the proof of Thm SH and Cor SH.1–SH.3; re-ran shift_toda, shift_existing (on
JZC_W2's caches), shift_dressing and shift_exact R1, R4, R5, R6 (engines from empty caches, byte-identical engine outputs); R2, R3, R7 not re-run; compared
LB with all seven toda_engine configurations, 96/96). Verdict ACCEPT WITH FIXES S1–S5, all applied below, each marked "(fixed per Rule
R review A, <id>)". Final labels: Thm SH with integer exponents, on the lattice line β′ = ν and on β′ ≠ ν (via JZC_TODA Theorem T_H):
PROVED-mod-cite + REVIEWED; at fractional/symbolic exponents the continued identities for the engine's model: PROVED-mod-cite +
REVIEWED, but their identification with JZC_W2's pole layers rests additionally on JZC_W2 Prop 2.1 (iii), NOT REVIEWED; Lemmas LB, D,
R, H: PROVED + REVIEWED; Prop DR: PROVED-mod-cite (Theorem T) + exact algebra + REVIEWED, with the g_j split for j > 10 and the
h(j, k) closed form CONJECTURE (unchanged). Labels per VERIFICATION_POLICY.md. Novelty: UNCHECKED (no Rule L pass; §8). No claim about RH: no measure built from zeta zeros is used (the "zeta times"
are the band-factor parameters of the formal model, treated as free parameters). Scope: JZC_W2 Obs 2.3 (the index-shift law) and
JZC_W2 §6 item 2 (dressings). Branch plan-e2-d2; committed in af22e48 (fixed per Rule R review A, T5: was "nothing committed").
Inputs, with their labels: **JZC_TODA Theorem T and T_H** (Toda structure of the layers; PROVED-mod-cite + REVIEWED) (fixed per Rule
R review A, S1: was "JZC_M4 §8 Theorem T (… proof sketch, NOT REVIEWED)");
JZC_M4_proof **Theorem N.6** (PROVED-mod-cite + REVIEWED) and its exact layer identities (m4_zeta_exact2 (A), (B)); E3 **Lemma E3.7**
(REVIEWED); JZC_W2 **Prop 2.1** (NOT REVIEWED; built on K.12′, BT.5, WE.1, all REVIEWED) and its exact outputs; JZC_SIGMA Theorem Σ
(REVIEWED; used only in remarks). No external theorem is used: the Toda hierarchy is derived in JZC_M4 §8 and proved in full as JZC_TODA Lemma T.1 (elementary), and the one
classical identity needed (Lagrange inversion) is proved in §1.2 (Rule C: nothing to quote).

Checks (all in `checks/`, Python = the session venv, `-B`; caches in `tmp/shift/`; every `.out` prints the sha256 of its script and
modules):
- `shift_common.py`: the closed form LB, a series-reversion check of it, and **FT**, a formal discrete-Toda engine (formal series in
  1/n with symbolic exponents p(k + Σβ_aj_a), shifts n ↦ n ± 1, the Toda hierarchy for every exponent set).
- `shift_toda.py` → `shift_toda.out` (§2: the proof mechanism; 31 identities, 9 controls).
- `shift_existing.py` → `shift_existing.out` (§1.3: LB against every existing exact engine output; 40 identities, 20 controls).
- `shift_predict.py` → `shift_predict.out`, **`shift_predictions.json`** (§4.1: registration, **2026-10-23 08:32:31 −06:00**).
- `shift_exact.py` → `shift_exact_R{1..6}.out` (§4.2: the registered exact engine runs; w2_engine.py by subprocess, not modified).
- `shift_dressing.py` → `shift_dressing.out` (§5: dressings from the Toda flow of the integer layers). (Updated 2026-10-23 after
  JZC_TODA / JZC_SHIFT review: review A found that the (E4) comparison with R1 was skipped silently when `tmp/shift/eng_R1_*.json` was
  absent; the script now stops with an error unless exactly one tmp/w2/exact_H_*.json and one tmp/shift/eng_R1_*.json exist, and prints
  the sha256 of the R1 cache. Re-run 2026-10-23: ALL 18 CHECKS PASSED (14 identities, 4 controls), unchanged verdicts.)
- `shift_hjk.py` → `shift_hjk.out`, `shift_predict2.py` → `shift_predict2.out`, **`shift_predictions2.json`** (registration 2,
  2026-10-23T09:02:55−06:00), `shift_exact.py R7 shift_predictions2.json` → `shift_exact_R7.out` (§5.3).
The `shift_exact_R1..R6.out` files are the final script re-run on the cached engine outputs (`tmp/shift/eng_R*.json`, created
08:35–08:55, after the registration); the engine times quoted in §4.2 are those of the first runs.

| # | Statement | Label |
|---|---|---|
| **Thm SH** | (index-shift law) For the formal model with band-factor times μ_a of exponents j_a, write n^pb_n/c = Σ_kn^{−k}b_k(μ). (i) **b_k is a polynomial of degree ≤ k in the times** (an order-m layer starts at n^{−m}); (ii) its degree-k part is the n^{−k} coefficient of **(n/x)^p, x = n − (1/p)Σ_aε_ax^{−pj_a}** (ε_a = (pj_a/2)c^{j_a}C(2j_a, j_a)μ̂_a, μ_a = μ̂_an^{−pj_a}); in natural form the leading coefficient of e^β is **LB(β) = Π_a(pj_a/2)^{β_a}·(p + 1 + S)_{\|β\|−1}/(β!p^{\|β\|−1})**, S = pΣβ_aj_a, at N^{−\|β\|} | lattice line β = ν, integer j_a: **PROVED-mod-cite + REVIEWED** (JZC_TODA Theorem T, Theorem N.6, E3.7) + exact algebra (Lemmas D, R, H); every p ≠ 1, ν on β = ν and every exponent (integer, fractional, symbolic): same label via rationality (Cor SH.1–SH.2) — the identification with JZC_W2's pole layers uses JZC_W2 Prop 2.1 (iii) (NOT REVIEWED); the continued identities themselves hold for the engine's model at every exponent (fixed per Rule R review A, S3); **β ≠ ν: PROVED-mod-cite + REVIEWED** via JZC_TODA Theorem T_H + Cor T.3 (Cor SH.3) (fixed per Rule R review A, S1) |
| Lemma LB | Taylor coefficients of x^{−p} in closed form (Lagrange inversion, proved in §1.2) | PROVED + REVIEWED (+ exact check `shift_toda` (L)) |
| Lemma D | formal dispersionless limit of the discrete Toda hierarchy: defect ≥ 0 and the defect-0 parts obey the dispersionless hierarchy | PROVED + REVIEWED (algebra, §2.2, wording S2; exact check (D) to order 7) |
| Lemma R | hard-edge reduction: the line α = 2b is invariant under every dispersionless flow; on it the flow is the Hopf equation ∂_{t_j}b = (jC(2j, j)/2)b^j∂_nb | PROVED + REVIEWED (algebra, §2.3; (S)) |
| Lemma H | hodograph: b = cx^{−p}, x = n + Σ_at_a(j_aC(2j_a, j_a)/2)c^{j_a}x^{−pj_a}, is the solution | PROVED + REVIEWED (§2.4; (H)) |
| §1.3 | LB = all existing exact data (B, T, M, Q, H; (3p+1)/(2p); W2 Cor 2.4) | PROVED (exact computer algebra, 40 identities) |
| §4 | registered exact runs R1–R6 (orders 4, 4 mixed, 5 mixed, 6; symbolic j at p = 3/2; e₁²e₂² symbolic (j, k) at p = 5/2; j = q₁ at p = 3/2, 5/2) and Toda-dressing predictions | PROVED (exact computer algebra), predictions registered before the runs: **all hold**, all controls fail |
| **Prop DR** | (dressings) every layer is the discrete Toda flow of the two integer layers; at relative order N⁻² it depends on them only through f₂ and a₂; the diagonal a₂ = −(p+1)/24 + (p+1)(p+2)ν²/8 is **derived** from (T1); g_j = [c₀(j) + c_a(j)a₂ + c_f(j)f₂] in closed form; h₂ and h(j, k) (p = 3/2) reproduced | PROVED-mod-cite (JZC_TODA Theorem T) + exact algebra + REVIEWED (review A; re-run 18/18); the split of g_j into three parts for integer j > 10: CONJECTURE (the sum is proved) |
| Obs DR′ | no "dressed index shift" (x = N − (1/p)Σε_ax^{−pj_a}(1 + γ_ax^{−2}), F(x) = integer layer) reproduces h₂ | PROVED (exact; OBSTRUCTION for that ansatz) |
| §5.3 | h(j, k) (second-order dressing) in closed form in (p, ν, j, k) | exact at integer j, k ≤ 9 for all p (PROVED-mod-cite, Theorem T); closed form: CONJECTURE (interpolated in (j, k)), identical to the exact symbolic-(j, k) engine output at p = 3/2 and (registered) p = 5/2 |

## 0. Answer

**The index-shift law holds to all orders, and the mechanism is the dispersionless limit of the Toda hierarchy at a hard edge.**
Theorem T (JZC_TODA; PROVED-mod-cite + REVIEWED) says that all multi-time layers of the lattice model are the Toda-hierarchy flow of the two integer layers
(b_n, α_n). Grade a term t^βn^{−p(1+Σβ_aj_a)−i} by its **defect** i − |β|. Every Toda equation is in conservation form,
∂_t(·) = (1 − S_{−1})(·), and a difference raises the defect by one, so by induction every layer has defect ≥ 0 (this is the degree
bound (i)), and the defect-0 parts satisfy the *dispersionless* Toda hierarchy (Lemma D). The hard edge (band [0, 4b], i.e. α = 2b at
leading order) is a Riemann invariant r₋ = α − 2b = 0 and is preserved (Lemma R); on it each flow is the Hopf equation
∂_{t_j}b = V_j(b)∂_nb with V_j(b) = (jC(2j, j)/2)b^j, whose characteristic (hodograph) solution with b(n, 0) = cn^{−p} is
b = cx^{−p}, **x = n + Σ_jt_jV_j(cx^{−p})** (Lemma H) — exactly Obs 2.3's x = N − (1/p)Σε_ax^{−pj_a}. The leading coefficients are its
Lagrange–Bürmann coefficients LB(β). Fractional exponents (pole times) follow because every engine coefficient is a rational function
of the exponents with denominators Π(2j − odd), so the identities at all integer exponent tuples continue (Cor SH.2). The decoupled
case β ≠ ν needs Theorem T for the Hurwitz family (T_H), which is JZC_TODA Theorem T_H with Cor T.3 (fixed per Rule R review A, S1).

**Running index.** In the language of task (2): each Toda time acts, to leading order, as a translation of the index by the
characteristic speed, x − n = Σ_jt_jV_j(b(x)), which depends on the local value of b — a *running* index. For the Szegő "time" (the
weight tilt x^{−2γ} of JZC_SIGMA's z^γ gauge, Hamiltonian log x) the symbol is H_log(2b, b) = log b, so V = ½ is constant and the
shift x = n − γ is rigid; Theorem Σ says that shift is exact to all orders. For x^j the speed depends on b, the shift is implicit,
and it is exact only at defect 0: the dressings are dispersive.

**Dressings.** They are the defect ≥ 2 part of the same discrete Toda flow (Prop DR). At relative order N⁻² every layer depends on
the integer layers only through f₂ (of B) and a₂ (of the diagonal A); a₂ is derived here from the exact j = 1 layer by (T1)
(it equals m4_diag's NUMERICAL closed form), and with it the Toda flow reproduces, without any fitting: g_j for j = 2..8 (JZC_M4 §6),
h₂ (all p, ν), h(j, k) at p = 3/2 (JZC_W2 H), and the registered new values (h(1, 2) at p = 5/2 symbolic ν; the μ₁², μ₁³ dressings at
p = 5/2). The first-order dressing splits as g_j = [c₀(j) + c_a(j)a₂ + c_f(j)f₂] with c_a(j) = j(jp + 2)/((2j − 1)p),
c_f(j) = ((j² + j − 1)p + 2(j − 1))/((2j − 1)p), c₀(j) = j(jp + 2)((j² + 2j − 2)p + 2j − 1)/(24(2j − 1)): the 1/(2j − 1) of g_j is
in all three parts. A "dressed index shift" does not reproduce h₂ (Obs DR′): the dressings are not an index reparametrisation.

## 1. The statement

### 1.1 Setting and the grading

Formal model M(β, ν) of JZC_M4 §7 (Bessel order ν, Szegő exponent β, c = c(p)), band factor exp(−Σ_aμ_az^{j_a}) in the n^p frame
(z = n^px), r times μ_a with exponents j_a > 0. The engine's normalised time is e_a := μ_ac^{j_a}C(2j_a, j_a) (C(2j, j) :=
Γ(2j + 1)/Γ(j + 1)², so c^jC(2j, j) = W(j) of JZC_W), and the **natural lead** ε_a := (pj_a/2)e_a (JZC_W2 §0). The unscaled time is
μ̂_a := μ_an^{pj_a} = −t_a (tilt exp(Σt_ax^{j_a})), and ε̂_a := (pj_a/2)c^{j_a}C(2j_a, j_a)μ̂_a, so ε_a = ε̂_an^{−pj_a}.
By JZC_W2 Prop 2.1(i), n^pb_n/c = Σ_kn^{−k}b_k(μ) with b_k entire in the times, n-free Taylor coefficients b_{k,β}.

**Defect.** The term b_{k,β}μ^βn^{−k} = b_{k,β}μ̂^βn^{−k−pΣβ_aj_a} has defect k − |β|. In the natural form of the engine
(nat[β][k] := coefficient of N^{−k} in (N/n)^{(Σβ_aj_a+1)p}·Σ_kb_{k,β}n^{−k}, N = n + (β + 1)/2), the defect is k − |β| as well,
since re-expanding n^{−k} in 1/N only adds higher k at fixed β.

**What "leading term" means.** At each multi-index β (order m = |β| in the times) the leading term is the defect-0 term: the
coefficient of μ^βn^{−m}, i.e. in natural form (n/N)^pε̂^β·LB(β)·N^{−m−pΣβ_aj_a}. For a single Toda time t_j this is the power
N^{−m(1+pj)}; for a pole time q_m (pq_m = pm − 1) it is N^{−|β|−Σβ_a(pm_a−1)}; mixed layers multiply.

**Theorem SH (index-shift law).** (i) b_{k,β} = 0 whenever |β| > k. (ii) Σ_kn^{−k}[b_k]_{deg k} = (n/x)^p with
x = n − (1/p)Σ_aε̂_ax^{−pj_a} (a formal power series in the ε̂'s whose coefficients are monomials in n); equivalently, with
ξ := x/N and s_a := ε̂_aN^{−1−pj_a}, **n^pb_n/c = (n/N)^pξ^{−p} + (defect ≥ 1), ξ = 1 − (1/p)Σ_as_aξ^{−pj_a}**, and
nat[β][k] = 0 (k < |β|), nat[β][|β|] = LB(β).

(N and n may be interchanged in (ii): the difference has defect ≥ 1.) Generating function, single time: ξ^{−p} = Σ_m
(p + 1 + mpj)_{m−1}/(m!p^{m−1})·s^m (a Raney/generalised-binomial series).

### 1.2 Lemma LB (closed form; Lagrange inversion, proved)
With s_a = λσ_a, y := ξ − 1 solves y = λψ(y), ψ(y) := −(1/p)Σ_aσ_a(1 + y)^{−pj_a}. For formal power series, [λ^m]H(y(λ)) =
(1/m)[y^{m−1}]H′(y)ψ(y)^m. *Proof:* y(λ) = λ·(unit), so λ = y/ψ(y) is a formal change of variable; [λ^m]H(y(λ)) = Res_λ
H(y(λ))λ^{−m−1}dλ = (1/m)Res_λ H′(y(λ))y′(λ)λ^{−m}dλ (integration by parts: Res of a derivative is 0) = (1/m)Res_y H′(y)(ψ(y)/y)^mdy
(invariance of the formal residue under y = λ·unit: Res_λ f(y(λ))y′(λ) = Res_y f(y), checked on monomials y^k: (y^{k+1})′/(k+1) has
zero residue for k ≠ −1, and y′/y = 1/λ + (unit)′/(unit) has residue 1). ∎ With H = (1 + y)^{−p}:
[λ^m] = (1/m)(−p)(−1/p)^mΣ_{|β|=m}(m!/β!)σ^β·binom(−p − 1 − S, m − 1) = **Σ_{|β|=m}σ^β(p + 1 + S)_{m−1}/(β!p^{m−1})**, S = pΣβ_aj_a.
Multiplying by Π(pj_a/2)^{β_a} (ε = (pj/2)e) gives LB(β). (`shift_toda` (L): equal to the direct fixed-point reversion for all
monomials, 1 time to order 6, 2 times to order 5, 3 times to order 4, symbolic p and j's; controls 1/(2p), p + 2 + S fail.)

### 1.3 Comparison with all existing exact data (`shift_existing.out`: 40 identities, 20 controls; ALL PASS)
Every monomial of the cached exact outputs of JZC_W2 (`tmp/w2/exact_{B,T,M,Q,H}_*.json`; symbolic p except Q (5/2), H (3/2);
symbolic α, β, j, k): zeros below |β| and LB(β) at N^{−|β|}, β-free — e₁, e₂ (= pj/2, E3.7), e₁e₂ (Prop 2.2(i)), e₁², e₁³ (ii), e₁²e₂
(ii), e₁⁴ (iii), and the e₁, e₂, e₁e₂ leads of H. The specialisations asserted in the notes are LB: the μ₁² bracket (3p + 1)/(2p)
(m4_zeta_exact2_B; JZC_M4_proof N.6(ii)), the e₁e₂ bracket (1 + p + pj + pk)/p, and JZC_W2 Cor 2.4's pole×pole
(p(1 + m + m′) − 1)/p and pole×Toda 1 + m + j. Controls: 1/(2p) and p + 2 + S at every order ≥ 2 lead (fail, 20/20).

## 2. The mechanism and the proof

### 2.1 Inputs
(a) **Toda hierarchy** (JZC_M4 §8 = JZC_TODA Lemma T.1, PROVED + REVIEWED, elementary; signs and the diagonal formula re-derived here). For a weight e^{Σt_jx^j}w with
orthonormal Jacobi matrix J (diagonal α_n, off-diagonal J_{n,n−1} = b_n, b_n² = h_n/h_{n−1}): ∂_{t_j}p_n = −((J^j)_− + ½(J^j)_0)p, hence
∂_{t_j}J = [B_j, J], B_j := −((J^j)_− + ½(J^j)_0), whose diagonal and subdiagonal entries give

  ∂_{t_j}b_n = ½b_n[(J^j)_{nn} − (J^j)_{n−1,n−1}],     ∂_{t_j}α_n = F_j(n) − F_j(n − 1),  F_j(n) := b_{n+1}(J^j)_{n+1,n}.   (Toda)

(j = 1: ∂α_n = b²_{n+1} − b²_n, the Toda lattice.) Both are in **conservation form** (1 − S_{−1})(·), S_k: n ↦ n + k.
(b) **Theorem T** (JZC_TODA Theorem T and T_H; PROVED-mod-cite + REVIEWED) (fixed per Rule R review A, S1): the μ-Taylor coefficients of Theorem N.6(i) and their α_n counterparts
are the (Toda)-derivatives at t = 0 of the integer layers b_n^{(0)} = cn^{−p}B(n), α_n^{(0)} = 2cn^{−p}A(n), as identities of formal
series in 1/n (shifted arguments re-expanded), for every p ≠ 1, |α| < 1, and every finite set of integer exponents.
(c) B(n) = 1 + O(1/n) (Theorem N.6(i), d₀ = 1); A(n) = A₀ + O(1/n) with **A₀ = 1**: by (T1) the first-order j = 1 lead is A₀p/2 in
engine units, and E3.7 [REVIEWED] says it is p/2 (`shift_toda` (A0)). (Updated 2026-10-23 after JZC_TODA / JZC_SHIFT review: A₀ = 1 is also
JZC_TODA Lemma T.B.3 directly; either route suffices, review A §4.2.)

### 2.2 Lemma D (formal dispersionless limit; PROVED)
Let (α_n(t), b_n(t)) be formal power series in t = (t_j)_{j∈𝒥} (𝒥 ⊂ ℕ finite) whose t^β-coefficients are n^{−p(1+Σβ_jj)}·(power series in
1/n), satisfying (Toda) coefficientwise, with α_n(0) = 2cn^{−p}(1 + O(1/n)), b_n(0) = cn^{−p}(1 + O(1/n)). Then (i) every term has defect
≥ 0; (ii) the defect-0 parts (α⁰, b⁰) solve the dispersionless hierarchy

  ∂_{t_j}b⁰ = ½b⁰∂_nH_j(α⁰, b⁰),   ∂_{t_j}α⁰ = ∂_nG_j(α⁰, b⁰),   H_j(a, b) := Σ_k j!/(k!²(j−2k)!)a^{j−2k}b^{2k},
  G_j(a, b) := b·Σ_k j!/((k+1)!k!(j−2k−1)!)a^{j−2k−1}b^{2k+1}

(the path counts of (J^j)_{nn} and b(J^j)_{n+1,n} with all entries frozen), with α⁰(0) = 2cn^{−p}, b⁰(0) = cn^{−p}; and this formal Cauchy
problem has exactly one solution.
*Proof.* Defect is additive under products (exponent bookkeeping n^{−p(k₁+…)}), a shift S_k keeps the defect-d part of a term and adds
terms of defect > d (binomial expansion of (n + k)^{−σ−i}), and (1 − S_{−1}) maps n^{−σ−i} to (σ + i)n^{−σ−i−1} + (defect > d + 1), i.e.
raises the defect by one and acts on the defect-(d+1) part as ∂_n. Induction on |β|: if all coefficients of order ≤ m have defect ≥ 0,
then (J^j)_{nn} and F_j (sums of products of shifted entries) have defect ≥ 0 at orders ≤ m, the right sides of (Toda) have defect ≥ 1,
and the t^{β+e_j} coefficient (= 1/(β_j + 1) times the t^β coefficient of the right side; the extra factor n^{−pj} of the right side is the weight of
t_j, so the n-order index i of the new coefficient is Σi_k + 1) (fixed per Rule R review A, S2) has defect ≥ 0: (i). Taking
defect-minimal parts: products of defect-0 parts and S_k (identity on defect-0 parts) turn (J^j)_{nn}, F_j into H_j(α⁰, b⁰), G_j(α⁰, b⁰)
and (1 − S_{−1}) into ∂_n: (ii). Uniqueness: the order-(m+1) Taylor coefficients are given by the order-≤ m ones. ∎
(`shift_toda` (D): with generic initial data α_n = 2n^{−p}(1 + ΣA_in^{−i}), b_n = n^{−p}(1 + ΣB_in^{−i}), A_i, B_i free, p symbolic, the
discrete FT flow has every coefficient of defect < 0 equal to 0 and defect-0 coefficients free of all A_i, B_i and equal to LB, for
exponent sets {1} (order 7), {2} (6), {3} (5), {1, 2} (5), {1, 3} (4), {1, 2, 3} (4); 42 commutation checks of the flows.)

### 2.3 Lemma R (hard-edge reduction; PROVED)
On the line a = 2b: H_j(2b, b) = C(2j, j)b^j and G_j(2b, b) = C(2j, j)(j/(j + 1))b^{j+1} (coefficients of x^j and x^{j+1} in
(1 + x)^{2j} = (1 + 2x + x²)^j, stay ↦ 2x, up ↦ x², down ↦ 1). Hence d_nG_j(2b, b) = C(2j, j)jb^jb_n = b·d_nH_j(2b, b), so
∂_t(α⁰ − 2b⁰) = 0 whenever α⁰ = 2b⁰: the line is invariant (α − 2b is the Riemann invariant of the lower band edge, which sits at 0),
and on it ∂_{t_j}b = V_j(b)∂_nb, V_j(b) := (jC(2j, j)/2)b^j. (`shift_toda` (S): identities for j ≤ 15, invariance for j ≤ 10 as
functions of a(n), b(n); control: the line a = 3b is not invariant.) (Note the hard edge is used: with α⁰(0) = 0 or 3cn^{−p} the leads
are not LB — `shift_toda` (D) controls.)

### 2.4 Lemma H (hodograph; PROVED) and the proof of Theorem SH
Let x be the formal solution of x = n + Σ_jt_jV_j(cx^{−p}) = n + Σ_jt_j(jC(2j, j)/2)c^jx^{−pj}. Implicit differentiation gives
∂_{t_j}x = V_j∂_nx, so b̃ := cx^{−p} solves every reduced flow, α̃ := 2b̃ solves the α-equations by Lemma R, b̃(0) = cn^{−p}, and the
t^β coefficient of x is a constant times n^{1−|β|−pΣβ_jj} (defect 0). By uniqueness (Lemma D) (α⁰, b⁰) = (α̃, b̃). With μ̂_j = −t_j:
−(1/p)ε̂_j = (j/2)C(2j, j)c^jt_j, so x = n − (1/p)Σε̂_jx^{−pj} and n^pb⁰/c = (n/x)^p; Lemma LB gives LB(β). (`shift_toda` (H): the
hodograph series solves the reduced flows and has the LB coefficients, exponent sets {1}, {1, 2}, {2, 3}.)
*Proof of Thm SH on the lattice line, integer exponents.* Theorem T (2.1(b)) puts the layers of M(α, α) into Lemma D's hypotheses
(2.1(c) for the initial data): (i) is Lemma D(i) (defect ≥ 0 ⇔ b_{k,β} = 0 for |β| > k), (ii) is Lemma D(ii) + R + H. ∎
(PROVED-mod-cite: Theorem T, Theorem N.6, E3.7.)

**Cor SH.1 (all p ≠ 1, ν, on β = ν).** The engine's coefficients are rational in (p, α); the identities hold on p ≠ 1, |α| < 1 (JZC_TODA Theorem T), hence
identically (fixed per Rule R review A, S4). (PROVED-mod-cite + REVIEWED, as Thm SH.)

**Cor SH.2 (every exponent: fractional, symbolic, pole layers).** In w2_engine.py (any number of exponents by the same construction) the
exponents enter only through the gauge's Taylor data, rational in j with denominators 2(2j − 2i − 1) (at 0) and j-free ones (at 4), and
through the natural-form power, polynomial in j; no other j-dependent quantity is inverted (the gauge G and G^{−1} are explicit, the
series inversions and the extraction's square root act on j-free leading terms). So every output is in
ℚ(p, α, β)[j₁, …][Π(2j_a − odd)^{−1}], and its value at positive integer exponents is the integer-exponent run, which is the E3-gauge
model of Theorem N.6 (m4_zeta_exact2 (A) asserts the Taylor data). A rational function of (j₁, …, j_r) vanishing on ℕ^r_{≥1} is 0;
so Thm SH holds identically in the exponents, in particular at j = q_m: by JZC_W2 Prop 2.1(iii) these are the pole layers, and
**Obs 2.3 of JZC_W2 is a theorem on β′ = α** (κ-families with δ = 0). (PROVED-mod-cite: as Thm SH + JZC_W2 Prop 2.1.) The
identification with JZC_W2's pole layers uses JZC_W2 Prop 2.1 (iii) (NOT REVIEWED); the continued identities themselves hold for the
engine's model at every exponent (fixed per Rule R review A, S3). Label: the continued identities PROVED-mod-cite + REVIEWED; the
statement about the pole layers PROVED-mod-cite (JZC_W2 Prop 2.1 (iii), NOT REVIEWED) + REVIEWED for the step from it.

**Cor SH.3 (β ≠ ν; PROVED-mod-cite + REVIEWED).** Hypothesis **(T_H)**: Theorem T holds for the Hurwitz lattices σ^δ (λ_k = (k + δ)^p,
−1 < δ ≤ 0), whose formal model is M(α + 2δ, α) (Theorem H(i), JZC_M3a_H §4, PROVED-mod-cite + REVIEWED). (T_H) is JZC_TODA Theorem
T_H with Cor T.3; hence Thm SH holds for all (β, ν): PROVED-mod-cite (fixed per Rule R review A, S1; was CONDITIONAL). The argument above runs on
{(β, ν) = (α + 2δ, α)}, an open set, and rationality in (β, ν) gives Thm SH for all (β, ν). Exact evidence without (T_H): the leads are
β-free in every symbolic-β output (B, T, M, Q, H, R1), and R2–R4 (β ≠ ν, rational) obey LB.

**Consequences.** (1) E3.7 ("the n⁻¹ coefficient is exactly linear in μ") is the case k = 1 of (i). (2) JZC_W2 §6 item 4 (quartic
start at N⁻⁴ for general p): by (i), every order-m monomial starts at n^{−m}, so in JZC_W2 Thm 2.5 the cubic pole monomials are
O(n^{−3p}) and all quartic ones O(n^{−4p}): the remainder is O(n^{−3p}) for all p > 1, p ≠ 2 (on β′ = α; for β′ ≠ α by Cor SH.3).
(Updated 2026-10-23 after JZC_TODA / JZC_SHIFT review: propagated to JZC_W2 Thm 2.5.)

### 2.5 The running-index reading, and why no exact gauge is expected (HEURISTIC)
The m-frame gauge z^{γσ₃} of JZC_SIGMA changes the Szegő exponent by −2γ, i.e. it is the Szegő part of the weight tilt
x^{−2γ} = exp(−2γ log x) (the Bessel order, which the tilt would also move, is invisible at defect 0). As a Toda-type flow its Hamiltonian is log x, with dispersionless symbol H_log(2b, b) = (1/2π)∫log(4b cos²(θ/2))dθ = log b, so the reduced
flow is ∂_τb = ½∂_nb (τ = −2γ): a **rigid** translation n ↦ n − γ, the leading part of Theorem Σ's N = n + (β + 1)/2, which Theorem Σ
proves exact to all orders. For a tilt x^j the characteristic speed V_j(b) ∝ b^j depends on the solution: the translation runs with
the local b, and the shift is implicit (Lemma H). This is the analogue asked for in task (2), at defect 0. Beyond defect 0 it fails
(Obs DR′): there is no index reparametrisation of the implicit form that carries the dressings; they are dispersive (difference vs
derivative, and the non-local structure of (J^j)_{nn}), §5.

## 3. Where the old observations sit
- N.6(ii)'s ζ(−p)² bracket (3p + 1)/(2p) = LB((2), (1))/ε₁²; JZC_W2 Prop 2.2(i)–(iii) and Cor 2.4: LB at orders 2–4 (§1.3).
- E3.7 (linearity of the n⁻¹ coefficient): Thm SH(i), k = 1.
- JZC_W2 Obs 2.3's wording "x = N − …": N or n is immaterial at defect 0 (§1.1).

## 4. Registered exact runs (Rule X)

### 4.1 Registration
`shift_predict.py` wrote `shift_predictions.json` at **2026-10-23T08:32:31−06:00**, before any of these engine runs existed (the
first engine output is from 08:35:57; `shift_exact.py` asserts registration < output mtime and engine sha unchanged). Runs
(w2_engine.py, sha256 8e69b2e3…, by subprocess, not modified):

| run | data | registered |
|---|---|---|
| R1 | p = 3/2, symbolic (α, β, j), E = (4, 0), KORD 4 | LB for e₁^m, m ≤ 4, zeros below; leads β-free |
| R2 | p = 5/2, α = −3/5, β = −11/10, symbolic (j, k), E = (2, 2), KORD 4 | LB for all e₁^ae₂^b, a, b ≤ 2 (e₁²e₂² at N⁻⁴) |
| R3 | p = 3/2, α = −1/5, β = −7/10, j = 1/3 (= q₁), k = 1, E = (5, 1), KORD 5 | LB through order 5 (e₁⁵, e₁⁴e₂) |
| R4 | p = 5/2, α = −3/5, β = −11/10, j = 3/5 (= q₁), E = (6, 0), KORD 6 | LB for e₁^m, m ≤ 6 |
| R5 | p = 5/2, lattice (β = α), symbolic α, j = 1, k = 2, E = (1, 1), KORD 4 | LB + **Toda dressings**: g₁, g₂, and h(1, 2) = (10449α² + 49903)/384 at N⁻⁴ |
| R6 | p = 5/2, lattice, α = −3/5, j = 1, E = (3, 0), KORD 5 | LB + Toda: μ₁² N⁻⁴ = 156411/12800, μ₁³ N⁻⁴ = 0, N⁻⁵ = 11030827/153600 |

The Toda predictions (R5, R6) come from FT with the lattice integer layers to n⁻² (B from N.1/N.6(ii), A from (T1) and the exact j = 1
layer, §5.1) and generic symbols beyond n⁻²; only coefficients free of those symbols were registered (asserted).

### 4.2 Results (`shift_exact_R*.out`)

| run | engine time | result |
|---|---|---|
| R1 | 162 s | 4 LB leads (e₁⁴: 3j⁴(4j + 3)(12j + 5)(12j + 7)/2048 at p = 3/2) + 10 zeros hold, β-free; 6 controls fail |
| R2 | 997 s | 8 LB leads incl. **e₁²e₂²: 5j²k²(10j + 10k + 7)(10j + 10k + 9)(10j + 10k + 11)/1024** + 18 zeros; 12 controls fail |
| R3 | 160 s | 10 LB leads incl. e₁⁵ = 7/2592, e₁⁴e₂ = 7/96 + 36 zeros; 16 controls fail |
| R4 | 142 s | 6 LB leads incl. **e₁⁶ = 64881729/40960000** + 21 zeros; 10 controls fail |
| R5 | 16 s | 3 LB + 13 Toda-dressing coefficients hold (incl. h(1, 2) at p = 5/2, symbolic α); control "no dressing" fails |
| R6 | 33 s | 3 LB + 15 Toda coefficients hold (μ₁² and μ₁³ dressings); 2 "no dressing" controls fail |

All registered predictions hold exactly; every control fails. (Orders 5 and 6 and the mixed fourth order e₁²e₂² are new; the fourth
order for symbolic j now holds at p = 3/2 as well as 5/2.)

## 5. The dressings (Prop DR)

### 5.1 The diagonal layer from (T1) (`shift_dressing` (E1))
With b_n^{(0)} from N.1/N.6(ii) to n⁻² and α_n^{(0)} = 2n^{−p}(1 + A₁n^{−1} + A₂n^{−2} + …) (c = 1), the exact first-order j = 1 layer
(natural N⁻² = 0, N⁻³ = (p/2)g₁; m4_zeta_exact2 (A)) determines, via (T1), **A₁ = −p(α/2 + 1)** (A is centred at M = n + α/2 + 1 =
N + ½) and **A₂ = p(p + 1)(α/2 + 1)²/2 + a₂, a₂ = −(p + 1)/24 + (p + 1)(p + 2)α²/8** — m4_diag's closed form (NUMERICAL there; now
PROVED-mod-cite (Theorem T, N.6(ii)) for the M⁻¹, M⁻² coefficients on the lattice line). (Updated 2026-10-23 after JZC_TODA /
JZC_SHIFT review: also confirmed by direct extraction, JZC_TODA Prop T.4, which gives a₂ and a₄ identically in (p, ν, β); REVIEWED.)

### 5.2 Everything at relative order N⁻² from (f₂, a₂) (`shift_dressing` (E2)–(E7))
By Theorem T the layers are the discrete Toda flow of (A, B); the relative-order-N^{−r} (defect-r) coefficients depend only on the
initial data to n^{−r} (Lemma D's bookkeeping: an initial-data term of defect d contributes only at defects ≥ d; also asserted in FT
with generic symbols beyond). So at relative N⁻² everything is a function of (f₂, a₂) and p, ν. Without any
further input:
- **first order** (E2): j = 2..8: N^{−2} = 0 and g_j = A_j + B_jα² (JZC_M4 §6; exact symbolic-j result) — predicted from g₁ alone;
  control a₂ := 0 fails.
- **μ₁²** (E3): N⁻³ = 0 and N⁻⁴ = (p²/4)h₂, h₂ of JZC_M4_proof, identically in (p, α); control f₂ := 0 fails.
- **h(j, k) at p = 3/2** (E4): Toda = the exact symbolic-(j, k) engine output (JZC_W2 H) for 1 ≤ j ≤ k ≤ 4; and R1's e₁² N⁻⁴ (symbolic
  j, p = 3/2) for j ≤ 4.
- **decomposition** (E5): with f₂, a₂ free, g_j = c₀(j) + c_a(j)a₂ + c_f(j)f₂,
    c_a(j) = j(jp + 2)/((2j − 1)p),  c_f(j) = ((j² + j − 1)p + 2(j − 1))/((2j − 1)p),  c₀(j) = j(jp + 2)((j² + 2j − 2)p + 2j − 1)/(24(2j − 1)),
  exact for j = 1..10 (read off j ≤ 7; the closed forms are asserted on j ≤ 10) and, after inserting the lattice f₂, a₂, identical to
  A_j + B_jα² for symbolic j. So the 1/(2j − 1) of g_j (JZC_M4 §6, §8's "C(2j − 2, j − 1)/C(2j, j)" heuristic) sits in all three parts:
  the dispersive part c₀, the diagonal-layer part (a₂) and the off-diagonal part (f₂).
- **parity** (E7): with generic even integer layers (B even in N, A even in M = N + ½; f₂, f₄, f₆, a₂, a₄, a₆ free) every layer of
  exponents (1, 2) to order 3 has zero relative N⁻¹ and N⁻³ coefficients; with A centred at N instead (control) it does not. This is
  JZC_M4 Corollary T′ (parity of S1-N′ from the evenness of the two integer layers), checked to that order.
- **Obs DR′** (E6, OBSTRUCTION for that ansatz): n^pb/c = (n/x)^pF(x), F = 1 + f₂x⁻², x = N − (1/p)εx^{−p}(1 + γx⁻²), γ fixed by g₁
  (γ = g₁ − (p + 2)f₂/p), gives at μ₁² a bracket N⁻² coefficient differing from h₂ by (2p + 3)[(p + 2)³ν² − (p + 1)(p² + p + 2)]/(8p²) ≠ 0.

PROVED-mod-cite (Theorem T) for "layers = Toda flow of (A, B)"; exact algebra for the rest. The split of g_j into c₀, c_a, c_f for
integer j > 10 is read off (CONJECTURE); their sum is proved for all j.

### 5.3 h(j, k) in closed form (`shift_hjk.out`, R7)
h(j, k) := the natural N⁻⁴ coefficient of the e₁e₂ layer in engine units (JZC_W2 Prop 2.2(iv)); JZC_W2 had it at p = 3/2 only. Step 1 (exact at each point, mod Theorem T): the Toda flow gives h(j, k) for 1 ≤ j ≤ k ≤ 9, symbolic (p, ν),
with f₂, a₂ free; it is linear in them, h = H₀ + H_f f₂ + H_a a₂ (and N⁻² = LB, N⁻³ = 0 at every pair). Step 2 (Rule X: an
**interpolation** in (j, k)): (2j − 1)(2k − 1)×each part is matched to a symmetric polynomial of total degree ≤ 8 on the 33 pairs
with j + k ≤ 12; the interpolant reproduces the 12 other pairs exactly. Result (the full H₀ is printed in `shift_hjk.out` and stored
in `tmp/shift/hjk_closed.json`):

  H_f = jk·[p²(2j³k − j³ + 4j²k² + 3j²k − 2j² + 2jk³ + 3jk² − 2jk − k³ − 2k² + 1) + p(10j²k − 5j² + 10jk² + 2jk − 3j − 5k² − 3k + 5)
        + 6(2jk − j − k + 1)] / (4(2j − 1)(2k − 1)),
  H_a = jk·[p²(2j³k − j³ + 4j²k² − j²k − j² + 2jk³ − jk² − k³ − k²) + p(10j²k − 5j² + 10jk² − 2jk − 2j − 5k² − 2k) + 6(2jk − j − k)]
        / (4(2j − 1)(2k − 1)),
  H₀ = jkp·[p³P₃ + p²P₂ + pP₁ + 6(j + k)(2j − 1)(2k − 1)] / (96(2j − 1)(2k − 1)), P_i symmetric polynomials (shift_hjk.out).

Independent checks: at p = 3/2 the closed form (lattice f₂, a₂, ν = α) equals the exact symbolic-(α, j, k) engine output of JZC_W2 H
**identically**; at j = k = 1 it equals p²h₂/2 identically in (p, α); control (f₂ := 0) fails. The value at p = 5/2 for symbolic
(j, k) was **registered** (`shift_predictions2.json`, 2026-10-23T09:02:55−06:00) before the engine run R7 (JZC_W2's H configuration
at p = 5/2: symbolic α, β, j, k; 584 s): **it holds identically in (α, β, j, k)** — e₁e₂ N⁻⁴ = h(j, k) at p = 5/2, β-free —
together with the leads 5j/4, 5k/4, 5jk(5j + 5k + 7)/16 = LB and the zeros (N⁰, N⁻¹, N⁻³); the control "no dressing" fails
(`shift_exact_R7.out`, 9 identities, 1 control).
Label: exact at integer j, k ≤ 9 for all p (PROVED-mod-cite, Theorem T); the closed form in (j, k): CONJECTURE (interpolated),
verified identically in (j, k) at p = 3/2 and (registered, R7) p = 5/2. Denominator only (2j − 1)(2k − 1): JZC_W2's "simple poles at j = ½ and k = ½
only" holds for all p in this form.
*p = 2 (JZC_W2 §2 end, §6 item 3), from the closed form (CONJECTURE):* Res_{j=½}h = −k(4α² − 1)(2k² + k + 9)/(32(2k − 1)) and
Res_{j=½}Res_{k=½}h = 5(1 − 4α²)/64: like the first-order W′ term, the would-be finite p = 2 pole×Toda and pole×pole limits are
∝ (1 − 4ν²). Not turned into a statement about b_n here (the W′-limit bookkeeping of JZC_W_exact §4 is not redone).

## 6. Rule A (adversarial pass) — log
1. *Rule X.* Registration (08:32:31) before every engine run; `shift_exact.py` asserts it per run. A first launch of the R1/R3 runs
   (08:33) was started as a detached shell job and killed by pid after ~1 min, before either engine finished (no output file existed;
   `tmp/shift/` was empty when checked); the runs were restarted as tracked background jobs. The registration files were first
   committed in af22e48 (09:13:39), after the runs; precedence rests on the filesystem mtimes and the in-file timestamps. eng_R1 and
   eng_R3 (mtimes 08:35:57) come from the 08:33 launch: the kill stopped the detached shell but not the engine subprocesses. Rule R
   review A re-ran R1, R4, R5, R6 from empty caches: byte-identical engine outputs. (fixed per Rule R review A, S5; the sentence
   "killed … before either engine finished" above is inaccurate in that respect.) The Toda predictions use the exact j = 1
   first-order layer and f₂ as inputs; the registered targets (h(1, 2) at p = 5/2, the μ₁², μ₁³ dressings at p = 5/2) are other
   coefficients. g₂ (also in R5) was already known (JZC_M4 §6) and is not counted as a prediction. The comparisons of §1.3 and §5.2 are
   with pre-existing data, made with formulas not fitted to them (LB; Toda), except the decomposition of g_j (read off j ≤ 7; labelled).
2. *Does Lemma D prove too much?* It needs the hard edge: with α_n(0) = 0 or 3cn^{−p} the leads are not LB (controls). It does not use
   any property of B, A beyond the leading coefficients (generic A_i, B_i drop out) — consistent with LB being α-, β-, ν-free.
3. *Defect vs natural form.* Interchanging n and N (N − n = (β + 1)/2) changes only defect ≥ 1 terms; the engine's natural form and FT's
   n-expansion are converted explicitly (`to_natural`), and FT reproduces exact engine coefficients at defects 0, 1, 2 (§5.2).
4. *Normalisations (Rule N 5).* e = μC(2j, j)c^j, μ = −tn^{−jp}; the sign/normalisation of (Toda) is fixed by E3.7 (A₀ = 1) and then
   tested against independent exact data (g_j, h₂, h(j, k)); a wrong ½ in ∂b or a wrong sign would break those.
5. *Equal exponents.* e₁e₂ at j = k is twice the μ² coefficient: used in (E4) and R1, consistent.
6. *Commuting flows.* FT computes each new coefficient through every admissible flow and asserts equality (42 checks in (D)).
7. *Symbolic exponents.* Substitution at integers commutes with the engine's operations (only j-denominators 2j − odd); the
   symbolic Taylor data at integer j are the integer polynomials (m4_zeta_exact2 (A), asserted j ≤ 8). The pole exponents q_m = m − 1/p
   are never half-integers for p ≠ 2 (JZC_W2), so the continued identities hold there.
8. *Fast engine.* FTfast (transfer recursion for (J^j)) = FT (path enumeration) asserted on generic data before use.
9. *Theorem T.* ~~Theorem T is a sketch; its analytic step is not reviewed.~~ Theorem T and T_H are now JZC_TODA (PROVED-mod-cite +
   REVIEWED); no uniformity in the tilt is needed (Baire, JZC_TODA Lemma T.2) (fixed per Rule R review A, S1). Its formal consequences are tested independently by m4_toda.out (numerical) and here by the exact
   agreement of the Toda-derived g_j, h₂, h(j, k) with the engine.
10. *pkill.* A `pkill -f` pattern again matched its own shell (cf. JZC_W2 Rule A 11); no data affected; processes then killed by pid.
11. *Interpolation of h(j, k).* Degree 8 was taken from the p = 3/2 form (jk × degree 6); the fit is unique and over-determined (25
    unknowns per part, 33 fit pairs) and reproduces 12 held-out pairs and the exact p = 3/2 symbolic form; still, the closed form is
    labelled CONJECTURE for general p (a degree bound in (j, k) is not proved). R7 is the registered out-of-sample test at p = 5/2.
12. *Edits after registration.* `shift_exact.py` gained an optional registration-file argument (for R7) after R1–R6 had run; R1–R6
    were then re-compared with the final script on the cached outputs (identical verdicts). `shift_common.py` was not changed after
    the registration (its sha256 1a4c1c70… is printed in every output).

## 7. What remains
1. ~~Rule R for this note.~~ Done: REVIEW_JZC_TODA_SHIFT_A.md, fixes S1–S5 applied.
2. ~~(T_H)~~: supplied by JZC_TODA Theorem T_H + Cor T.3 (PROVED-mod-cite + REVIEWED) (fixed per Rule R review A, S1). Remaining: a
   Rule R review of JZC_W2 Prop 2.1 (iii), on which the pole-layer reading of Cor SH.2 rests (S3).
3. The p = 2 second-order W′-type terms from the residues of §5.3 (needs JZC_W_exact §4's limit bookkeeping); a proof of the
   (j, k)-degree bound behind the h(j, k) closed form.
4. A closed form of the defect-2 part to all orders in the times (a dispersive correction to the hodograph solution, e.g. via the
   quasi-classical expansion of the Toda hierarchy/string equation); §5 gives the first and second orders.
5. Propagation: done 2026-10-23 after JZC_TODA / JZC_SHIFT review (JZC_W2 Obs 2.3 → Thm SH, Thm 2.5's remainder; JZC_M4 §8 a₂'s
   label; Paper IV).
6. Rule L (§8).

## 8. Literature (Rule L) — not done
Novelty UNCHECKED. The ingredients (dispersionless Toda hierarchy, Riemann invariants, hodograph solutions, string equations for
orthogonal polynomials with varying weights; cf. NOVELTY_JZC item N, Bleher–Its 2005) are of the kind found in the literature on
dispersionless limits and random matrices; none was read for this note, and nothing here depends on them.
