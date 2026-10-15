# Rule R review: Plan 64 (uniformity in s for the pure powers, UL.md)

Reviewer: independent second reader (Rule R). Branch `plan-64-uniform-lambda`, HEAD c813c50 (`git show c813c50`).
Targets:
- research/G1/RH/second_order/UL.md (all of §§0–7);
- checks/check_ul.py and check_ul.out;
- the two MANIFEST.sha256 lines added for them.

Context I re-read: SECOND.md §0, §2 (the Lommel input), §3.1 (Prop 3.1, Thm 3.2), §3.2 (Cor 3.6), §3.3 (Prop 3.7, (UΛ),
(CVX), Thm 3.8, Cor 3.9), §3.4 (Thm 3.10). Internal inputs I checked against their sources, with hypotheses and labels:
- G1 PROOF.md §3.4, Lemma TL: n ≥ 2, T′, T″, the bound ρ_{n+1}(k) ≤ 1156(C/c)(T″/k)^s, and μ_n ≤ ρ_{n+1};
- §3.8, Lemma LP: the weak convergence ν_n → ν_arc. It is in the *proof*, by the method of moments; UL cites it as such;
- §3.16, Theorem QLP(c): for each fixed σ, every ϑ < min(p/2, σ − 1), n ≥ n₀, m ∈ {n − 1, n}, all M ≥ 1. Also
  Corollary QLP-Λ and hypothesis (RU);
- §3.21, Lemmas CP, CT, CS;
- REVIEW_Plan62.md F10.

UL.md reads no external source, so I had no new Rule C item to check.

## Overall verdict: **ACCEPT WITH FIXES**

I found no mathematical error in any PROVED, PROVED-mod-cite or CONDITIONAL statement. I re-derived every proof
independently. The highest-risk claims all hold:
- the lower half (D) of Lemma V (a correct duality argument);
- the chaining in Thm UF;
- the limit identification in UF-lim;
- the pointwise uniform Law P (Thm UP), which is not circular;
- the o(log n) bound in Thm UΛ.

All findings are minor or INFO: label wording, one false-but-harmless monotonicity remark, one misattributed remark,
a missing Novelty field, and check hygiene. The check reproduces byte-for-byte. An independent numerical test I wrote
(including p = ½, s = 1.3 and non-lattice shifts) agrees with UF-lim and the Cor UL-3.8 constant.

| Statement | Verdict | Label after fixes |
|---|---|---|
| Lemma V (variational sandwich) | ACCEPT | PROVED (elementary) |
| Thm UF | ACCEPT WITH FIXES (F5: remark only) | PROVED-mod-cite ((P), (QLP-c) at finitely many fixed t) |
| Lemma W | ACCEPT | PROVED-mod-cite ((LP), (QLP-c), (P) at fixed t) |
| Thm UF-lim | ACCEPT WITH FIXES (F2) | PROVED-mod-cite ((P), (LP), (QLP-c) at fixed points only; (CS)) |
| Cor UL-3.8 | ACCEPT (F2 wording) | PROVED-mod-cite |
| Cor UL-3.9 | ACCEPT WITH FIXES (F4) | CONDITIONAL on (E) only + PROVED-mod-cite |
| Cor UL-3.10 (c′), (d′) | ACCEPT WITH FIXES (F3) | PROVED-mod-cite (UF-lim; Lommel input; RH_p1 §1, DLMF 5.11) |
| Thm UP | ACCEPT WITH FIXES (F2, F9) | PROVED-mod-cite |
| Prop UΛ⁻ | ACCEPT | PROVED-mod-cite |
| Thm UΛ | ACCEPT WITH FIXES (F6) | PROVED-mod-cite |
| Prop UΛ-L¹ | ACCEPT | PROVED-mod-cite |
| (UΛ-O(1)) | ACCEPT WITH FIXES (F7) | GAP |
| Prop R | ACCEPT WITH FIXES (F7) | PROVED-mod-cite; (SCVX) a HYPOTHESIS |
| Prop SV | ACCEPT | PROVED (elementary) |
| Remark CVX-fin | ACCEPT (F10 INFO) | PROVED |
| (CVX) status paragraph | ACCEPT (F11 INFO) | HYPOTHESIS; NUMERICAL |
| §6 checks | ACCEPT WITH FIXES (F8) | NUMERICAL |
| §7 Integration | ACCEPT WITH FIXES (F3, F12) | — |
| Novelty | missing (F1) | UNCHECKED |

## 1. Checks performed

**Re-run.** `csrc/build` was already present (`make -C csrc`: nothing to do). I ran
`PYTHONPATH=src …/jacobi-asymptotics/.venv/bin/python research/G1/RH/second_order/checks/check_ul.py`: exit 0, no
stderr. The output is **byte-identical** to the committed check_ul.out. The MANIFEST.sha256 hashes of check_ul.py and
check_ul.out match the files.

**Numbers quoted in UL.md vs check_ul.out.** All match:
- Lemma V min slack 8.8·10⁻³ (0.00882241);
- Prop SV agreement "to 10⁻⁵⁰" (max relative 2.17·10⁻⁵¹);
- CVX-fin: all six values negative;
- UF-lim remark (iii): 2.8·10⁻³ (p = 1) and 6.6·10⁻³ (p = 2) at n = 400, halving per doubling;
- UP remark (ii): 3.7·10⁻³ ≈ (4 − 1)/800 = 3.75·10⁻³;
- §5′ secant proxy: [0.691, 0.697] for p = 1 and [0.2435, 0.2449] for p = 2, against λ = 0.6931 and 0.2416.

The §5 (CVX) figures n·dd = 1.996, 0.4996, 0.2222, 0.1250, 0.0556, 0.0313 are 1600 × the n = 1600 values in
check_so_convex.out [2], as stated.

**Script logic.** In [1], Em = Σk^{−t−u}π_t²/h_t = E_t[k^{t−s}] and Ep = E_t[k^{s−t}], so (U) and (D) are tested in the
right direction. The skip condition t − |u| ≤ 1 is exactly the finiteness condition |s − t| < t − 1. In [2] and [3],
f_ij is computed in the Cholesky-orthonormal basis, and the numerical second derivative is taken of exact Hankel ratios.
[4] uses the same truncated-measure method as SECOND §1. As Rule N requires, this is NUMERICAL, not certified.

**Independent numerical test (mine, not committed; scratch script).** I used RKPW binary128 on `so_coeffs.measure`,
n ≤ 200, s ∈ {1.3, 1.55, 2.0, 2.7, 3.3}: non-grid points, one of them close to s = 1.

| p | K | max over s of \|F_n(s) − F_n(1.3) − (s − 1.3)log c/p\|, n = 50 / 100 / 200 | Cor UL-3.8 LHS − (predicted log term + constant), s₀ = 1.55, s₁ = 2.7, n = 50 / 100 / 200 |
|---|---|---|---|
| ½ | 8·10⁴ | 0.080 / 0.042 / 0.021 | 1.6·10⁻² / 8.2·10⁻³ / 4.2·10⁻³ |
| 1 | 2·10⁴ | 0.028 / 0.014 / 0.007 | −1.0·10⁻² / −5.0·10⁻³ / −2.5·10⁻³ |

In both columns the error halves with each doubling of n. So UF-lim and the constant ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁))
also hold numerically at p = ½ and for non-lattice shifts, which the committed check does not cover (p ∈ {1, 2} only).
For p = ½, max_s|n^{1/2}b_n/c − 1| = 2.4·10⁻², 1.2·10⁻², 5.8·10⁻³ at n = 50, 100, 200, consistent with Thm UP.

## 2. Statement-by-statement re-derivation

**Notation check.** μ_n^{(t)}(k) = k^{−t}π_n^{(t)}(x_k)²/h_n(t), a probability measure on ℕ, and E_t := E_{μ_n^{(t)}}.
- Its x-mean is α_n(t), the standard (diagonal) pairing: ⟨xπ_n, π_n⟩/h_n.
- (J²)_{nn} = α_n² + b_n² + b_{n+1}².
- UL writes h_n^{ch} for the chain h_n of SECOND §0 / Lemma CT. This avoids SECOND's clash with h_n = ∫π_n².

The definitions are precise and used consistently.

**Lemma V.** (U): h_n(s) = min over monic π of degree n of ∫π²dσ_s (orthogonal decomposition). The competitor π_t
gives h_n(s) ≤ Σk^{−s}π_t(x_k)² = h_n(t)E_t[k^{t−s}]. Adding (s − t)log n gives F_n(s) − F_n(t) ≤ log E_t[(k/n)^{t−s}].

(D) is the dual characterisation h_n(s)^{1/2} = dist_s(xⁿ, 𝒫_{n−1}) = sup{⟨xⁿ, φ⟩_s/‖φ‖_s : φ ⊥_s 𝒫_{n−1}}, used with
one admissible φ. I checked each step:
- φ(x_k) := k^{s−t}π_t(x_k) satisfies ⟨P, φ⟩_s = Σk^{−t}Pπ_t = ⟨P, π_t⟩_t. This is absolutely convergent, since P and
  π_t are bounded on [0, 1] and Σk^{−t} < ∞. So φ ⊥_s 𝒫_{n−1}.
- ⟨xⁿ, φ⟩_s = ⟨π_n^{(s)}, φ⟩_s = h_n(t).
- ‖φ‖_s² = Σk^{s−2t}π_t² = h_n(t)E_t[k^{s−t}].
- Cauchy–Schwarz gives h_n(t)² ≤ h_n(s)h_n(t)E_t[k^{s−t}].

The sign conventions and the k/n normalisation are right. (k/n)^{t−s} = Y^{(s−t)/p} and (k/n)^{s−t} = Y^{−(s−t)/p}, with
Y = n^px_k. So for s > t, (U) is a positive moment of Y (band side) and (D) a negative one (hard edge), both at the
single base point t. E_t[k^{s−t}] < ∞ iff s − t < t − 1, because μ_n^{(t)}(k) ≍ k^{−t} (π_t(0) ≠ 0, Lemma CP). The
vacuous case is handled. ACCEPT.

**Thm UF.** Put u₀ = ½m₀ and ϑ₀ = ¾m₀, with m₀ = min(p/2, a − 1). For t ∈ K, ϑ(p, t) ≥ m₀ > ϑ₀ > u₀, and u₀ ≤ p/4.
- B_t: (k/n)^{u₀} ≤ 1 on k ≤ n. For k > n, (k/n)^{u₀} = 1 + ∫_1^{k/n}u₀M^{u₀−1}dM. Tonelli turns the sum into
  ∫_1^∞u₀M^{u₀−1}μ_n((Mn, ∞))dM. QLP(c) with ϑ₀ applies for all M ≥ 1 and n ≥ n₀(t), which gives 2 + C_{ϑ₀}u₀/(ϑ₀ − u₀).
  For n < n₀ the terms are finite because t − u₀ > 1.
- Upper side: Jensen for r ≤ ¼, with E_t[Y] = n^pα_n(t) ≤ A_t (Law P at t; finitely many n). The log⁺ handles
  n^pα_n < 1.
- Lower side: (k/n)^{pr} ≤ 1 + (k/n)^{u₀} for 0 ≤ pr ≤ u₀.
- The cell bounds hold at both endpoints, and the chaining over J fixed cells is legitimate.

Both moment bounds are uniform in n, as the plan asked. The large-k (deep tail) side is controlled by QLP(c) for all M,
which covers the Bessel range and beyond. The small-k side is Law P via E_t[Y]. The exponent ranges are right. ACCEPT.
The Remark's justification for u ≥ p/2 is misattributed (F5).

**Lemma W.** V₋ is bounded as for B_t with u = pa′ < ϑ(p, t); this needs a QLP exponent strictly between pa′ and
ϑ(p, t), which exists. V₊ is bounded by Law P. ν_arc has the same two bounds, since pa′ < ϑ ≤ p/2 means a′ < ½. The
truncation estimates use three inequalities, each valid for Y < ε < 1:

  Y^{−a} ≤ Y^{−a′}ε^{a′−a},  ε^{−a} ≤ Y^{−a′}ε^{a′−a},  1 ≤ Y^{−a′}ε^{a′} ≤ Y^{−a′}ε^{a′−a}.

The large-Y side is the same with Y²R^{b−2}, b < 2. The constant 6C is generous but correct. g_{ε,R} is bounded and
continuous on [0, ∞), so the weak convergence of the proof of Lemma LP applies. ν_n has no mass at 0, and ν_arc has no
atom there. Uniform integrability is as stated. The growth conditions pa < min(p/2, t − 1) and b < 2 are exactly what
V₋, V₊ and ν_arc-integrability need. ACCEPT.

**φ and A₀.**
- φ(r) = log∫Y^r dν_arc is finite for r > −½.
- On [−¼, ¼], domination by Y^{±1/4}(1 + log²Y) is ν_arc-integrable: the density is ≍ y^{−1/2} at 0.
- φ″ is a tilted variance, so it is bounded on [−¼, ¼], and A₀ does not depend on u.
- ∫log y dν_arc = log(4c) + 2∫_0^{π/2}log sin²θ (2/π)dθ/2 = log 4c − 2log 2 = log c. Checked.

**Thm UF-lim.** Fix u ≤ u₀ and the grid t_i = a + iu.
- φ_n is convex (Hölder) and finite on [−r_u, r_u].
- Lemma V gives −φ_n(−r) ≤ F_n(s) − F_n(t_i) ≤ φ_n(r). Convexity with φ_n(0) = 0 gives the chord bounds
  ±(r/r_u)φ_n(±r_u).
- Lemma W applies with g = y^{±r_u}: pa = u < ϑ₀ < ϑ(p, t_i), and b = r_u ≤ ¼.
- Expanding φ(±r_u) = ±r_uφ′(0) + e_± gives |F_n(s) − F_n(t_i) − rφ′(0)| ≤ (r/r_u)(A₀r_u² + η_{n,i}). I re-derived
  both signs.
- The per-cell error is A₀r_u·r. Summed over the cells from a to s it is A₀r_u(s − a)/p ≤ A₀u(b − a)/p². This includes
  the partial last cell, because the bound is proportional to r.
- For fixed u the grid is finite, so sup_s → limsup ≤ A₀u(b − a)/p². Then u ↓ 0, with A₀ independent of u.

Identification: F_n(a + p) − F_n(a) = log(h_n(a+p)/h_n(a)) + p log n. By Prop 3.1, h_n(a+p)/h_n(a) = g_0·(g_n/g_0) = g_n.
Lemma CS with Law P at a gives log(n^pg_n(a)) → log c, so φ′(0) = log c. This is independent of, and consistent with,
the arcsine computation. Enlarging K to b ≥ a + p is harmless.

The order of limits is correct: n → ∞ at fixed u, then u → 0. The uniformity on K × K follows by differences. One
wording issue: the "at finitely many fixed points" label is not literally right (F2). ACCEPT WITH FIXES.

**Cor UL-3.8.** h_n = ζ(s)Πb_j², so 2Σlog(b_j(s₁)/b_j(s₀)) = F_n(s₁) − F_n(s₀) − (s₁ − s₀)log n − log(ζ(s₁)/ζ(s₀)).
UF-lim then gives −((s₁ − s₀)/2)log n + ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) + o(1). At s₁ − s₀ = p this is exactly SECOND
Thm 3.2: −(p/2)log n + ½log(cζ(s₀)/ζ(s₀ + p)). It is also consistent with Cor UL-3.10(c′). ACCEPT.

**Cor UL-3.9.**
- (E_ε) at s gives log(j^pb_j/c) = d₁/j + O(j^{−1−ε}) + O(j^{−2}), so 𝒟_n(s) = d₁log n + O(1).
- The difference of two such sums, compared with Cor UL-3.8, gives the slope.
- The p = 1 route via Cor UL-3.10(d′) is valid.
- The p = 2 anchor needs no hypothesis (F4).

ACCEPT WITH FIXES.

**Cor UL-3.10.**
- (c′) is a direct rewriting: 𝒟_n(s) − 𝒟_n(s₀) = ½(F_n(s) − F_n(s₀)) − ½(s − s₀)log n − ½log(ζ(s)/ζ(s₀)). The constant
  ((s − s₀)/(2p))log c − ½log(ζ(s)/ζ(s₀)) checks out.
- (d′), p = 2: from b_n = π²/((4n+1)√((4n−1)(4n+3))) and c(2) = π²/16, I get
  n²b_n/c = (1 + 1/(4n))⁻¹(1 + 1/(4n) + O(n⁻²))⁻¹ = 1 − 1/(2n) + O(n⁻²). So 𝒟_n(2, 2) = −½log n + const + o(1).
- (d′), p = 1: Cor 3.6(i) has an O(1/n) remainder, and log(nb_n^{TC}/c) = −½log(1 + 1/(2n)) = −1/(4n) + O(n⁻²). So
  𝒟_n(1, 3/2) = −¼log n + const + o(1).
- With (c′), 𝒟_n(p, s) + ((s − 1)/2)log n converges for every s > 1 at p ∈ {1, 2}. The Hankel restatement follows.

The math is correct. The labels and citations name SECOND Thm 3.10(a),(b), but the proof uses the stronger convergent
forms of the underlying inputs (F3). ACCEPT WITH FIXES.

**Thm UP (scrutinized as a strong claim; it is sound and not circular).**
- For n ≥ 2, log b_n(s)² = log h_n(s) − log h_{n−1}(s), with F_{n−1} built with log(n − 1).
- So log(b_n(s)²/b_n(s₀)²) = Δ_n(s) − Δ_{n−1}(s) − (s − s₀)log(n/(n − 1)) exactly; I re-derived it.
- UF-lim gives sup_K|Δ_n − L| → 0 with L(s) = ((s − s₀)/p)log c independent of n. So sup_K|Δ_n − Δ_{n−1}| → 0. This
  is a first difference of a uniformly convergent sequence. A bound alone (Thm UF) would not suffice, as §5′ notes
  correctly.
- Nothing circular: UF-lim uses only fixed-point inputs ((P), (LP), (QLP-c) at grid points) plus Lemma CS at one point.
- The g-part: n^pg_n(s) = exp(F_n(s + p) − F_n(s)), via h_n(s+p)/h_n(s) = g_n(s) (Prop 3.1). UF-lim on [a, b + p]
  gives → c uniformly.
- The α-part: Lemma CT gives n^pα_n = n^pg_n + (n^pb_n)²/(n^pg_{n−1}), with (n/(n−1))^p → 1, so → c + c = 2c uniformly.

The step from h_n ratios to individual b_n is valid. ACCEPT WITH FIXES (F2: the "(P) at one point" wording; F9).

**Prop UΛ⁻.** For y ≥ 1, log y ≤ y^p/p, so Σ_{k<n}log(n/k)μ_n ≤ (1/p)n^pα_n(s). Thm UP covers n ≥ N₀. For the
finitely many smaller n, α_n(s) is continuous in s on K (a rational function of ζ-moments). ACCEPT.

**Thm UΛ.**
- *Step 1.* The contradiction argument is valid. The i-th moment of the rescaled μ_{n_j}^{(s_j)} uses only α_m(s_j),
  b_m(s_j) with |m − n_j| ≤ i, and n_j^pb_m(s_j) = (n_j/m)^p·m^pb_m(s_j) → c by the *uniform* Thm UP along any s_j ∈ K.
  The limit is compactly supported, so the method of moments applies, and ν_arc has no atoms at M^{−p}. This is
  "Lemma LP's method with uniform coefficients", correctly applied.
- *Step 2.* Lemma TL applies to w = k^{−s} with c = C = 1, for n ≥ 2. T′ and T″ do not depend on s. T = T″^m is an
  integer ≥ T″. With m = ⌈(a+1)/(a−1)⌉ ≥ (s+1)/(s−1) for s ≥ a, s − m(s − 1) ≤ −1. The integral is
  T^{1−s}(log T/(s−1) + (s−1)^{−2}), and max(x, x²) ≤ 1 + x² gives the stated uniform bound O((log T″)/T″) → 0. One
  side remark is false but harmless (F6).
- *Step 3.* Tonelli, monotonicity of the tail, log M_ε + ε·log(T/n), and T″ ≤ (8p + 2)n^{2+2/p}, so
  log T ≤ mC_p log n.
- No hidden log n: the coefficient εmC_p has ε arbitrary and m, C_p depending only on K and p.

ACCEPT WITH FIXES (F6).

**Prop UΛ-L¹.**
- Λ_n = −(1/p)E_s[log Y].
- Lemma W with g = log (|log y| ≤ C_δ(y^{−δ} + y^δ), pδ < ϑ) gives the pointwise limit −(log c)/p.
- ∫_K(Λ_n + C) = F_n(a) − F_n(b) + C(b − a), because F_n′ = −Λ_n (Prop 3.7 plus the s log n term). UF-lim gives the
  limit of the integrals.
- Scheffé applies, since f_n ≥ 0 and f is a constant. Correct.

ACCEPT.

**Prop R.** (UΛ-O(1)) ⇔ bounded Lipschitz constants holds because F_n′ = −Λ_n. (SCVX) gives F_n″ ≥ −C (s log n is
linear), so Λ_n(s) ≤ Λ_n(a) + C(b − a). Λ_n(a) = O(1) at the fixed point a by QLP-Λ (k ≥ n) and Law P (k < n). Correct.
ACCEPT WITH FIXES (F7: table wording).

**Prop SV.** I re-derived it:
- ∂_s⟨A, B⟩_s = −⟨A, LB⟩ + ⟨Ȧ, B⟩ + ⟨A, Ḃ⟩;
- c_i = f_in for i < n, and c_n = f_nn/2;
- L_n′ = −(L²)_nn + 2Σ_{i≤n}c_if_in = −(L²)_nn + 2Σ_{i<n}f_in² + f_nn²;
- ∂_s²log h_n = −L_n′ = Var − 2Σ_{i<n}f_in².

Parseval needs completeness of the polynomials in L²(σ_s). That holds: σ_s is a finite measure on the compact [0, 1],
so C[0, 1] is dense and Weierstrass applies. Hence Var = Σ_{j≠n}f_nj², and the second form and the bracket for Λ_n′
follow. ACCEPT.

**Remark CVX-fin.** For N atoms, L²(σ^{(N)}) = 𝒫_{N−1}, so there is no j > N − 1. If all f_{i,N−1} = 0 (i < N − 1), then
(log k − f)P_{N−1}(x_k) = 0 at every atom. The log k are distinct, so P_{N−1} is supported at no more than one atom.
⟨P_{N−1}, 1⟩ = 0 kills that atom too, contradicting ‖P_{N−1}‖ = 1. The [3] numerics agree. The concluding sentence is
slightly broader than what is shown (F10). ACCEPT.

**§5 (CVX) status.** The numbers check out (§1). "No longer needed for Thms 3.8–3.10" is correct, given Cor UL-3.8,
UL-3.9 and UL-3.10. ACCEPT.

**§0 inputs.** Each bullet matches its source's hypotheses and label, as checked in the header. Two points:
- (QLP-c) is used only at fixed t, as claimed: no (RU).
- (TL)'s "c = C = 1" is the sandwich constant pair of Lemma TL, not c(p). That is clear from context.

## 3. Findings

**F1 (minor; Novelty field missing).**
*Issue.* UL.md has no Novelty line. VERIFICATION_POLICY requires the separate field, default UNCHECKED, and no Rule L
search was done.
*Fix.* Under the summary table, add:

  "Novelty: UNCHECKED throughout (no Rule L search). Lemma V (minimum/duality sandwich) and Prop SV (second variation
  of log h_n) are elementary variational computations; novelty not claimed."

**F2 (minor; dependency wording "finitely many fixed points" and "(P) at one point").**
*Issue.* Thm UF uses finitely many base points. Thm UF-lim does not: its proof takes u ↓ 0, and each u needs its own
grid. In all it uses (P), (LP) and (QLP-c) at countably many fixed points (each fixed, with no uniformity in σ). This
is harmless, since these inputs are proved for every fixed σ > 1, but the label is inaccurate in four places:
- the UF-lim heading ("at finitely many fixed points");
- the §7 Integration row for Thm 3.8 and THEOREMS §2.10 ("Law P, QLP(c) at finitely many fixed σ");
- Thm UP's label "(P) at one point";
- §5′ "Uses (P) at one point only for the value c".

UP inherits UF-lim's whole footprint.
*Fix.*
- UF-lim, Cor UL-3.8 and UL-3.10, and the §7 texts: write "(P), (LP), (QLP-c) at fixed points only (finitely many for
  each grid, countably many in all); no uniformity in σ, (RU) not used".
- Thm UP's label: "PROVED-mod-cite (Thm UF-lim, hence (P), (LP), (QLP-c) at fixed points; Lemma CT)".
- §5′: "(P) at s₀ is used directly only for the value c".

**F3 (minor; Cor UL-3.10 citations and §7).**
*Issue.* The label of Cor UL-3.10 and its summary row cite "SECOND Thm 3.10(a),(b) anchors". Those state only O(1)
remainders. The proof of (d′) correctly uses stronger inputs (const + o(1)):
- p = 2: the exact Lommel b_n (SECOND §2 Input: VA §3, DLMF-Lommel, via Paper 2 Remark rem:pure-lommel);
- p = 1: Cor 3.6(i) (RH_p1 §1, DLMF 5.11).

*Fix.*
- Change the label to "PROVED-mod-cite (UF-lim; SECOND §2 Input (VA, DLMF-Lommel); SECOND Cor 3.6(i) (RH_p1 §1,
  DLMF 5.11))", in the heading, the summary row and the §7 rows for Thm 3.10(d).
- In §7, also update SECOND §3.4's sentence "Equivalently, for the Hankel ratios … in cases (a), (b)" to "for every
  s > 1 at p ∈ {1, 2} (UL.md Cor UL-3.10(d′)), with O(1) improvable to const + o(1)".

**F4 (minor; Cor UL-3.9).**
*Issue.* The summary row says "under (E) at s (and, for p = 2, at 2)". (E) at (2, 2) is not a hypothesis: SECOND
Thm 2.3 proves the exact expansion.
*Fix.* Delete "(and, for p = 2, at 2)". Optionally, prove the p = 2 case through Cor UL-3.10(d′), exactly as for
p = 1, so that both anchors are hypothesis-free.

**F5 (minor; Remark after Thm UF).**
*Issue.* "for u ≥ p/2 it is not bounded in n (the arcsine tail M^{−p/2} of QLP(a))" has the wrong reason. QLP(a) is an
upper bound and cannot show unboundedness.
*Fix.* Write: "for u ≥ p/2, liminf_n E_t[(k/n)^u] ≥ ∫y^{−u/p}dν_arc = ∞ (Lemma LP's weak convergence and Fatou; the
arcsine density is ≍ y^{−1/2} at 0)".

**F6 (minor; Thm UΛ step 2).**
*Issue.* "y^{−s}log y is decreasing for y ≥ 2" is false for 1 < s < 1/log 2 ≈ 1.443: it decreases only for
y ≥ e^{1/s}, which lies in (2, e) there. The bound survives, since T ≥ T″ ≥ 32p·4^{1/p} ≥ 120 > e.
*Fix.* Replace with "decreasing for y ≥ e^{1/s}, in particular for y ≥ e, and T ≥ T″ ≥ 3".

**F7 (minor; summary table, (UΛ-O(1)) and Prop R).**
*Issue.* The row "(UΛ-O(1)) | GAP; ⇐ (RU) …" does not say that the (RU) implication is at PROOF SKETCH level (Audit U).
§4 does say so. (SCVX) is a new named assumption with no label.
*Fix.*
- Write "⇐ (RU) (PROOF SKETCH level, Audit U)".
- Add a row "(SCVX): ∃C, n₀: (log h_n)″ ≥ −C on K, n ≥ n₀ | HYPOTHESIS (⇐ (CVX))".

**F8 (minor; check hygiene).**
*Issue.* The docstring of check_ul.py and the header of section [4] refer to "Prop. UB", which does not exist in UL.md
(it is Thm UP). Also, [4] tests only the b-part of Thm UP; the g- and α-parts are not printed.
*Fix.*
- Rename "Prop. UB" to "Thm UP".
- Optionally print sup_s|n^pα_n(s)/(2c) − 1| (jc.a is available).
- Re-run, commit the new .out, and update the two MANIFEST lines.
- In §6, state that [4] covers the b-part.

**F9 (INFO; Thm UP proof).** "UF-lim on K ∪ (K + p)": that set is not an interval when b − a < p, and UF-lim is stated
for compact intervals. Write "on the interval [a, b + p]".

**F10 (INFO; Remark CVX-fin last sentence).** "Any proof of (CVX) for σ_{p,s} must use the infinite support" is broader
than what is shown. The remark shows that no argument valid for all exponential families x^{s/p}σ₀, including finitely
supported σ₀, can give (CVX) at every level n < dim L². The failure is at the top level n = N − 1 only.
*Suggest:* "must use a property of σ₀ that fails for finite truncations (the failure shown is at the top level
n = N − 1)".

**F11 (INFO; (CVX) numerics).** dd in check_so_convex.py is the standard second divided difference (≈ f″/2). So
n·dd ≈ 1/(2p²) means (log h_n)″ ≈ 1/(p²n). UL.md quotes only n·dd, which is correct. Keep the factor of 2 straight if
the integrator merges this with SECOND §3.3's "roughly 1/(2p²n)", which also refers to dd.

**F12 (minor; §7 Integration completeness).** The list is accurate. Every SECOND and THEOREMS location it names exists:
- SECOND summary rows for Thm 3.8, Cor 3.9, Thm 3.10 and (CVX);
- SECOND §3.3 (UΛ) status, Thm 3.8, Cor 3.9 and "(CVX) suffices";
- SECOND §3.4 Thm 3.10;
- SECOND §4 "Soft routes tried";
- THEOREMS §2.10 rows (lines 377–378), §4 item 13 (line 517 ff.), and the QLP row (line 319).

Add:
- (a) the §3.4 "Equivalently … in cases (a), (b)" sentence (F3);
- (b) the THEOREMS §2.10 heading: add "and UL.md (Plan 64, REVIEWED <date>, REVIEW_Plan64.md)";
- (c) UL.md's own Status line: REVIEWED, with this file, once the fixes are applied;
- (d) carry the F2 and F3 label wording into every row copied to SECOND and THEOREMS.

## 4. Required before REVIEWED

Apply F1–F8 and F12 (F9–F11 are optional). Re-run check_ul.py after F8 and update MANIFEST.sha256. After that, the
PROVED, PROVED-mod-cite and CONDITIONAL statements of UL.md can carry REVIEWED with the labels in the table above, and
the §7 integration into SECOND.md and THEOREMS.md can proceed. A diff-check of the fixes by a second reader is
sufficient; no re-derivation is needed.
