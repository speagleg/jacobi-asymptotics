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

**Additional verbatim quotes** (added for RH₁(r), Rule R F11; read in kv.txt §5):

> (5.4) "For α < 0, the matrix function P(z) has the following behavior as z → 0: P(z) = O([[1, |z|^{2α}], [1,
> |z|^{2α}]]), as z → 0."
>
> (5.5) "For α > 0, the matrix function P(z) has the following behavior as z → 0: P(z) = O([[1, 1], [1, 1]]), as z → 0
> from outside the lens, P(z) = O([[|z|^{−2α}, 1], [|z|^{−2α}, 1]]), as z → 0 from inside the lens."
>
> (5.9) "In order to transform to constant jumps we use a piecewise analytic function W corresponding to the analytic
> continuation of |x|^{2α}. For z ∈ Uδ, we define W(z) = z^α, if π/2 < |arg f(z)| < π, (−z)^α, if 0 < |arg f(z)| <
> π/2, with principal branches of powers. Then W is defined and analytic in Uδ \ (Σ1 ∪ Σ3 ∪ Σ5 ∪ Σ7)."
>
> (5.10) "P(z) = E_n(z)P^{(1)}(z)W(z)^{−σ3}e^{−nφ(z)σ3}. Here the matrix valued function E_n is analytic in a
> neighborhood of Uδ".
>
> (5.21) "For α < 0 the matrix function Ψα(ζ) has the following behavior as ζ → 0: Ψα(ζ) = O([[|ζ|^α, |ζ|^α],
> [|ζ|^α, |ζ|^α]])"; (5.22) "For α > 0 … Ψα(ζ) = O([[|ζ|^α, |ζ|^{−α}], [|ζ|^α, |ζ|^{−α}]]), as ζ → 0 with ζ ∈ II, III,
> VI, VII, Ψα(ζ) = O([[|ζ|^{−α}, |ζ|^{−α}], [|ζ|^{−α}, |ζ|^{−α}]]), as ζ → 0 with ζ ∈ I, IV, V, VIII."
>
> (5.23) "Ψα(ζ) = ½√π ζ^{1/2} [[H^{(2)}_{α+½}(ζ), −iH^{(1)}_{α+½}(ζ)], [H^{(2)}_{α−½}(ζ), −iH^{(1)}_{α−½}(ζ)]]
> e^{−(α+¼)πiσ3}, for 0 < arg ζ < π/4."
>
> (5.26)–(5.27) "En(z) = E(z)e^{nφ₊(0)σ3}e^{−πiσ3/4}(1/√2)[[1, i], [i, 1]], where the matrix valued function E is given
> by E(z) = P^{(∞)}(z)W(z)^{σ3}e^{½απiσ3}, for z ∈ f^{−1}(I ∪ II)"; (5.28) "E(z) = P^{(∞)}(z)W(z)^{σ3}e^{−½απiσ3},
> for z ∈ f^{−1}(III ∪ IV)"; (5.29) "E(z) = P^{(∞)}(z)W(z)^{σ3}[[0, 1], [−1, 0]]e^{−½πiασ3}, for z ∈ f^{−1}(V ∪ VI)";
> (5.30) "E(z) = P^{(∞)}(z)W(z)^{σ3}[[0, 1], [−1, 0]]e^{½πiασ3}, for z ∈ f^{−1}(VII ∪ VIII)."
>
> (p. 19) "Following the proof of [38, Proposition 4.5], we obtain that E is analytic in a full neighborhood of Uδ.
> Here we need the fact that D(z)/W(z) and W(z)/D(z) remain bounded as z → 0, which follows from (5.9) and Lemma 4.2.
> Then we see from (5.26) that En is also analytic in a neighborhood of Uδ."

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
> z^{2k−1})." §5.11(ii), verbatim (re-read 2026-10-13 for RH₁(r), Rule R F9): the sums are "terminated at k=n−1 (k≥0)", and
> "If z is complex, then the remainder terms are bounded in magnitude by sec^{2n}(½ ph z) for (5.11.1), and
> sec^{2n+1}(½ ph z) for (5.11.2), times the first neglected terms." (The page states no further phase restriction
> beyond the sector |ph z| ≤ π − δ of 5.11.1. sec(½ph z) is finite for |ph z| < π. RH₁(r) Lemma S uses
> |ph t| ≤ 2π/3, n = m + 1, with sec(π/3) = 2.)

**Also used in:** RH_plt1.md Lemma 1.1′(ii): 5.11.1 + §5.11(ii) with n = 1, applied to Γ(1 − t) with the principal Ln, and to
Γ(t) on S_lens. RH_plt1b.md §1 (D̃ on S_in; Lemma S(i)–(iii)).

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
> (4.27) "For ζ ∈ II, Ψλ(ζ) = [[√π ζ^{1/2} I_{λ+½}(ζe^{−πi/2}), −(1/√π) ζ^{1/2} K_{λ+½}(ζe^{−πi/2})],
> [−i√π ζ^{1/2} I_{λ−½}(ζe^{−πi/2}), −(i/√π) ζ^{1/2} K_{λ−½}(ζe^{−πi/2})]] e^{−½λπiσ3}"; (4.28), (4.31), (4.32) are the
> analogues in III, VI, VII.
>
> (Theorem 4.2, proof) "The functions I_{λ±1/2}, K_{λ±1/2}, H^{(1)}_{λ±1/2} and H^{(2)}_{λ±1/2} are defined and
> analytic in the complex plane with a branch cut along the negative real axis. … Condition (c) follows easily from
> [1, formulas 9.1.9, 9.6.7 and 9.6.9]."
>
> (4.34) "… = √π ζ^{1/2} I_{λ+½}(ζe^{−πi/2}) e^{−½λπi}" (the continuation across Γ₂).
>
> **Used in:** RH₁(r) Lemma O1(i) (Rule R re-check R4).
>
> (§4.1, Rule R F9) "Since h is analytic in U with positive real part": this is used only to fix the branch of h^{1/2}.
> RH₁(r) uses an analytic nonvanishing branch of h₀^{1/2} on the disc instead.
>
> (4.53) "det P_{xν} ≡ 1" ("Using the behavior of Ψλν near 0 … the isolated singularity of det Ψλν at 0 has to be
> removable … By Liouville's theorem we then have that det Ψλν ≡ 1").

**Used in:** RH_p1_general.md §5 (Lemmas B, M).
- Theorem 1.1 itself is **not** applied: our weight is n-dependent after rescaling and the problem is discrete.
- We use only the local construction, its hypotheses, and these facts:
  - an interior FH point with exponent λ = a > −1/2;
  - the analytic, nonvanishing factor h₀, absorbed into W;
  - the Ψ asymptotics.

## (KMVV) Kuijlaars–McLaughlin–Van Assche–Vanlessen, arXiv:math/0111252v2 — READ (§1, §6), for Plan 12 (RH_px)
"The Riemann–Hilbert approach to strong asymptotics for orthogonal polynomials on [−1, 1]" (Adv. Math. 188 (2004)).

> (1.1) "w(x) = (1 − x)^α(1 + x)^β h(x), x ∈ [−1, 1], where α, β > −1 and h(x) is real analytic and strictly positive
> on [−1, 1]."
>
> (§6, RHP for P) "(b) P(z) satisfies the following jump relations on Uδ ∩ Σ°: P₊(z) = P₋(z)[[1, 0], [w(z)^{−1}ϕ(z)^{−2n},
> 1]], for z ∈ Uδ ∩ (Σ°₁ ∪ Σ°₃), (6.1); P₊(x) = P₋(x)[[0, w(x)], [−w(x)^{−1}, 0]], for x ∈ Uδ ∩ Σ°₂. (6.2) (c) On ∂Uδ
> we have, as n → ∞, P(z)N^{−1}(z) = I + O(1/n) … (6.3) (d) For α < 0 … P(z) = O([[1, |z − 1|^α], [1, |z − 1|^α]]) …
> (6.4); For α = 0 … O(log |z − 1|) … (6.5); For α > 0 … O([[1, 1], [1, 1]]) as z → 1 outside the lens,
> O([[|z − 1|^{−α}, 1], [|z − 1|^{−α}, 1]]) as z → 1 inside the lens. (6.6)"
>
> "RHP for Ψ … contour ΣΨ consisting of three infinite rays, γ1: arg ζ = 2π/3, γ2: arg ζ = π, γ3: arg ζ = −2π/3 …
> Ψ₊ = Ψ₋[[1, 0], [e^{απi}, 1]] on γ1 (6.16), Ψ₊ = Ψ₋[[0, 1], [−1, 0]] on γ2 (6.17), Ψ₊ = Ψ₋[[1, 0], [e^{−απi}, 1]] on γ3
> (6.18)"; the behaviour (6.19)–(6.21) at 0; "Theorem 6.3 The matrix valued function Ψ(ζ), defined in (6.23)–(6.25),
> is a solution of the RHP for Ψ."
>
> (6.27) "P(z) = E_n(z)Ψ(n²f(z))W(z)^{−σ3}ϕ(z)^{−nσ3}, with E_n an analytic matrix valued function in U_{δ0}";
> (6.28) "Ψ(ζ) = (2πζ^{1/2})^{−σ3/2}(1/√2)[[1 + O(ζ^{−1/2}), i + O(ζ^{−1/2})], [i + O(ζ^{−1/2}),
> 1 + O(ζ^{−1/2})]]e^{2ζ^{1/2}σ3}" uniformly as ζ → ∞; (6.31) "E_n(z) = N(z)W(z)^{σ3}(1/√2)[[1, −i], [−i, 1]]
> f(z)^{σ3/4}(2πn)^{σ3/2}"; (6.33) "det E_n(z) = 1".
>
> (Prop. 6.5, proof) "Thus by (6.31), (6.37), and (6.38) we have that all entries of En(z) have at most a square-root
> singularity at z = 1. Since we already know that En is analytic in a punctured neighborhood of 1, the isolated
> singularity at 1 is removable. Thus, En is analytic in U \ (−∞, −1]."
>
> (§6, endpoint −1, added for Rule R F1) "ϕ̃(z) = ϕ(−z) = −ϕ(z), (6.42) … ϕ̃₊(x)ϕ̃₋(x) = 1, for x ∈ (−1, 1). (6.43) The
> function W̃(z) = ((1 − z)^α(−1 − z)^β h(z))^{1/2}, for z ∈ U \ [−1, ∞), (6.44) is analytic in U \ [−1, ∞), and
> satisfies W̃²(z) = e^{−βπi}w(z) for Im z > 0, e^{βπi}w(z) for Im z < 0. (6.45) … W̃₊(x)W̃₋(x) = w(x) (6.46)";
> "P̃(z) = Ẽn(z)P̃^{(1)}(z)W̃(z)^{−σ3}ϕ̃(z)^{−nσ3} (6.47)"; "f̃(z) = g̃²(z)/4 (6.50). Then ζ = f̃(z) is a one-to-one
> conformal mapping of Ũδ onto a neighborhood of ζ = 0. However the ordering is reversed. Thus if z < −1, then ζ > 0,
> while if z > −1, then ζ < 0. The contours Σ1 and Σ3 are chosen such that f̃(Σ1 ∩ Ũδ) is part of the ray γ3, and
> f̃(Σ3 ∩ Ũδ) is part of the ray γ1"; "The reversal of the directions is taken care of by conjugating with the Pauli
> matrix σ3. Thus we take Ψ̃(ζ) = σ3Ψ(ζ; α → β)σ3, (6.51)"; "P̃(z) = Ẽn(z)Ψ̃(n²f̃(z))ϕ̃(z)^{−nσ3}W̃(z)^{−σ3}, (6.52)";
> "Ẽn(z) = N(z)W̃(z)^{σ3}(1/√2)[[1, i], [i, 1]]f̃(z)^{σ3/4}(2πn)^{σ3/2}, for z ∈ Ũδ. (6.53) Similar reasoning as before
> shows that Ẽn is analytic in U \ [1, ∞), and that the matching condition is satisfied."

**Used in:** RH_px §4.1 (corrected per Rule R F1), Lemmas 4.2 and 4.3, and §5. Our hard edge is at x = 0 with the band
to the right, which is KMVV's endpoint −1. The reversal is absorbed by (6.51) and (6.53), not by f.

**Hypothesis gap (flagged; addressed by RH_px Lemma 3.4).** KMVV assume h is real analytic on the closed interval. Our
h_N is analytic on (0, 4c + ε) and Hölder-ν at 0, and W̃ jumps super-exponentially little on (−δ, 0). The
removability step (Prop. 6.5, quoted above) needs:
- E_n analytic in a punctured disc — RH_px Lemma 4.2(iii) splits off the super-small jump;
- at most square-root growth — RH_px Lemma 3.4 gives D_w/W̃ bounded for Hölder h.

(This reading of what the step needs is ours, not KMVV's.)

## (WLXZ-v1, additional quotes for RH_px; Rule R F5) — read in 1410.3948.txt

> (3.10) "U^△_±(z) := Π(z)^{−σ3}[[1, 0], [−(1/(Π(z)w(z)))e^{±iθ(z)}, 1]]"; (3.11) "R(z) := U(z) × {U₊(z), z ∈ Ω_{l,+} ∪
> Ω_{r,−}; U₋(z), z ∈ Ω_{l,−} ∪ Ω_{r,+}; U^△₊(z), z ∈ Ω^△_{l,+} ∪ Ω^△_{r,−}; U^△₋(z), z ∈ Ω^△_{l,−} ∪ Ω^△_{r,+}; I, z ∈ Ω∞}";
> (3.12) "R11(z) = U11(z), R12(z) = U12(z) − U11(z)(w(z)/Π(z))e^{±iθ(z)}"; (3.15) "R11(z) = U11(z)Π(z)^{−1} −
> w(z)^{−1}U12(z)e^{±iθ(z)}, R12(z) = U12(z)Π(z)".
>
> (4.1) "T(z) := e^{(−nl/2)σ3}R(z)e^{(−ng(z)+nl/2)σ3}"; (4.4) "g₊(x) + g₋(x) = l, x ∈ (−2, 2); > l, x ∈ (−∞, −2) ∪ (2,
> +∞)"; (4.10), on (2, k_n): "[[e^{−2i(θ(z)+πα)}, 0], [(2iγ(z)/w(z))e^{n(l−g₊(z)−g₋(z))}, e^{2i(θ(z)+πα)}]]", and on
> (k_n, +∞): "[[e^{−2nπi/z²}, 0], [0, e^{2nπi/z²}]]".
>
> (4.12) "Q(z) := T(z) × {−V₋(z), z ∈ Ω_{l,+} ∪ Ω_{r,−}; V^△₊(z), z ∈ Ω^△_{l,−} ∪ Ω^△_{r,+}; V₊(z), …; V₋(z), z ∈
> Ω_{l,−} ∪ Ω_{r,+}; I, z ∈ Ω∞}"; (4.13) "V±(z) := [[1, 0], [±(e^{2nφ(z)}/(2iγ(z)w(z))), 1]] and V^△±(z) :=
> [[(1/(2iγ(z)))e^{±iθ(z)}, 0], [0, 2iγ(z)e^{∓iθ(z)}]]"; and "for z ∈ Σ^△_{r,±}, since 1 − e^{∓2iθ(z)} = O(1) when
> z = O(k_n), the jump matrix J_Q(z) ≁ I near the critical point z = k_n."
>
> (5.1) "V(z) := n^{(α−1/2)σ3}Q(z)E(z)^{σ3} × {D̂(z)^{σ3}, z ∈ Ω_{l,±} ∪ Ω^△_{l,±}; D̃(z)^{σ3}, z ∈ Ω_{r,±} ∪
> Ω^△_{r,±}; D(z)^{σ3}, z ∈ Ω∞}"; (5.7) "V(z) = O(1)(z² − 4)^{(1/2−α)σ3}" as z → ±2; (5.9) "N₊(x) = N₋(x)[[0,
> −(4 − x²)^{2α−1}e^L], [(4 − x²)^{1−2α}e^{−L}, 0]]"; (5.11), the explicit N.
>
> (6.4) the local jumps near 2 (band [[0, w₀/D̃²], [−D̃²/w₀, 0]]; vertical segments [[1, w̃/(D̃²e^{2nφ̃})], [0, 1]];
> (2, 2 + ε) [[1, 0], [D̃²e^{2nφ̃}/w̃, 1]]); (6.5) "P(z) = V_loc(z) × (w̃^{1/2}/D̃)^{σ3}e^{−nφ̃(z)σ3} for z ∈ U(2, ε)";
> (6.10) "f̃_n(z) = (−(3/2)nφ̃(z))^{2/3}"; (6.11) "φ̃(z) = −(2/3)(z − 2)^{3/2} + O((z − 2)²)"; (6.12)
> "V_r(z) = E_r(z)σ2Ψ(f̃_n(z))σ2e^{nφ̃σ3}(D̃/w̃^{1/2})^{σ3}".

> (re-read 2026-10-14 for Plan 14 §3, general α) Abstract: "… Tricomi–Carlitz polynomials f_n(z) where α is a positive
> parameter"; §6.1 "(V_loc,4) as z → ±2, V_loc(z) has the behavior V(z) = O(1)(z² − 4)^{(1/2−α)σ3}. (6.3)"; "If we set
> P(z) = V_loc(z) × (w̃^{1/2}/D̃)^{σ3}e^{−nφ̃(z)σ3} for z ∈ U(2, ε) … then the jump conditions on P(z) become (6.6)–(6.7)
> [[0, −1], [1, 0]], [[1, 1], [0, 1]], [[1, 0], [1, 1]] … The jumps suggest that P(z) can be constructed by using Airy
> functions"; (4.19) "E(z) := (√(2π)/Γ(α))(4 − z²)^{1/2−α}" and (4.26) "w₀(z) := 2iγ(z)w(z)/E²(z)" (the α-dependence
> enters only through E, which is absorbed in w₀, w̃).

**Used in:** RH_px §3 (transformations, V^△, F2), §4.2 (Airy) and §4.3 (the Σ^△ entries). In x: γ ↦ θ′, there is no
α-shift in θ, and the region is one-sided.

## (C–D) Conway–Deift, arXiv:1711.01590v4 = SIGMA 14 (2018) 056 — READ (abstract, §§1–5; App. A–C statements), for Plan 14
"Asymptotics of Polynomials Orthogonal with respect to a Logarithmic Weight". Local text: pdftotext of v4.

> (Abstract) "We use Riemann–Hilbert/steepest-descent methods, but not in the standard way as there is no known
> parametrix for the Riemann–Hilbert problem in a neighborhood of the logarithmic singularity at x = 1."
>
> (§4.1) "The operators C_Σ^± are bounded from L²(Σ) → L²(Σ) (and in fact in L^p(Σ) for all 1 < p < ∞) if and only if
> Σ is Carleson." "We will say that a pair of functions A± ∈ L^p(Σ) belongs to ∂C(L^p(Σ)) iff A± = C_Σ^± f for some
> (unique) f ∈ L^p(Σ)."
>
> "Theorem 4.4. Suppose v_A, v_B ∈ L^∞(Σ) and A± solves the RHP: A₊(x) = A₋(x)v_A(x), for x ∈ Σ, A± ∈ I + ∂C(L^p(Σ)),
> and B± the RHP: B₊(x) = B₋(x)v_B(x), for x ∈ Σ, B± ∈ I + ∂C(L^p(Σ)). Suppose further that v_B^{−1} ∈ L^∞(Σ) and
> B±^{−1} ∈ I + ∂C(L^q(Σ)) where 1/p + 1/q = 1, then if A, B are the analytic extensions of A± and B± respectively,
> AB^{−1} = I + C_Σ(A₋(v_A v_B^{−1} − I)B₋^{−1})."
>
> (§4.2) "(C_h f)(x) = C_Σ^−(f(h − I))(x)"; "If 1 − C_{v_Σ} is an invertible operator from L²(Σ) to L²(Σ), then
> µ = (1 − C_{v_Σ})^{−1}I (4.3) … the unique solution X to the RHP normalized at infinity with jump v_Σ is given by
> X(z) = I + C_Σ(µ(v_Σ − I))."
>
> "Proposition 4.6. A family of operators (1 − C_{h_n})^{−1} is bounded uniformly with respect to n if and only if the
> inhomogeneous RHP m₊(s) = m₋(s)h_n(s) + g(s) for s ∈ Σ, m± ∈ ∂C(L²(Σ)) is (uniquely) solvable for all g ∈ L²(Σ) with
> ||m±||_{L²} ⩽ c||g||_{L²} with c independent of both n and g." (attributed to [10] Deift–Zhou, Prop. 2.14, and [4])
>
> (Thm 4.7, proof) "‖v_Σ − ṽ_Σ‖_{L^∞(Σ)} → 0, which, in particular, implies that ‖C_{v_Σ} − C_{ṽ_Σ}‖_{L²→L²} → 0.
> Combined with Theorem 4.5, we see that ‖(C_{v_Σ} − C_{ṽ_Σ})(1 − C_{ṽ_Σ})^{−1}‖_{L²→L²} → 0. (4.12) Writing
> (1 − C_{v_Σ})(1 − C_{ṽ_Σ})^{−1} = 1 − (C_{v_Σ} − C_{ṽ_Σ})(1 − C_{ṽ_Σ})^{−1} (4.13) … the series … converges in operator
> norm … (1 − C_{v_Σ})^{−1} = (1 − C_{ṽ_Σ})^{−1}(1 − (C_{v_Σ} − C_{ṽ_Σ})(1 − C_{ṽ_Σ})^{−1})^{−1}"
>
> "Proposition 4.9. Q₁ − Q̃₁ = −∫_Σ µ(v_Σ − ṽ_Σ)µ̃^{−1} đz, (4.14) where µ = (1 − C_{v_Σ})^{−1}I, µ̃ = (1 − C_{ṽ_Σ})^{−1}I.
> Proof. The functions µ and µ̃ are given in terms of the RHP solutions Q and Q̃ … by µ = Q₋, µ̃ = Q̃₋"
>
> "Remark 4.10. … the standard approach of comparing the RHPs for Q, Q̃ by their quotient breaks down."
>
> Theorem 4.5 (uniform invertibility for the Legendre comparison) is proved by unwinding to a polynomial moment problem
> ("As det(∫_{−1}^1 s^{k+j}ds) ≠ 0, equation (4.9) is a system of n independent, linear equations") and the bound
> "‖p_{n−1}‖_{L²} ⩽ c‖ĝ₂‖_{L²}" with "c … independent of n".
>
> Results: (5.5) "Q₁ − Q̃₁ = (3/(16 n log²n))[[−1, i], [i, 1]] + O(1/(n log³n))"; Theorem 1.2: b_{n−1} − b̃_{n−1} =
> 3/(32 n² log²n) + O(1/(n² log³n)).

**Used in:** RH_zeta_close.md §1 (Plan 14, the hard edge). We use Theorem 4.4 (general) and the *argument* of
Theorem 4.7 and Proposition 4.9 (reproduced there). We do **not** use Theorem 4.5: its proof is Legendre-specific
(a polynomial moment problem with Lebesgue measure). Our replacement is Lemma UR, proved from an explicit solution of
the comparison problem. We use only the easy direction of Proposition 4.6, which is re-proved in §1.4.

## (DLMF-2) NIST DLMF §§1.14, 5.5, 5.12, 10.27, 10.39 — READ (web pages, 2026-10-14), for Plan 14 (Rule R F2)

> 1.14(iv): (1.14.32) "ℳf(s) = ∫₀^∞ x^{s−1}f(x)dx"; (1.14.38) (for real f) "∫₀^∞(f(x))²dx = (1/2π)∫_{−∞}^{∞}|ℳf(½ +
> it)|²dt"; (1.14.39) "(f∗g)(x) = ∫₀^∞f(y)g(x/y)dy/y"; (1.14.40) "∫₀^∞x^{s−1}(f∗g)(x)dx = ℳf(s)ℳg(s)" (for x^{σ−1}f,
> x^{σ−1}g absolutely integrable).
(Use in Lemma W: (Tf)(r) = ∫k(ρ/r)f(ρ)dρ/r is a 1.14.39 convolution in the multiplicative variable, so ℳ(Tf)(s) =
ℳk̃(s)ℳf(s) with k̃(u) := k(1/u)/u. Apply 1.14.38 to the real and imaginary parts of complex f.)
>
> (5.5.3) "Γ(z)Γ(1−z) = π/sin(πz), z ≠ 0, ±1, …".
>
> (5.12.1) "B(a,b) = ∫₀¹t^{a−1}(1−t)^{b−1}dt = Γ(a)Γ(b)/Γ(a+b)"; (5.12.3) "∫₀^∞ t^{a−1}/(1+t)^{a+b} dt = B(a,b)"; "In
> (5.12.1)–(5.12.4) it is assumed ℜa > 0 and ℜb > 0."
>
> (10.27.3) "K_{−ν}(z) = K_ν(z)"; (10.27.4) "K_ν(z) = ½π(I_{−ν}(z) − I_ν(z))/sin(νπ)".
>
> (10.39.1) "I_{1/2}(z) = (2/(πz))^{1/2}sinh z, I_{−1/2}(z) = (2/(πz))^{1/2}cosh z"; (10.39.2) "K_{1/2}(z) = K_{−1/2}(z) =
> (π/(2z))^{1/2}e^{−z}".

**Used in:** RH_zeta_close.md §1.4 Lemma W (Mellin–Parseval, the PV symbol −π cot πs from 5.12.3 and 5.5.3), and §1.2 (the
local form Ψ = Ψ̂ζ^{−σ₃/4}S for α = −½). RH_plt1.md Lemma 1.1′ (5.5.3: the identity D_up = t^{t−½}e^{−t}e^{iπt}Γ(1−t)/(i√(2π))).

## (KMVV, additional quotes for Plan 14; Rule R F2) — read in math/0111252v2 (pdftotext)

> "(c) For α < 0, the matrix function Ψ(ζ) has the following behavior as ζ → 0: Ψ(ζ) = O([[|ζ|^{α/2}, |ζ|^{α/2}],
> [|ζ|^{α/2}, |ζ|^{α/2}]]), as ζ → 0. (6.19)"; "We define Ψ(ζ) for |arg ζ| < 2π/3 as Ψ(ζ) = [[I_α(2ζ^{1/2}),
> (i/π)K_α(2ζ^{1/2})], [2πiζ^{1/2}I′_α(2ζ^{1/2}), −2ζ^{1/2}K′_α(2ζ^{1/2})]]. (6.23)"; for 2π/3 < arg ζ < π, (6.24) in terms
> of ½H^{(1)}_α(2(−ζ)^{1/2}), ½H^{(2)}_α(2(−ζ)^{1/2}) and πζ^{1/2}H′ times e^{½απiσ3}; for −π < arg ζ < −2π/3, (6.25)
> likewise with e^{−½απiσ3}; "Theorem 6.3 The matrix valued function Ψ(ζ), defined in (6.23)–(6.25), is a solution of
> the RHP for Ψ."

## (KMVV, angle freedom; Plan 15b) — read in math/0111252v2 (pdftotext), §6 after (6.21)

> "In the above, we have chosen the angle 2π/3 rather arbitrarily. It could be replaced by any angle in (0, π). However,
> having chosen the angle, we define the contours Σ1 ∩ Uδ and Σ3 ∩ Uδ in Uδ as the preimages of the rays γ1 and γ3 under
> the mapping ζ = n²f(z) … Note that this definition does not depend on n."

**Used in:** RH_plt1b.md §2. For all 0 < p < 1 the Ψ-rays are taken at angle π − θ_L, θ_L = πp/4, so that the lips lie in the inner sector.

## (DLMF-3) NIST DLMF §§10.25, 10.31 — READ (web pages, 2026-10-14), for Plan 48 (route2/ROUTE2.md §3.2)

> (10.25.2) "I_ν(z) = (½z)^ν Σ_{k=0}^∞ (¼z²)^k/(k! Γ(ν+k+1))"; §10.25(ii): "the principal branch of I_ν(z) … corresponds
> to the principal value of (½z)^ν, is analytic in ℂ∖(−∞,0], and two-valued and discontinuous on the cut ph z = ±π."
>
> (10.31.2) "K_0(z) = −(ln(½z) + γ)I_0(z) + ¼z²/(1!)² + (1 + ½)(¼z²)²/(2!)² + (1 + ½ + ⅓)(¼z²)³/(3!)² + ⋯" (γ Euler's
> constant; the n = 0 case of 10.31.1, stated for n = 0, 1, 2, …).

**Used in:** route2/ROUTE2.md §3.2: the local form Ψ = Ψ̂ζ^{ασ₃/2}S of KMVV's Bessel matrix (6.23) for every non-integer
α ∈ (−1, 1) (with 10.27.4, quoted in DLMF-2), and Ψ = Ψ̂[[1, κ log ζ], [0, 1]]S for α = 0. Hypotheses: none beyond the
principal branches, which match KMVV (6.23) in |arg ζ| < 2π/3. KMVV (6.16)–(6.18), (6.23)–(6.25), (6.28), (6.45), Prop. 6.5
and C–D Theorem 4.4 / the arguments of 4.7, 4.9 are used as quoted above (KMVV, C–D entries); no new statement of those
sources is used.
