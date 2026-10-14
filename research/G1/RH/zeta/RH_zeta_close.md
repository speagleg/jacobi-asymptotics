# RH_zeta_close: closing the smooth-ζ pointwise Law P (Plan 14)

Status: **in progress (Plan 14).** §1 (hard edge) is a PROOF, pending Rule R. §§2–4 are to come.

Notation is as in RH_zeta.md §4 and RH_px.md §§3–5:
- the rescaled variable z = sx, with s = 1/x_N ≍ N²/log²N;
- the band [0, β̂] and its equilibrium (Lemma E1);
- φ, the V-frame (T, lenses, V^△, the normalization F·Ξ, and C_∞), and the global parametrix N = D_∞^{σ₃}N₀D_w^{−σ₃};
- D_w is the Szegő function of the band weight w₀ on [0, β̂], and D_∞ := D_w(∞).

The far field (Lemma Z, §2) and the uniform conformal maps at both edges (§3) are used as stated there.

## 1. The hard edge with a log weight (Rule R F1 of Plan 13)

**The problem.** At 0 the band weight is w₀ ∝ z^{−1/2}·log(γ/2π)·k_N with Λ := log(γ/2π) ≍ log N. Λ is unbounded,
so the KMVV/RH_px §4.1 construction fails:
- the continuations of w₀ from the two half-planes do not glue on (−δ, 0);
- the mismatch (Λ − iπ/2)/(Λ + iπ/2), conjugated by the Bessel parametrix, is O(N/log N) at the Bessel scale;
- so no small-norm argument closes. This is Conway–Deift's Remark 4.10 situation.

**The route** (C–D, adapted):
1. Build an *exactly solvable comparison problem*. It is σ_ζ's own problem with the Bessel parametrix built from
   W̃ := D_w (H1). Then the band jump is exact and nothing jumps on (−δ, 0). The price is a lip mismatch of size
   O(1/log N) in sup norm (LW1).
2. Prove that its resolvent is bounded uniformly in N (UR). It is not taken from C–D Thm 4.5, which is
   Legendre-specific.
3. Run C–D's Neumann series (Theorem C) and difference formula (Proposition D). They give a log-weight effect of
   O(1/(N log N)) on Q₁ and Q₂.

### 1.0 The frame

Q := D_∞^{−σ₃}·V·D_w^{σ₃}. Then Q → I at ∞, and its jumps v = Q₋^{−1}Q₊ are:
- band [0, β̂]: J₀ := [[0, 1], [−1, 0]] (since D_{w,+}D_{w,−} = w₀);
- lens lips: [[1, 0], [(D_w²/w₀)e^{2Nφ}, 1]], plus the super-small (h1) entries of RH_px Lemma 4.3, all
  O(exp(−cN|z|^{−1/2}/log N)) near 0;
- saturated region (β̂, X₁ + δ′): [[1, 0], [(D_w²/w₀)e^{2Nφ̃}, 1]];
- the vertical segments at β̂: [[1, (W̃/(F̃²D_w²))e^{−2Nφ̃}], [0, 1]], in RH_px §4.2's notation;
- Σ^△ lips and the top pieces: I + O(e^{−cN}poly(N)), and I + O(N^{−cN}) at the top;
- nothing on (−∞, 0) (F·Ξ is jump-free there), nothing on the far-field curve C (Ξ), and nothing beyond.

Here w₀(z) on a lip means the analytic continuation of w₀ from the band.

### 1.1 Lemma A1 (the only non-RH_px feature is Λ)

**Lemma A1.** On (0, x_e), with Λ := log(γ/2π) and γ = (s/z − ¼)^{1/2},

  w₀(z) = C_N · z^{−1/2} · Λ(z) · k_N(z),  k_N(z) := (1 − z/(4s))^{−1/2}(β̂ − z)^{1/4}/(D̃(z)B(z))².

Moreover:
- **(i)** Λ is analytic in U(0, δ) ∖ (−δ, 0], with |Λ(z)| ≥ ½log(s/(4π²δ)) − 2 ≥ c log N there.
- **(ii)** log k_N is Hölder-½ on U(0, δ) from each side of (−δ, 0), with constants uniform in N.

*Proof.*
- The band weight is w₀ = |W|(β̂ − z)^{−2κ}/(D̃B)², with κ = −1/8 (RH_zeta §3(a)) and |W| = 4π z|dt/dz| (RH_zeta §3).
  Here t = N₀(γ) + ½, N₀′(γ) = Λ/(2π) and dγ/dz = −s/(2z²γ). Hence

    4πz|dt/dz| = Λ·s/(zγ) = Λ·s^{1/2}z^{−1/2}(1 − z/(4s))^{−1/2},

  exactly.
- (i): γ ≥ (s/δ − ¼)^{1/2} on U(0, δ), and |arg γ| ≤ π/2.
- (ii) is RH_px Lemma 3.4's consequence:
  - (log D̃)′ = O(|z|^{−1/2}/(√s Λ)) = O(|z|^{−1/2}/N), since μ′(t) = O(t^{−2}) and t′/t² ≍ 1/(zγΛ);
  - log B is Hölder-½ near 0, because ℓ̂(y) = O(|y|^{1/2}) as y → 0⁻ (checks/check_z_e2e_xi.out prints ℓ̂ = 2arg D₊
    on (−∞, 0); |ℓ̂| ≤ 2·10⁻⁸ at |y| ~ 10⁻⁹) and ℓ̂ is bounded far out;
  - the remaining factors are analytic. ∎

### 1.2 The comparison problem

**Lemma H1 (Bessel parametrix with W̃ := D_w).** In U(0, δ) put

  P̃₀ := (−1)^N·Ẽ_N·σ₃Ψ(N²f)σ₃·D_w^{−σ₃}·e^{Nφσ₃},  Ẽ_N := N·D_w^{σ₃}·M·f^{σ₃/4}(2πN)^{σ₃/2}
       = D_∞^{σ₃}·N₀Mf^{σ₃/4}·(2πN)^{σ₃/2}.

Here:
- Ψ is the KMVV Bessel matrix of order α = −½, (6.23)–(6.25);
- f is the conformal map of RH_px Lemma 4.1, which is univalent on U(0, δ) uniformly in N by §3;
- M = [[1, i], [i, 1]]/√2.

Then:
- **(i)** Ẽ_N is analytic in U(0, δ), with det Ẽ_N = 1, and D_∞^{−σ₃}Ẽ_N(2πN)^{−σ₃/2} = N₀Mf^{σ₃/4} is bounded with
  bounded inverse there, uniformly in N.
- **(ii)** In U(0, δ), P̃₀ has exactly V's band jump, no jump on (−δ, 0), and on the lips the jump
  [[1, 0], [c_± e^{2Nφ}/D_w², 1]], where c_± := e^{∓iπα} = ±i is the factor in KMVV (6.45) (W̃² = e^{∓βπi}w).
- **(iii)** On ∂U(0, δ): D_∞^{−σ₃}(P̃₀N^{−1} − I)D_∞^{σ₃} = O(1/N).

*Proof.*
- (i):
  - Band: N₀ jumps by J₀, and f₊^{σ₃/4} = diag(−i, i)f₋^{σ₃/4}. This is RH_px Lemma 4.2(i)'s computation verbatim,
    since M^{−1}J₀M = diag(i, −i).
  - (−δ, 0): N₀ and f are analytic there (f > 0, principal root).
  - At 0, |N₀| = O(|z|^{−1/4}) and |f^{±1/4}| = O(|z|^{±1/4}). So the singularity is O(|z|^{−1/2}) and therefore
    removable (KMVV Prop. 6.5's argument, quoted in CITATIONS).
  - Boundedness: N₀Mf^{σ₃/4} is analytic on U(0, 2δ) by the same argument, and depends on N only through f and β̂,
    which are uniform (§3).
- (ii):
  - The band jump is exact because D_{w,+}D_{w,−} = w₀.
  - D_w is analytic off [0, β̂], so nothing jumps on (−δ, 0).
  - The lip entries follow from Ψ's jumps on γ₁, γ₃, as in KMVV (6.1). With KMVV's W̃ (W̃² = e^{∓iπα}·w) they would
    be e^{2Nφ}/w₀ exactly; with W̃ = D_w they are c_±e^{2Nφ}/D_w².
- (iii): KMVV (6.28), with Ẽ_N bounded in the D_∞-frame. ∎

**The comparison solution.**
- P̃ := N outside the discs, P̃₀ in U(0, δ), and P_r (WLXZ §6.1 Airy, for σ_ζ's own weight, uniform by §3) in
  U(β̂, ε).
- 𝒵̃ solves the RHP with jumps:
  - P̃₀N^{−1} on ∂U(0, δ) and P_rN^{−1} on ∂U(β̂, ε), both O(1/N) in the D_∞-frame;
  - N·(V's jumps)·N^{−1} outside the discs, which are exponentially small.
- RH_px §5's small-norm argument applies verbatim: 𝒵̃ exists for N ≥ N₀, and D_∞^{−σ₃}(𝒵̃ − I)D_∞^{σ₃} = O(1/N)
  uniformly, with the same O(1/N) for its first two moments at ∞.
- Q̃ := D_∞^{−σ₃}𝒵̃P̃D_w^{σ₃} then solves Q̃₊ = Q̃₋ṽ on the contour Σ of Q, with ṽ = v **except** on the lips inside
  U(0, δ). There ṽ = [[1, 0], [c_± e^{2Nφ}, 1]] (in the Q-frame: D_w^{−σ₃}[[1, 0], [c_±e^{2Nφ}/D_w², 1]]D_w^{σ₃}),
  and the (h1) entries are dropped.

### 1.3 Lemma LW1 (lip mismatch)

**Lemma LW1.** On the lips in U(0, δ),

  |D_w(z)²/w₀(z) − c_±| ≤ C(|z|^{1/3} + 1/log N),

uniformly in N. Hence ‖v − ṽ‖_{L^∞(Σ)} ≤ C/log N. Moreover v − ṽ = δ(z)e₂e₁ᵀ + (h1), where
δ := (D_w²/w₀ − c_±)e^{2Nφ} and |e^{2Nφ}| ≤ e^{−cN|z|^{1/2}} on the lips.

*Proof.*
- Write w₀ = C_N·z^{−1/2}·Λ·k_N (A1). Then D_w = C_N^{1/2}·D_{x^{−1/2}}·G·D_k, where G := D_Λ and D_k := D_{k_N}, and
  D_w²/w₀ is the product of the three corresponding ratios.
- Each ratio uses the representation (from (R(z)/2π)∫_0^{β̂}dx/(√(x(β̂ − x))(z − x)) = ½, as in RH_px Lemma 3.4):

    log D_q(z) − ½log q(z) = (R(z)/2π)∫_0^{β̂}(log q(x) − log q(z)) dx/(√(x(β̂ − x))(z − x)),  R = (z(z − β̂))^{1/2}.

  - **q = x^{−1/2}:** the ratio D_q²/q equals the constant c_± that makes KMVV's W̃ consistent (RH_px Lemma 4.2), up to
    1 + O(|z|^{1/2}). The O(|z|^{1/2}) is the β̂-end contribution; the 0-end part is scale-invariant.
  - **q = Λ:** |log Λ(x) − log Λ(z)| ≤ (|log(x/|z|)| + π)·sup|d log Λ/d log z| ≤ (|log(x/|z|)| + π)/(c log N), by
    A1(i) and d log Λ/d log z = −½(1 − z/(4s))^{−1}/Λ. For z on a lip, |x − z| ≥ c(x + |z|). So the integral is at most
    (C/log N)∫_0^∞(|log u| + π)u^{−1/2}(1 + u)^{−1}du = C′/log N, i.e. **|G²/Λ − 1| ≤ C/log N**.
  - **q = k_N:** Hölder-½ (A1(ii)) gives |log D_k² − log k_N| ≤ C|z|^{1/2}log(1/|z|) ≤ C|z|^{1/3}.
- Finally |e^{2Nφ}| ≤ e^{−cN|z|^{1/2}} on the lips (Re φ < 0, φ ~ −2(−f)^{1/2}). The (h1) entries are
  O(exp(−cN|z|^{−1/2}/log N)). Away from U(0, δ), v = ṽ. ∎

*Numerical check* (`checks/check_z_lw1.out`): sup over the lips at angles π/3 and π/6 of |G²/Λ − 1|, for
N = 10², 10³, 10⁴, 10⁶, 10⁹, 10¹²:
- 0.285, 0.206, 0.161, 0.111, 0.0744, 0.0564;
- times log N: 1.31, 1.42, 1.49, 1.53, 1.54, 1.56, i.e. C/log N with C ≈ 1.6.
- Band sanity: |G₊G₋/Λ − 1| ≤ 6·10⁻¹⁰.

### 1.4 Uniform resolvent for the comparison problem

Σ is a finite union of C² arcs whose Carleson constant is uniform in N. Its long pieces (Σ^△ lips of length O(N²))
are straight. C_ṽ f := C₋(f(ṽ − I)) acts on L²(Σ), with L^∞ jumps ṽ, ṽ^{−1}.

**Lemma W (power-weighted Cauchy operator on a star).** Let Σ_* be a finite union of C² arcs leaving z₀ at distinct
angles, and let |a| < ½. Then f ↦ |z − z₀|^a C_±(|s − z₀|^{−a}f) is bounded on L²(Σ_* ∩ U(z₀, r)), with norm depending
only on a, the angles and the C² norms. It is invariant under dilation about z₀.

*Proof.*
- Flatten each arc to its tangent ray. The error kernel is O(1) and harmless.
- On rays the operator is a matrix of Mellin convolutions in r = |z − z₀|, with kernel homogeneous of degree −1.
- Off the diagonal (ray i ≠ j), the Mellin symbol is ∫_0^∞u^{−a−1/2+iτ}du/(ue^{iθ_j} − e^{iθ_i}). It is absolutely
  convergent and bounded in τ iff |a| < ½.
- On the diagonal, the symbol is PV∫_0^∞u^{s−1}du/(u − 1) = −π cot(πs), with s = ½ − a + iτ. It is bounded on
  Re s = ½ − a ∈ (0, 1).
- Plancherel for the Mellin transform finishes the proof. ∎

**Lemma UR.** There are N₀ and C such that, for N ≥ N₀, 1 − C_ṽ is invertible on L²(Σ) and
‖(1 − C_ṽ)^{−1}‖ ≤ C.

*Proof.*

**(a) Reduction** (the easy half of C–D Prop. 4.6, re-proved).
- Let f ∈ L²(Σ), and suppose m ∈ ∂C(L²) solves m₊ = m₋ṽ + f(ṽ − I) with ‖m±‖ ≤ C‖f‖. Then μ := m₋ + f satisfies
  μ − C₋(μ(ṽ − I)) = f:
  - m = C(h) with h = m₊ − m₋ = μ(ṽ − I), so m₋ = C₋(μ(ṽ − I)).
  - Moreover ‖μ‖ ≤ C′‖f‖.
- Uniqueness: if μ = C₋(μ(ṽ − I)), then m := C(μ(ṽ − I)) solves m₊ = m₋ṽ, so mQ̃^{−1} has no jump on Σ.
  - At the edge points, |m| = O(|z − z₀|^{−1/2}) in sectors (an L² Cauchy integral) and |Q̃^{−1}| = O(N|z − z₀|^{−1/4})
    by (d). So the singularities are removable.
  - mQ̃^{−1} → 0 at ∞, so m ≡ 0 and μ = m₋ = 0.

**(b) Explicit solution.** m := C(gQ̃₊^{−1})·Q̃ satisfies m₊ − m₋ṽ = (C₊ − C₋)(gQ̃₊^{−1})Q̃₊ = g. It remains to show
‖m±‖ ≤ C‖g‖. (gQ̃₊^{−1} ∈ L¹_loc by the bounds below, so C(·) is defined.)

**(c) Partition.** Take a smooth partition of unity on Σ subordinate to:
- U(0, 2δ);
- U(β̂, 2ε);
- the rest, where Q̃ and Q̃^{−1} are uniformly bounded (Q̃ = 𝒵̃′N₀, with 𝒵̃′ = I + O(1/N) and N₀ = M₀a^{σ₃}M₀^{−1},
  |a|^{±1} ≤ C there).

Pieces with separated supports have bounded smooth kernels. The weights below are L² there, so they contribute
O(‖g‖). On the third piece the Carleson bound for C± applies directly.

**(d) Hard-edge piece.** On U(0, 2δ), (H1) gives

  Q̃ = A₀(z)·(2πN)^{σ₃/2}·Φ(N²f(z))·(constant sign),  A₀ := 𝒵̃′N₀Mf^{σ₃/4},  Φ(ζ) := σ₃Ψ(ζ)σ₃e^{Nφσ₃},

with A₀^{±1} analytic and bounded uniformly.
- Φ is N-free as a function of ζ: e^{Nφ} = e^{∓2ζ^{1/2}} branchwise.
- KMVV (6.28) and the local form at 0 for α = −½ give Φ(ζ) = B(ζ)·ζ^{−σ₃/4}·Θ(ζ). Here B is analytic, bounded and
  boundedly invertible on f(U(0, 2δ)) after scaling: B = (2π)^{−σ₃/2} const for |ζ| ≥ 2 and B = Ψ̂ for |ζ| ≤ 3. Θ, Θ^{−1}
  are bounded and piecewise smooth.
- Write C(gQ̃^{−1})Q̃ = C(gΦ^{−1}N^{−σ₃/2}A₀^{−1})A₀N^{σ₃/2}Φ, and split A₀^{−1}(s)A₀(z) = I + (s − z)K(s, z), with K
  analytic and bounded.

The I-term. The constant N^{∓σ₃/2} pass through C. What remains is g ↦ C(gΦ^{−1})Φ.
- Change variables ζ = N²f(z). This is conformal with f′ ≍ 1; the Cauchy kernel changes by a bounded smooth term,
  and L² norms scale by the same factor on both sides.
- In ζ the operator is h ↦ C(hΘ^{−1}ζ^{σ₃/4}B^{−1})Bζ^{−σ₃/4}Θ. The B-commutator again has a bounded analytic kernel,
  N-free on |ζ| ≤ 3, and is treated like the K-term. The core h ↦ C(hζ^{σ₃/4})ζ^{−σ₃/4} is two copies of Lemma W,
  with a = ±¼.

The K-term has kernel

  Φ^{−1}(ζ_s)N^{−σ₃/2}K(s, z)N^{σ₃/2}Φ(ζ_z).

Since N^{σ₃/2}ζ^{−σ₃/4} = f^{−σ₃/4}, for |ζ_s|, |ζ_z| ≥ 2 the entries are O(|s|^{±1/4}|z|^{∓1/4}). Their
Hilbert–Schmidt norm on U(0, 2δ)² is O(1).
- If |ζ_s| ≤ 2 (|s| ≲ N^{−2}), the s-factor is O(N^{1/2}|ζ_s|^{−1/4}), and similarly for z.
  - Both small: HS² ≲ N²(N^{−2}∫|ζ|^{−1/2})² = O(N^{−2}).
  - Mixed: HS² ≲ N·N^{−2}·O(1).
- So the K-term is O(‖g‖).
- In particular |Q̃^{±1}| ≤ C N^{1/2}|ζ|^{−1/4} for |ζ| ≤ 2 and ≤ C|z|^{−1/4} for |ζ| ≥ 2, which is what (a) used.

**(e) Soft-edge piece.** The same argument applies, with the WLXZ Airy matrix:
- Q̃ = A_r N^{σ₃/6}Φ_Ai(ζ), with Φ_Ai = (balanced) ζ^{−σ₃/4}Θ for |ζ| ≥ 2 and bounded for |ζ| ≤ 2 (Airy functions are
  entire);
- the small-ζ HS² is ≲ N^{2/3}(N^{−2/3})² → 0. ∎

### 1.5 Theorem C (uniform resolvent for the true problem)

**Theorem C.** For N ≥ N₁, 1 − C_v is invertible on L²(Σ), with ‖(1 − C_v)^{−1}‖ ≤ 2C.

*Proof.* This is C–D Theorem 4.7's argument (quoted in CITATIONS), with Lemma UR in place of their Theorem 4.5:
- ‖C_v − C_ṽ‖ ≤ ‖C₋‖·‖v − ṽ‖_∞ ≤ C″/log N (LW1);
- so ‖(C_v − C_ṽ)(1 − C_ṽ)^{−1}‖ ≤ ½ for N ≥ N₁;
- (1 − C_v)^{−1} = (1 − C_ṽ)^{−1}(1 − (C_v − C_ṽ)(1 − C_ṽ)^{−1})^{−1}. ∎

### 1.6 Proposition D (the log weight moves Q₁, Q₂ by O(1/(N log N)))

Q (the true problem, from the OPs of σ_ζ) and Q̃ satisfy C–D Theorem 4.4's hypotheses with p = q = 2:
- Q₋, Q̃₋^{±1} ∈ I + ∂C(L²(Σ)): Σ is bounded, and Q, Q̃ = O(|z|^{−1/4}Λ^{1/2}) at 0;
- for Q this is (Y4)_x of RH_px §5 with the extra Λ factor; for Q̃ it is (d) above.

Then (C–D (4.15), (4.14)), with μ := Q₋ = (1 − C_v)^{−1}I and μ̃ := Q̃₋:

  Q₁ − Q̃₁ = −(1/2πi)∫_Σ μ(v − ṽ)ṽ^{−1}μ̃^{−1}dz,  and Q₂ − Q̃₂ is the same with an extra factor z.

**Proposition D.** Q₁ − Q̃₁ and Q₂ − Q̃₂ are O(1/(N log N)).

*Proof.* (v − ṽ)ṽ^{−1} = δe₂e₁ᵀ + (h1), since e₁ᵀ[[1, 0], [−c, 1]] = e₁ᵀ. Split μ = μ̃ + (μ − μ̃).

**Main term.** ∫δ·μ̃e₂e₁ᵀμ̃^{−1}.
- By (d), μ̃e₂e₁ᵀμ̃^{−1}·e^{2Nφ} = A₀N^{σ₃/2}[σ₃Ψe₂e₁ᵀΨ^{−1}σ₃]N^{−σ₃/2}A₀^{−1}. Note that e^{Nφσ₃} cancels e^{2Nφ}.
- For |ζ| ≥ 2: Ψe₂e₁ᵀΨ^{−1} = e^{−4ζ^{1/2}}ζ^{−σ₃/4}(const)ζ^{σ₃/4}(1 + O(ζ^{−1/2})), and Re ζ^{1/2} ≥ ½|ζ|^{1/2} on γ₁, γ₃.
  So the integrand is ≤ C(|z|^{1/3} + 1/log N)|z|^{−1/2}e^{−cN|z|^{1/2}}.
- For |ζ| ≤ 2 it is ≤ C(N^{−2/3} + 1/log N)·N|ζ|^{−1/2}.
- Integrating: (1/log N)(∫_0^δ r^{−1/2}e^{−cN√r}dr + N∫_0^{N^{−2}}(N²r)^{−1/2}dr) + N^{−5/3}·O(1) = O(1/(N log N)).

**Correction term.** It is at most ‖μ − μ̃‖₂·‖δe₁ᵀμ̃^{−1}‖₂.
- μ − μ̃ = (1 − C_v)^{−1}C₋(μ̃(v − ṽ)), so ‖μ − μ̃‖₂ ≤ 2C‖δμ̃e₂‖₂ (Theorem C).
- By (d), ‖δμ̃e₂‖₂² and ‖δe₁ᵀμ̃^{−1}‖₂² are ≲ (1/log²N)(∫r^{−1/2}e^{−cN√r}dr + N·N^{−2}) = O(1/(N log²N)).
- So the term is O(1/(N log²N)).

The (h1) parts and the moment z only improve the bounds. ∎

### 1.7 Consequence for the coefficients

- By RH_px §5's invariance lemma (extraction), (Q₁)₁₂(Q₁)₂₁ = (V₁)₁₂(V₁)₂₁ = (s b_N)². The same holds for a(·).
- For Q̃ = D_∞^{−σ₃}𝒵̃P̃D_w^{σ₃}: (Q̃₁)₁₂(Q̃₁)₂₁ = (β̂/4)²(1 + O(1/N)) and a(Q̃) = (β̂/2)(1 + O(1/N)), from (N₁)₁₂(N₁)₂₁ =
  (β̂/4)² and 𝒵̃ = I + O(1/N).
- Proposition D, with every entry of Q₁ and Q̃₁ O(1) in this frame, gives:

  **b_N = (β_N/4)(1 + O(1/N)),  a_N/(2b_N) = 1 + O(1/N),**

  conditional only on §2 (Lemma Z) and §3 (uniform conformal maps and Airy). The log weight's own contribution is
  O(1/(N log N)).

**Numerical corroboration** (`checks/check_z_cmp.out`, J = 4·10⁵ and 8·10⁵, identical).
- σ̃ has the same nodes and masses 2x_j/Λ(x_j), i.e. the log removed. Then
  N log N·(b_N(σ_ζ)/b_N(σ̃) − 1) = 0.41, 0.44, 0.47, 0.49, 0.50, 0.51, 0.52 for N = 50 … 3200.
- So the log's effect is ≈ 0.5/(N log N), the order of Proposition D.
- The a_N/(2b_N) difference is ~10⁻⁴/N, i.e. smaller still.

## 2. Lemma Z (far field) — PROVED, with a CERTIFIED (Arb) sign/winding computation

**Setting** (RH_zeta §4.2). Work in x-units, so C is fixed: the circle through −r and x_m, with r = 0.0017 and
x_m = 0.015. Then:
- x₁ = x(1) ≈ 0.00474 < x_m < x_e ≈ 0.02527;
- r < |x_cross| = 1/(4π²e² − ¼) ≈ 0.00343, the point where t(x) crosses the negative real t-axis.

The two scalars are:
- inside C, F_in = D·B·K, with D = D̃/(1 − e^{∓2πit}), B the full-axis Binet-cut scalar, and K = (β − x)^{−1/8} up to the
  constant s^{−1/8};
- outside C, F_out = exp H, with H(z) := ∫_β^{x_e}t̂(y)dy/(y − z) and t̂ = t − 3/8.

**N-independence.** In x-units, t(x) = N₀(γ(x)) + ½, D̃, D and B (built from ℓ̂ = 2arg D₊ on (−∞, 0)) do not depend on
N. N enters only through β = β_N → 0 (in H and K) and through the constant s^{−1/8}.

**Lemma Z.**
- **(i)** F_in is analytic and zero-free in int(C) ∖ ((−∞, 0] ∪ [0, x_m]), with exactly the jumps used in RH_zeta §4.1.
- **(ii)** L := log(F_out/F_in) has a continuous single-valued determination on C, for every N. Its non-constant part is
  bounded: sup_C|L − c_N| ≤ C, with c_N = (1/8)log s + const.
- **(iii)** Ξ(z) := exp((1/2πi)∮_C L(ζ)dζ/(ζ − z)) is analytic off C and bounded near C (L is Lipschitz on C). Inside C,
  for |x| ≤ 2β_N, Ξ = e^{c_N}Ξ₀(1 + O(β_N)), with β_N = O(log²N/N²). So F·Ξ (on both sides) has no jump on C, and near
  the band and both edges it differs from a constant by O(log²N/N²). This is absorbed into 𝒵 at that cost.

*Proof of (i).* Im t is harmonic in Ω := ℂ₊ ∩ int(C), and its boundary values satisfy:
- on (0, x_m), Im t = 0 (t is real on the monotone branch);
- on (−r, 0), Im t₊ = −(η/2π)log(η/2πe) < 0, with η = (¼ − 1/x)^{1/2} > 2πe because |x| < |x_cross|;
- on the upper arc of C, Im t < 0. This is **certified** (check_z_Zcert.out): 224 Arb balls on θ ∈ [10⁻³, π], plus a
  certified derivative bound on [0, 10⁻³] (t′ = −11.3 ± 0.05 at x_m);
- near 0, Im t → −∞, since arg γ ∈ (−π/2, 0).

So Im t < 0 in Ω by the maximum principle. Hence there:
- t ∉ (−∞, 0], so μ(t) is analytic;
- |e^{−2πit}| < 1, so D_up is zero- and pole-free.

The lower half follows by conjugation symmetry, D_low(z̄) = conj D_up(z). ∎

*Proof of (ii).*
- Parametrize C counterclockwise from x_m. On each open arc, continuous determinations exist for:
  - H (single-valued off [β, x_e]);
  - log B (off (−∞, 0]);
  - log K (off [β, ∞));
  - log D_up on the upper arc and log D_low on the lower arc (by (i)), each started at x_m from its principal value.
- R := F_out/F_in has winding −(1/2πi)(J(x_m) + J(−r)), where J(p) is the jump at p of the sum of these determinations.

**At x_m.** The three jumps are:
- H₊ − H₋ = 2πit̂(x_m) (Plemelj);
- log D_up − log D_low = Log(1 − e^{2πit}) − Log(1 − e^{−2πit}) = i(2πt − π), at real t = t(x_m) ∈ (3/8, 1) (certified:
  0.41530…);
- log K₊ − log K₋ = iπ/4.

So J(x_m) = 2πi(t − 3/8) − i(2πt − π) − iπ/4 = **0 exactly**. This is the α-shift identity; without the shift
(K = (β − z)^{−1/2}) it is 3πi/4, which is Rule R's control.

**At −r.** H and K are continuous there.
- log B jumps by +iℓ̂_axis(−r) (Plemelj, with ℓ̂ continued along the axis from 0⁻, where it vanishes).
- Conjugation symmetry gives log D_low − log D_up = −iℓ̂_arc(−r), with ℓ̂_arc := 2·(arg D_up continued along the upper
  arc from x_m).
- So J(−r) = i(ℓ̂_arc − ℓ̂_axis)(−r), and

    **winding(R) = −(ℓ̂_arc(−r) − ℓ̂_axis(−r))/2π.**

**Certification** (`checks/check_z_Zcert.py` → `.out`; Arb, 128 bits; DLMF 5.11 for the tail).
- Every continuous-arg step is certified to equal the principal Arg of the endpoint ratio. This is done by showing
  Re(D(Z)/D(z_a)) > 0 on a ball Z covering the step, with t(Z) ∩ (−∞, 0] = ∅.
  - Steps: 280 + 1856 on the arc, and 42950 on the axis segment [−r, −10⁻⁷] (in log|x|).
- On (−10⁻⁷, 0), η ≥ 3162.
  - |μ(t)| ≤ sec²(½ph t)/(12|t|) ≤ 8.6·10⁻⁵ (DLMF 5.11, n = 1) and |e^{−2πit}| ≤ 3·10⁻⁷¹⁷¹ at η₀.
  - Both decrease in η, since |t| and −Im t increase and ph t moves toward −π/2.
  - So arg D₊ stays in (−π/2, π/2) and ℓ̂(0⁻) = 0.
- Result: ℓ̂_arc(−r) = ℓ̂_axis(−r) = −0.00944078831849753 (±5·10⁻¹⁸), so W ∈ [±2·10⁻²⁸]. **The winding is 0.**

**Bound.**
- The winding is N-independent: every quantity above is N-free in x-units.
- L − c_N = L₀ + E_N, where L₀ is the β = 0 limit (continuous on C, N-free) and |E_N| ≤ Cβ^{1/2}log(1/β) on C. That
  bound comes from |∫_0^β t̂/(y − z)| ≤ dist(C, 0)^{−1}∫_0^β|t̂| with t̂ ≍ y^{−1/2}log(1/y), and from
  (β − x)^{−1/8}/(−x)^{−1/8} = 1 + O(β).
- This matches the Plan 13 measurement that sup|L| grows like log N (3.8, 5.5, 7.1 at N = 20, 40, 80): that growth is
  all c_N. ∎

*Proof of (iii).*
- L is piecewise analytic on C and continuous (by (ii)), hence Lipschitz. So its Cauchy integral is bounded up to C.
- The constant c_N contributes exactly e^{c_N} inside and 1 outside.
- For |x| ≤ 2β: |log Ξ(x) − log Ξ(0) − c_N·0| ≤ |x|·sup_C|L − c_N|·|C|/(2π dist(·, C)²) = O(β_N).
- Derivatives are similar. ∎

Lemma Z is thus **PROVED** (with a certified computation). This closes Rule R F4's open item and RH_zeta §4.2's "What
remains".
