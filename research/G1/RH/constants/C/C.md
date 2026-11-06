# Conjecture C: the absolute constant 2π/p in h_n (agent C)

**Label.** PROVED-mod-cite (Paper II thm:window, prop:moments, prop:frame, lem:outer, lem:binetcut, lem:seam,
lem:corner, lem:pottersector, and the frame lemmas cited inline: lem:interp, eq:Y-extract, lem:normalisation,
lem:szego, lem:gfunction, lem:signs, lem:bandweight, def:outer-admissible; Paper III lem:telescope; DLMF 5.11.1 +
§5.11(ii), 5.12.1, 5.5.1 — quoted in research/G1/RH/CITATIONS.md entries (DLMF), (DLMF-2), (DLMF-5.11, Plan 51))
+ REVIEWED (Rule R: review/REVIEW_C_R1.md, findings F1–F3 applied 2026-11-05). Novelty UNCHECKED (Rule L not done).
References to Papers II/III are by LaTeX label.
Branch `g1-constants`, 2026-11-05. Scripts and outputs: `checks/`.

Notation as in the brief and Paper II: σ = σ_{p,s,ℓ}, monic P_n, h_n = ∫P_n² dσ, c = c(p), γ_p = log c + p,
α = (s−1−p)/p, κ₀ := (4c)^{−1/p} = 2I(p)/π (= μ*((4c,∞)) < 1), nodes X_k = (n/k)^p, θ(x) = πn x^{−1/p},
and the arcsine mean on the band
  ⟨f⟩ := (1/π) ∫₀^{4c} f(x) dx / √(x(4c−x)),  so ⟨log x⟩ = ⟨log(4c−x)⟩ = log c.

## 0. Statement

**Theorem C.** For every p > 0 and s > 1,
  h_n(σ_{p,s}) = (2π/p) · c^{2n+1} · (c^{1/p}/n)^{s−1} · Γ(n+1)^{−2p} · (1 + o(1)).        (C)

Moreover, for 1 < s < 1+2p and every ℓ analytic of angle ϑ > 0 (Paper II Definition 1.1),
  h_n(σ_{p,s,ℓ}) = ℓ(n) · [right side of (C)] · (1 + o(1)).                                 (C_ℓ)

The proof has two layers.

**Theorem 1 (exact frame formula).** Let p > 0, 1 < s < 1+2p, ℓ analytic of angle ϑ > 0. Then
  h_n = (2π/p) ℓ(n) R_n · c^{2n} c^{α+1} · n^{1−s−2pn} · exp(S_n − M_n) · (1 + O(1/n)),     (1.1)
where R_n := exp⟨log r_n⟩ (r_n of Paper II eq:w-rn; R_n ≡ 1 for ℓ ≡ 1) and
  S_n := Σ_{k ≥ 1, X_k > 4c} 4 arccosh(√(X_k/(4c))),   M_n := ⟨log(4 sin²θ)⟩ = 2⟨log|2 sin(πn x^{−1/p})|⟩.

**Lemma 3 (saturated nodes).** S_n = 2np + log c − p log(2πn) + o(1).
**Lemma 4 (band oscillation).** M_n → 0.

Then exp(S_n − M_n) = c e^{2np}(2πn)^{−p}(1+o(1)) = c n^{2pn} Γ(n+1)^{−2p}(1+o(1)) (Stirling), and (1.1) becomes
(C_ℓ) with the extra factor R_n → 1; with ℓ ≡ 1 this is (C) for 1 < s < 1+2p. For the remaining s, Paper III
Lemma lem:telescope gives h_n(s₁)/h_n(s₀) = c^{(s₁−s₀)/p} n^{−(s₁−s₀)}(1+o(1)) for **all** s₀, s₁ > 1 (pointwise in s; the
uniform version needs S_p), and the right side of (C) has exactly this ratio. So (C) holds for all s > 1.

Where 2π/p comes from: it is the modulus of the band-weight constant ŵ_n = −(2πi/p)n^{1+p−s}ℓ(n) (Paper II Lemma lem:bandweight),
which enters h_n linearly through D_∞². The factor (2πn)^{−p} that turns n^{−2pn}e^{2pn}c^{2n} into Γ(n+1)^{−2p} comes
from Stirling's formula for N_s!, N_s = #{saturated nodes} ≈ κ₀ n (Lemma 3), not from the particular outer scalar:
Lemma 2 shows that the outer-scalar constant is independent of the choice of F. (The analysts' guess "Binet constant
(2π)^{−1/2} in the outer scalar" is right for p = 1, where F(∞)² = 1/(2πn) and nothing else contributes, see §6.)

No special choice of s (such as α = −½) is needed: the band-weight constant and Lemma 2 do not depend on s.

## 1. Extraction of h_n from Q (proof of (1.1) modulo Lemma 2)

Fix n ≥ n₀ and let F be the outer scalar of Paper II Lemma lem:outer (p = 1), Lemma lem:binetcut(iv) (p > 1), Lemma lem:seam(iv) (p < 1).

Step 1. (Y₁)₁₂ = h_n. [Paper II §tool-wlxz(a), proof of (Y-extract): "(Y₁)₁₂ = h_n, (Y₁)₂₁ = h_{n−1}^{−1}".]
Step 2. (U₁)₁₂ = n^{p(2n+1)} h_n. [Paper II Lemma lem:interp proof: U_j = n^{jp} n^{pnσ₃} Y_j n^{−pnσ₃}; the (1,2) entry of
  the conjugation by n^{pnσ₃} picks up n^{2pn}.]
Step 3. (Q₁)₁₂ = k_∞^{−2} (U₁)₁₂. [Paper II eq:Q-at-infinity /Prop. prop:frame(viii): Q = k_∞^{−σ₃}(Uz^{−nσ₃})k^{σ₃} with k analytic at
  ∞, k(∞) = k_∞. The (1,2) entry is k_∞^{−1}(Uz^{−nσ₃})₁₂ k^{−1} = k_∞^{−2}(U₁)₁₂/z + O(z^{−2}).]
Step 4. k_∞ = e^{nγ_p} D_∞ / 𝗁_∞(∞) [Paper II Lemma lem:normalisation], and 𝗁_∞ = F^{−1}e^{n(g−Log z)} with g − Log z → 0
  [Paper II Lemma lem:gfunction(ii)], so F(z) → F(∞) := 1/𝗁_∞(∞) ≠ 0 and |k_∞|² = e^{2nγ_p}|D_∞|²|F(∞)|².
Step 5. |D_∞|² = exp⟨log|W₀|⟩ with W₀ = ŵ_n x^α(4c−x)H_n r_n [Paper II eq:DW-factor, eq:W0], hence
  |D_∞|² = |ŵ_n| c^α · c · G_n · R_n,   G_n := exp⟨log H_n⟩,   |ŵ_n| = (2π/p)n^{1+p−s}ℓ(n).
  (Equivalently Paper II Lemma lem:szego(i): D_{x^α}(∞)² = c^α, D_{4c−x}(∞)² = c.)
Step 6. (Q₁)₁₂ = ic + O(1/n). [Paper II proof of Theorem thm:window: "Proposition prop:moments gives Q₁ = P₁ + O(1/n)", (P₁)₁₂ = ic;
  hypotheses: p > 0, 1 < s < 1+2p, ℓ analytic of angle ϑ > 0 — exactly ours.]
Since h_n > 0, taking moduli in Steps 1–6:
  h_n = n^{−p(2n+1)} e^{2nγ_p} (2π/p) n^{1+p−s} ℓ(n) c^{α+1} R_n · X_n · c (1 + O(1/n)),   X_n := |F(∞)|² G_n.  (1.2)
(Taking moduli avoids every branch question for ŵ_n^{1/2}, D_∞ and the sign of 𝗁_∞(∞).)
Lemma 2 below gives X_n = c^{−1} e^{−2np} exp(S_n − M_n) exactly; inserting it in (1.2) and using e^{2nγ_p} = c^{2n}e^{2np}
gives (1.1). ∎

## 2. Lemma 2 (the outer-scalar constant is F-free)

**Lemma 2.** For every n ≥ n₀ (and every p > 0; no condition on s, which does not enter F),
  log|F(∞)|² + ⟨log H_n⟩ = −log c − 2np − M_n + S_n.                                         (2.1)
All terms are finite; in particular log|2 sin θ| ∈ L¹(arcsine).

*Proof.* Let N := N_s := #{k ≥ 1 : X_k > 4c} and Π(z) := Π_{k≤N}(z − X_k). Put
  A(z) := F(z) e^{nφ(z)} z^{n−N} Π(z),   φ = γ_p − g.
(a) *A is analytic and zero-free on Ω := (ℂ ∪ {∞}) \ [0,4c], with A(∞) = e^{nγ_p}F(∞).*
On ℂ \ [0,∞): F is analytic, zero-free and has no jump on (−∞,0) [Def. def:outer-admissible(a)]; e^{−ng} has no jump there
(g₊ − g₋ = 2πi, n ∈ ℕ) [Lemma lem:gfunction(i)]; z^{n−N} is an integer power. On (4c,∞) off the nodes, F₊ = F₋e^{2iθ}
[Def. def:outer-admissible(a)] and e^{−ng₊} = e^{−ng₋}e^{−2iθ} (g₊ − g₋ = 2iθ/n there, Lemma lem:gfunction(i)), so A is continuous, hence analytic
(Morera). At a node X_k > 4c: X_k ∈ Z_n (Paper II §frame-contour: |z| ≤ n^p + δ′ < e^{pc₀}n^p), and on each side
F = υ_± F̃ with F̃² analytic and zero-free on Z_n [Def. def:outer-admissible(b)] and υ_± = (1−e^{∓2iθ})^{−1} meromorphic with a simple
pole at X_k (e^{2iθ(X_k)} = 1, θ′(X_k) ≠ 0); so |A| ≤ C|z−X_k|^{−1} on a punctured disc on which A is analytic, the
singularity is a simple pole, and Π cancels it. For |z| > n^p + δ′, A = e^{nγ_p} z^{−n}·z^{n−N}Π(z)/𝗁_∞(z) [Lemma lem:normalisation],
which is analytic at ∞ with value e^{nγ_p}/𝗁_∞(∞) = e^{nγ_p}F(∞). Zero-freeness: every factor is zero-free on Ω
except Π, whose zeros are exactly the cancelled poles.
(Node at 4c (Rule R F3) — possible only when nκ₀ ∈ ℕ, e.g. p = 1, n even. It is not counted in N; it is a boundary
point of Ω, where υ_± has a simple pole and K = (4c−z)^{−1/2}, so A ≍ (z−4c)^{−3/2} there. This is harmless: Im L stays
bounded near 4c (arg υ₊ ∈ (−π/2,π/2), arg K and arg(z−4c) bounded), and log|A| has only a logarithmic singularity at
4c, integrable for the arcsine law, so (c)–(d) are unaffected. (2.1) is also unchanged by moving the node into Π,
since its arccosh term is 0 and ⟨log|x−4c|⟩ = log c. Paper II's frame treats this case explicitly since commit
2d0bb9a: sec4_frame Step 1 of §frame-transf (the pole removal is local to each region, so R is regular at the common
corner 4c) and appB prop:apriori(ii).)

Ω is simply connected on the sphere, so L := log A has an analytic branch on Ω. Let z = J(w) := c(w + 2 + w^{−1}),
a conformal map of {|w| > 1} ∪ {∞} onto Ω with J(∞) = ∞, J(e^{iψ}) = 4c cos²(ψ/2). Then ℓ(w) := L(J(w)) =
Σ_{k≥0} a_k w^{−k} for |w| > 1 (Taylor series of L∘J(1/ζ) in |ζ| < 1), a₀ = L(∞).

(b) *Mean value and Parseval.* For r > 1 put u_r(ψ) := Re ℓ(re^{iψ}), v_r(ψ) := Im ℓ(re^{iψ}). Orthogonality of
e^{ikψ} on [0,2π] (the series converges absolutely on |w| = r) gives
  (1/2π)∫ u_r = Re a₀ = log|A(∞)|,   ‖u_r − Re a₀‖²_{L²} = ‖v_r − Im a₀‖²_{L²} = π Σ_{k≥1}|a_k|² r^{−2k}.   (2.2)

(c) *Im L is bounded on J({1 < |w| < r₁}) for some r₁ > 1.* The image of the upper (lower) half-annulus is a thin
neighbourhood of the band in ℂ₊ (ℂ₋), simply connected, on which L differs by a constant from the sum of the
following logarithms, each with bounded imaginary part for fixed n: (n−N)Log z; Σ_k Log(z−X_k); −n·g (Im g ∈ (0,π) in
ℂ₊, as Im g = ∫arg(z−y)dμ*); and log F written through its construction:
– p > 1: F = υ₊ D̃ B K in ℂ₊ with |e^{−2iθ}| < 1 on all of ℂ₊ [eq:imtheta with min(π,πp) = π], so
  |Im Log υ₊| = |arg(1−e^{−2iθ})| < π/2; −j(t) is continuous and bounded on {|arg t| ≤ π/p, |t| ≥ n(4c+1)^{−1/p}}
  (π/p < π, so no pole of Γ is near; t ranges there); log B is bounded near 0 uniformly up to the cut and continuous
  elsewhere [Lemma lem:binetcut(iii)]; Im log K = −½arg(4c−z) is bounded.
– p = 1 (Rule R F1): here |arg t| reaches π, and LnΓ(t) has poles at t = −k, i.e. z = −n/k → 0, so j(t) is *not*
  bounded on the whole region. Cover the image region by two overlapping pieces: on {0 < arg z ≤ π − η} use
  F = υ₊D̃K (|arg t| ≤ π − η, j bounded there for |t| ≥ n(4c+1)^{−1}; |Im Log υ₊| < π/2 on all of ℂ₊); on
  {η ≤ arg z < π} use F = DK = e^{j(−n/z)}K [eq:reflection], with |arg(−n/z)| ≤ π − η, so j(−n/z) is bounded there.
  On the overlap the two logarithms differ by a constant, so Im L is bounded on the union.
– p < 1: in S_in, F = υ₊D̃B_in K e^χ with |e^{−2iθ}| < 1 for 0 < arg z < πp ⊃ S_in ∩ ℂ₊; in S_out,
  F = B_out K e^χ; χ is bounded near 0 uniformly up to the seams [Lemma lem:corner(iii)] and continuous elsewhere; B_in, B_out,
  D̃ are bounded with bounded logs on the relevant compact pieces.
Hence sup_{1<r<r₁}‖v_r‖_∞ < ∞, and by (2.2) sup_{1<r<r₁}‖u_r‖_{L²} =: 𝔐 < ∞.

(d) *Passage to the band.* For every ψ except the countably many preimages of 0, 4c and the nodes in (0,4c), u_r(ψ) →
log|A_±(J(e^{iψ}))| as r ↓ 1 (+ for 0<ψ<π, since Im J(re^{iψ}) = c(r−1/r)sin ψ), because F, hence A, has continuous
boundary values from each side off the nodes [Def. def:outer-admissible(a)]. Let u be this limit; by Fatou ‖u‖_{L²} ≤ 𝔐. For K > 0
let T_K be truncation at ±K. Dominated convergence gives ∫T_K u_r → ∫T_K u, while
∫|u_r − T_K u_r| ≤ ∫_{|u_r|>K}|u_r| ≤ 𝔐²/K, and the same for u. Hence ∫u_r → ∫u, and with (2.2)
  log|A(∞)| = (1/2π)∫₀^{2π} u = ½⟨log|A₊|⟩ + ½⟨log|A₋|⟩                                         (2.3)
(the substitution x = 4c cos²(ψ/2) maps dψ/π on (0,π) to the arcsine law).

(e) *Evaluation.* On (0,4c) off the nodes: |e^{nφ_±}| = 1 (Re φ_± = 0, Lemma lem:signs(i)); F_± = υ_±F̃ with F̃ > 0 and
F̃² = 1/((4c−x)H_n) [Def. def:outer-admissible(b)]; |υ_±|^{−1} = |1 − e^{∓2iθ}| = |2 sin θ|. So
  log|A_±| = −log|2 sin θ| − ½log(4c−x) − ½log H_n + (n−N)log x + Σ_{k≤N} log|x − X_k|.
For X > 4c, ⟨log|x − X|⟩ = log(Υ(X)/4), Υ(X) = (√X + √(X−4c))² [Paper II proof of Lemma lem:gfunction(iii): 𝔲_β(x) =
Re 𝔤_β(x), 𝔤_β = 2log((√x+√(x−β))/2), with β = 4c]. Insert in (2.3), with log|A(∞)| = nγ_p + log|F(∞)|:
  nγ_p + log|F(∞)| = −½M_n − ½log c − ½⟨log H_n⟩ + (n−N)log c + Σ_{k≤N} log(Υ(X_k)/4).
Multiply by 2, use γ_p = log c + p and 2log(Υ(X)/(4c)) = 4 arccosh(√(X/(4c))):
  log|F(∞)|² + ⟨log H_n⟩ = −log c − 2np − M_n + S_n.  ∎
(Finiteness of ⟨|log|2 sin θ||⟩ follows from u ∈ L² and the other terms being integrable.)

*Remark 2.1.* Nothing in the proof uses s, ℓ, or which of the three constructions of F is taken beyond (c); so X_n
is the same for every admissible F satisfying (c), as it must be (h_n does not depend on F).

## 3. Lemma 3 (saturated nodes)

N = ⌈nκ₀⌉ − 1, ρ := nκ₀ − N ∈ (0,1]. With u = k/n, X_k/(4c) = (κ₀/u)^p, so S_n = Σ_{k=1}^N f(k/n),
f(u) := 4 arccosh((κ₀/u)^{p/2}) on (0,κ₀], f(κ₀) = 0.

(i) ∫₀^{κ₀} f = 2p. Integrating by parts (boundary terms vanish: u·arccosh((κ₀/u)^{p/2}) → 0 at 0, f(κ₀) = 0),
∫₀^{κ₀} arccosh((κ₀/u)^{p/2})du = (p/2)∫₀^{κ₀} du/√(1−(u/κ₀)^p) = (κ₀/2)B(1/p,½) = (pκ₀/2)·√πΓ(1/p+1)/Γ(1/p+½)
= (pκ₀/2)·π/(2I(p)) = p/2, using κ₀ = 2I(p)/π. Hence ∫f = 4·(p/2) = 2p and n∫₀^{κ₀}f = 2np.
(ii) f_r(u) := f(u) + 2p log u. From arccosh w = log(2w) + O(w^{−2}) (w → ∞): f_r(0⁺) = 4 log 2 + 2p log κ₀;
f_r(κ₀) = 2p log κ₀; f_r′ = (2p/u)(1 − w/√(w²−1)), w = (κ₀/u)^{p/2}, is O(u^{p−1}) at 0 and O((κ₀−u)^{−1/2}) at κ₀,
so f_r is absolutely continuous on [0,κ₀] with f_r′ ∈ L¹.
(iii) First-order Euler–Maclaurin for G(x) = f_r(x/n) (absolutely continuous), proved by ∫_k^{k+1}(x−k−½)G′ =
½(G(k)+G(k+1)) − ∫_k^{k+1}G:
  Σ_{k=1}^N f_r(k/n) = n∫₀^{N/n} f_r + ½(f_r(N/n) − f_r(0)) + ∫₀^{N/n} P₁(nu) f_r′(u) du,  P₁(x) = {x} − ½.
The last integral → 0 (Riemann–Lebesgue for bounded 1-periodic mean-zero P₁ against f_r′ ∈ L¹: approximate f_r′ in L¹
by step functions, on each interval ∫ P₁(nu)du = O(1/n)). n∫_{N/n}^{κ₀} f_r = ρ f_r(κ₀) + o(1). Hence
  Σ f_r(k/n) = n∫₀^{κ₀} f_r − 2pρ log κ₀ − 2 log 2 + o(1).
(iv) Σ_{k≤N} log(k/n) = log N! − N log n = N log(N/n) − N + ½log(2πN) + O(1/N) (DLMF 5.11.1 for Γ(N), as in Paper II
eq:binet-bound), and N log(N/n) − N = nκ₀ log κ₀ − nκ₀ − ρ log κ₀ + o(1). So
  −2p Σ log(k/n) = −2pn∫₀^{κ₀} log u du + 2pρ log κ₀ − p log(2πκ₀ n) + o(1).
(v) Adding (iii) and (iv): the ρ-terms cancel and S_n = n∫₀^{κ₀}f − 2log 2 − p log(2πκ₀n) + o(1)
= 2np − 2 log 2 + log(4c) − p log(2πn) + o(1) = 2np + log c − p log(2πn) + o(1).  ∎

## 4. Lemma 4 (band oscillation)

With τ = x^{−1/p}, M_n = 2∫_{κ₀}^∞ λ(nτ) ρ(τ) dτ, λ(t) := log|2 sin πt| (1-periodic), ρ(τ) = (p/π)τ^{−p/2−1}(4c −
τ^{−p})^{−1/2} (a probability density on (κ₀,∞)).
(i) ∫₀¹ λ = 0: I := ∫₀¹λ is finite; from 2 sin 2πt = (2 sin πt)(2 cos πt), periodicity and the shift t ↦ t+½,
I = I + I, so I = 0. Also λ ∈ L⁴(0,1) (|λ| ≤ C + |log t| + |log(1−t)|).
(ii) ρ ∈ L^{4/3}(κ₀, T) for every T, and Σ_m ‖ρ‖_{L^{4/3}(m,m+1)} < ∞ (ρ ≍ (τ−κ₀)^{−1/2} at κ₀, ρ ≍ τ^{−1−p/2} at ∞).
(iii) Tail: |∫_T^∞ λ(nτ)ρ| ≤ Σ_{m≥⌊T⌋}‖λ(n·)‖_{L⁴(m,m+1)}‖ρ‖_{L^{4/3}(m,m+1)} = ‖λ‖_{L⁴(0,1)}Σ_{m≥⌊T⌋}‖ρ‖_{L^{4/3}(m,m+1)},
small for T large uniformly in n. On (κ₀,T): ‖λ(n·)‖_{L⁴(κ₀,T)} ≤ (T+1)^{1/4}‖λ‖_{L⁴(0,1)}; approximate ρ in L^{4/3}(κ₀,T)
by a step function; for an interval [a,b], |∫_a^b λ(nτ)dτ| = n^{−1}|∫_{na}^{nb}λ| ≤ 2‖λ‖_{L¹(0,1)}/n (whole periods
contribute 0). Hence M_n → 0.  ∎
(Numerically M_n = O(n^{−1/2}), with the same oscillation as S_n − (2np + log c − p log 2πn), which cancels it; see §7.)

## 5. Proof of Theorem C

By Lemmas 3, 4: S_n − M_n = 2np + log c − p log(2πn) + o(1). Stirling: 2p log Γ(n+1) = 2pn log n − 2pn +
p log(2πn) + O(1/n). Hence c^{2n}n^{−2pn}exp(S_n − M_n) = c^{2n+1}Γ(n+1)^{−2p}(1+o(1)), and (1.1) gives, for
1 < s < 1+2p, h_n = (2π/p)ℓ(n)R_n c^{2n+1}c^{α+1}n^{1−s}Γ(n+1)^{−2p}(1+o(1)) with c^{α+1} = c^{(s−1)/p}. R_n → 1: by
Paper II Lemma lem:pottersector(iii) with R = max(4c,1), |log r_n(x)| ≤ (ε_Λ(T_n)/p)|log x| on (0,4c], T_n = log n − (1/p)log R → ∞,
and ⟨|log x|⟩ < ∞. This is (C_ℓ), and (C) on the window.

All s > 1 (ℓ ≡ 1): Paper III Lemma lem:telescope ("For all s₀, s₁ > 1, Φ_n(s₁) − Φ_n(s₀) → ((s₁−s₀)/p) log c", Φ_n(s) =
log h_n(s) + s log n; its proof uses Paper III Theorem thm:UFlim on {t₀,t₁} ⊂ (1,1+p] ⊂ S_p and the product identity, both
proved there). Take any s₀ ∈ (1,1+2p) and s₁ = s: then h_n(s) = h_n(s₀)c^{(s−s₀)/p}
n^{−(s−s₀)}(1+o(1)), and (C) at s₀ times this ratio is (C) at s.  ∎

## 6. Cross-check at p = 1 without Lemma 2

At p = 1, F = DK and F(iy) → (2πn)^{−1/2} [Paper II Lemma lem:outer, property (e)], so |F(∞)|² = 1/(2πn); H_n = e^{2j(n/x)}
with 0 < j(n/x) ≤ x/(12n) on the band [eq:binet-bound], so G_n = 1 + O(1/n). Thus X_n = (2πn)^{−1}(1+O(1/n)) directly, which is
what Lemmas 2–4 give at p = 1. (checks/identity_F.py confirms (2.1) at p = 1 to 1e−9.)

## 7. Numerical checks (Rule N; all NUMERICAL, not certified)

| claim | script / output | result |
|---|---|---|
| Lemma 2 for Paper II's own F (F(∞), B, H_n computed from the Binet-cut formulas) | `checks/identity_F.py` → `identity_F.out` | p=1: diff 2e−8, 3e−9, 9e−10 (n=10,20,40); p=2: 8e−9, 2e−9; p=3: 2e−6 at dps 20, 8e−8 at dps 25 (quadrature-limited) |
| Lemma 3, Lemma 4, and log(X_n(2πn)^p) → 0 | `checks/xn_freeform.py` → `xn_freeform.out` | S_n−pred and M_n are O(n^{−1/2}) and cancel; log(X_n(2πn)^p): p=1 → 1/(6n); p=2,3 ≤ 1e−8; p=½ ≈ 0.35 n^{−1/2} |
| p < 1 slow rate | `checks/xn_plt1_large.py` → `xn_plt1_large.out` | n^p·log(X_n(2πn)^p) ≈ 0.342 (p=½), ≈ 0.245 (p=¾), stable for n = 160…1280: o(1) holds, rate ≍ n^{−p} |
| (1.1) against exact h_n (moments ζ(s+pj), Chebyshev algorithm, two precisions) | `checks/hn_vs_frame.py` → `hn_vs_frame.out` | n·log(h_n/h_n^frame) converges (−0.60 … −3.19) for (p,s) = (½,1.4),(1,1.5),(1,2.5),(2,2),(2,4),(3,2.5), n ≤ 64: ratio 1+O(1/n) as Theorem 1 asserts |
| (C) itself | same | log(h_n/h_n^C) → 0; rate O(1/n) for p ≥ 1, ≈ O(n^{−p}) for p = ½ |

Provenance (Rule X): h_n is computed from the exact moments; S_n, M_n are computed from their definitions; no fitted
constants.

## 8. Adversarial pass (Rule A) — by the author, not a second reader

1. *Branches/signs.* Only moduli are used (h_n > 0); D_∞², ŵ_n^{1/2}, sign of 𝗁_∞(∞) never enter. ✔
2. *Is (Q₁)₁₂ = ic + O(1/n) really proved for the F of Lemma lem:outer/A.1/A.2?* Paper II Theorem thm:window uses Prop. prop:frame with
   that F; Q₁ − P₁ = O(1/n) entrywise (proof of Theorem thm:window). ✔ For s outside (1,1+2p) the Christoffel shift
   (Paper II sec:shift) gives b_n but not h_n's constant, which is why Paper III Lemma lem:telescope is used instead. ✔
3. *Poles of A on the saturated segment.* Missing them was the first error in this derivation: without Π the "mean"
   of log|2 sin θ| would have to be −2np+…, contradicting Lemma 4. With Π, (2.1) is confirmed numerically at p = 1,2,3.
4. *Node at 4c* (nκ₀ ∈ ℕ; for p = 1 every even n, since κ₀ = ½). (2.1) is insensitive (§2(a)). Paper II now states
   that its frame covers this case (commit 2d0bb9a: sec4_frame Step 1, appB prop:apriori(ii)); Rule R F4 found no gap.
   The numerics in `hn_vs_frame.out` use even n at p = 1 and agree with Theorem 1.
5. *Uniform integrability near 0 with infinitely many nodes.* Handled by boundedness of Im L (§2(c)) + Parseval, not by
   pointwise domination (which fails: the curves pass ever closer to more nodes). The bound on Im L uses arg(1−q) ∈
   (−π/2,π/2) because |q| = |e^{∓2iθ}| < 1 in the relevant half-plane (sector for p < 1). ✔
6. *Lemma 3 endpoint.* f has a square-root zero at κ₀; f_r′ ∈ L¹ suffices for first-order Euler–Maclaurin plus
   Riemann–Lebesgue; the fractional part ρ cancels exactly at order 1. The o(1) in S_n is genuinely O(n^{−1/2}) and
   oscillating (numerics), as is M_n; only their sum is smooth. ✔
7. *Paper III Lemma lem:telescope scope.* Pointwise for all s₀, s₁ > 1 (not uniform outside S_p) — pointwise is all (C) needs. ✔
8. *Converse/degenerate checks.* (p,s) = (2,2) (Lommel, exact) and (1,3/2) (Tricomi–Carlitz) are covered by the
   numerics; two-point/ finite measures are outside the frame (no hard edge), not applicable.

## 9. Routes not needed / OBSTRUCTION notes

- Route 1 (RH with full constants) succeeded; the only new ingredient is Lemma 2, which removes the outer scalar.
- Route 2 (differential identity in s): not needed; Paper III already supplies the s-dependence.
- Route 3 (Tricomi–Carlitz / Lommel comparison): fixes the constant only at p = 1 and p = 2 (exact anchors); not used.
- OBSTRUCTION (heuristic): computing X_n directly from F for p ≠ 1 needs the n-dependent constants B(∞)/B(0) (p > 1)
  or χ(0) (p < 1), Mellin-type integrals of Binet's function along the ray arg t = −π/p (or −π/2); Lemma 2 makes these
  unnecessary.

## 10. Remaining GAP

None for (C) as stated. Rule R done (review/REVIEW_C_R1.md; F1–F3 applied, F4 resolved in Paper II commit 2d0bb9a).
The rate is not claimed: the proof gives o(1); numerically O(1/n) for p ≥ 1 and O(n^{−p}) for 0 < p < 1 (confirmed
independently by the reviewer at (2.5,6) and (0.7,1.6)). Novelty: UNCHECKED (Rule L literature search not done).
