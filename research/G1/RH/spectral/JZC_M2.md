# JZC M2: the discreteness layer — Theorem K for all p ≠ 1 (Plan JZC, milestone M2)

Status (2026-10-21): NOT REVIEWED. Labels per VERIFICATION_POLICY.md. Builds on SPEC §3.14 (Theorem K for p > 1) and E_plt1
Lemma F.1 (REVIEWED).

| # | Statement | Label |
|---|---|---|
| Thm K′ | For every p ∈ (0, 1) ∪ (1, ∞), Lemma E3.7's functional on the full band factor of σ_{p,s} equals (1/2πi)∫_{(c₀)}pW(w)ζ(−wp)n^{−wp}·π[cot(πwp/2) − cot(πw)]dw (0 < c₀ < 1); its residues are E3's ε_j | PROVED-mod-cite (p > 1: SPEC §3.14; p < 1: E_plt1 Lemma F.1 [REVIEWED], DLMF 5.2.1, 25.2.1, 25.4.1; Mellin–Barnes for (1 + x)^{−3/2}, NOT QUOTED) |
| Prop M2.2 | General index function κ, conditional on (G2): the first-order band-factor change has integer residues pW(j)δZ(−j); the pole of Z lies outside the strip; tan pole at (m + 1)/p | CONDITIONAL (G2); computation PROVED (SPEC Prop 3.14.4) |
| Checks | m2_thmK_plt1.out (p = 0.3, 0.6, 0.75; 16 digits); spec_kernel.out (p > 1) | NUMERICAL |

## 1. Theorem K′ (p < 1)

**Setting.** E_plt1 Lemma F.1 (seam geometry, θ = θ_s = pπ/2) gives

  𝒢(z) − 𝒢(1) = (1/2πi)∫_0^∞ℓ(r)[e^{iθ}K(re^{iθ}, z) − e^{−iθ}K(re^{−iθ}, z)]dr,

with ℓ(r) = −log(1 − e^{−2πnr^{−1/p}}) and H_n = e^{−2𝒢}. Its moments are m_k = ζ(−kp)/(kn^{kp}) (Lemma F.1(iii)).

**Theorem K′.** Let 0 < p < 1 and define

  e_n := (2cp/π)∫_0^∞ℓ(r)·Im[e^{iθ}k(re^{iθ})]dr,   k(ζ) := ζ^{−2}(1 − 4c/ζ)^{−3/2}.

Then:
- (i) e_n = cp·Σ_k2m_kQ_k(4c) term by term. That is, e_n is Lemma E3.7's functional on the full band factor.
- (ii) e_n = (1/2πi)∫_{(c₀)} pW(w)ζ(−wp)n^{−wp}·π[cot(πwp/2) − cot(πw)]dw for 0 < c₀ < 1. This is the same formula as for p > 1.
- (iii) For every J, e_n = Σ_{j≤J}pW(j)ζ(−jp)n^{−jp} + O(n^{−(J+1)p}).

*Proof.*
- **(i).** As for p > 1, from Σ_kQ_k(4c)ζ^{−k−1} = ζ^{−2}(1 − 4c/ζ)^{−3/2} (|ζ| > 4c) and the moments of Lemma F.1(iii). The seam
  integrand is exponentially small for |ζ| ≤ 2R₁ (Lemma F.1(iv), near part). On the seam, Im(1 − 4c/ζ) = (4c/r)sin θ > 0, so the
  principal branch is never crossed.
- **(ii).** The Mellin transform of ℓ is ∫_0^∞ℓ(r)r^{−w−1}dr = p(2πn)^{−wp}Γ(wp)ζ(1 + wp) for Re w > 0. The proof is Lemma F.1(iii)
  with complex w; the strip comes from ℓ(r) ~ (1/p)log r at ∞ and its super-exponential decay at 0.
  - Expand (1 + v)^{−3/2} with v = −4ce^{−iθ}/r by Mellin–Barnes (arg v = π − θ ∈ (0, π)). Put w = s + 1. The angular factor is
    Im[e^{iθ}e^{−2iθ}e^{−iθs}e^{iπs}] = −sin((π − θ)w).
  - The functional equation (DLMF 25.4.1) gives pΓ(wp)ζ(1 + wp)(2π)^{−wp} = −πζ(−wp)/(w sin(πwp/2)).
  - Γ(1 − w)/w = π/(sin(πw)Γ(1 + w)).
  Collecting, the integrand is pW(w)ζ(−wp)n^{−wp}·π·sin(πw − πwp/2)/(sin πw·sin(πwp/2)), using θ = pπ/2. And

    sin(πw − πwp/2)/(sin πw·sin(πwp/2)) = cot(πwp/2) − cot(πw).

- **(iii).** As for p > 1: the bracket decays like e^{−min(p, 2)π|Im w|}, the cot(πwp/2) poles (w = 2l/p > 2) sit on trivial
  zeros, and the integer poles give −Res = pW(j)ζ(−jp)n^{−jp}. ∎

**Check** (`checks/m2_thmK_plt1.py`, `checks/m2_thmK_plt1.out`): quadrature against Mellin–Barnes agrees to all 16 printed
digits at (p, n) = (0.6, 10), (0.3, 8), (0.75, 20). The residue sums converge to it asymptotically, slowly at p = 0.3, where
many ε_j are relevant.

**Reading.** The negative-axis geometry (p > 1, θ = π − π/p measured from the cut) and the seam geometry (p < 1, θ = pπ/2) give
literally the same kernel. In both, the angle enters only through sin(πw − πwp/2), and the functional equation turns that into
cot(πwp/2) − cot(πw). So the discreteness layer has one formula for all p ≠ 1. At p = 1 the two cot terms merge (resonance), which
is where E2 and E3 also stop.

## 2. Proposition M2.2 (general index function; CONDITIONAL on G2)

Suppose the band factor of a perturbed node set is the Cauchy integral of 𝔢_κ, with phase t_κ(z) = κ(n^p/z) (Hypothesis G2,
SPEC §3.14). SPEC Proposition 3.14.4 computes the first-order change of e_n for κ(λ) = λ^{1/p} − γλ^{−m/p}. Its Mellin–Barnes
integrand is pW(w)δZ(−w)n^{−pw}·π[−cot(πw) − tan(π(pw − m)/2)] (p > 1; the seam version is analogous). Hence:
- the integer residues give pW(j)δZ(−j)n^{−jp}, the zeta layer of the perturbed set;
- the pole of δZ(−w) at q = m/p lies outside the convergence strip (Re w > (m + 1)/p), so the pole term is not carried by the
  band factor. It comes from the equilibrium layer (JZC_M1, Proposition M1.2);
- the tan pole at w = (m + 1)/p sits at the order of the subleading pole terms. Its role next to the Jacobian tilt (SPEC §3.15)
  is open.

## 3. Status of the correspondence after M1 and M2

| Layer | Content | Status |
|---|---|---|
| L1 continuum | leading law; all poles of Z with π cot; nonlinear terms | Theorem Q, Prop M1.2 (PROVED + REVIEWED, two readers; updated 2026-10-23), as a statement about the equilibrium; its identification with b_n needs G1 |
| L2 discreteness | the Z(−j) | Theorem K′ for the lattice, all p ≠ 1 (PROVED-mod-cite); general κ needs G2 |
| L3 second order | δ_eff (rule H), Jacobian tilt | NUMERICAL (S1⁗, §3.15); derivation open (M4) |
| Link to b_n | G1–G3 (Riemann–Hilbert for non-lattice nodes) | open (M3) |
