# JZC M3a, step H-c: the band-factor gauge for the Hurwitz lattice (item 5 of Theorem H)

Status (2026-10-21): NOT REVIEWED (Rule R pending for everything below). Labels per VERIFICATION_POLICY.md. Novelty: UNCHECKED.
Closes, modulo review, item 5 of JZC_M3a_H.md §4 for **p > 1**; for **0 < p < 1** it reduces item 5 to E_plt1 Lemma F.1 with complex
seam densities, which is JZC_M3a_H_G23plt1.md Lemma F.1_δ (NOT REVIEWED; cited, not redone here).
Setting: Hurwitz lattice λ_k = (k + δ)^p, k ≥ 1, **−1 < δ ≤ 0** (δ < 0 for p < 1), a := 1 + δ, **1 < s < 1 + 2p**, α := (s − 1 − p)/p,
β′ := α + 2δ, c = c(p). H-c itself does not use s (the band factor is s-free); the hypothesis on s is the Setting of Theorem H, where
H-c is used (G1u Prop (B)).
Checks: `checks/m3a_hc_pgt1.py/.out` (Lemmas Hc.1–Hc.2), `checks/m3a_hc_gauge.py/.out` (Lemmas Hc.3, Hc.5); counts in §5.

| # | Statement | Label |
|---|---|---|
| Hc.1 | E_pgt1 Lemma E.2 for H_n^δ = (D̃_δB_δ)^{−2}, p > 1: jump i𝔢_δ on (−∞, 0) with **δ-free** majorants; representation (E.2.1)_δ; G_δ − G_δ(1) = O(n^{−p}) with one derivative, C = C(p) | PROVED-mod-cite (G12 L1.2, L1.3, P1.4 [NOT REVIEWED]; Paper 2 Lemma binetcut (iii), (eq:binet-bound) via G12) |
| Hc.2 | E3 Lemma F.1′ for δ, p > 1: (i) m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ) (Fourier sum); (ii) G_δ(z) − G_δ(1) = Σ_{k≤K}m_k(δ)(z^k − 1) + O(n^{−(K+1)p}) on \|z\| ≤ 4c + 2, boundary values included, with derivative bounds; C = C(p, K) **independent of δ** | PROVED-mod-cite (Hc.1; DLMF 5.9.1, 25.2.1 as quoted in RH/CITATIONS.md "(Plan E3)", "(DLMF-zeta, Plan 67)") |
| Hc.3 | the gauge (E3 Lemma E3.5 / JZC_M4_proof N.6a, band part) in G1u's α-frame, p > 1: for every k and J, uniformly on both circles, Δ_k♮ = G_{μ^δ_n}Δ_k^{mod,β′}G_{μ^δ_n}^{−1} + O(n^{−(J+1)p}), μ^δ_{n,j} := 2m_j(δ) | PROVED-mod-cite (Hc.2; E3 Lemma E3.4 [REVIEWED]; Paper 2 (eq:szego-repr); G1u L1, L2 [NOT REVIEWED]) |
| Cor Hc.4 | H-c holds for p > 1: Prop G1u (B) no longer depends on H-c; item 5 of JZC_M3a_H §4 is closed for p > 1 | PROVED-mod-cite, NOT REVIEWED |
| Hc.5 | p < 1: the gauge of Hc.3 with the seam band factor (complex densities ℓ_±; circles crossing the seams, sector-wise) | PROVED-mod-cite given G23plt1 Lemma F.1_δ (iv) (NOT REVIEWED); the hard-edge data in the α-frame need the glued W̃♮ (G1u "p < 1", not part of H-c) |
| Rem | m_k(δ) = ζ(−kp, 1+δ)/(kn^{kp}) | NUMERICAL only (JZC_M3a_H Remark 3.3; Hurwitz's formula NOT QUOTED) |

## 0. Setting, notation, what is reused

p > 1. t = nz^{−1/p} (principal), θ_δ := π(t − δ), j_δ(t) := LnΓ(t−δ) − (t−δ−½)ln t + t − ½ln 2π, D̃_δ := e^{−j_δ(t)},
𝔟_δ(y) := 2Im(−j_δ(t₊) − Log(1 − e^{−2iθ_δ+})) (y < 0, t₊ = n|y|^{−1/p}e^{−iπ/p}), B_δ := exp(−(1/2π)∫_{−∞}^0𝔟_δ(y)[1/(y−z) − 1/(y−1)]dy)
(all as in G12 §1). Put
- **G_δ := −j_δ(t) + log B_δ**, analytic on ℂ∖(−∞, 0], so that **H_n^δ = (D̃_δB_δ)^{−2} = e^{−2G_δ}** (G12 P1.4(a); G1u §2's h_n^δ);
- q(y) := e^{−2iθ₊(y)} (lattice), q_δ(y) := e^{−2iθ_δ+(y)} = e^{2πiδ}q(y), |q_δ| = |q| = exp(−2π sin(π/p)n|y|^{−1/p}) < 1;
- **𝔢_δ(y) := 2Im Log(1 − q_δ(y))** (y < 0), real-analytic and real (= SPEC §3.1's density);
- m_k(δ) := (1/2π)∫_{−∞}^0𝔢_δ(y)y^{−k−1}dy, S_k(δ) := Σ_{m≥1}sin(πkp/2 − 2πmδ)/m^{1+kp} (absolutely convergent, |S_k| ≤ ζ(1+kp));
  m̂_k(δ) := n^{kp}m_k(δ) is n-free;
- μ^δ_{n,j} := 2m_j(δ) = 2m̂_j(δ)n^{−jp} (real), P_μ(x) := Σ_jμ_jx^j, M_μ, Q_k, G_μ, 𝓡 as in E3 §§0, 3 (G_μ := P₀^∞e^{−𝓡M_μσ₃/2}(P₀^∞)^{−1});
- R₁ := 4c + 2.

**Notation correction (JZC_M3a_H.md §1).** §1 wrote μ^δ_{n,j} := 2m_j(δ)n^{jp}. With §3.2's m_j(δ) (which contains (2πn)^{−jp}) that is
n-free, while Theorem N.6 uses μ_{n,j} = 2ζ(−jp)/(jn^{jp}) (n-dependent). The consistent definition is μ^δ_{n,j} := 2m_j(δ) =
2m̂_j(δ)n^{−jp}, as above (applied in JZC_M3a_H.md §1, marked "(fixed per H-c)"). Also §3.2 cites DLMF 5.2.1 for
∫_0^∞e^{−mu}u^{kp−1}du = Γ(kp)m^{−kp}: for p > 1 the exponent constant is complex (m·aₙ, aₙ = 2πine^{−iπ/p}) and the input is DLMF
5.9.1 (μ = 1, Re z > 0), as in E3 Lemma F.1′(i); 5.2.1 is the p < 1 input (real constant).

*Reused verbatim:* E3 Lemma E3.4 (PROVED, REVIEWED: purely algebraic, holds for every real μ); JZC_M4_proof Lemma N.6a's formulas for
Δ_k^0, Δ_k^r (k-free conjugation structure); Paper 2 (eq:szego-repr) ("for every z ∉ [0, 4c] and every number 𝔠",
papers/paper2/sec_6.tex l. 170–173). *Inputs from this repo (NOT REVIEWED):* G12 L1.1–L1.3, P1.4; G1u L1, L2.

## 1. Lemma Hc.1 (E_pgt1 Lemma E.2 for δ)

**Lemma Hc.1.** Let p > 1, −1 < δ ≤ 0. Then:
(a) *(jump)* G_δ has continuous boundary values on (−∞, 0) from both sides, G_δ₊ − G_δ₋ = i𝔢_δ there, and, with C = C(p) independent of
  δ and n,
  |𝔢_δ(y)| ≤ π|q(y)|,  |𝔢_δ′(y)| ≤ 4π|q||t₊|/(p|y|(1 − |q|)) (≤ C n|y|^{−1−1/p}|q| for |q| ≤ ½; ≤ C/|y| for |y| ≥ 1).
(b) *(representation)* for z ∉ (−∞, 0] and for the boundary values on (−∞, 0),
  G_δ(z) − G_δ(1) = (1/2π)∫_{−∞}^0𝔢_δ(y)(z − 1)/((y − z)(y − 1))dy.   (E.2.1)_δ
(c) *(flatness)* there is C = C(p), independent of δ, such that for all n ≥ 1: |G_δ(z) − G_δ(1)| ≤ Cn^{−p} on |z| ≤ R₁ (boundary values on
  (−R₁, 0) included); |G_δ′(z)| ≤ Cn^{−p} on |z| ≤ R₁/2 (incl. boundary values on (−R₁/2, 0)); and |G_δ′(z)| ≤ Cn^{−p}/η on |z| ≤ R₁ − η,
  dist(z, (−∞, 0]) ≥ η, η ∈ (0, 1]. Hence log H_n^δ(z) − log H_n^δ(1) = O(n^{−p}) with the same uniformity.

*Proof.* (a) j_δ is real on (0, ∞) and analytic on ℂ∖(−∞, 0] (G12 L1.2(a)); since t₋ = conj t₊ on (−∞, 0), j_δ(t₋) = conj j_δ(t₊), and
j_δ(t±) are continuous (|arg t₊| = π/p < π, so t₊ − δ stays off (−∞, 0], G12 L1.1). log B_δ is the Cauchy integral of the real-analytic
density 𝔟_δ (G12 L1.3(ii)); its boundary values are continuous and (log B_δ)₊ − (log B_δ)₋ = −i𝔟_δ (Sokhotski–Plemelj, as in Paper 2
Lemma binetcut (iii), which holds verbatim for B_δ by G12 L1.3(iii)). Hence
  G_δ₊ − G_δ₋ = −2i Im j_δ(t₊) − i𝔟_δ = −2i Im j_δ(t₊) + 2i Im j_δ(t₊) + 2i Im Log(1 − q_δ) = i𝔢_δ.
For |w| < 1, 1 − w lies in the disc |ζ − 1| < 1, so |arg(1 − w)| ≤ arcsin|w| ≤ (π/2)|w|; with w = q_δ, |q_δ| = |q|, this is the first
majorant. 𝔢_δ′ = 2Im(−q_δ′/(1 − q_δ)), q_δ′ = e^{2πiδ}q′, |q′| = |q|·2π|dt₊/dy| = 2π|q||t₊|/(p|y|) (dt₊/dy = −t₊/(py)), and
|1 − q_δ| ≥ 1 − |q|: the second. For |q| ≤ ½ it is ≤ 8π|q||t₊|/(p|y|) = Cn|y|^{−1−1/p}|q|. In general, with x := 2π sin(π/p)|t₊|,
|q| = e^{−x} and |t₊||q|/(1 − |q|) = (x/(2π sin(π/p)))/(e^x − 1) ≤ 1/(2π sin(π/p)), so the majorant is ≤ C(p)/|y| for all y < 0. Only |𝔢_δ|, |𝔢_δ′| enter below, and both majorants are those of
E_pgt1 Lemma E.2 (a) for δ = 0: they do not depend on δ.
(b) Put K_δ(z) := G_δ(z) − G_δ(1) − (1/2π)∫𝔢_δ(y)[1/(y−z) − 1/(y−1)]dy. The integral converges absolutely (|𝔢_δ| ≤ π, bracket O(|y|^{−2}))
and has continuous boundary values with jump i𝔢_δ (Plemelj; 𝔢_δ real-analytic). With (a), K_δ is continuous across (−∞, 0) and analytic
off it, hence analytic on ℂ∖{0} (Morera).
- *Near 0.* For z ∉ (−∞, 0], |arg t| ≤ π/p and |t| = n|z|^{−1/p} → ∞, so |j_δ(t)| ≤ C_J/|t| (G12 L1.2(b), φ = π/p, also at the boundary values);
  log B_δ is bounded near 0 including boundary values (G12 L1.3(iii), (eq:B-bounds), and the (O5)-near-0 window argument, G12 P1.4(a));
  the integral is bounded near 0 since 𝔢_δ is super-small there (a). So 0 is removable.
- *At ∞.* (i) j_δ: for δ < 0, |j_δ(t)| ≤ C(1 + |ln|t||) for |t| ≤ |δ|/2 in the sector (G12 L1.2(c)), j_δ is bounded on the compact
  {|δ|/2 ≤ |t| ≤ 2, |arg t| ≤ π/p} (t − δ avoids (−∞, 0]: G12 L1.1), and |j_δ| ≤ C_J/2 for |t| ≥ 2; with ln|t| = ln n − (1/p)ln|z| this is
  O_n(1 + log|z|). For δ = 0 this is E_pgt1's line (DLMF 5.5.1 via Paper 2) verbatim. (ii) |log B_δ(z)| ≤ C_n(1 + log|z|) uniformly up to the
  cut (G12 P1.4(c), window argument with |𝔟_δ′| ≤ C/|y|, G12 L1.3(ii)). (iii) The 𝔢_δ integral is O_n(1 + log|z|) uniformly up to the cut:
  away from the cut by |𝔢_δ| ≤ π, and next to it by the same window argument with |𝔢_δ′| ≤ C/|y| on |y| ≥ 1 ((a); E_pgt1 states "the integral
  is O(log|z|)" without this; the window makes it uniform in arg z, which Liouville needs on whole circles).
- So K_δ is entire with |K_δ(z)| ≤ C_n(1 + log|z|): constant (Cauchy's estimate). K_δ(1) = 0. This is (E.2.1)_δ; at boundary values it holds
  by continuity.
(c) E_pgt1 Lemma E.2 (c) and (ii) verbatim: the far part |y| ≥ 2R₁ uses only |𝔢_δ| ≤ π e^{−2π sin(π/p)n|y|^{−1/p}} (substitute |y| = n^pw);
the near part y ∈ [−2R₁, 0) uses only |𝔢_δ|, |𝔢_δ′| = O(e^{−c₂n}) and the vanishing to all orders at 0 (window subtraction of 𝔢_δ(Re z));
the derivative bounds are differentiation under the integral (far part), integration by parts (near part) and Cauchy's estimate. All
constants enter through the majorants of (a), which are δ-free. ∎ (PROVED-mod-cite: G12 L1.1–L1.3, P1.4 [NOT REVIEWED], through them
Paper 2 (eq:binet-bound) and Lemma binetcut (iii).)

### 1.1 Line-by-line record: E_pgt1 Lemma E.2 → Hc.1

"verbatim" = holds as written after (j, B, 𝔟, 𝔢, G, θ) ↦ (j_δ, B_δ, 𝔟_δ, 𝔢_δ, G_δ, θ_δ) and no other change.

| E_pgt1 L E.2, line | with δ | status |
|---|---|---|
| G := −j(t) + log B, H_n = e^{−2G} | G_δ := −j_δ + log B_δ, H_n^δ = e^{−2G_δ} (G12 P1.4(a)) | CHANGED (definition) |
| (a) "j real on (0, ∞), so j(t₋) = conj j(t₊)" | G12 L1.2(a) | verbatim (new reference) |
| (a) "(log B)₊ − (log B)₋ = −i𝔟 (binetcut (iii))" | G12 L1.3(iii) | verbatim (new reference) |
| (a) G₊ − G₋ = 2i Im Log(1 − e^{−2iθ₊}) =: i𝔢 | q ↦ q_δ = e^{2πiδ}q; 𝔢_δ = 2Im Log(1 − q_δ) | CHANGED (density); same algebra |
| (a) "\|q\| = exp(−2π sin(π/p)n\|y\|^{−1/p}) < 1", "\|Im Log(1 − q)\| ≤ arcsin\|q\|" | \|q_δ\| = \|q\| (δ real); bound for complex w | CHANGED (one line: \|q_δ\| = \|q\|) |
| (a) "\|q′/(1 − q)\| ≤ 2\|q′\| for \|q\| ≤ ½", "for \|q\| > ½ … \|𝔢′\| ≤ C/\|y\|" | \|q_δ′\| = \|q′\|, \|1 − q_δ\| ≥ 1 − \|q\| | CHANGED (one line); constants δ-free |
| (b) absolute convergence, Plemelj, Morera | 𝔢_δ real, real-analytic, \|𝔢_δ\| ≤ π | verbatim |
| (b) near 0: "j(t) → 0 by (eq. binet-bound), φ = π/p" | G12 L1.2(b) (\|j_δ\| ≤ C_J/\|t\|, C_J δ-uniform) | CHANGED (reference) |
| (b) near 0: "log B bounded near 0 incl. boundary values" | G12 L1.3(iii), P1.4(a) (O5) near 0 | CHANGED (reference) |
| (b) at ∞: "DLMF 5.5.1: LnΓ(t) = LnΓ(1+t) − ln t, \|j(t)\| ≤ C(1 + \|log\|z\|\|)" | δ < 0: G12 L1.2(c) + compactness (no Γ-pole: t − δ ∉ (−∞, 0]); δ = 0: verbatim | CHANGED (δ < 0 needs no 5.5.1) |
| (b) at ∞: "\|log B\| ≤ C_n(1 + log\|z\|) (proof of binetcut (iv), (O5))" | G12 P1.4(c) (window argument, explicit; Paper 2 wording gap, G12 §4 item 6) | CHANGED (reference) |
| (b) at ∞: "the integral is O(log\|z\|)" | uniform up to the cut by the window argument with \|𝔢_δ′\| ≤ C/\|y\| | ADDED (justification; also needed at δ = 0) |
| (b) Liouville, K(1) = 0, (E.2.1) | — | verbatim |
| (c) far part, near part, (ii) | only the majorants of (a) | verbatim; C = C(p) δ-free |
| Remark (3): "at p = 2, 𝔢 ≡ 0, H_n exactly constant" | at p = 2, q_δ = e^{2πiδ}e^{−2πn\|y\|^{−1/2}} ∉ (0, 1) for δ ∉ {0, −½}: 𝔢_δ ≢ 0, H_n^δ **not** constant; m_k(δ) = −(2/π)Γ(2k)(2πn)^{−2k}Σ_m sin(πk − 2πmδ)/m^{1+2k} ≠ 0 in general; = 0 at δ = −½ | CHANGED (statement false for δ; not used) |
| Remark (1) (1/n cancellation between −j and log B) | not used anywhere in H-c | not re-derived |

## 2. Lemma Hc.2 (E3 Lemma F.1′ for δ)

**Lemma Hc.2.** Let p > 1, −1 < δ ≤ 0.
(i) For k ≥ 1, m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ); m_k(δ) is real and |m_k(δ)| ≤ M̄_kn^{−kp}, M̄_k := (p/π)Γ(kp)(2π)^{−kp}ζ(1+kp).
  At δ = 0, m_k(0) = ζ(−kp)/(kn^{kp}) (E3 Lemma F.1′(i)).
(ii) For every K ≥ 1 there is C = C(p, K), independent of δ, with
  |G_δ(z) − G_δ(1) − Σ_{k≤K}m_k(δ)(z^k − 1)| ≤ Cn^{−(K+1)p}  for |z| ≤ R₁ (boundary values on (−R₁, 0) included), n ≥ 1,
  and the derivative bounds of Hc.1 (c) hold for the left side with n^{−p} replaced by n^{−(K+1)p}. Hence, with
  E_n^{(K)}(z) := G_δ(z) − G_δ(1) − Σ_{k≤K}m_k(δ)(z^k − 1),
  log H_n^δ(z) − log H_n^δ(1) = −P_{μ^δ_n}(z) + P_{μ^δ_n}(1) − 2E_n^{(K)}(z),  i.e.  H_n^δ ∝ e^{−P_{μ^δ_n}}e^{−2E_n^{(K)}},  |E_n^{(K)}| ≤ Cn^{−(K+1)p}.

*Proof.* (i) On y = −r < 0, q_δ(r) = e^{2πiδ}exp(−aₙr^{−1/p}), aₙ := 2πine^{−iπ/p}, Re aₙ = 2πn sin(π/p) > 0 (p > 1). Since |q_δ| < 1,
Log(1 − q_δ) = −Σ_{m≥1}e^{2πimδ}q^m/m. Fubini: Σ_m(1/m)∫_0^∞|q|^mr^{−k−1}dr = pΓ(kp)ζ(1+kp)(2πn sin(π/p))^{−kp} < ∞ (E3's bound; |e^{2πimδ}| = 1;
DLMF 5.9.1 with real z for the moduli; ζ(1+kp) by DLMF 25.2.1). With w = r^{−1/p} and DLMF 5.9.1 (μ = 1, ν = kp, z = maₙ, Re z > 0,
principal power, arg aₙ = π/2 − π/p ∈ (−π/2, π/2)): ∫_0^∞q^mr^{−k−1}dr = pΓ(kp)(maₙ)^{−kp} = pΓ(kp)(2πmn)^{−kp}(−1)^ke^{−iπkp/2}. Hence
  ∫_0^∞𝔢_δ(−r)r^{−k−1}dr = −2(−1)^kpΓ(kp)(2πn)^{−kp}Σ_m m^{−1−kp}Im e^{i(2πmδ − πkp/2)} = 2(−1)^kpΓ(kp)(2πn)^{−kp}S_k(δ),
and, substituting y = −r (y^{−k−1} = (−1)^{k+1}r^{−k−1}), ∫_{−∞}^0𝔢_δ(y)y^{−k−1}dy = (−1)^{k+1}∫_0^∞𝔢_δ(−r)r^{−k−1}dr, so
m_k(δ) = (1/2π)(−1)^{k+1}·2(−1)^kpΓ(kp)(2πn)^{−kp}S_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ). Reality: S_k(δ) ∈ ℝ. Bound: |S_k| ≤ ζ(1+kp).
At δ = 0, S_k(0) = sin(πkp/2)ζ(1+kp) and DLMF 25.4.1 at s = 1 + kp gives ζ(−kp)/(kn^{kp}) (E3's last step, verbatim).
(ii) E3 Lemma F.1′(ii) verbatim, with (E.2.1)_δ (Hc.1 (b)) and the δ-free majorants (Hc.1 (a)): for |y| ≥ 2R₁, |z| ≤ R₁,
(z − 1)/((y − z)(y − 1)) = Σ_{k≤K}(z^k − 1)y^{−k−1} + O(|y|^{−K−2}); the far part of the remainder is ≤ C∫|𝔢_δ||y|^{−K−2}dy ≤ C′n^{−(K+1)p}
(|y| = n^pw); the near parts of (E.2.1)_δ and of the m_k are O(e^{−cn}) with derivatives (Hc.1 (c)). Derivatives: as in Hc.1 (c). ∎
(PROVED-mod-cite: Hc.1; DLMF 5.9.1, 25.2.1 (and 25.4.1 at δ = 0 only), quoted in RH/CITATIONS.md "(Plan E3)", "(DLMF-zeta, Plan 67)".)

*Remark (NUMERICAL, not used; Hurwitz's formula NOT QUOTED).* m̂_k(δ) = ζ(−kp, 1+δ)/k (JZC_M3a_H Remark 3.3), so μ^δ_{n,j} =
2ζ(−jp, a)/(jn^{jp}); confirmed again in m3a_hc_pgt1 [3] (k ≤ 3, 12 (p, δ), ≤ 10⁻²⁵ relative).

### 2.1 Line-by-line record: E3 Lemma F.1′ → Hc.2

| E3 L F.1′, line | with δ | status |
|---|---|---|
| (i) "q(r) := e^{−2πit₊} = exp(−aₙr^{−1/p})", "Log(1 − q) = −Σq^m/m" | q_δ = e^{2πiδ}q; −Σe^{2πimδ}q^m/m | CHANGED |
| (i) Fubini bound pΓ(kp)ζ(1+kp)(2πn sin(π/p))^{−kp} | \|e^{2πimδ}\| = 1 | verbatim |
| (i) DLMF 5.9.1 at z = maₙ | — | verbatim |
| (i) "= 2(−1)^kpΓ(kp)ζ(1+kp)(2πn)^{−kp}sin(πkp/2)" | ζ(1+kp)sin(πkp/2) ↦ S_k(δ) | CHANGED |
| (i) "= ζ(−kp)/(kn^{kp}) by DLMF 25.4.1" | replaced by the Fourier-sum statement; 25.4.1 only at δ = 0 | CHANGED (Hurwitz's formula would be needed for ζ(−kp, a); not used) |
| (i) "At p = 2 all m_k vanish" | false for δ ∉ {0, −½} (§1.1, Remark (3)) | CHANGED |
| (ii) far/near parts, derivatives | δ-free majorants | verbatim; C(p, K) δ-free |

## 3. Lemma Hc.3 (the gauge on the circles, p > 1) and the closure of item 5

Circles: ∂U_0 = {|z| = δ_r} (G1u, Paper 2's hard-edge radius) and ∂U_r = {|z − 4c| = ε}, radii fixed and n-free, δ_r, ε < c, clockwise; boundary
values where they cross the contour. Data (G1u L2 (iii), JZC_M4_proof N.6a, with the Hurwitz weight W₀^{(β′)} = 𝗐_nz^{β′}(4c−z)H_n^δ):
  Δ_k♮,0 = (2f^{1/2})^{−k}P₀^∞ρ♮^{σ₃}Y_kρ♮^{−σ₃}(P₀^∞)^{−1},  Y_k := σ₃Ξ_k(α)σ₃  (Bessel order α),
  Δ_k^r = (−1/φ̃)^kP₀^∞(−ω^{(β′)})^{−σ₃/2}X_k(−ω^{(β′)})^{σ₃/2}(P₀^∞)^{−1},
and "mod,β′" means the same with H_n^δ replaced by a constant: ρ♮^{mod} = (Υ̂/4c)^{(1+β′)/2} (G1u L1 (v)), (−ω^{(β′),mod})^{1/2} =
(2√c/(z^{1/2} + (z − 4c)^{1/2}))^{1+β′} (E_pgt1 L E.4(iii) with α ↦ β′).

**Lemma Hc.3.** Let p > 1, −1 < δ ≤ 0, J ≥ 1, k ≥ 1. Uniformly on ∂U_0 ∪ ∂U_r (boundary values included) and in n ≥ 1,
  Δ_k♮ = G_{μ^δ_n}Δ_k^{mod,β′}G_{μ^δ_n}^{−1} + O(n^{−(J+1)p}),  μ^δ_n := (μ^δ_{n,1}, …, μ^δ_{n,J}),
with the constant depending on (p, s, J, k, δ_r, ε) and not on δ beyond β′ (through Δ_k^{mod,β′}).

*Proof.* Step 1 (exact factorisation). Write h° := H_n^δ/H_n^δ(1) on the band and log h°(z) := −2(G_δ(z) − G_δ(1)) on ℂ∖(−∞, 0] (boundary values
on (−∞, 0)); this is the continuation used in G1u's W̃♮ (G1u L1 uses the normalisation H_n^δ(0⁺) instead of H_n^δ(1); the constant cancels in
(h°)^{1/2}/D_{h°}). By multiplicativity of Szegő functions (Paper 2 (eq:DW-factor)), D_W = D_W^{mod}D_{h°}·const^{1/2}, hence
  ρ♮ = ρ♮^{mod}·(h°)^{1/2}/D_{h°} = ρ♮^{mod}e^{−L/2},  (−ω^{(β′)})^{1/2} = (−ω^{(β′),mod})^{1/2}e^{L/2},  L := log D_{h°}² − log h°
(for the soft-edge root: Paper 2 (eq:omega-4c), L₁ is (eq:szego-repr) applied to q₁ = x^{β′}h°, which is additive in log q₁). By (eq:szego-repr)
with 𝔠 = log h°(z) and Hc.2 (ii) with K = J (log h°(x) = −P_μ(x) + P_μ(1) − 2E(x), E := E_n^{(J)}, μ := μ^δ_n):
  L(z) = (𝓡(z)/π)∫_0^{4c}(log h°(x) − log h°(z))dx/(√(x(4c−x))(z−x)) = 𝓡(z)M_μ(z) + T(z),
  T(z) := −(2𝓡(z)/π)∫_0^{4c}(E(x) − E(z))dx/(√(x(4c−x))(z−x)),
the first term being E3 Lemma E3.4(i)'s computation ((P_μ(z) − P_μ(x))/(z − x) = Σ_kμ_kΣ_{j<k}x^jz^{k−1−j} and the arcsine moments).
Since diagonal matrices commute, with G_T := P₀^∞e^{−Tσ₃/2}(P₀^∞)^{−1} (which commutes with G_μ),
  Δ_k♮ = G_μG_TΔ_k^{mod,β′}G_T^{−1}G_μ^{−1}  on both circles, exactly (E3 Lemma E3.4(iii)'s argument, k-free).
Step 2 (|T| = O(n^{−(J+1)p}) on the circles). Each circle meets [0, 4c] in one point x₀ (δ_r, resp. 4c − ε). Put η₀ := δ_r/4, resp. ε/4.
For z on the circle with |z − x₀| ≥ η₀, dist(z, [0, 4c]) ≥ d > 0 (d depends on the radii), and |T(z)| ≤ (2|𝓡|/d)·2 sup_{|w|≤R₁}|E(w)|·
(1/π)∫dx/√(x(4c−x)) ≤ Cn^{−(J+1)p} (Hc.2 (ii), boundary values included — this covers the point −δ_r on the cut). For |z − x₀| < η₀: on the
convex disc U(x₀, 2η₀), which has distance ≥ η := 2η₀ from (−∞, 0] (δ_r ≤ c, 4c − ε − 2η₀ > 0) and lies in |w| ≤ R₁ − η, |E′| ≤ Cn^{−(J+1)p}/η
(Hc.2 (ii), derivative part), so |E(x) − E(z)| ≤ Cn^{−(J+1)p}|x − z|/η for x ∈ (x₀ − 2η₀, x₀ + 2η₀) ∩ (0, 4c), and that part of the integral is
≤ Cn^{−(J+1)p}/η·∫dx/√(x(4c−x)); the rest has |x − z| ≥ η₀ and the sup bound. |𝓡| is bounded on the circles. So sup|T| ≤ Cn^{−(J+1)p}.
Step 3. P₀^∞ and (P₀^∞)^{−1} are bounded on both circles (n-free: they are n-free functions, analytic off [0, 4c] and the circles avoid 0,
4c), so |G_T^{±1} − I| ≤ C|T|; Δ_k^{mod,β′} is bounded on the circles (explicit, n-free); G_μ^{±1} is bounded since G_μ is entire in (z, μ)
(E3 L E3.4(ii)) and |μ^δ_n| ≤ C (Hc.2 (i)). Hence Δ_k♮ − G_μΔ_k^{mod,β′}G_μ^{−1} = O(|T|) = O(n^{−(J+1)p}). ∎
(PROVED-mod-cite: Hc.2; E3 Lemma E3.4 [REVIEWED]; Paper 2 (eq:szego-repr), (eq:DW-factor), (eq:omega-4c); G1u L1–L2 for the form of the data.)

*What changed vs E3 Lemma E3.5 / N.6a.* (1) Weight exponent α ↦ β′ in the model (ρ♮^{mod}, ω^{(β′),mod}); the gauge G_μ does not see the
exponent. (2) μ_{n,k} = 2ζ(−kp)/(kn^{kp}) ↦ μ^δ_{n,k} = 2m_k(δ) (Fourier sums), real. (3) E3.5's "Δ_k depends analytically on (ρ²)^{±1},
(−ω)^{±1/2}, bounded above and below" is replaced by the exact conjugation identity of Step 1, which gives the remainder directly as O(|T|)
and is valid for every k (N.6a needs all k). (4) The hard-edge Bessel matrices Y_k keep the order α (G1u L2); the gauge acts only through
ρ♮. (5) Step 2 is E_pgt1 L E.3's "n-dependence" paragraph written with explicit windows.

**Corollary Hc.4 (item 5 for p > 1).** For p > 1, −1 < δ ≤ 0, 1 < s < 1 + 2p, the input "H-c" of Prop G1u (B) (Δ_k♮ =
G_{μ^δ}Δ_k^{mod,β′}G_{μ^δ}^{−1} + O(n^{−(J+1)p}), with μ^δ_{n,j} = 2m_j(δ)) holds (Hc.3), so Prop G1u (B) is PROVED-mod-cite with remainder
O(n^{−K−1} + n^{−1−(J+1)p}), conditional only on H-a, which JZC_M3a_H_Ha.md supplies (PROVED-mod-cite). With JZC_M3a_H §3.3 (N.6a–c for
M(β, ν)) this removes the last listed open item of Theorem H (i) for p > 1. Label: PROVED-mod-cite, NOT REVIEWED (every link of the chain —
G12, G1u, Ha, Hd, Hc — is NOT REVIEWED).

## 4. p < 1 (Lemma Hc.5): what changes

The band factor is the seam one, H_n^δ = (D̃_δB_in^δe^{χ_δ})^{−2} = e^{−2𝒢_δ} (G3 §2, Lemma 3 (iii)). Its analogue of Hc.1–Hc.2 is
JZC_M3a_H_G23plt1.md **Lemma F.1_δ** (E_plt1 Lemma F.1 with the complex seam densities ℓ_±(r) = −Log(1 − e^{±2πiδ}e^{−2πnr^{−1/p}}),
majorants |ℓ_±| ≤ ℓ, |ℓ_±′| ≤ ℓ′ (Lemma M), moments the same Fourier sums m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ), real; (iv) with C, n₀
independent of δ). It is cited, not redone here (coordinator's instruction; NOT REVIEWED; m3a_g23_F1.out, 398 checks). What H-c needs beyond
F.1_δ:

**Lemma Hc.5.** Let 0 < p < 1, −1 < δ < 0, J ≥ 1, and assume G23plt1 Lemma F.1_δ (i)–(iv). Define the circle data as in §3 with log h° :=
−2(𝒢_δ − 𝒢_δ(1)) taken **sector-wise** (𝒢_δ,in in S_in, 𝒢_δ,out in S_out, both boundary values on the seams), i.e. with E_plt1's glued W̃
(RH_plt1b §2) in the α-frame form W̃♮ = (𝗐(−z)^{β′}(4c−z))^{1/2}e^{−𝒢_δ}·const. Then Step 1–3 of Hc.3 hold: Δ_k = G_{μ^δ_n}Δ_k^{mod,β′}G_{μ^δ_n}^{−1}
+ O(n^{−(J+1)p}) uniformly on both circles, boundary values at the seams and at (−δ_r, 0) included.
*Proof (the changed lines only).* (1) Reality: ℓ₋ = conj ℓ₊ (Lemma M (M1)) and (F.1_δ) give 𝒢_δ(z̄) = conj 𝒢_δ(z), so log h° is real on the band
and μ^δ_n is real (F.1_δ (iii)): E3 L E3.4 applies. (2) Step 1: (eq:szego-repr) holds for every number 𝔠, so 𝔠 := log h°(z) may be the
sector value at z ∈ S_out or either seam boundary value; P_μ is entire, so the split L = 𝓡M_μ + T holds sector-wise with E := the sector
value of E_n^{(J)}. (3) Step 2: the sup bound uses F.1_δ (iv) on |z| ≤ R₁ with seam boundary values; the derivative bound is needed only on
U(x₀, 2η₀) around x₀ ∈ {δ_r, 4c − ε}, which lies in S_in at distance ≥ η₀ sin(πp/2) from the seams (choose η₀ ≤ δ_r sin(πp/2)/4) — F.1_δ (iv),
derivative part. The points where ∂U_0 crosses the seams are at distance δ_r sin(πp/2) from [0, 4c], where the sup bound suffices.
(4) Step 3 verbatim. ∎ (PROVED-mod-cite, given G23plt1 F.1_δ (iv) [NOT REVIEWED]; Paper 2 (eq:szego-repr); E3 L E3.4.)

*Not part of H-c, still open for p < 1 (G1u "p < 1"):* the glued hard-edge parametrix rebuilt with W̃♮ (its glue jumps are super-small,
1 − e^{∓2πi(t−δ)}, |·| = e^{−2πn|z|^{−1/p}}), and items 2–3 of JZC_M3a_H §4 (now in G23plt1). Hc.5 is the band-factor part only.
*What changes vs p > 1:* densities complex (two seams, conjugate) instead of one real density on (−∞, 0); circles cross the seams (sector values);
the Möbius factor in B_in^δ does not affect 𝒢_δ − 𝒢_δ(1) (G3 Rule A 8, Lemma 1); 5.2.1 (real Mellin constant) instead of 5.9.1.

## 5. Numerical checks (Rule N: NUMERICAL, not certified; finite samples of universally quantified statements)

**m3a_hc_pgt1.py/.out** (mpmath dps 34; p ∈ {5/4, 3/2, 3} × δ ∈ {0, −0.3, −0.7, −0.95}): **240 assertions, ALL 240 CHECKS PASSED**; 39 of them are controls that must
fail and do (C1: 9, C2: 6, C3: 24).
- [1] the δ-free majorants of Hc.1 (a) on 37 points y ∈ [−10⁶, −10⁻³], n = 8 (|e_δ′|/majorant reaches 1.0: the derivative majorant is attained
  when q_δ > 0, asserted ≤ 1 + 10⁻¹²).
- [2] (E.2.1)_δ: G_δ(z) − G_δ(1) from the **construction** (−j_δ + log B_δ, B_δ by quadrature of 𝔟_δ) equals the Cauchy integral of 𝔢_δ at 5
  points (4c + 1, 2 + 1.5i, −1.5 + 0.5i, −2 + 10⁻⁶i, 0.3), n = 8: ≤ 10⁻³³.
- [3] m_k(δ) by quadrature = Fourier sum (residue classes mod 20; cross-checked by lerchphi), k ≤ 3; δ = 0 = ζ(−kp)/(kn^{kp}); Remark 3.3 (NUMERICAL).
- [4] remainder: r_K := [G_δ(z) − G_δ(1)] − Σ_{k≤K}m_k(δ)(z^k − 1), K = 1, 2, n = 8…64 (p = 3: …32), 7 points incl. |z| = R₁ and both sides of
  (−R₁, 0): n^{(K+1)p}max|r_K| below the δ-free majorant 2M̄_{K+1}max|z^{K+1} − 1|, and r_K/(m_j(z^j − 1)) → 1 at rate n^{−p} (j the first index
  > K with m_j(δ) ≠ 0: j = 3 at p = 3, δ = 0, K = 1, where m₂(0) = 0 — but m₂(δ) ≠ 0 for δ ≠ 0).
- Controls (must fail, and do): [C1] lattice moments m_k(0) for δ ≠ 0; [C2] reflected parameter ζ(−kp, −δ); [C3] n^{jp+1/2}|r_K| unbounded
  (sharpness of the exponent).
**m3a_hc_gauge.py/.out** (dps 24; (p, δ) ∈ {(3/2, −0.7), (3, −0.3), (5/4, 0)} via (E.2.1)_δ, {(0.6, −0.5), (0.75, −0.3)} via (F.1_δ); n = 8, 16, 32;
8–9 circle points, both circles, incl. next to the negative axis and both sides of a seam; p < 1 also n = 64): **34 assertions, ALL 34 CHECKS
PASSED**; 9 are controls that must fail and do. sup|T_J| (Hc.3 Step 2) decays with
exponent (J+1)p (J = 1, 2) to within 0.35; Gauss–Chebyshev N = 16 vs 48 agree to ≤ 3·10⁻¹⁵·sup|T|; controls (must fail, and do): no gauge
(exponent p, not 2p) and lattice moments for δ ≠ 0.
Examples (last doubling): p = 3/2, δ = −0.7: exponents 2.96 (J = 1, target 3), 4.47 (J = 2, target 4.5); no gauge 1.51, lattice
moments 1.50. p = 3, δ = −0.3: 6.00, 8.99; no gauge 3.00. p = 0.75, δ = −0.3: 1.52, 2.22 (targets 1.5, 2.25); no gauge 0.89.
p = 0.6, δ = −½, J = 2: 1.59 vs 1.8 — pre-asymptotic, because m̂₃(−½) = 0.0018 and m̂₄(−½) = −0.0016 nearly cancel at these n
(n^{1.8}sup|T₂| = 4.9, 6.8, 7.8 ·10⁻³ at n = 16, 32, 64: bounded, converging); a first run with n ≤ 32 failed this exponent test (1.34) and
the range was extended to n = 64 for p < 1 (Rule A item 12).
Key numbers of m3a_hc_pgt1: [2] construction = representation to ≤ 6·10⁻³⁴; [4a] n^{(K+1)p}max|r_K| ≤ 0.27 against δ-free majorants
0.08–0.54; [4b] relative error vs the first non-zero next term at n_max: 2·10⁻⁴…1.2·10⁻² (decaying like n^{−p}); [C1] lattice moments: relative
errors 18 → 2.9·10⁵ (growing like n^p).

## 6. Rule A (adversarial pass) — log

1. *Is the jump of G_δ really free of j_δ?* Yes: the Im j_δ(t₊) terms cancel identically (Hc.1 (a)); checked by [2], where the construction
   (which contains j_δ and 𝔟_δ) equals the pure-𝔢_δ Cauchy integral to 10⁻³³.
2. *δ-dependence of the constants.* Hc.1–Hc.2 use 𝔢_δ only through |q_δ| = |q| and |1 − q_δ| ≥ 1 − |q|: δ-free. So, unlike C1.5 (whose C_n
   ∝ 1/|sin πδ|), H-c has **no crossover** at δ → 0⁻ and none at δ → −1⁺ (tested δ = −0.95; [4a] holds below the δ-free majorant). The
   δ-dependent constants C_n of the Liouville step (G12 P1.4(c), L1.2(c)) enter only qualitatively.
3. *Liouville uniformity up to the cut.* E_pgt1's "the integral is O(log|z|)" is true but needs the window argument next to (−∞, 0); added
   (Hc.1 (b), third bullet), with the derivative majorant of (a) (|𝔢_δ′| ≤ C/|y| on |y| ≥ 1).
4. *p = 2.* E_pgt1 Remark (3) ("H_n exactly constant") fails for δ ∉ {0, −½}; the lemma does not use it. δ = −½: S_k(−½) = Σ sin(πk + πm)/m^{1+2k} = 0,
   consistent with ζ(−2k, ½) = (2^{−2k} − 1)ζ(−2k) = 0 (NUMERICAL side remark).
5. *Zero moments.* At p = 3, δ = 0, m₂ = 0 (sin 3π = 0); the rate test then uses m₃ (j = 3). For δ ≠ 0, m₂(δ) ≠ 0 at p = 3 — the lattice
   zero is not structural for Hurwitz lattices.
6. *Is μ^δ real, and is h° positive?* m_k(δ) real (S_k real); G_δ real on (0, ∞) (j_δ real there, 𝔟_δ real); so E3.4(i) (stated for real μ)
   applies. For p < 1: via ℓ₋ = conj ℓ₊ (Hc.5 (1)).
7. *Branch of (h°)^{1/2} and of the soft-edge root.* All roots are exp(½·log) of the continuous logarithms defined in Hc.3 Step 1; the
   identities are additive in log h°, so no branch ambiguity enters T. The model roots are G1u L1 (v) and Paper 2 (eq:omega-root) (unchanged).
8. *Normalisation H_n^δ(1) vs H_n^δ(0⁺).* Constants cancel in h°^{1/2}/D_{h°} (eq:szego-repr with constant 𝔠 gives 0).
9. *Circle point −δ_r on the cut (p > 1).* Only the sup bound of E is needed there (|z − x| ≥ δ_r for x ∈ [0, 4c]); Hc.2 (ii) includes boundary
   values. Checked numerically at angle 0.95π in m3a_hc_gauge.
10. *Converse/scope.* Hc.1 uses p > 1 only via sin(π/p) > 0 (|q| < 1 on the cut) and |arg t| ≤ π/p < π; at p = 1 it fails as for δ = 0
    (E_pgt1 §9). δ > 0 is outside (phantom nodes; H-a), though Hc.1 (a)–(c) themselves would hold verbatim for any real δ for which G12
    L1.1–L1.3 hold.
11. *Rule N.* An early version of [1] asserted |𝔢_δ′|/majorant ≤ 1 with tolerance 0 and failed by rounding where the majorant is attained;
    tolerance 10⁻¹² with the reason stated. The C3 sharpness control was first written with exponent (K+1)p, which is not the leading
    exponent when m_{K+1} = 0; corrected to jp before the run. The first full run evaluated S_k(δ) with mp.nsum, which is inaccurate
    here (relative errors up to 4·10⁻⁶ at δ = 0, p = 5/4, where the terms do not oscillate); 38 of 243 assertions failed, all traceable to
    it (moment comparisons, and rate tests contaminated by a wrong m₁). S_k is now evaluated by residue classes mod 20 with the
    Hurwitz series ζ(s, j/20), s = 1 + kp > 2 (DLMF 25.11.1 used as a definition), cross-checked against mp.lerchphi. The same run
    showed that control [C2] (reflected parameter a ↦ 1 − a) is degenerate at p = 3: ζ(−3, a) = −B₄(a)/4 = ζ(−3, 1 − a); [C2] is now
    applied only for non-integer p.
12. *Pre-asymptotics at p < 1, δ = −½.* See §5 (gauge check): accidental near-cancellation of the m₃ and m₄ terms; the remainder is
    bounded at the claimed rate, the local exponent converges slowly. Not a counterexample.
13. *Rule X.* Nothing fitted. The Fourier sums, the construction and the representation are three independent evaluations; ζ(−kp, a) enters only
    in the NUMERICAL remark and in a control.

## 7. What remains

- Rule R second reader for Hc.1–Hc.5 (and for the NOT REVIEWED inputs G12, G1u, G23plt1).
- p < 1: Hc.5 is conditional on G23plt1 Lemma F.1_δ (NOT REVIEWED); the α-frame glued hard-edge parametrix (G1u "p < 1") and the a-priori
  bound (item 2, G23plt1) are outside H-c.
- Hurwitz's formula is still NOT QUOTED: Theorem H's constants are the Fourier sums S_j(δ); their identification with ζ(−jp, a) is NUMERICAL.
- Notation corrections applied in JZC_M3a_H.md §1 (μ^δ_{n,j} = 2m_j(δ)) and §3.2 (DLMF 5.9.1 for p > 1).
