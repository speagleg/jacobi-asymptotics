# Theorem RH₁(r): pointwise Law P for σ_r = Σ k^{−r} δ_{1/k}, every r > 1 (p = 1)

Status: **DRAFT, pending Rule R** (2026-10-13, plan-11). This extends Theorem RH₁ (RH_p1.md, REVIEWED; r = 3/2) to all r > 1.
Requested label after review: PROVED-mod-cite (WLXZ v1 §§2–6; KV §5; Vanlessen math/0212014 §4).

Notation is RH_p1.md's:
- WLXZ = Wu–Lin–Xu–Zhao, arXiv:1410.3948v1, run at their α = 1 (written α_W below);
- t = n/z² is the rescaled index variable;
- H(t) = Γ(t+1)e^t/(√(2π)t^{t+1/2});
- H_n(z) := H(n/z²).

Fisher–Hartwig exponent. Throughout,

  **a := r − 3/2 > −1/2.**

RH.md writes this as α_FH = (2r − 2 − p)/(2p) at p = 1. Here it is a, to keep it apart from WLXZ's α_W = 1.

## 0. Statement

**Theorem RH₁(r).** Let r > 1 and σ_r := Σ_{k≥1} k^{−r} δ_{1/k}. Let β_N be the squared recurrence coefficients of
σ_r's symmetrization, so that a_m = β_{2m−2} + β_{2m−1} and b_m² = β_{2m−1}β_{2m}, as in RH_p1.md §3. Then

  N β_N = 1 + O(1/N),

and consequently

  n b_n = ½(1 + O(1/n)) = c(1)(1 + O(1/n))  and  a_n/(2b_n) = 1 + O(1/n).

This is the **pointwise Law P for σ_r, with a rate, for every r > 1.** By G1-T and A4 it discharges (T3) and (CL) for
this family. At r = 3/2 (a = 0) it reduces to RH₁.

**Numerics** (`checks/check_p1_general_r.out`, NUMERICAL). The fit Nβ_N − 1 = (k₀ + k₁(−1)^N)/N + O(N⁻²) gives:

| r    | a     | k₀      | k₁      |
|------|-------|---------|---------|
| 1.25 | −0.25 | −0.7500 | +0.7407 |
| 1.5  | 0     | −1.0000 | −0.0001 |
| 2    | 0.5   | −1.4998 | −1.4997 |
| 2.5  | 1     | −1.9992 | −2.9988 |
| 3    | 1.5   | −2.4980 | −4.4972 |

The fits are stable under K-doubling. So the rate O(1/N) is sharp.
- **k₀ = ½ − r** (to fit accuracy; conjecture).
- **k₁ ≈ −3a.** This is a conjecture. The earlier p = 2 fits gave ≈ −4a, which suggests k₁ = −(p+2)a.
- The (−1)^N term is the expected signature of a Fisher–Hartwig point at the band centre (compare Vanlessen
  Theorem 1.1, A₁(n) ∝ λ cos(2n arccos 0)). Vanlessen's fixed-weight constant does not transfer directly, because here
  the weight is n-dependent after rescaling.

The theorem asserts only the O(1/N) rate, not the constants.

## 1. Identification (exact)

- k^{−r} = k^{−3/2}·k^{−a}, and σ_{3/2} = √(2π)H(k)·TC(α_W = 1) (RH_p1.md §1).
- In WLXZ's rescaled symmetric variable the node index is t = n/z². So σ_r's analytic weight is

    w(z)·H_n(z)·(n/z²)^{−a} = n^{−a}·w(z)·H_n(z)·(z²)^{a},

  with (z²)^a principal. This is analytic on ℂ ∖ iℝ and positive on ℝ ∖ {0}.
- The constant n^{−a} multiplies every mass. Monic OPs and β_N are unchanged, and in the RHP it acts by a constant
  diagonal conjugation of Y. **We drop it.**
- Write F(z) := H_n(z)(z²)^a. So σ_r is TC(α_W = 1) with masses multiplied by √(2π)F(node).

## 2. Running WLXZ with weight wF (outside the special discs)

**Lemma W1(r).** Run WLXZ §§3–5 verbatim with weight w·F, exactly as Lemma W1 does with w·H_n:
- R, T, Q, V and the D-functions D, D̃, D̂, E are unchanged (they depend only on n/z² and α_W);
- the residual weights acquire F^{±1};
- the sign structure is unchanged.

*Proof.* This is RH_p1.md §2, steps 1–2, with H_n replaced by F. The extra factor (z²)^a is analytic and nonvanishing
on the same domain ℂ ∖ iℝ, so pole removal (3.13)–(3.18) is unchanged.

On the long saturated pieces, 2 − ε ≤ |z| ≤ k_n ≍ √n. There |(z²)^a| ≤ C n^{|a|}, a polynomial factor. So entries
that are O(e^{−cn}) for σ_{3/2} remain O(e^{−cn}) for σ_r. ∎

**Weight bookkeeping.** By RH_p1.md §2 (iii), the band jump of V on (−2,0) ∪ (0,2) is

  [[0, −m_σ(x)], [1/m_σ(x), 0]],  with m_σ(x) = e^L(4 − x²)·H_n(x)²·|x|^{2a}.

The lens and saturated jumps carry the same factor:
- upper-right entries × F;
- lower-left entries × F^{−1};
- diagonal entries D/D̂ unchanged.

This is (5.3) with w₀, ŵ ↦ w₀F, ŵF. The rule "multiplying the weight by an analytic f ⇔ V ↦ V f^{−σ₃/2} locally" is
used below.

## 3. Global parametrix with the Fisher–Hartwig factor

- **Stirling truncation.** Fix an integer m ≥ max(0, (|a| − 1)/2). Define the entire, nonvanishing function

    Q_m(z) := exp( 2 Σ_{k=1}^{m} B_{2k}/(2k(2k−1)) · (z²/n)^{2k−1} ),

  with Q_0 ≡ 1.
- **Lemma S (DLMF 5.11.1 and §5.11(ii); read, CITATIONS (DLMF)).** Uniformly for |arg(±z)| ≤ π/3,

    κ_n(z) := H_n(z)²/Q_m(z) = 1 + O((|z|²/n)^{2m+1}).

  - *Proof.* log H(t) = Σ_{k=1}^{m} B_{2k}/(2k(2k−1)t^{2k−1}) + R_m(t). This is lnΓ(t+1) = ln t + lnΓ(t) together
    with DLMF 5.11.1, where the leading terms cancel identically.
  - |arg(±z)| ≤ π/3 gives |ph t| ≤ 2π/3. There |R_m(t)| ≤ sec^{2m+2}(π/3)·|B_{2m+2}|/((2m+2)(2m+1)|t|^{2m+1}). ∎
  - Numerically (`checks/check_general_r_parametrix.out` [2]), sup |κ_n − 1|/(|z|²/n)^{2m+1} = 1/6, 1/180, 1/630
    for m = 0, 1, 2, independent of n. These are the leading Stirling coefficients.
- **Szegő functions.** Let Φ(z) := (z + √(z² − 4))/2 (the branch ~ z at ∞) and
  - D_a(z) := (z/Φ(z))^a, with log(z/Φ) → 0 at ∞;
  - D_Q(z) := exp( (√(z²−4)/2π) ∫_{−2}^{2} log Q_m(x) dx / (√(4−x²)(z − x)) ).
- **Lemma G.**
  - (i) D_a and D_Q are analytic and nonvanishing on ℂ ∖ [−2,2], and D_a(∞) = 1.
  - (ii) On (−2,2) ∖ {0}: D_{a,+}D_{a,−} = |x|^{2a} and D_{Q,+}D_{Q,−} = Q_m(x).
  - (iii) D_Q = 1 + O(1/n) uniformly on ℂ, and D_{Q,∞} = 1 + O(1/n).
  - (iv) |D_a(z)|/|z|^a is bounded above and below near 0.
  - (v) D_a is smooth and nonvanishing up to the band near ±2 from each side.
  - *Proof.*
    - (i) z/Φ(z) has no zeros or poles off [−2,2]. Its winding around [−2,2] is 0, since both z and Φ wind once. So
      the log is single-valued.
    - (ii) Φ₊Φ₋ = 1 on the band, so (z/Φ₊)(z/Φ₋) = x². log(z/Φ) is real on ℝ ∖ [−2,2], and z/Φ(±2) = 2 > 0, so the
      sum of boundary logs is continuous and equals log x² at ±2, hence everywhere. D_Q is the standard Szegő
      function. log Q_m = O(x²/n) on the band, which gives (iii).
    - (iv) Φ₊(0) = i, so D_a(z) ∼ (∓iz)^a near 0 in ℂ±.
  - Numerically ([1]): |D₊D₋/|x|^{2a} − 1| ≤ 1e−16 and |D_a|/|z|^a ∈ [0.987, 1.002] for a ∈ {−0.4, 0.5, 1.5, 2.5}.
- **Global parametrix.** Let N be WLXZ's (§5; band weight e^L(4 − x²), i.e. α_W = 1). Put D := D_aD_Q and

    N_r(z) := D_{Q,∞}^{σ₃} N(z) D(z)^{−σ₃}.

  N_r is analytic off [−2,2], N_r → I at ∞, and N_r has the band jump [[0, −m_r], [1/m_r, 0]] with

    m_r(x) := e^L(4 − x²)|x|^{2a}Q_m(x).

  (The jump follows from D₋^{σ₃}[[0,A],[B,0]]D₊^{−σ₃} = [[0, AD₊D₋],[B/(D₊D₋), 0]].)
- **The model mismatch** on the band is m_σ/m_r = κ_n. Outside the discs it is 1 + O(n^{−2m−1}), uniformly on
  [−2+ε, −ε] ∪ [ε, 2−ε], where N_r is bounded. So J_S = N_{r,−}·diag(κ_n^{−1}, κ_n)·N_{r,−}^{−1} = I + O(1/n) there,
  as in RH₁ step 3.
- **Extraction value.** Write D(z) = D_∞(1 + d₁/z + O(z⁻²)). Then

    N_{r,1} = D_{Q,∞}^{σ₃}(N₁ − d₁σ₃)D_{Q,∞}^{−σ₃},

  so (N_{r,1})₁₂(N_{r,1})₂₁ = (N₁)₁₂(N₁)₂₁ = 1 (RH_p1.md §3).

## 4. Airy discs U(±2, ε)

Let P^{(3/2)} be RH₁'s local parametrix at ±2 (RH_p1.md §2, step 4). It has exactly the jumps of V_{σ_{3/2}} in
U(±2, ε), and P^{(3/2)}N^{−1} = I + O(1/n) on ∂U(±2, ε).
- In U(±2, ε), f(z) := (z²)^a is analytic and nonvanishing, since |z| ≈ 2. V_{σ_r} has the jumps of
  V_{σ_{3/2}}·f^{−σ₃/2} (§2 bookkeeping).
- Put g := (fQ_m)^{1/2}/D. Then g₊g₋ = 1 on the band, so N g^{σ₃} has the same band jump as N (an off-diagonal J
  satisfies g₋^{−σ₃}Jg₊^{σ₃} = J when g₊g₋ = 1). Hence A := N g^{σ₃}N^{−1} has no jump in U(±2, ε).
- At ±2, |A| = O(|z∓2|^{−1/2}), since N = O(|z∓2|^{−1/4}) and g is bounded by Lemma G(v). So the singularity is
  removable. A is analytic, with A and A^{−1} bounded uniformly in n.
- Define P_r := D_{Q,∞}^{σ₃}·A·P^{(3/2)}·f^{−σ₃/2}. It has V_{σ_r}'s jumps exactly. On ∂U(±2, ε),

    P_rN_r^{−1} = D_{Q,∞}^{σ₃}·A(I + O(1/n))·N(f^{−1/2}D)^{σ₃}N^{−1}·D_{Q,∞}^{−σ₃}.

  Since f^{−1/2}D = Q_m^{1/2}/g, the middle factor is A^{−1}·N Q_m^{σ₃/2}N^{−1} = A^{−1}(I + O(1/n)). So

    P_rN_r^{−1} = I + O(1/n). ∎

## 5. The origin U(0, ε): a Bessel (Fisher–Hartwig) parametrix

**Contours.**
- Let ψ be WLXZ's equilibrium density (TC, α_W = 1). It is even, with ψ(0) > 0.
- WLXZ's φ satisfies φ = l/2 − g in ℂ± (from (4.29) and (4.34)–(4.35)). So φ₊ + φ₋ = 0 on the band and φ₊ is
  imaginary there.
- With KV's convention φ_KV := −φ (see the dictionary below), set f(z) := iφ_KV(z) − iφ_KV,₊(0) in ℂ₊ and −iφ_KV(z) − iφ_KV,₊(0)
  in ℂ₋ (KV (5.6)). Then f(x) = π∫₀^x ψ and f′(0) = πψ(0) > 0 (KV (5.7)–(5.8)).
- **Parity.** ψ is even, so f is odd and real on ℝ, hence f(iℝ) ⊂ iℝ. So KV's Σ₃ ∪ Σ₇ = iℝ ∩ U(0, ε) exactly, and
  KV's Σ₁ ∪ Σ₅ is the band.
- Inside U(0, ε), deform WLXZ's lips Σ_{l,±}, Σ_{r,±} to KV's Σ₂, Σ₄, Σ₆, Σ₈ = f^{−1}(arg ζ = ±π/4, ±3π/4). For
  small ε these lie in |arg(±z)| ∈ [π/4 − η, π/4 + η]. That is inside WLXZ's admissible sectors (away from both ℝ and
  iℝ), and there Re φ < 0 (WLXZ (4.33); Re φ = −Im f·(1 + o(1))).

**Dictionary WLXZ → KV.**
- WLXZ (6.24)/(5.3) on the band reads [[0, −m], [1/m, 0]], and on the lips [[1, 0], [−e^{2nφ}/m, 1]] plus terms that
  are discarded below. Conjugation by σ₃ gives [[0, m], [−1/m, 0]] and [[1, 0], [m^{−1}e^{−2nφ_KV}, 1]].
- With m = h|x|^{2a}, this is KV (5.1)–(5.2) with weight |x|^{2a} times the analytic factor h. So V ↦ σ₃Vσ₃ (a
  constant conjugation, harmless) puts us in KV's frame.

**Local model jumps.**
- h₀(z) := e^L(4 − z²)Q_m(z) is analytic and nonvanishing in U(0, ε).
- The model jumps are those with m = m_r = h₀|x|^{2a} on the band, and lower-triangular lip jumps with h₀(z²)^{a}.
- The true jumps of V_{σ_r} differ from these in two ways:
  - (J1) multiplicatively, by κ_n on the band (in the off-diagonal entries) and by κ_n^{−1} in the lip lower-left
    entries;
  - (J2) by the discarded diagonal D/D̂ − 1 and upper-right −(ŵF/D̂²)e^{−2nφ̂} lip entries.

**Construction** (KV §5 with Vanlessen's absorption of h; CITATIONS (KV), (Van)):

  P₀(z) := E_n(z)·Ψ_a(n f(z))·W_h(z)^{−σ₃}·e^{−nφ_KV(z)σ₃},  W_h := W·h₀^{1/2},

where:
- W = (−z)^a or z^a by sector (KV (5.9));
- Ψ_a is KV's Bessel model (5.17)–(5.23), which exists for every a > −1/2;
- E_n := E·e^{nφ_KV,₊(0)σ₃}e^{−πiσ₃/4}(1/√2)[[1, i], [i, 1]], with E := P^{(∞)}W_h^{σ₃}e^{±aπiσ₃/2} (and the
  anti-diagonal factor in sectors V–VIII). This is KV (5.26)–(5.30) and Vanlessen (4.47), with P^{(∞)} := σ₃N_rσ₃.

**Lemma B.**
- (i) P₀ has exactly the model jumps in U(0, ε).
- (ii) det P₀ ≡ 1.
- (iii) E_n is analytic in U(0, ε). E_n and E_n^{−1} are bounded uniformly in n.
- (iv) P₀N_r^{−1} = I + O(1/n) uniformly on ∂U(0, ε).

*Proof.*
- (i) This is KV (5.10)–(5.24). The analytic h₀ enters only through W_h, exactly as in Vanlessen's W_{x_ν} (his p. 18:
  "W_{xν}(z) = (1−z)^{α/2}(1+z)^{β/2}h^{1/2}(z) …").
- (ii) This is Vanlessen (4.53).
- (iii) E_n's analyticity is KV p. 19 ("E is analytic in a full neighborhood of U_δ. Here we need the fact that
  D(z)/W(z) and W(z)/D(z) remain bounded as z → 0"). This holds by Lemma G(iv): D/W_h = (D_a/W)(D_Q/h₀^{1/2}), and
  both factors are bounded above and below.
  - Boundedness in n: N_r is uniformly bounded near ∂U(0, ε). |e^{nφ_KV,₊(0)σ₃}| = 1 because φ₊(0) ∈ iℝ. The
    remaining factors are constant.
  - E_n is analytic, so the maximum principle bounds it inside the disc.
- (iv) This uses Vanlessen (4.43)–(4.46) (Ψ = B(I + O(1/ζ))e^{−iζσ₃}C with constant B, C) and KV (5.26). ∎

**Lemma M (mismatch).** Let H := V P₀^{−1} in U(0, ε). On Σ ∩ U(0, ε),

  |J_H − I| ≤ C n^{−1}  (uniformly, including at 0),  and  ‖J_H − I‖_{L¹∩L²∩L^∞} = O(1/n).

*Proof.* J_H = P₀₋ (J_V J_{P₀}^{−1}) P₀₋^{−1}. Write P₀ = E_n Ψ_a(nf) Λ, with Λ := W_h^{−σ₃}e^{−nφ_KVσ₃}, which is
analytic across the lips and the band. Let ζ = nf(z) and ρ = |ζ| ≍ n|z|.

- **(J1), band.** J_V J_P^{−1} = diag(κ_n^{−1}, κ_n), which commutes with Λ₋. So

    J_H − I = E_nΨ₋ M Ψ₋^{−1}E_n^{−1},  M = diag(κ_n^{−1} − 1, κ_n − 1).

  M is a combination of I and σ₃ with coefficients O(|κ_n − 1|).
- **(J1), lips.** J_V J_P^{−1} − I is lower-triangular. After conjugation by Λ₋ it is (κ_n^{−1} − 1)(J_Ψ − I), where
  J_Ψ is Ψ_a's constant lip jump. (Λ conjugates the model lip jump into J_Ψ: that is how Ψ_a was built.) So

    J_H − I = (κ_n^{−1} − 1)·E_n(Ψ₊Ψ₋^{−1} − I)E_n^{−1}.

- **Amplification bound** (from KV (5.21)–(5.22) for ρ ≤ 1, Vanlessen (4.43)–(4.46) for ρ ≥ 1, and det Ψ = 1):

    |Ψσ₃Ψ^{−1}| + |Ψ₊Ψ₋^{−1} − I| ≤ C·(1 + ρ^{−2|a|}(1 + |log ρ|)²).

  - For ρ ≥ 1: Ψ = B(I + O(1/ζ))e^{−iζσ₃}C, where C is diagonal or anti-diagonal, so Cσ₃C^{−1} = ±σ₃ commutes with
    e^{−iζσ₃}. Also Ψ₊Ψ₋^{−1} − I = O(1/ζ).
  - For ρ ≤ 1: the entries are O(ρ^{−|a|}) (log at a = 0) and det = 1.
  - Numerically ([3], a ∈ {−0.4, 0, 0.5, 1.5, 2.5}, ρ ∈ [1e−6, 1e2]): the band amplification is ≈ ρ^{−2|a|}
    (e.g. 4.07e31 at a = 2.5, ρ = 1e−6), with ratio to the weight ≤ 1.3 for ρ ≤ 1e−2 and ≤ 68 at ρ = 1. The lip
    amplification is ≤ C for ρ ≥ 1 and decays like e^{−2ρ sin(π/4)}.
- **Combining with Lemma S.**
  - For ρ ≥ 1: |J_H − I| ≤ C(|z|²/n)^{2m+1} ≤ Cn^{−2m−1}.
  - For ρ ≤ 1, i.e. |z| ≲ 1/n: |J_H − I| ≤ C(|z|²/n)^{2m+1}(n|z|)^{−2|a|}log² ≤ C n^{−2m−1−2|a|}|z|^{4m+2−2|a|}log².
    This is ≤ Cn^{−1} because 4m + 2 ≥ 2|a| (the choice of m).
- **(J2).** The discarded lip terms are O(e^{−cn/|z|²}). By (4.29)–(4.30), φ̂ = φ ∓ (1/z² − 1)πi, and D̃ = D(1 − e^{∓2iθ})
  (4.16) with θ = πn/z² + O(1). On rays with |arg(±z)| ∈ [π/4 − η, π/4 + η], |e^{∓2πin/z²}| = e^{−2πn|sin 2arg z|/|z|²}
  in the relevant half-plane: this is WLXZ's "exponentially small … so long as arg z keeps a distance to ±π/2" made
  explicit.
  - The crude bound |P₀₋||M||P₀₋^{−1}| ≤ poly(n, 1/|z|)·e^{2n|Re φ|}·e^{−cn/|z|²} applies, with |Re φ| ≤ C|z|. It is
    O(n^{−K}) for every K once ε³ < c/(4C).
- **L¹ and L².** Σ ∩ U(0, ε) has length O(1), so these follow from the uniform bound. ∎

**Remark (the role of m).** For |a| ≤ 1, i.e. 1 < r ≤ 5/2, m = 0 works, so Q ≡ 1 and κ_n = H_n². For larger a, the
truncation Q_m is needed: the bare H_n² − 1 = O(|z|²/n) is not small enough against the (n|z|)^{−2a} growth of
Ψ_a near 0. Q_m cannot be replaced by H_n² itself, since H_n has poles on iℝ accumulating at 0 (Γ(t+1) at t = −1, −2, …).

## 6. Behaviour at 0 and identification (Lemma O)

**(Y4)_r.** As z → 0 with δ ≤ |arg(±z)| ≤ π/2 (δ > 0 fixed),

  Y(z) = O([[1, 1 + |z|^{2a}(1 + |log|z||)], [1, 1 + |z|^{2a}(1 + |log|z||)]]),

and the same holds in the sectors |arg(±z)| ≤ δ for R (the pole-free transform).

*Proof.*
- **Sectors away from ℝ.** Y₁₂(z) = Σ_k μ_k π_n(x_k)/(z − x_k) with μ_k ≍ k^{−r} (both signs of nodes), and π_n is
  bounded near 0. For such z, |z − x_k| ≥ c_δ max(|x_k|, |z|) with x_k ≍ k^{−1/2}. So

    |Y₁₂| ≤ C Σ_k k^{−r}/max(k^{−1/2}, |z|) ≤ C(Σ_{k≤|z|^{−2}} k^{−r}|z|^{−1} + Σ_{k>|z|^{−2}} k^{1/2−r}).

  This is O(1 + |z|^{2r−3}) = O(1 + |z|^{2a}), with a log at a = 0 and at r = 3/2. Row 2 is the same with π_{n−1}.
- **Lens sectors.** In Ω_{r,±}, WLXZ (3.12) gives R₁₂ = U₁₂ − U₁₁(w/Π)e^{±iθ}, which is pole-free. By the residue
  identity behind (3.13), the representation

    R₁₂(z) = −(1/2πi)∫_{Γ_z} U₁₁(s)(w(s)/Π(s))e^{±iθ(s)} ds/(s − z)

  holds. Here Γ_z runs from 0 to 2 through the opposite half of the lens sector, where |e^{±iθ}/Π| = |θ′|·O(e^{−2|Im θ|})
  is small; in the opposite half-plane, that factor is O(|θ′|e^{−cn/|s|²}). Its weight factor is O(|s|^{2a}·|s|^{−3}).
  This gives the same bound.

**Ruling (identification of V with the small-norm solution).** WLXZ (and RH₁, inheriting it) identify the transformed Y
with the parametrix solution via (Y4) and Fokas–Its–Kitaev uniqueness (their Theorem 2.3, (2.17)). We do the same, with
(Y4) replaced by (Y4)_r.

At the origin, H := VP₀^{−1} has jumps J_H with |J_H − I| = O(|z|^{4m+2−2|a|}) → 0 at 0 (Lemma M). (Y4)_r together
with KV (5.4)–(5.5) for P₀ gives |H| = O(|z|^{−2|a|−}) in every sector.
- For |a| < 1/4 this is in E² near 0, and the L² theory applies directly.
- For larger |a| we use the KV device, as in their removability argument: the column structure of (Y4)_r matches that of
  KV (5.4)–(5.5) (the second column carries the |z|^{2a}). So the entries of H = V P₀^{−1} are O(|z|^{−1+}) in fact.

*Rigour level.* This is the step at which RH₁ also relied on WLXZ. It is **flagged for the reviewer.** Cost if wrong:
the label becomes PROVED-mod-(Y4)_r-identification, and Lemmas S, G, B, M and the numerics are unaffected.

## 7. Small norm and extraction

- **Final contour.** Σ_S = (Σ ∖ discs) ∪ ∂U(0, ε) ∪ ∂U(±2, ε) ∪ (Σ ∩ U(0, ε)). Inside the Airy discs the residual jump
  is exactly I (§4). Inside U(0, ε) the residual is J_H (Lemma M).
- **Jump sizes:**
  - J_S − I = O(1/n) on the circles (Lemmas B(iv) and §4), on the band pieces (§3), and on Σ ∩ U(0, ε) (Lemma M);
  - J_S − I = O(e^{−cn}) on the lips and saturated pieces outside the discs (Lemma W1(r)).
- The long pieces have length ≍ √n, so ‖J_S − I‖_{L¹∩L²∩L^∞} = O(1/n). Hence S = I + O(1/n) and S₁ = O(1/n), as in
  RH_p1.md W1, step 6.
- **Extraction** (RH_p1.md §3 verbatim, with N_r):

    Nβ_N = (N_{r,1})₁₂(N_{r,1})₂₁ + O(1/N) = 1 + O(1/N).

  The fold gives n b_n = ½(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n). ∎

## 8. What is cited, what is new

- **Cited** (read):
  - WLXZ v1 §§2–6 (via RH₁);
  - KV §5: the Bessel model RHP (5.17)–(5.23), the parametrix form (5.10)/(5.25) and E_n (5.26)–(5.30);
  - Vanlessen math/0212014 §4: the absorption of analytic h into W, E_n (4.47), det = 1 (4.53) and the Ψ asymptotics
    (4.43)–(4.46);
  - DLMF 5.11.
- **New:**
  - the identification F = H_n(z²)^a;
  - Lemma S (Stirling truncation Q_m);
  - Lemma G and N_r;
  - the reduction of the Airy discs to RH₁ via A = Ng^{σ₃}N^{−1};
  - the parity observation Σ₃ ∪ Σ₇ = iℝ;
  - Lemma M (the structured mismatch: diagonal on the band, proportional to J_Ψ − I on the lips, with amplification
    ≤ ρ^{−2|a|});
  - (Y4)_r.
- **Reliance.**
  - As RH₁: WLXZ's O(e^{−cn}) uniformly up to k_n, and their identification step (§6, flagged).
  - KV's Ψ_a needs a > −1/2 ⇔ r > 1, which is exactly the theorem's range (r ≤ 1 gives an infinite measure).
