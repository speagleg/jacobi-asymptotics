# REVIEW_RH1r: Rule R second reading of RH_p1_general.md (Theorem RH₁(r)), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus), on branch plan-11-RH-general-r. It edited no repo file
  except this one.
- **Read:** RH_p1_general.md in full; RH_p1.md; REVIEW_RH1.md; CITATIONS.md. From the sources: WLXZ v1 §2 (2.14)–(2.18),
  §3 (3.1)–(3.24), §4 (4.1)–(4.40), §5 (5.1)–(5.12), §6.2 (6.22)–(6.28) and Remark 6.1; KV §5 (5.1)–(5.30) and p. 19;
  Vanlessen §4.1 (4.6), §4.2 (λ > −1/2), §4.3 (4.42)–(4.53) and Proposition 4.5.
- **Re-runs.** `check_p1_general_r.py` and `check_general_r_parametrix.py` were re-run from the repo root with
  .venv/bin/python. Both outputs are **byte-identical** to the committed .out files.

| Item | Verdict | Findings |
|---|---|---|
| §1 identification F = H_n(z²)^a | ACCEPT | — (t = k at the nodes; n^{−a} is a constant diagonal conjugation) |
| §2 W1(r), weight bookkeeping vs (5.3)/(5.4) | ACCEPT | checked entry by entry: upper-right ∝ weight, lower-left ∝ 1/weight, diagonal D/D̂, D/D̃ weight-free |
| §3 Lemma S, Lemma G, N_r, extraction invariance | ACCEPT WITH FIXES | F9 (DLMF sector quote) |
| §4 Airy discs via A = N g^{σ₃} N^{−1} | ACCEPT WITH FIXES | F5 (wrong exponent for N, conclusion survives) |
| §5 dictionary, parity, Lemma B | ACCEPT WITH FIXES | F6, F8, F9 |
| §5 Lemma M | ACCEPT WITH FIXES | **F2** (strict choice of m), F6, F7 |
| §6 (Y4)_r | ACCEPT WITH FIXES | **F3** (lens representation garbled), F4 (sums swapped) |
| §6 identification ruling | **FIX REQUIRED** | **F1 (blocking)** |
| §7 small norm and extraction | ACCEPT (conditional on F1) | — |
| Numerics | ACCEPT WITH FIXES | F7, F10 |
| Citations | FIX | F11 |

**Verdict: ACCEPT WITH FIXES.** F1 is blocking, so a re-check is needed before the label. Everything else is sound
or needs local rewording.

## What was verified (and holds)

- **§1–§2.** At the nodes, t = n/z² = k, so k^{−r} = k^{−3/2}·t^{−a} = n^{−a}·(TC mass)·√(2π)H_n·(z²)^a. (z²)^a is
  principal, analytic off iℝ, and equals z^{2a} for Re z > 0 and (−z)^{2a} for Re z < 0. So on each side of iℝ it is
  the analytic continuation of |x|^{2a}, which is what KV's ω needs.
- **Weight entries in (5.3)/(5.4).** Every V-jump has its weight in the expected place:
  - band (0,2): [[0, w₀/D̃²], [−D̃²/w₀, 0]];
  - lips: [[D/D̃, (w̃/D̃²)e^{−2nφ̃}], [(DD̃/w₀)e^{2nφ}, 1]];
  - Σ^Δ and (2, k_n): lower-left D̃²/w̃;
  - vertical segments: upper-right w̃/D̃²;
  - the same on the left side with hats.

  So multiplying the weight by F multiplies upper-right entries by F and lower-left entries by F^{−1}, and leaves the
  diagonal unchanged. This is conjugation by F^{σ₃/2}, as claimed.
- **WLXZ φ.** (4.34)–(4.35) give φ̃ = −g + l/2 ± πi/z², and (4.29) gives φ̃ = φ ± πi/z². So φ = l/2 − g in both
  ℂ±. Then φ₊ + φ₋ = l − (g₊ + g₋) = 0 on the band by (4.4). From (4.3), φ₊ is imaginary there.
- **Conformal map.** With φ_KV = −φ, f = iφ_KV − iφ_KV,₊(0) in ℂ₊, so f′ = ig₊′ = πψ on the band (correct). I also
  computed ψ(0) from (4.2) at α = 1: g₊′(x) = i[4 arccos(x/2)/x³ + √(4−x²)/x² − 2π/x³] → −i/3, so **ψ(0) = 1/(3π) > 0**.
  ψ is even.
- **Dictionary.** WLXZ (6.24) gives band [[0, −m₀], [1/m₀, 0]] and lips [[1, 0], [−e^{2nφ}/m₀, 1]]. After σ₃
  conjugation these are KV (5.2) and (5.1), the latter with lower-left +ω^{−1}e^{−2nφ_KV}. Correct.
- **Re φ on the lips.** In ℂ₊, φ = φ₊(0) + if, so Re φ = −Im f exactly; in ℂ₋, Re φ = Im f. Both are negative off
  the axis. (The "(1 + o(1))" in §5 is unnecessary.)
- **(J2) discards.** On Σ_{l,+} (upper-left), Im(1/z²) > 0. So |e^{2iθ}| = e^{−2πn|sin 2arg z|/|z|²}. Then
  D/D̂ − 1 = e^{2iθ}/(1 − e^{2iθ}), by (4.23), and e^{−2nφ̂} = e^{−2nφ}e^{2πin/z²}, by (4.30). The other three lips are
  the same with (4.16) and (4.29).
  - So WLXZ (4.16), (4.23), (4.29), (4.30) **do** give e^{−cn/|z|²} on the lips near 0, with c ≍ |sin 2arg z| ≈ 1 at
    arg ≈ π/4.
  - I checked the Λ/Ψ bookkeeping: Λe₁₂Λ^{−1} carries e^{+2nφ}, which cancels u's e^{−2nφ}, and Ψ contributes
    e^{2n|Re φ|}. So the crude bound poly·e^{2n|Re φ|}e^{−cn/|z|²} is right.
- **Lemma M, structure.**
  - On the band, J_V J_P^{−1} is diagonal and commutes with Λ₋.
  - On a lip, the (J1) part equals Λ₋^{−1}[(κ^{−1} − 1)(J_Ψ − I)]Λ₋, and Ψ₋(J_Ψ − I)Ψ₋^{−1} = Ψ₊Ψ₋^{−1} − I.
  - The amplification exponents follow from KV (5.21)–(5.22). For ρ ≤ 1 they give ρ^{−2|a|}: sectors I, IV, V, VIII
    (adjacent to the band and the lips) are "O(|ζ|^{−α}) in all entries" for α > 0.
  - Combined with Lemma S this gives |J_H − I| ≤ C n^{−1} uniformly whenever 4m + 2 ≥ 2|a|.
- **Lemma S.** log H(t) = Σ_{k≤m} B_{2k}/(2k(2k−1)t^{2k−1}) + R_m(t) follows from lnΓ(t+1) = ln t + lnΓ(t). Also
  |ph t| ≤ 2π/3 ⟺ |arg(±z)| ≤ π/3, and sec(π/3) = 2. The numerical constants 1/6, 1/180, 1/630 equal
  2|B_{2m+2}|/((2m+2)(2m+1)) for m = 0, 1, 2.
- **Lemma G and N_r.**
  - z/Φ has no zeros off [−2,2], and its winding number is 0.
  - z/Φ(±2) = 2, so the boundary-log sum is log x² on both sides of 0.
  - Φ₊(0) = i.
  - The jump of N_r is D₋^{σ₃}[[0,A],[B,0]]D₊^{−σ₃} = [[0, AD₊D₋],[B/(D₊D₋), 0]] (correct), and N_r → I.
  - (N_{r,1})₁₂(N_{r,1})₂₁ = D_∞²(N₁)₁₂·D_∞^{−2}(N₁)₂₁ = 1.
- **§4.**
  - g₊g₋ = (x²)^a Q_m/(|x|^{2a}Q_m) = 1. g has no other cut in U(±2, ε), and N has no jump on (2, 2+ε).
  - The matching factor is N Q_m^{σ₃/2}g^{−σ₃}N^{−1} = (NQ_m^{σ₃/2}N^{−1})·A^{−1}, since the diagonal factors commute.
    So P_rN_r^{−1} = D_∞^{σ₃}A(I + O(1/n))A^{−1}D_∞^{−σ₃} = I + O(1/n).
  - Reusing RH₁'s P^{(3/2)} is legitimate. It has exactly V_{σ_{3/2}}'s jumps, and V_{σ_r}'s jumps in the disc are their
    f^{σ₃/2}-conjugates.
- **Lemma B.**
  - E's analyticity is KV's computation with h₀ absorbed into W, as in Vanlessen (4.6).
  - Removability at 0 needs only D/W_h bounded above and below. It is: D_a/W by Lemma G(iv), and D_Q/h₀^{1/2} because
    4 − z² ≠ 0 near 0.
  - The |e^{nφ₊(0)σ₃}| = 1 argument and the maximum principle are fine. det E = 1 gives E^{−1} bounded.
- **§7 and extraction.**
  - Bounded pieces are O(1/n), and pieces of length ≍ √n are O(n^{|a|}e^{−cn}). So the L¹, L² and L^∞ norms are O(1/n).
  - The added conjugations (constant n^{−a}, σ₃, D_∞^{σ₃}) do not change the off-diagonal product.
  - The fold is as in RH₁.

## Findings

**F1 (blocking): §6 identification for |a| ≥ 1/4 is not proved as written.**

The ruling says the column structure of (Y4)_r "matches KV (5.4)–(5.5) … so the entries of H = VP₀^{−1} are
O(|z|^{−1+}) in fact". There are two problems.

- **(i) The bound does not follow.** Take a > 0 inside the lens. Then V = O(|z|^{−2a}, 1) by columns, and KV (5.5)
  gives P₀ = O(|z|^{−2a}, 1) (KV: "O(|z|^{−2α} 1; |z|^{−2α} 1), as z → 0 from inside the lens"). So P₀^{−1} has rows
  O(1) and O(|z|^{−2a}), and H = V_{·1}(P₀^{−1})_{1·} + V_{·2}(P₀^{−1})_{2·} = O(|z|^{−2a}). For a ≥ 1/2 this is not
  O(|z|^{−1+}). Column structure alone yields no cancellation.
- **(ii) Even O(|z|^{−1+}) would not suffice.** KV's removability device applies to S P^{−1} when that function has
  **no jumps** in the punctured disc. Here J_H ≠ I on the band and the lips through 0 (Lemma M). The small-norm theory
  needs H to be the L² (E²) solution, i.e. O(|z|^{−1/2+δ}) on the contours, or a separate uniqueness argument.

For a ∈ (−1/2, −1/4], H = O(|z|^{2a}) (column 2 is singular in both V and P₀). That is not L² on the rays.

So the step is **strictly worse than RH₁/WLXZ as written**. There, (Y4) gives a log singularity, which is in L², and
Remark 6.1's L² argument applies. It is fixable at the same level with standard tools.

*Fix.* Replace the ruling by:

- **(a) a > 0: un-lensing.**
  - In Ω_{r,±} write V = V^u·L_V, with:
    - V^u := n^{(α−½)σ₃}T E^{σ₃}D̃^{σ₃}, which is O(1) by (Y4)_r for R, since D̃ = 1/H_n is bounded in the lens
      sector;
    - L_V := I + (e^{2nφ}/m_σ(z))e₂₁ (in WLXZ's sign convention). This is the exact analytic lens factor, because
      (ED̃)^{−σ₃}V_∓(ED̃)^{σ₃} has lower-left ±e^{2nφ}D̃²/w₀F.
  - Similarly write P₀ = P^u·L_P. Here P^u is the continuation of P₀ from outside the lens, which is O(1) with
    O(1) inverse by KV (5.5) "outside the lens" and det = 1, and L_P = I + (e^{2nφ}/m_r)e₂₁.
  - Then

      H = V^u (I + e^{2nφ}m_r^{−1}(κ_n^{−1} − 1) e₂₁)(P^u)^{−1} = O(1)·(I + O(|z|^{4m+2−2a}))·O(1) = O(1),

    using |e^{2nφ}| ≤ 1 and Lemma S. Outside the lens, H = O(1)·O(1). So H is bounded (log² at a = 0), and the L²
    theory applies directly.
- **(b) a < 0: a local bounded solution.**
  - Let X solve the jump problem J_H on Σ ∩ U(0, ε) by small norm.
  - X is bounded with bounded inverse near 0, because J_H − I is analytic on each ray and O(|z|^δ) at the vertex
    (δ > 0 by F2), and the cyclic product condition holds automatically. This is standard Hölder theory for Cauchy
    integrals at a junction (Muskhelishvili). Cite it, or prove it in a lemma.
  - HX^{−1} has no jump and is O(|z|^{2a}) with 2a > −1, so it is removable. Hence H = (analytic)·X is bounded.
- Alternatively, (b) can be applied for all a once (a) supplies the a priori bound for a > 0.

With (a) and (b) written out, the identification is at standard RHP rigour (stronger than WLXZ's own §6.2).

**F2 (important): m must satisfy 4m + 2 > 2|a| strictly.**

- With m ≥ (|a| − 1)/2, equality 4m + 2 = 2|a| occurs at |a| = 1, 3, 5, … For example r = 5/2 (a = 1), which is in the
  numerics table, gets m = 0.
- At equality, for ρ ≤ 1, |J_H − I| ≍ (|z|²/n)(n|z|)^{−2} = n^{−3}. That is uniformly O(1/n), so Lemma M survives.
  But it does **not** tend to 0 at z = 0, contrary to §6 ("O(|z|^{4m+2−2|a|}) → 0 at 0"). F1(b) also needs
  δ = 4m + 2 − 2|a| > 0.
- Fix:
  - take m := ⌊(|a| + 1)/2⌋, i.e. m > (|a| − 1)/2;
  - in the Remark, change "|a| ≤ 1 … m = 0 works" to "|a| < 1";
  - state δ := 4m + 2 − 2|a| > 0 explicitly in Lemma M.

**F3 (important): the proof of (Y4)_r in the lens sectors is garbled, though the conclusion is right.**

- For z ∈ Ω_{r,+}, R uses U₋, i.e. the factor e^{−iθ}/sin θ. That factor is small (e^{−2|Im θ|}) in the **same**
  (upper) half-plane, not the opposite one.
- A single contour Γ_z cannot represent R₁₂. The representation must also include:
  - the closing path below ℝ, where one switches to e^{+iθ} (small in ℂ₋). The difference
    U₁₁(wF/Π)(e^{−iθ} − e^{iθ}) = −2iγU₁₁wF is pole-free and gives a continuous Cauchy integral of a density
    O(|s|^{2a});
  - the negative-node sum;
  - the nodes in (2, k_n).
- The "weight factor O(|s|^{2a}·|s|^{−3})" should read |wF| ≍ |s|^{3+2a}, so |wF·θ′| ≍ |s|^{2a}.
- Each piece is O(1 + |z|^{2a}) (log at a = 0) by the max(|s|, |z|) estimate. Fix: rewrite the lens paragraph with
  these three pieces. F1(a) depends on it.

**F4 (minor): the (Y4)_r sector estimate has its two sums swapped.**

- For k ≤ |z|^{−2}, max(k^{−1/2}, |z|) = k^{−1/2}, so the terms are k^{1/2−r}. For k > |z|^{−2}, the terms are
  k^{−r}/|z|.
- As written, the first sum gives |z|^{−1}, which is wrong. The corrected sums give O(1 + |z|^{2a}) as claimed.
- Also, "with a log at a = 0 and at r = 3/2" is redundant: these are the same case.

**F5 (minor): §4 states "N = O(|z∓2|^{−1/4})".**

- At α_W = 1, WLXZ (5.11) has first column ∝ (z²−4)^{1/4−α} = (z²−4)^{−3/4}, and second column ∝
  (z²−4)^{α−3/4} = (z²−4)^{1/4}.
- The conclusion |A| = O(|z∓2|^{−1/2}) still holds. Each term of A = N g^{σ₃}N^{−1} pairs a column of N with the
  matching row of N^{−1}: (−3/4) + (1/4) = −1/2. Fix the wording.

**F6 (minor): §3 and Lemma M write the band mismatch as diag(κ_n^{−1}, κ_n).**

- In fact [[0, −m_σ],[1/m_σ, 0]]·[[0, m_r],[−1/m_r, 0]] = diag(κ_n, κ_n^{−1}). This is immaterial.
- Also, P₀ is defined in KV's frame, so "P₀N_r^{−1}" should read P₀(σ₃N_rσ₃)^{−1}, or the σ₃ should be stated as
  absorbed.

**F7 (minor): the amplification bound and how it is reported.**

- For a ≠ 0 the small-ρ growth is a pure power ρ^{−2|a|}. KV (5.21)–(5.22) have no log, and the K₀-type logs at
  half-integer a are subdominant. The (1 + |log ρ|)² padding is harmless but unnecessary.
- The text "band amplification ≈ ρ^{−2|a|} (e.g. 4.07e31 at a = 2.5, ρ = 1e−6)" hides a constant of about 40: ρ^{−5}
  is 1e30.
- The "ratio ≤ 1.3" is measured against ρ^{−2|a|}(1 + |log ρ|)², not ρ^{−2|a|}.
- check [3] samples only sector I (the band ray at arg 0⁺ and the lip at arg π/4⁻). The other sectors follow by KV's
  symmetry.
- Say all three things. Also, (4.43) is an "as ζ → ∞" statement; for 1 ≤ ρ ≤ R₀ boundedness comes from continuity.

**F8 (minor): the parity observation is correct but not load-bearing.**

- f is odd and real-analytic, so f(iℝ) ⊂ iℝ.
- KV define W (5.9) by sectors of arg f, so their Σ₃, Σ₇ are wherever f^{−1}(iℝ) is.
- V has no jump on iℝ near 0: iℝ lies in Ω_∞, where V = n^{…}QE^{σ₃}D^{σ₃}, and D has no cut there.
- Fix: keep it as a convenience, and drop it from the "New" list or mark it cosmetic.
- Also, the letter f is used for (z²)^a in §4 and for the conformal map in §5. Rename one of them.

**F9 (minor): hypotheses of cited lemmas.**

- **Vanlessen.** §4.1 says "Since h is analytic in U with positive real part". Here h₀ = e^L(4 − z²)Q_m, with e^L
  purely imaginary at α_W = 1, so Re h₀ is not positive. Only an analytic nonvanishing branch of h₀^{1/2} on U(0, ε)
  is used. Say so.
- **DLMF 5.11(ii).** Lemma S needs the sec^{2K}(½ph t) remainder bound on |ph t| ≤ 2π/3. Quote the DLMF sentence
  verbatim, including its sector of validity, in CITATIONS (DLMF). The current quote omits the range.

**F10 (minor): numerics wording.**

- The table and the claims match the .out files exactly (re-run byte-identical): [1] ≤ 1e−16 and [0.987, 1.002];
  [2] 1/6, 1/180, 1/630; [3] as quoted.
- "Stable under K-doubling" is weak evidence. With the Euler–Maclaurin tail to 1e16, K = 1e5 and 2e5 agree to all
  printed digits by construction. A different tend, or a different fit window, would be a real stability test.
- k₁ at r = 1.25 is +0.7407 against −3a = +0.75 (1.2% off). The other cases agree to < 0.1%. The "k₁ ≈ −3a"
  conjecture should note this.
- The script's printed "pred" for k₁ is −4a, which the text rejects. Align the docstring.

**F11 (minor; citation gate): verbatim quotes missing from CITATIONS.md.**

- §6, Lemma M and Lemma B rely on the following, which have no verbatim quote in CITATIONS (KV):
  - KV (5.4)–(5.5) and (5.21)–(5.22) (the behaviour of P and Ψ_α at 0);
  - (5.9) (W);
  - (5.26)–(5.30) (E_n);
  - the p. 19 sentence ("Following the proof of [38, Proposition 4.5], we obtain that E is analytic in a full
    neighborhood of U_δ. Here we need the fact that D(z)/W(z) and W(z)/D(z) remain bounded as z → 0"). The doc has
    this sentence, but CITATIONS does not.
- I checked these against kv.txt; they read as the doc uses them. Add them.
- The Vanlessen quotes in CITATIONS ((4.6), λ > −1/2, (4.42), (4.43), (4.53)) match van.txt.

## Recommended label

- **After F1 (with F2, F3) is fixed and re-checked:** PROVED-mod-cite (WLXZ v1 §§2–6; KV §5; Vanlessen math/0212014 §4;
  DLMF 5.11), with the same WLXZ reliance as RH₁ (uniform O(e^{−cn}) up to k_n).
- **If F1 is not fixed:**
  - PROVED-mod-cite only for |a| < 1/4 (5/4 < r < 7/4), where H = O(|z|^{−2|a|}) is in L² and the L² argument applies
    as in RH₁.
  - PROVED-mod-(Y4)_r-identification for the remaining r > 1.

  Lemmas S, G, B, M, the Airy reduction, the extraction and the numerics are unaffected either way.

## Fixes applied (author, 2026-10-13) — pending re-check

- **F1:** §6 rewritten: (Y4)_r(a), (b); Lemma O1 (i) un-lensing and (ii) a < 0; Lemma X (inverse-jump local solution
  X̃, so G = HX̃); identification by circle integrals, H₋ ∈ L², and L² uniqueness.
- **F2:** m := ⌈|a|/2⌉ (δ ≥ 2); the Remark is updated (m = 0 suffices for |a| < 3/4).
- **F3, F4:** the lens representation is rebuilt (K_±, the switch on the lower ray, negative nodes, nodes in [b, k_n]);
  the sums are corrected.
- **F5:** the N exponents −3/4 and 1/4 are stated.
- **F6:** diag(κ, κ^{−1}); the KV frame is stated; matching is P₀(σ₃N_rσ₃)^{−1}.
- **F7:** the amplification constant (≈ 40), log only at a = 0, sector I only, and continuity for 1 ≤ ρ ≤ R₀.
- **F8:** parity is marked cosmetic; (z²)^a in §4 is renamed q.
- **F9:** the h₀ branch note; the DLMF verbatim quote with n = m + 1.
- **F10:** the numerics caveats; the script docstring.
- **F11:** the KV quotes (5.4), (5.5), (5.9), (5.10), (5.21)–(5.23), (5.26)–(5.30) and p. 19; the Vanlessen
  positive-real-part sentence (van.txt l. 896).
