# Plan 10 (RH) citations

Citation gate (AGENTS.md rule 4). Read from the arXiv PDFs, 2026-10-13. WLXZ and BKMM are as in
research/G1/CITATIONS.md.

## (KV) Kuijlaars–Vanlessen — READ (abstract, §5)

A. B. J. Kuijlaars, M. Vanlessen, "Universality for eigenvalue correlations at the origin of the spectrum",
arXiv:math-ph/0305044 (Commun. Math. Phys. 243 (2003)).

> (§5) "RH problem for P: (a) P(z) is defined and analytic for z ∈ U_{δ0} \ Σ for some δ0 > δ. (b) On Σ ∩ Uδ, P
> satisfies the same jump relations as S, that is, P₊(z) = P₋(z)[[1, 0], [ω(z)^{−1}e^{−2nφ(z)}, 1]], for
> z ∈ Σ ∩ (Uδ ∩ ℂ±), (5.1); P₊(x) = P₋(x)[[0, |x|^{2α}], [−|x|^{−2α}, 0]], for x ∈ (−δ, δ) \ {0}. (5.2) (c) On ∂Uδ we
> have, as n → ∞, P(z)P^{(∞)}(z)^{−1} = I + O(1/n), uniformly for z ∈ ∂Uδ \ Σ."
>
> "f′(0) = πψ(0) > 0 … ζ = f(z) is a conformal mapping on Uδ onto a convex neighborhood of 0".
>
> "This RH problem was solved in [38, formulas (4.26)–(4.33)]. It is built out of the modified Bessel …" (Vanlessen,
> generalized Jacobi weights; [38] not read).

**Used in:** RH.md §7, the origin parametrix for α ≠ 0. Hypotheses to match: an interior band point with
ψ(0) > 0, a band jump with |x|^{2α} times an analytic nonvanishing factor, lens jumps of the (5.1) form, and four lens
contours meeting at 0.

## (WLXZ-v1) Wu–Lin–Xu–Zhao, arXiv:1410.3948v1 — READ (§§1–7), for Theorem RH₁

The arXiv v1 PDF was read via pdftotext. The Anal. Appl. 14 (2016) version was not read. Hypothesis throughout:
"α is a positive parameter" (TC(α)); RH₁ uses α = 1. Quotes are textual, with formulas transcribed from the PDF.

> (2.15) "w_d(z) = (1/z²)^{1/z²−1−α} e^{−1/z²+α} / Γ(1/z² + 1 − α), and the branch is chosen such that w_d(z) is
> analytic in ℂ \ iℝ and takes positive values for ℝ \ {0};" (Y4) "Y(z) = O(1 log|z|; 1 log|z|), z ∉ [−1/√α, 1/√α]."
> "By the well-known theorem of Fokas, Its and Kitaev [11], we have Theorem 2.3. The unique solution of the IP for Y is
> given by (2.18)" (with Y₂₁ = γ²_{n−1}h⁻¹_{n−1}π_{n−1}, where γ_n is the leading coefficient (1.9)).
>
> (4.16)–(4.17) "D̃(z) = D(z)(1 − e^{∓2iθ(z)}), z ∈ ℂ±. Moreover, we have as n → ∞, D̃(z) = 1 + O(1/n), holding uniformly
> for z in any compact set K ⊂ ℂ \ (−∞, 0]".
>
> (5.8) "we can choose δ sufficiently small so that Re φ(z) < 0, Re φ̃(z) > 0 and Re φ̂(z) > 0 in both the upper and
> lower lens regions. These together with … imply that all jumps on the contour Σ are exponentially close to the
> identity matrix, provided that they are bounded away from the segment (−2, 2)."
>
> §6.1 "Parametrix at endpoints of the saturated-band region. We seek a local parametrix V_loc(z) defined on
> U(2, ε) ∪ U(−2, ε) such that … V_loc(z)N⁻¹(z) = I + O(1/n) as n → ∞; (6.2)" (constructed from Airy functions,
> (6.4)–(6.21)).
>
> (6.27)–(6.28) "J_{V⁰_loc}⁻¹(z)J_V(z) = I + O(z²/n), uniformly for z ∈ {U(0, ε) ∩ Σ} ∪ ∂U(0, ε). … we conclude that
> V₀(z) = V⁰_loc(z)(I + O(1/n))"; Remark 6.1 "Using the single-layer potential techniques … the nonhomogeneous
> equation is contractive. A unique solution is then determined such that μ_H(τ) = O(1/n) on Σ_ε."
>
> (6.34)–(6.37) "J_S(z) = I + O(1/n), z ∈ ∂(U(0, ε) ∪ U(−2, ε) ∪ U(2, ε)) ∪ (−2 + ε, −ε) ∪ (ε, 2 − ε); I + O(e^{−cn}),
> otherwise, … the error term is uniform for z ∈ Σ_S. Hence ‖J_S(z) − I‖_{L²∩L^∞(Σ_S)} = O(1/n). … S(z) = I + O(1/n)
> uniformly for z ∈ ℂ."

## (DLMF) NIST DLMF §5.11 — READ (web page)

> (5.11.1) "As z → ∞ in the sector |ph z| ≤ π − δ, Ln Γ(z) ∼ (z − ½) ln z − z + ½ ln(2π) + Σ_{k=1}^∞ B_{2k}/(2k(2k−1)
> z^{2k−1})." §5.11(ii): for complex z the remainder after truncation is bounded by "sec^{2n}(½ ph z)" times the first
> neglected term.

## (Van) M. Vanlessen, arXiv:math/0212014 — READ (§1, §4.1–4.3), for RH₁(r)
"Strong asymptotics of the recurrence coefficients of orthogonal polynomials associated to the generalized Jacobi weight"
(J. Approx. Theory 125 (2003)). KV's reference [38].

> (1.1) "w(x) = (1 − x)^α(1 + x)^β h(x) Π_{ν=1}^{n0} |x − x_ν|^{2λ_ν}, for x ∈ (−1, 1), where n0 is a fixed number, with
> −1 < x1 < x2 < · · · < x_{n0} < 1, 2λ_ν > −1, λ_ν ≠ 0, α, β > −1, and with h real analytic and strictly positive on
> [−1, 1]."
>
> "Theorem 1.1 The recurrence coefficients a_n and b_n of orthogonal polynomials associated to the generalized Jacobi
> weight (1.1) have a complete asymptotic expansion of the form a_n ∼ 1/2 + Σ_{k≥1} A_k(n)/n^k, b_n ∼ Σ_{k≥1} B_k(n)/n^k
> … A_1(n) = −(1/2)Σ_ν λ_ν √(1 − x_ν²) cos(2n arccos x_ν − Φ_ν)" (1.3)–(1.4).
>
> (§4.1, p. 18) "W_{xν}(z) = (1 − z)^{α/2}(1 + z)^{β/2} h^{1/2}(z) Π (z − x_k)^{λ_k} Π (x_l − z)^{λ_l} …" (the analytic
> factor h is absorbed into W).
>
> (4.42) "P_{xν}(z) = E_{n,xν}(z)Ψ_{λν}(n f_{xν}(z))W_{xν}(z)^{−σ3}ϕ(z)^{−nσ3}"; "We let λ > −1/2" (§4.2).
>
> (4.43) "Ψ_{λν}(ζ) = (1/√2)[[1, −i], [−i, 1]](I + O(1/ζ))e^{πiσ3/4}e^{−iζσ3}e^{−λν πiσ3/2}, uniformly for ζ in the
> first quadrant", and similarly in (4.44)–(4.46) for the other quadrants.
>
> (4.53) "det P_{xν} ≡ 1" ("Using the behavior of Ψλν near 0 … the isolated singularity of det Ψλν at 0 has to be
> removable … By Liouville's theorem we then have that det Ψλν ≡ 1").

**Used in:** RH_p1_general.md §5 (Lemmas B, M).
- Theorem 1.1 itself is **not** applied: our weight is n-dependent after rescaling and the problem is discrete.
- We use only the local construction, its hypotheses, and these facts:
  - an interior FH point with exponent λ = a > −1/2;
  - the analytic, nonvanishing factor h₀, absorbed into W;
  - the Ψ asymptotics.
