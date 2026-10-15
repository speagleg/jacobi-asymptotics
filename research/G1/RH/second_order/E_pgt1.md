# E_pgt1: the 1/n coefficient (E) for pure powers, p > 1, by second-order Riemann–Hilbert analysis (Plan 65)

Status (2026-10-15): written by the Plan 65 agent; **not REVIEWED** (Rule R pending). Labels per VERIFICATION_POLICY.md.
"RH" means Riemann–Hilbert throughout. This file closes, for p > 1, the GAP "(E)" of SECOND.md §4 and settles g(p) = 0
for p > 1. It does not edit SECOND.md or THEOREMS.md; the proposed changes are listed in §11 (Integration).

**Summary of labels.**

| # | Statement | Label |
|---|---|---|
| Thm E.1 | p > 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + O(n⁻²)), n^pα_n = 2c(1 − (s−1+p)/(2n) + O(n⁻²)); hence α_n/(2b_n) = 1 − p/(2n) + O(n⁻²) (e₁ˢ = −p/2) and α_{n−1}/(2b_n) = 1 + p/(2n) + O(n⁻²) (e₁ = p/2) | PROVED-mod-cite (RH_px [REVIEWED]; Paper 2 Lemmas binetcut, szego, airy, Frame Prop.; KMVV §6; DLMF 9.7.2, 9.7.5–6, 10.17, 10.40.1–4) + exact computer algebra (check_e_sym) |
| Cor E.6 | p > 1, s > 1: n^pg_{n−1} = c(1 + a/n + O(n⁻²)), a = (2s−2−p)/(2p); chain γ_N² = c(N/2)^{−p}(1 + (k₀ + k₁(−1)^N)/N + O(N⁻²)) with k₀ = −(s−1) − p/2, k₁ = −(p+2)a | PROVED-mod-cite (as Thm E.1, + DLMF 10.25.2) + exact computer algebra |
| Lemma E.2 | the band factor H_n = (D̃B)⁻² is constant up to O(n^{−p}) (with one derivative) on {\|z\| ≤ 4c+1}, boundary values on (−∞, 0) included | PROVED-mod-cite (Paper 2 Lemma binetcut; DLMF 5.5.1, 5.11 via Paper 2) |
| Lemma E.3 | jumps of the error matrix on the two circles: I + Δ₁/n + O(n⁻²), Δ₁ explicit (Bessel and Airy first corrections) | PROVED-mod-cite (KMVV (6.23)–(6.28) [via CITATIONS]; DLMF 10.40.1–4, 10.17.1, .5, .6, .8, .11, .12; DLMF 9.7.2, 9.7.5–6; Paper 2 Lemma airy) |
| Lemma E.4 | local data: f′(0) = −1/(c(p+2)²), f″(0)/f′(0) = 4τ₁/3 = (p+2)/(6c(3p+2)); φ̃ = −κu³(1 + κ₂u² + O(u⁴)), u = (z−4c)^{1/2}, κ = 1/(6pc^{3/2}), κ₂ = −(7p+4)/(40pc); ω and ρ of the model weight in closed form | PROVED (from G2's μ*, as quoted in RH_px §2 / Paper 2 Lemma signs; Paper 2 Lemma szego(i)) |
| Lemma E.5 | Laurent coefficients A₀, C₀ (at 0), A_r, B_r (at 4c) of Δ₁ | PROVED (exact sympy series, check_e_sym.py, all assertions pass) |
| Prop E.5′ | R = I + R⁽¹⁾/n + O(n⁻²) uniformly off the contour and for the first two moments at ∞, R⁽¹⁾ = A₀/z + A_r/(z−4c) + B_r/(z−4c)² outside the discs | PROVED-mod-cite (RH_px §5 small-norm bounds; Paper 2 Frame Prop. F1) |
| §8 | consequences for SECOND §3: Cor 3.3, Thm 3.4, Cor 3.9, Thm 3.8/3.10(d) become unconditional for p > 1; g(p) = 0 for p > 1 | PROVED-mod-cite (as Thm E.1) |
| §9 GAP | (E) for p = 1 and 0 < p < 1; the second-order coefficient d₂; Rule L | GAP |

Numerical cross-checks (NUMERICAL, not used in the proofs): `checks/check_e_num.out` (Airy and Bessel correction
matrices in all sectors; R⁽¹⁾ moments by contour integration of Δ₁ built from quadrature of g and of the Szegő integral —
reproduces d₁, e₁ˢ, k₁ at six (p, s) to ≤ 1.3·10⁻⁷), `checks/check_e_flat.out` (Lemma E.2), `checks/check_e_rate.out`
(second-order residuals of the actual coefficients bounded), `checks/check_e_grid.out` (80/80 grid constants), and the Plan 62 grid table (SECOND §1.1, `check_so_grid.out`):
the proved closed forms are exactly the conjectured ones there, and agree with every p > 1 row to the fit accuracy.

Novelty: UNCHECKED (Rule L not done; see §9).

## 0. Setting and conventions

- σ = σ_{p,s} = Σ_{k≥1}k^{−s}δ_{k^{−p}}, **p > 1**, s > 1; α := α_x = (s−1−p)/p > −1 (Bessel order at the hard edge, RH_px
  Lemma 1.2); a := α + ½ = (2s−2−p)/(2p); c = c(p) = ¼(π/(2I_p))^p, I_p = (√π/2)Γ(1/p+½)/Γ(1/p+1). We use
  B_p := B(1/p+½, ½) = 2I_p, so (4c)^{1/p} = π/B_p.
- Monic OPs xπ_n = π_{n+1} + α_nπ_n + b_n²π_{n−1} (SECOND §0). **Standard pairing** α_n/(2b_n) (coefficient e₁ˢ); repo
  pairing α_{n−1}/(2b_n) (coefficient e₁). Chain: g_n = −π_{n+1}(0)/π_n(0), h_n = b_n²/g_{n−1}, α_n = g_n + h_n
  (Lemma CT; SECOND Lemma 2.1: g_n = γ_{2n+1}², h_n = γ_{2n}²).
- **Frame.** We use the RH analysis of RH_px (REVIEWED) written in the Q-frame of Paper 2 (papers/paper2, §§5–6,
  specialised to ℓ₁ ≡ 1, p > 1): U(z) = n^{pnσ₃}Y(z/n^p), then R, T, S, V as in Paper 2 (eq. VM) with the outer scalar
  F = DBK (Paper 2 Lemma outer, = RH_px §3), band weight W₀ = 𝗐_n z^α(4c−z)H_n(z), H_n = (D̃B)^{−2} (Paper 2 (eq. W0),
  Lemma binetcut(iv)), D_W the Szegő function of W₀, ω := D_W²/W₀, and Q := D_∞^{−σ₃}VD_W^{σ₃} (Paper 2 (eq. Q)). In this
  frame the global parametrix is P₀^∞ = T a^{σ₃}T^{−1}, a = ((z−4c)/z)^{1/4}, T := [[1, 1], [i, −i]]/√2 (one checks
  P₀^∞(1, i)ᵀ = a(1, i)ᵀ and P₀^∞(1, −i)ᵀ = a^{−1}(1, −i)ᵀ, which is Paper 2 (eq. Pinf0)). RH_px's 𝒵 "in the D_{w,∞}-
  conjugated frame" is the error matrix R := Q·(parametrix)^{−1} below. Extraction (Paper 2 F8 / RH_px §5):
  (Q₁)₁₂(Q₁)₂₁ = n^{2p}b_n², (Q₂)₁₂/(Q₁)₁₂ − (Q₁)₂₂ = n^pα_n, for Q = I + Q₁/z + Q₂/z² + ….
- At ∞: P₀^∞ = I + P₁/z + P₂/z² + O(z⁻³), P₁ = [[0, ic], [−ic, 0]], P₂ = [[c²/2, 2ic²], [−2ic², c²/2]] (expand a =
  (1 − 4c/z)^{1/4}); so (P₁)₁₂(P₁)₂₁ = c², and the a-functional of P₀^∞ is 2c (the first-order statement of RH_px §5).
- M := [[1, i], [i, 1]]/√2. Note T^{−1}M = diag(1, i) and σ₃Mσ₃ = M^{−1}.

## 1. Main results

**Theorem E.1 (PROVED-mod-cite; inputs listed in the table).** Let p > 1 and s > 1. Then, as n → ∞,

  n^pb_n = c(p)(1 − (s−1)/(2n) + O(n⁻²)),
  n^pα_n = 2c(p)(1 − (s−1+p)/(2n) + O(n⁻²)),

and consequently

  α_n/(2b_n) = 1 − p/(2n) + O(n⁻²)  (e₁ˢ = −p/2),   α_{n−1}/(2b_n) = 1 + p/(2n) + O(n⁻²)  (e₁ = p/2).

In particular (E) of SECOND §4 holds for p > 1 with ε = 1 (that is, (E₁)), d₁ = −(s−1)/2, and Conjecture P62 holds for
p > 1 with the conjectured remainder O(n^{−1−min(1,p)}) = O(n⁻²).

**Corollary E.6 (chain; PROVED-mod-cite).** For p > 1, s > 1: n^pg_{n−1} = c(1 + a/n + O(n⁻²)). Equivalently
G_m := m^pg_m = c(1 + (a − p)/m + O(m⁻²)), H_m := m^ph_m = c(1 − (s−1+a)/m + O(m⁻²)), and the symmetric chain satisfies
γ_N² = c(N/2)^{−p}(1 + (k₀ + k₁(−1)^N)/N + O(N⁻²)) with **k₀ = −(s−1) − p/2, k₁ = −(p+2)a** — the values of SECOND §1.1.

The proof occupies §§2–7. The mechanism, in one paragraph: the 1/n terms of b_n and α_n come only from the first
corrections of the Bessel model at 0 and the Airy model at 4c (the global parametrix is exactly invariant, RH_px §5); these
corrections depend on the degree n only through the band factor H_n, and the identified missing step of SECOND §4
(step 3) is resolved by Lemma E.2: H_n is **constant to O(n^{−p})**, because the 1/n Binet term of D̃ and the 1/n part of
the Binet-cut scalar B cancel exactly (−z^{1/p}/(12n) + (z^{1/p} − 1)/(12n) = −1/(12n)). So the first corrections are
those of the fixed model weight x^α(4c − x), and their residues are explicit. The hard-edge residue is
c(p+2)(4α²−1)/16·[[1, i], [i, −1]], which is symmetric off the diagonal and so does not contribute to b_n at order 1/n;
d₁ comes entirely from the simple-pole residue of the Airy correction, where the p-dependence cancels.

## 2. Lemma E.2: the band factor is flat to O(n^{−p})

Notation of Paper 2 Lemma binetcut (= RH_px Lemma 3.2): j is Binet's function (j(t) = LnΓ(t) − (t−½)ln t + t − ½ln 2π),
t = nz^{−1/p}, θ = πt, D̃ = e^{−j(t)}, 𝔟(y) = 2Im(−j(t₊(y)) − Log(1 − e^{−2iθ₊(y)})) for y < 0, and
B(z) = exp(−(1/2π)∫_{−∞}^0 𝔟(y)[1/(y−z) − 1/(y−1)]dy). Put G := −j(t) + log B, analytic on ℂ ∖ (−∞, 0], so that
H_n = e^{−2G} (Paper 2 Lemma binetcut(iv)). Let R₁ := 4c + 2.

**Lemma E.2 (PROVED-mod-cite: Paper 2 Lemma binetcut (i)–(iii); the Binet bounds (eq. binet-bound), (eq. binet-small)
and DLMF 5.5.1 as quoted in Paper 2 §6).** For p > 1 there is C = C(p) such that for all n ≥ 1:
(i) |G(z) − G(1)| ≤ Cn^{−p} for |z| ≤ R₁, z ∉ (−∞, 0], and for the boundary values G_± on (−R₁, 0);
(ii) |G′(z)| ≤ Cn^{−p} for |z| ≤ R₁/2, z ∉ (−∞, 0], and for the boundary values on (−R₁/2, 0).
Hence log H_n(z) − log H_n(1) = −2(G(z) − G(1)) = O(n^{−p}) with the same uniformity, and so is its derivative.

*Proof.* (a) *Jump.* On (−∞, 0), t₋ = conj(t₊) and j is real on (0, ∞), so j(t₋) = conj j(t₊). By Paper 2 Lemma
binetcut(iii), (log B)₊ − (log B)₋ = −i𝔟. Hence

  G₊ − G₋ = −2i Im j(t₊) − i𝔟 = 2i Im Log(1 − e^{−2iθ₊}) =: i𝔢(y).

With q := e^{−2iθ₊(y)}, |q| = exp(−2π sin(π/p) n|y|^{−1/p}) < 1 (p > 1) and |Im Log(1 − q)| ≤ arcsin|q| ≤ (π/2)|q|, so

  |𝔢(y)| ≤ π exp(−2π sin(π/p) n|y|^{−1/p}),  |𝔢′(y)| ≤ C n|y|^{−1−1/p}exp(−2π sin(π/p)n|y|^{−1/p})

(the derivative from dt₊/dy = −t₊/(py) and |q′/(1 − q)| ≤ 2|q′| for |q| ≤ ½; for |q| > ½, |y| ≥ cn^p and the bound
|𝔢′| ≤ C/|y| suffices below). 𝔢 is real-analytic on (−∞, 0).

(b) *Representation.* Put K(z) := G(z) − G(1) − (1/2π)∫_{−∞}^0 𝔢(y)[1/(y−z) − 1/(y−1)]dy. The integral converges
absolutely (𝔢 bounded, bracket O(|y|⁻²)), and by the Sokhotski–Plemelj formula its jump on (−∞, 0) is i𝔢, so K has no
jump and is analytic on ℂ ∖ {0} (Morera). Near 0: |arg t| ≤ π/p < π and |t| → ∞, so j(t) → 0 by (eq. binet-bound) with
φ = π/p; log B is bounded near 0 including the boundary values (Paper 2 Lemma binetcut(iii), (eq. B-bounds) and the
(O5) argument there); the integral is bounded near 0 because 𝔢 is super-exponentially small there. So 0 is removable.
At ∞: for |t| ≤ 1, |arg t| ≤ π/p, DLMF 5.5.1 gives LnΓ(t) = LnΓ(1+t) − ln t with |1+t| ≥ sin(π − π/p) > 0, so
|j(t)| ≤ C(1 + |log|z||); |log B(z)| ≤ C_n(1 + log|z|) (proof of binetcut(iv), (O5)); the integral is O(log|z|). So K is
entire with K(z) = O(log|z|), hence constant, and K(1) = 0. Therefore

  G(z) − G(1) = (1/2π)∫_{−∞}^0 𝔢(y)·(z − 1)/((y − z)(y − 1)) dy.   (E.2.1)

(c) *Bounds.* Split at |y| = 2R₁. Far part: for |y| ≥ 2R₁ and |z| ≤ R₁, |z−1|/(|y−z||y−1|) ≤ C/|y|², and with |y| = n^pw,
∫_{2R₁}^∞ min(1, e^{−c₁nu^{−1/p}})u^{−2}du ≤ n^{−p}∫_0^∞ min(1, e^{−c₁w^{−1/p}})w^{−2}dw = C n^{−p}. Near part: on
[−2R₁, 0) the density 𝔢 and its derivative are O(e^{−c₂n}) (as |y|^{−1/p} ≥ (2R₁)^{−1/p}), and vanish to all orders at 0;
the Cauchy integral of such a C¹ density, and its boundary values on (−R₁, 0), are bounded by C·e^{−c₂n}(1 + |log
dist(z, −2R₁)|) ≤ C′e^{−c₂n} for |z| ≤ R₁ (subtract 𝔢(Re z) on a window, as in Paper 2 binetcut (O5)). This is (i). For
(ii) differentiate (E.2.1): the far part gives ∫|𝔢|/|y|² = O(n^{−p}), the near part O(e^{−c₂n}) (Cauchy integral of the
C¹ density 𝔢′ after an integration by parts; 𝔢(−2R₁)/(−2R₁ − z) is bounded for |z| ≤ R₁/2). ∎

*Remarks.* (1) The two O(1/n) pieces do exist separately: −j(t) = −z^{1/p}/(12n) + O(n⁻³) and log B(z) =
(z^{1/p} − 1)/(12n) + O(n^{−p}) on compacts — the Binet term's cut on (−∞, 0) is exactly what B is built to remove, and the
subtracted Cauchy transform of the jump of z^{1/p} is z^{1/p} − 1 (Liouville, since 1/p < 1). RH_px Lemma 3.2(iv) and
SECOND §4 step 3 bounded D̃ and B separately and so saw O(1/N). (2) Numerically (check_e_flat.out),
max|G(z) − G(1)|·n^p is stable in n at p = 3/2, 3 while |j(t(z)) − j(t(1))|·n is stable, i.e. each factor varies at
order 1/n and the product at order n^{−p}. (3) At p = 2, θ₊(y) = −iπn|y|^{−1/2} is purely imaginary, so e^{−2iθ₊} ∈ (0, 1), 𝔢 ≡ 0 and H_n is **exactly** constant
(check_e_flat.out: |G(z) − G(1)| ≤ 10⁻²⁷ at 30 digits) — consistent with the exact Lommel chains at p = 2. (4) The real
reason is structural: H_n = e^{−2G} where G has only the
super-small jump 𝔢 on (−∞, 0) near the origin; all its non-constant behaviour on compacts comes from |y| ≍ n^p.

## 3. Lemma E.3: the jumps on the two circles to second order

Let U_0 := U(0, δ), U_r := U(4c, ε) be the discs of RH_px / Paper 2 (radii fixed, small). In U_r use Paper 2's Airy
parametrix P̂_r (eq. airy); in U_0 use RH_px's Bessel parametrix P₀ (RH_px §4.1, KMVV (6.42)–(6.53) at the endpoint −1;
Paper 2 Remark rem:quotient-p1 records that this classical construction works for pure powers, p ≠ 1), written in the
Q-frame as P̂₀ := D_∞^{−σ₃}P₀D_W^{σ₃}. With ρ := W̃/D_W (RH_px §4.1 W̃² = W₀·e^{∓iπα} in ℂ_±, KMVV (6.45) pattern),
ρ² = e^{∓iπα}/ω.

**Lemma E.3 (PROVED-mod-cite).** Uniformly on the circles (boundary values where they cross the contour),

  P̂₀(P₀^∞)^{−1} = I + Δ₁⁰/n + O(n⁻²) on ∂U_0,   P̂_r(P₀^∞)^{−1} = I + Δ₁^r/n + O(n⁻²) on ∂U_r,

with

  Δ₁⁰ := (1/(16 f^{1/2})) P₀^∞ ρ^{σ₃} Q₀ ρ^{−σ₃}(P₀^∞)^{−1},  Q₀ := [[−(1+4α²), 2i], [2i, 1+4α²]],
  Δ₁^r := −(1/φ̃) P₀^∞ (−ω)^{−σ₃/2} X (−ω)^{σ₃/2}(P₀^∞)^{−1},  X := [[−1/72, −i/12], [−i/12, 1/72]],

where f is the hard-edge map (RH_px Lemma 4.1 / Paper 2 Lemma signs(iii), f^{1/2} = −(φ ± iπ)/2 in ℂ_±), φ̃ = −(2/3)f_r^{3/2}
(Paper 2 Lemma signs(iv)), and (−ω)^{1/2} is Paper 2's root (eq. omega-root). Moreover Δ₁⁰, Δ₁^r depend on n only
through H_n, and

  Δ₁^{⋄} = Δ₁^{⋄,mod} + O(n^{−p})  (⋄ ∈ {0, r}),

where "mod" means ω (hence ρ) computed for the model weight W₀^{mod} = 𝗐_n z^α(4c − z), i.e. with H_n replaced by a
constant.

*Proof.* *Bessel.* KMVV (6.28) and its derivation (CITATIONS "(KMVV-orient, Paper 2)": the I_α, K_α asymptotics in
|arg ζ| < 2π/3, the Hankel asymptotics in the other two sectors, "exactly the same formula") give the leading term; we
need one more term. In |arg ζ| < 2π/3, KMVV (6.23) is Ψ = [[I_α(w), (i/π)K_α(w)], [πi w I_α′(w), −wK_α′(w)]], w = 2ζ^{1/2},
and DLMF 10.40.1–10.40.4 (|ph w| ≤ π/3 < π/2 − δ) with a₁(α) = (4α²−1)/8 (10.17.1) and b₁(α) = (4α²+3)/8 (10.17.8) give,
entrywise with relative errors O(w⁻²): Ψ e^{−wσ₃} = (2πζ^{1/2})^{−σ₃/2}[M + (1/w)·diag-scaled corrections]. Writing
Ψe^{−wσ₃} = L(I + Ξ/w + O(w⁻²)), L := (2πζ^{1/2})^{−σ₃/2}M, one computes L^{−1}·(correction) = M^{−1}(1/√2)[[−a₁, ia₁],
[−ib₁, b₁]] = ½[[−(a₁+b₁), i(a₁−b₁)], [i(a₁−b₁), a₁+b₁]], and a₁ + b₁ = (4α²+1)/4, a₁ − b₁ = −½, so

  Ψ(ζ) = (2πζ^{1/2})^{−σ₃/2} M [I + (1/(16ζ^{1/2}))[[−(1+4α²), −2i], [−2i, 1+4α²]] + O(ζ^{−1})] e^{2ζ^{1/2}σ₃}.   (E.3.1)

In the sectors 2π/3 < ±arg ζ < π (KMVV (6.24)–(6.25), Hankel functions of 2(−ζ)^{1/2}), the same computation with DLMF
10.17.5, 10.17.6, 10.17.11, 10.17.12 (first two terms; the sectors of 10.17.5/6 contain ph 2(−ζ)^{1/2} ∈ (−π/6, π/6) —
CITATIONS "(DLMF-10.17, Plan 55)") gives the same formula (E.3.1); check_e_num.out [2] confirms (E.3.1) numerically in all
three sectors (α = 0.3, −0.6). Now insert into P₀ = (−1)^NẼ_Nσ₃Ψ(N²f)σ₃W̃^{−σ₃}e^{Nφσ₃} (RH_px §4.1): σ₃Ψσ₃ conjugates
the correction to Q₀/16; Ẽ_N(2πζ^{1/2})^{−σ₃/2} = N W̃^{σ₃}M (ζ^{1/2} = Nf^{1/2}); Mσ₃Mσ₃ = I; and
e^{2Nf^{1/2}σ₃}e^{Nφσ₃}(−1)^N = I since φ = ∓iπ − 2f^{1/2}. So P₀ = N W̃^{σ₃}(I + Q₀/(16Nf^{1/2}) + O(N⁻²))W̃^{−σ₃}, and
conjugating to the Q-frame (N = D_∞^{σ₃}P₀^∞D_W^{−σ₃}) gives the first claim. The O(N⁻²) is uniform on ∂U_0 because
|ζ^{1/2}| ≍ N there and P₀^∞, ρ^{±1} are bounded on ∂U_0 uniformly in n (Paper 2 Lemma szego(vi)(a),(c)).

*Airy.* Paper 2 (eq. airy-infty) is the leading term of Ψ^j. With DLMF 9.7.5–9.7.6 to two terms and 9.7.2 (u₁ = 5/72,
v₁ = −7/72; see the CITATIONS entry added for Plan 65), in sector I, with ξ = (2/3)ζ^{3/2}:
y₊ = (e^ξ/(2√π))ζ^{−σ₃/4}e^{iπ/6}(1 + u₁/ξ, 1 + v₁/ξ)ᵀ, y₀ = (e^{−ξ}/(2√π))ζ^{−σ₃/4}(1 − u₁/ξ, −(1 − v₁/ξ))ᵀ (relative errors
O(ξ⁻²)), hence Ψ^I = ζ^{−σ₃/4}M(I + X/ξ + O(ξ⁻²))e^{ξσ₃} with X = [[(u₁+v₁)/2, i(v₁−u₁)/2], [−i(u₁−v₁)/2, −(u₁+v₁)/2]] =
[[−1/72, −i/12], [−i/12, 1/72]]; the other sectors follow from the connection relations (eq. airy-relations) as in
Paper 2 (and check_e_num.out [1] confirms X numerically in all four sectors). With ξ = n·(2/3)f_r^{3/2} = −nφ̃ and
A_rn^{σ₃/6}ζ^{−σ₃/4} = P₀^∞(−ω)^{−σ₃/2}M^{−1}, the factors M^{−1}M cancel and e^{ξσ₃}((−ω)^{1/2}e^{nφ̃})^{σ₃} = (−ω)^{σ₃/2},
so P̂_r = P₀^∞(−ω)^{−σ₃/2}(I − X/(nφ̃) + O(n⁻²))(−ω)^{σ₃/2} — the second claim, uniformly on ∂U_r (Paper 2 Lemma airy(iii)
gives the bounds on P₀^∞, (−ω)^{±1/2}).

*n-dependence.* f, φ̃, P₀^∞ do not depend on n (Paper 2 Lemma signs). By (eq. omega), ω = ω^{mod}·(D²_{H°}/H°) with
H° := H_n/H_n(1); and (Paper 2 (eq. szego-repr) with 𝔠 = log H°(z)) log D²_{H°}(z) − log H°(z) =
(𝓡(z)/π)∫_0^{4c}(log H°(x) − log H°(z))dx/(√(x(4c−x))(z − x)). By Lemma E.2, |log H°| ≤ Cn^{−p} on (0, 4c] and on a fixed
complex neighbourhood of every point where a circle meets [0, 4c] (these points, δ and 4c − ε, are away from (−∞, 0]),
and |(log H°)′| ≤ Cn^{−p} there; splitting the integral into a window around Re z (derivative bound) and the rest (sup
bound, with ∫x^{−1/2}(4c−x)^{−1/2} < ∞), the right side is O(n^{−p}) uniformly on both circles. So ω/ω^{mod} = 1 + O(n^{−p}),
and Δ₁ depends smoothly on ρ² = e^{∓iπα}/ω and (−ω)^{±1/2}, which are bounded above and below uniformly
(Paper 2 Lemma szego(vi)). ∎

## 4. Lemma E.4: local data of the model

All from μ* = ∫_0^1 arc_{β_τ}dτ, β_τ = 4cτ^{−p}, with dμ*/dx = ψ* = λ_p I_{x/4c}(1/p + ½, ½), λ_p = (1/p)x^{−1−1/p}
(G2 input as quoted in RH_px §2 and Paper 2 Prop. equilibrium; I_y the regularized incomplete beta function). Put
a′ := 1/p + ½.

**Lemma E.4 (PROVED).**
(i) ψ*(x) = C₀x^{−1/2}(1 + τ₁x + O(x²)) with C₀ = (4c)^{−1/2}/(π(1 + p/2)), τ₁ = a′/(8c(a′+1)). Hence (Paper 2 Lemma
  signs(iii): f = −(π²/4)z𝔞(z)², μ*((0, x]) = x^{1/2}𝔞(x)) 𝔞 = 2C₀(1 + τ₁z/3 + O(z²)) and
  f(z) = −π²C₀²z(1 + (2τ₁/3)z + O(z²)); in particular f′(0) = −π²C₀² = −1/(c(p+2)²).
(ii) φ̃ = −κu³(1 + κ₂u² + O(u⁴)), u := (z − 4c)^{1/2} (principal), with κ = 1/(6pc^{3/2}) > 0, κ₂ = −(7 + 4/p)/(40c).
(iii) For the model weight: −ω^{mod} = (4c/Υ)^{1+α}, (−ω^{mod})^{1/2} = (2√c/(z^{1/2} + (z−4c)^{1/2}))^{1+α} near 4c, and near 0
  ρ^{mod} = ((−z)^{1/2}/(2√c) + (1 − z/(4c))^{1/2})^{1+α} (up to a sign, irrelevant in Δ₁⁰).

*Proof.* (i) I_y(a′, ½) = (1/B_p)∫_0^y t^{a′−1}(1−t)^{−1/2}dt = y^{a′}/(a′B_p)·(1 + a′y/(2(a′+1)) + O(y²)), and
λ_p(x)(x/4c)^{a′} = (1/p)(4c)^{−a′}x^{−1/2}; with (4c)^{−1/p} = B_p/π, (1/p)(4c)^{−a′}/(a′B_p) = (4c)^{−1/2}/(πpa′) = C₀.
Integrate for μ*((0, x]) and use Paper 2's formula for f; π²C₀² = π²/(4cπ²(1+p/2)²) = 1/(c(p+2)²).
(ii) Paper 2 Lemma signs(iv) (proof): φ̃₊(x) = iπ∫_x^{4c}(λ_p − ψ*) on the band. With y = 4c(1 − e), 1 − I_{1−e}(a′, ½) =
(1/B_p)∫_0^e(1 − τ)^{a′−1}τ^{−1/2}dτ = (1/B_p)(2e^{1/2} − (2/3)(a′ − 1)e^{3/2} + O(e^{5/2})) and λ_p(y) =
(1/p)(4c)^{−1−1/p}(1 + (1 + 1/p)e + O(e²)); integrating, with v := 4c − x, ∫_x^{4c}(λ_p − ψ*) =
((4c)^{−1/p}/(pB_p))[(4/3)(v/4c)^{3/2} + (2/5)(7/3 + 4/(3p))(v/4c)^{5/2} + O(v^{7/2})]. On the band from ℂ₊, u = iv^{1/2}, so
−κu³(1 + κ₂u²) = iκv^{3/2}(1 − κ₂v); comparing: κ = π(4c)^{−1/p}(4/3)(4c)^{−3/2}/(pB_p) = (4/(3p))(4c)^{−3/2} =
1/(6pc^{3/2}) and −κ₂ = (3/4)(2/5)(7/3 + 4/(3p))/(4c) = (7 + 4/p)/(40c). φ̃/u³ is analytic at 4c because φ̃² = (4/9)f_r³
(Paper 2 Lemma signs(iv)), so the band values determine the expansion.
(iii) Paper 2 Lemma szego(i): D²_{x^α} = (4cz/Υ)^α, D²_{4c−x} = 4c(z−4c)/Υ, Υ = (z^{1/2} + (z−4c)^{1/2})²; so for the model
ω = (4cz/Υ)^α z^{−α}·(−4c/Υ), which near 4c is −(4c/Υ)^{1+α} (all arguments small), and its root is (eq. omega-root) with
L₁ = α log(4c/Υ). Near 0, in ℂ_±, z^{1/2} = ±i(−z)^{1/2} and (z−4c)^{1/2} = ±i(4c−z)^{1/2}, so Υ = −Υ̂ with
Υ̂ := ((−z)^{1/2} + (4c−z)^{1/2})²; (4cz/Υ)^α = (−z)^α(4c/Υ̂)^α and z^α = (−z)^αe^{±iπα}, so ω^{mod} = e^{∓iπα}(4c/Υ̂)^{1+α} and
ρ² = e^{∓iπα}/ω^{mod} = (Υ̂/4c)^{1+α}. ∎

## 5. Lemma E.5: the Laurent coefficients (exact computer algebra)

**Lemma E.5 (PROVED; checks/check_e_sym.py, sympy, all assertions pass, output check_e_sym.out).** For the model data of
Lemma E.4, Δ₁^{r,mod} and Δ₁^{0,mod} are meromorphic in U_r, U_0 (all half-integer powers of (z − 4c), resp. z, cancel) with

  Δ₁^{r,mod} = B_r/(z−4c)² + A_r/(z−4c) + O(1),   Δ₁^{0,mod} = A₀/z + C₀ + O(z),

  B_r = (5c²p/12)[[1, −i], [−i, −1]],
  A_r = (c/48)[[12α²p + 24αp + 11p + 2, −i(12α²p + 48αp + 49p + 2)], [−i(12α²p + p + 2), −(12α²p + 24αp + 11p + 2)]],
  A₀ = (c(p+2)(4α²−1)/16)[[1, i], [i, −1]],
  C₀ = ((p+2)/(96(3p+2)))[[−(10α²p + 8α² − 36αp − 24α − 7p − 5), i(26α²p + 16α² + 72αp + 48α + 70p + 47)],
        [i(26α²p + 16α² − 2p − 1), 10α²p + 8α² − 36αp − 24α − 7p − 5]].

*Method.* Δ₁^r: write P₀^∞ Z (P₀^∞)^{−1} = T[[Y₁₁, a²Y₁₂], [a^{−2}Y₂₁, Y₂₂]]T^{−1}, Y = T^{−1}ZT, with a² = u/z^{1/2},
z^{1/2} = (4c + u²)^{1/2}, (−ω)^{±1} from Lemma E.4(iii), φ̃ from E.4(ii), expanded as power series in u to the needed
order (the truncation orders are exact: B_r, A_r need the coefficients of u^{−4}, u^{−2}, i.e. u-series of the
numerator to u²). Δ₁⁰: the same on the negative axis z = −v², v > 0 (outside the lens, where f > 0 and f^{1/2} > 0), with
f from E.4(i) and ρ from E.4(iii); A₀ and C₀ are the coefficients of the even powers; the odd ones are verified to vanish.
The hand computation of A₀ (K := lim z a²/f^{1/2} = −2√(c/|f′(0)|) = −2c(p+2), T^{−1}Q₀T|_{ρ=1} = [[0, 1−4α²], [−(3+4α²), 0]],
Te₁₂T^{−1} = ½[[1, i], [i, −1]], A₀ = (K(1−4α²)/16)·½[[1, i], [i, −1]]) agrees. Independent NUMERICAL confirmation:
check_e_num.out [3] integrates the Δ₁ built from quadrature (no closed form of Lemma E.4 used) over the circles.

*Remark (why A₀ does not affect b_n).* A₀ has equal off-diagonal entries; the b-functional at order 1/n is
i((R₁)₂₁ − (R₁)₁₂)/c (§7), which annihilates such matrices. This is the same mechanism by which the hard-edge residues
give no 1/n term for fixed Jacobi weights in KMVV (Theorem 1.10 there; not used here).

## 6. Proposition E.5′: second-order small norm

Let R := Q(P₀^∞)^{−1} outside Ū_0 ∪ Ū_r, R := QP̂₀^{−1} in U_0, R := QP̂_r^{−1} in U_r (RH_px §5's 𝒵 in the D_∞-frame). Orient
both circles clockwise, so that R₊ (outside) = R₋ (inside)·J on the circles.

**Proposition E.5′ (PROVED-mod-cite: RH_px §5 (small norm, identification), Paper 2 Prop. frame F1 (uniform Cauchy bound,
length O(n^p)), F5).** For p > 1, s > 1:

  R(z) = I + R⁽¹⁾(z)/n + O(n⁻²)

uniformly for z at distance ≥ d > 0 from the contour Σ_R, and for the moments at ∞: R = I + R_1/z + R_2/z² + O(z⁻³) with
R_k = R_k⁽¹⁾/n + O(n⁻²), where (Lemma E.3, E.5)

  R⁽¹⁾(z) = A₀/z + A_r/(z − 4c) + B_r/(z − 4c)²  (z outside the discs),
  R_1⁽¹⁾ = A₀ + A_r,  R_2⁽¹⁾ = 4cA_r + B_r,
  R⁽¹⁾(0) = −C₀ − A_r/(4c) + B_r/(16c²)  (value at the centre of U_0, used in §7.2).

*Proof.* The jump of R: on the circles J = P̂(P₀^∞)^{−1} = I + Δ₁/n + O(n⁻²) with Δ₁ = Δ₁^{mod} + O(n^{−p}) (Lemma E.3);
inside U_r there is no jump (P̂_r has exactly the jumps of Q, Paper 2 Lemma airy(ii)); inside U_0 the jump is the
hard-edge mismatch, O(n^{−K}min(1, |z|^K)) for every K (RH_px Lemma 4.3); on the band outside the discs there is no jump
(P₀^∞ has the band jump of Q); on the lips, Σ_v, the saturated segment, Σ^△ and the top segment J − I = O(e^{−n/C}),
resp. O(n^{−pn/4}) (RH_px Gate 3, §4.3; Paper 2 F5), on pieces of total length O(n^p). So ‖J − I‖_{L¹∩L²∩L^∞} = O(1/n),
and with ‖𝒞₋‖_{L²→L²} ≤ C (Paper 2 F1) the singular integral equation R₋ = I + 𝒞₋(R₋(J − I)) gives ‖R₋ − I‖_{L²} = O(1/n)
(this is RH_px §5's first-order statement; identification of Q with this solution: RH_px §5). Then

  R(z) − I = (1/2πi)∫_{Σ_R}(J − I)(s)ds/(s − z) + (1/2πi)∫_{Σ_R}(R₋ − I)(J − I)(s)ds/(s − z),

and the second integral is ≤ ‖R₋ − I‖_{L²}‖J − I‖_{L²}/d = O(n⁻²). In the first, the circles contribute
(1/n)(1/2πi)∮_{cw}Δ₁^{mod}(s)ds/(s − z) + O(n⁻² + n^{−1−p}) and everything else O(e^{−n/C}). For p > 1, n^{−1−p} ≤ n⁻². Since
Δ₁^{mod} is meromorphic in the discs with the Laurent data of Lemma E.5, (1/2πi)∮_{cw}Δ₁(s)ds/(s − z) = −Res_{s=e}[Δ₁(s)/(s−z)]
summed over e ∈ {0, 4c}, which equals the principal parts A₀/z + A_r/(z−4c) + B_r/(z−4c)² for z outside the discs, and
(at z = 0) −C₀ − A_r/(4c) + B_r/(16c²) (residue of Δ₁⁰(s)/s at 0 is C₀; residue of Δ₁^r(s)/s at 4c is A_r/(4c) − B_r/(16c²)).
The moments: R_k = −(1/2πi)∫R₋(J − I)s^{k−1}ds (k = 1, 2), with the same splitting; on the far pieces |s|^{k−1} ≤ Cn^p is
absorbed by e^{−n/C} or n^{−pn/4}; and −(1/2πi)∮_{cw}Δ₁ s^{k−1}ds = Σ_e Res Δ₁ s^{k−1} gives A₀ + A_r and 4cA_r + B_r. For the
value at 0 (inside U_0, near the contour pieces in U_0): those pieces carry jumps O(n^{−K}|s|^K) and super-small entries,
so their contribution to R(0) is O(n^{−K}); the circle ∂U_0 is at distance δ from 0. ∎

## 7. Proof of Theorem E.1 and Corollary E.6

### 7.1 b_n and α_n

By Paper 2 F8 / RH_px §5 and the invariance lemma, the extraction functionals of Q equal those of R·P₀^∞ for |z| large.
Q₁ = P₁ + R_1, Q₂ = P₂ + R_1P₁ + R_2. With R_1 = A/n + O(n⁻²), A := A₀ + A_r, and R_2 = (4cA_r + B_r)/n + O(n⁻²):

  n^{2p}b_n² = (ic + A₁₂/n)(−ic + A₂₁/n) + O(n⁻²) = c²(1 + i(A₂₁ − A₁₂)/(cn)) + O(n⁻²).

A₀ contributes 0 (equal off-diagonal entries). From A_r: A₂₁ − A₁₂ = −(ic/48)[(12α²p + p + 2) − (12α²p + 48αp + 49p + 2)] =
ic·p(α + 1), so i(A₂₁ − A₁₂)/c = −p(α+1) and

  n^pb_n/c = 1 − p(α+1)/(2n) + O(n⁻²) = 1 − (s−1)/(2n) + O(n⁻²).

For α_n, a(Q) = (Q₂)₁₂/(Q₁)₁₂ − (Q₁)₂₂ expanded to first order in 1/n (check_e_sym.py does this symbolically; the α²-terms
coming from A₀ and A_r cancel) gives n^pα_n = 2c − cp(α+2)/n + O(n⁻²), i.e. n^pα_n/(2c) = 1 − (s−1+p)/(2n) + O(n⁻²), since
p(α+2) = s − 1 + p. Dividing: α_n/(2b_n) = 1 − p/(2n) + O(n⁻²). For the repo pairing, (n/(n−1))^p = 1 + p/n + O(n⁻²) gives
α_{n−1}/(2b_n) = (1 − (s−1+p)/(2n))(1 + p/n)/(1 − (s−1)/(2n)) + O(n⁻²) = 1 + p/(2n) + O(n⁻²). ∎

### 7.2 The chain (Corollary E.6)

*Identity.* With Y the Fokas–Its–Kitaev matrix (Paper 2 Lemma interp), Y₁₁ = π_n, Y₂₁ = κ_nπ_{n−1} with κ_n = (Y₁)₂₁ (the
coefficient of z^{−1} in Y₂₁z^{−n}); so g_{n−1} = −π_n(0)/π_{n−1}(0) = −(Y₁)₂₁Y₁₁(0)/Y₂₁(0). Under U = n^{pnσ₃}Y(·/n^p),
U₁₁(0) = n^{pn}Y₁₁(0), U₂₁(0) = n^{−pn}Y₂₁(0), (U₁)₂₁ = n^pn^{−2pn}(Y₁)₂₁; and on the negative axis near 0 (in Ω_∞, outside
the lens) Q = k_∞^{−σ₃}U·(diagonal) (Paper 2 (eq. VM), (eq. Q-at-infinity)), while (Q₁)₂₁ = k_∞²(U₁)₂₁. Column ratios are
unchanged by right diagonal factors, so

  n^pg_{n−1} = −(Q₁)₂₁ · lim_{z→0⁻} Q₁₁(z)/Q₂₁(z).   (E.6.1)

*Evaluation.* For z ∈ U_0 on the negative axis, Q = R·P̂₀, and the first column of P̂₀ is proportional to
P₀^∞ρ^{σ₃}M f^{σ₃/4}(2πn)^{σ₃/2}(Ψ₁₁, −Ψ₂₁)ᵀ(n²f). There f > 0, ζ = n²f > 0 lies in the I_α/K_α sector, and by DLMF 10.25.2
(Ψ₂₁/Ψ₁₁ = πi·xI_α′(x)/I_α(x), x = 2ζ^{1/2}) Ψ₂₁/Ψ₁₁ → πiα as z → 0 (α > −1, I_α(x) > 0 for small x > 0). So the direction
of the first column of Q(0) is that of R(0)·(w⁽⁰⁾ + w⁽¹⁾/n), with

  w⁽⁰⁾ = lim_{z→0⁻}P₀^∞ρ^{σ₃}M(f^{1/4}, 0)ᵀ = (1, i)ᵀ/√(p+2),  w⁽¹⁾ = lim_{z→0⁻}P₀^∞ρ^{σ₃}M(0, −iαf^{−1/4}/2)ᵀ,

both finite (P₀^∞ ~ |z|^{−1/4}, f^{±1/4} ~ |z|^{±1/4}; check_e_sym.py computes them: w⁽¹⁾ = (α(α+2), iα²)ᵀ√(p+2)/4). Note that
w⁽⁰⁾ depends on ρ only through ρ(0) = 1 (T^{−1}ρ^{σ₃}T = [[ch, sh], [sh, ch]] with sh = O(|z|^{1/2}), killed by f^{1/4}/a).
With R(0) = I + R⁽¹⁾(0)/n + O(n⁻²) (Prop. E.5′) and (Q₁)₂₁ = −ic + A₂₁/n + O(n⁻²), (E.6.1) gives (exact sympy, check_e_sym.py)

  n^pg_{n−1} = c(1 + (α + ½)/n) + O(n⁻²) = c(1 + a/n + O(n⁻²)).

*Remainder.* The model was used for ρ in w⁽¹⁾ and in R⁽¹⁾(0). The true ρ_n = ρ^{mod}(D²_{H°}/H°)^{−1/2}; on the negative
axis z = −v², log(D²_{H°}/H°)(−v²) = v·λ_n + O(n^{−p}v²) with |λ_n| ≤ Cn^{−p} by (eq. szego-repr) and Lemma E.2(ii)
(log H°(x) − log H°(0) = O(n^{−p}x)), so w⁽¹⁾ changes by O(n^{−p}) and the total change is O(n^{−1−p}) = O(n⁻²).

*Unfolding.* G_m = m^pg_m: n^pg_{n−1} = (1 + p/n + O(n⁻²))G_{n−1} gives G_m = c(1 + (a − p)/m + O(m⁻²)). From
Theorem E.1, n^{2p}b_n² = n^{2p}g_{n−1}h_n = c²(1 − (s−1)/n + O(n⁻²)), so H_n := n^ph_n = c(1 − (s−1+a)/n + O(n⁻²)). In
the symmetric variable (g_m = γ_{2m+1}², h_m = γ_{2m}²), γ_N²/(c(N/2)^{−p}) = 1 + (k₀ + k₁(−1)^N)/N + O(N⁻²) holds iff
H_m = c(1 + (k₀+k₁)/(2m)) and G_m = c(1 + (k₀ − k₁ − p)/(2m)) (expand ((2m+1)/2)^{−p}m^p = 1 − p/(2m) + O(m⁻²)); so
k₀ + k₁ = −2(s−1+a) and k₀ − k₁ = 2a − p, i.e. k₀ = −(s−1) − p/2, k₁ = −(s−1) − 2a + p/2 = −(p+2)a (using s − 1 = p(a + ½)).
∎

*Consistency with RH.md Lemma 5.1* (unfolding: d₁ = (p/2 + k₀)/2, e₁ = p/2): (p/2 − (s−1) − p/2)/2 = −(s−1)/2 ✓.

## 8. Comparisons and consequences

### 8.1 Comparison with the exact p = 2 results and the grid (no mismatch)

- SECOND Thm 2.3 (p = 2, s ∈ {2, 4, 6, 8, 10}, exact): d₁ = −(s−1)/2 ✓; e₁ˢ = −1 = −p/2 ✓; k₀ = −s = −(s−1) − 1 ✓;
  k₁ = −2(s−2) = −(2+2)(2s−4)/4 ✓. And n²α_n/(2c) for σ_{2,2} (Lommel, α_n = 2π²/((4n+1)(4n+5)), c = π²/16):
  16n²/((4n+1)(4n+5)) = 1 − 3/(2n) + O(n⁻²) = 1 − (s−1+p)/(2n) ✓.
- SECOND §1.1 grid (check_so_grid.out), rows p ∈ {3/2, 2, 3, 4}, s ∈ {3/2, 2, 3, 4}: every fitted d₁, e₁, e₁ˢ, k₀, k₁ equals
  the proved value to within max(fit half-range, 5·10⁻¹⁰ table rounding); largest deviation 5.3·10⁻⁸ (k₁ at (2, 3/2), fit
  half-range 2.5·10⁻⁶); 80/80 pass (`checks/check_e_grid.out`). The p = 1, ½ rows are not covered by Theorem E.1.
- check_e_num.out [3]: d₁, e₁ˢ, n^pg_{n−1}/c, a, k₁ from contour integration of the quadrature-built Δ₁ at (p, s) = (2, 3),
  (3/2, 2), (3, 5/2), (5/2, 9/2), (2, 2), (5/4, 4) (α from −½ to 1.4): all agree with the closed forms to ≤ 1.3·10⁻⁷.
- check_e_rate.out: the second-order residuals n²(n^pb_n/c − 1 + (s−1)/(2n)), n²(n^pα_n/(2c) − 1 + (s−1+p)/(2n)) and
  n²(n^pg_{n−1}/c − 1 − a/n) of the actual coefficients (n = 50…799; (p, s) = (3/2, 2), (2, 3), (3, 5/2), (5/4, 4)) stay bounded
  (≤ 5.73 in absolute value, still drifting slowly at p = 3/2, 5/4 as an n^{1−p} term would): an illustration of the
  O(n⁻²), NUMERICAL.

### 8.2 What becomes unconditional (for p > 1)

Theorem E.1 gives (E_1), i.e. (E_ε) with ε = 1, at every (p, s) with p > 1, s > 1. Hence, for p > 1:
- **SECOND Cor 3.3** (needs (E) at s and s + p, both > 1): unconditional — d₁(s+p) = d₁(s) − p/2 and n(G_n − G_{n−1}) → 0
  (the latter also directly from Cor E.6: n(G_n − G_{n−1}) = O(1/n)). The hypothesis of G1 Remark SH-1/n holds.
- **SECOND Thm 3.4** (needs (E_ε), ε > ½): unconditional, and superseded by Theorem E.1 (which gives O(n⁻²) instead of
  O(n^{−2ε′})).
- **SECOND Cor 3.9**: its conclusion d₁(s₁) − d₁(s₀) = −(s₁ − s₀)/2 holds for p > 1 without (E) and without (UΛ)/(CVX) (it
  is read off Theorem E.1). In particular **g(p) = 0 for every p > 1** (PROVED-mod-cite). For p = 1 Cor 3.9 remains
  CONDITIONAL.
- **SECOND Thm 3.8** for p > 1: Σ_{j≤n}log(b_j(s₁)/b_j(s₀)) = −((s₁−s₀)/2)log n + O(1), unconditionally (sum Theorem E.1);
  (UΛ), (CVX) are not proved by this (they remain HYPOTHESIS), only no longer needed for p > 1.
- **SECOND Thm 3.10(d)** for p = 2: the log-average form 𝒟_n = −((s−1)/2)log n + O(1) holds for every s > 1 (from E.1);
  for p = 1 off the lattice 3/2 + ℕ₀ it stays CONDITIONAL.
- **Conjecture P62**: PROVED-mod-cite for p > 1 (all five constants d₁, e₁, e₁ˢ, k₀, k₁, with the conjectured remainder
  O(n⁻²) for b_n, α_n and the chain). Open for 0 < p ≤ 1.
- **THEOREMS item 13**: (E) is proved for p > 1; the −1/24 second-order conjecture at p = 1 is untouched.

## 9. What remains open (GAP)

- **(E) for p = 1** (GAP). The same scheme in RH₁(r)'s symmetric frame or the x-frame of route2: the outer scalar at p = 1
  is D = e^{j(−n/z)} (Paper 2 eq. reflection), which has no cut, so H_n = e^{2j(n/z)} = 1 + z/(6n) + O(n⁻²) is **not** flat
  at order 1/n: the analogue of Lemma E.2 fails, and the 1/n term of H_n enters Δ₁ at order n⁻¹·n⁻¹ only — so it is
  harmless for d₁ — but the hard edge at p = 1 cannot use the classical Bessel parametrix (Paper 2 Remark
  rem:quotient-p1) and Paper 2's comparison parametrix has no rate (Paper 2 §1 "The hard edge"). Missing: a hard-edge
  parametrix at p = 1 with an O(n⁻²) matching error. The predicted value d₁ = −(s−1)/2 at p = 1 also follows from the
  Airy residue computation above if the hard-edge residue is again off-diagonal-symmetric (HEURISTIC).
- **(E) for 0 < p < 1** (GAP): Γ's poles enter the slit plane; Paper 2's seam scalar. The numerics (SECOND §1) show
  remainders n^{−1−p}, which the present scheme would have to produce from the seam (the H_n of the seam geometry is not
  flat to o(1/n) near 0: (O3) only gives |z|(1 + log(1/|z|)) there).
- **d₂** (second order): would need Δ₂ and the O(n^{−p}) part of H_n, which enters Δ₁ and hence n^pb_n/c at order
  n^{−1−p}; so for 1 < p < 2 the remainder O(n⁻²) of Theorem E.1 presumably contains an n^{−1−p} term below an n⁻² term
  (HEURISTIC; consistent with the SECOND §1 fit basis {n^{−1−i−jp}} and with the slow drift in check_e_rate.out).
- **Rule L** (novelty) not done: second-order RH expansions for varying weights with hard + soft edges are standard
  (KMVV §8 for fixed Jacobi weights); what is specific here is Lemma E.2 and the discrete/saturated geometry.

## 10. Rule A (adversarial pass) — log

- *Sign of Δ₁^r.* A first symbolic pass had −1/φ̃ replaced by +1/φ̃ and produced d₁ = +(s−1)/2; traced to the sign of
  φ̃ = −κu³ in the code (κ > 0 because φ̃ < 0 on (4c, ∞)). After the fix, d₁ = −(s−1)/2, and the fully independent
  quadrature check [3] (which uses φ̃ from g by quadrature, no κ) agrees.
- *Orientation of R.* Clockwise circles with R_out = R_in·J ⇒ R⁽¹⁾_out = principal parts of Δ₁ (not their negatives); checked
  by the jump identity R⁽¹⁾_out − R⁽¹⁾_in = Δ₁ and by the numerics.
- *Pairing.* The RH problem of degree n yields α_n (diagonal of π_n) and b_n² = h_n/h_{n−1} (Paper 2 Lemma interp,
  (eq. extractU)); the standard pairing α_n/(2b_n) gives −p/2, and the repo pairing +p/2, as in SECOND §0.
- *Meromorphy.* Odd powers of (z−4c)^{1/2}, resp. z^{1/2}, cancel identically (asserted in check_e_sym.py) — a nontrivial test
  of the branch choices of a², (−ω)^{1/2}, ρ, f^{1/2}.
- *A₀ normalisation.* Tested three ways: hand computation (§5), sympy series, contour integral ([3]: (1,1) entry agrees to
  10⁻⁹); and α = ±½ (4α² = 1) gives A₀ = 0 (the Bessel model is then elementary): numerically 4·10⁻⁹, 10⁻⁹.
- *H_n flatness.* Could the n^{−p} bound of Lemma E.2 fail near 0 or on (−δ, 0)? Near 0 the jump density 𝔢 is
  super-exponentially small; the far part is the only source. check_e_flat.out samples points at |z| = 10⁻³, on the band,
  at 4c + 1, and on |z| = 0.3 near the negative axis (arg 3.1).
- *Converse / scope.* The argument uses p > 1 in: Lemma 1.1 of RH_px (slit plane free of Γ-poles), Lemma E.2 (|e^{−2iθ₊}| < 1
  on (−∞, 0) needs sin(π/p) > 0, and the far-part integral converges), n^{−1−p} ≤ n⁻². At p = 1 Lemma E.2 is false (§9).
- *Large α.* α ≥ 1 (s ≥ 1 + 2p) is outside Paper 2's standing assumption but inside RH_px's (all s > 1); the lemmas of
  Paper 2 used here (szego (i), (iv), (vi)(b); airy) do not use α < 1. Numerics at α = 1.4 ([3], (p, s) = (5/4, 4)) agree.

## 11. Integration (for the integrator; nothing below has been applied to SECOND.md / THEOREMS.md)

**SECOND.md summary table** (rows as in the REVIEWED version on master 928a2b3):
- Row "Conj. P62": label → "CONJECTURE for 0 < p ≤ 1; **PROVED-mod-cite for p > 1** (E_pgt1.md Thm E.1, Cor E.6; not
  REVIEWED)".
- Row "Cor 3.3": append "; unconditional for p > 1 (E_pgt1 Thm E.1 gives (E₁))".
- Row "Thm 3.4": append "; unconditional for p > 1 and superseded there by E_pgt1 Thm E.1 (remainder O(n⁻²))".
- Row "Cor 3.9": append "; for p > 1 the conclusion holds unconditionally, and g(p) = 0 (E_pgt1 §8.2)".
- Row "Thm 3.8": append "; for p > 1 the conclusion holds with O(1), unconditionally (E_pgt1 §8.2); (UΛ), (CVX) remain
  HYPOTHESIS".
- Row "Thm 3.10": part (d) for p = 2 → "PROVED-mod-cite for all s > 1 (E_pgt1 §8.2)".
- Row "§4 (E)": label → "**PROVED-mod-cite for p > 1** with ε = 1 (E_pgt1.md Thm E.1; not REVIEWED); GAP for 0 < p ≤ 1".
- Row "§4 g(p)": label → "g(p) = 0 for p > 1: PROVED-mod-cite (E_pgt1 §8.2); GAP for 0 < p < 1 (p = 1: g(1) = 0 CONDITIONAL
  on (E) via Cor 3.9)".
- New row "Thm E.1 / Cor E.6 (E_pgt1.md)": statements of §1 here; label as in the table at the top of this file.
- §4 text: after "(E) for pure powers (GAP)", add a pointer: "For p > 1 closed by E_pgt1.md: step 1 as stated; step 3 is
  resolved by E_pgt1 Lemma E.2 (H_n is constant to O(n^{−p}), so Δ₁^{(N)} = Δ₁^{(∞)} + O(N^{−p})); steps 2, 4, 5 are E_pgt1
  Lemmas E.3–E.5 and Prop. E.5′; the computed values are d₁ = −(s−1)/2, e₁ˢ = −p/2, k₀, k₁ as in Conj. P62."
- §4 "Computing d₁ itself": add "Done for p > 1 (E_pgt1 §§4–7): the hard-edge residue is c(p+2)(4α²−1)/16·[[1, i], [i, −1]]
  and does not enter d₁; d₁ comes from the Airy simple-pole residue A_r."

**THEOREMS.md §2.10** (Plan 62 table):
- Row "Conjecture P62": label → "CONJECTURE (0 < p ≤ 1); PROVED-mod-cite for p > 1 (E_pgt1.md Thm E.1, Cor E.6)".
- Row "(E), g(p)": label → "(E): PROVED-mod-cite for p > 1 (E_pgt1.md; second-order RH, Lemma E.2 flatness of H_n), GAP for
  p ≤ 1; g(p) = 0 for p > 1 PROVED-mod-cite, GAP for p < 1".
- Row "Cor 3.3, Thm 3.4": append "unconditional for p > 1 (E_pgt1)".
- Row "Prop 3.7, Thm 3.8, Cor 3.9": append "for p > 1: conclusions unconditional (E_pgt1)".
- New row "Plan 65: Thm E.1, Cor E.6 | p > 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + O(n⁻²)), n^pα_n = 2c(1 − (s−1+p)/(2n) +
  O(n⁻²)), α_n/(2b_n) = 1 − p/(2n) + O(n⁻²); n^pg_{n−1} = c(1 + a/n + O(n⁻²)), k₀ = −(s−1) − p/2, k₁ = −(p+2)a |
  PROVED-mod-cite (RH_px, Paper 2 Lemmas binetcut/szego/airy/frame, KMVV §6, DLMF 9.7, 10.17, 10.25.2, 10.40) + exact
  computer algebra; not REVIEWED | research/G1/RH/second_order/E_pgt1.md, checks/check_e_*.out".

**THEOREMS.md §4 item 13**: replace "Still open: **(E)** … (GAP; PROOF SKETCH for p > 1)" by "(E) is PROVED-mod-cite for
p > 1 (Plan 65, E_pgt1.md: n^pb_n = c(1 − (s−1)/(2n) + O(n⁻²)) and all five constants of Conjecture P62; not REVIEWED);
still open: (E) for 0 < p ≤ 1 and g(p) for p < 1 (GAP)".

**RH/CITATIONS.md**: entry "(DLMF-9.7.2, Plan 65)" added in this branch (DLMF 9.7.2 quoted in full).
