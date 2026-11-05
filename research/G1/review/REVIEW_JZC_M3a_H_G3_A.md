# Rule R review: JZC M3a, gap G3 (0 < p < 1), reviewer A: JZC_M3a_H_G3.md

Reviewer: independent second reader (Rule R), reviewer **A**. Date: 2026-10-21.
- Target: research/G1/RH/spectral/JZC_M3a_H_G3.md (Lemma 1, Lemma 2, §2 construction and Lemma 3, Prop 4, Cor 5, §§5–7);
  checks/m3a_g3_seam.py/.out, checks/m3a_g3_model.py/.out.
- Context read: AGENTS.md, VERIFICATION_POLICY.md; spectral/JZC_M3a_H.md, JZC_M3a_Hd.md, JZC_M3a_H_G12.md (for L1.1–L2.3,
  reviewed separately in REVIEW_JZC_M3a_H_G12_A.md); papers/paper2/app_outer.tex §A.2 (Lemma seam, Lemma corner and proofs),
  sec_5.tex ((O1)–(O5), eq:angles, eq:Zn), sec_6.tex (eq:binet-bound, eq:binet-small, Lemma normalisation, Lemma szego), app_c.tex;
  RH/CITATIONS.md entries (DLMF), (DLMF-2), (DLMF-5.5/5.11, Plan 54).
- I edited no file except this report. My scripts are in the session scratchpad (`…/scratchpad/review/g3_spot.py`).

## Overall verdict: **ACCEPT WITH FIXES**

The core of the memo is correct. That covers:
- the obstruction to the verbatim route;
- the re-balanced elementary factors with the Möbius factor;
- Lemma 3;
- Lemmas 1 and 2;
- Prop 4.

I re-derived both cancellations of §2 (the Log ζ coefficient and the constant) and confirmed Prop 4 by independent quadrature of
χ_δ. One **MAJOR** fix concerns scope: Cor 5 claims Lemma H-d **(iv)**, the a-priori bound, for p < 1. That is not proved here.
JZC_M3a_H.md §4 lists it as OPEN, and G3's own §7 lists it as remaining (F1). There is also one MINOR proof gap: the polynomial
bound near the seams at ∞, which Lemma 2 needs, is inherited from an unproved sentence of Paper 2 (F2). The other fixes are
MINOR or INFO.

| Item | Verdict | Fixes |
|---|---|---|
| §0 obstruction (lattice densities ∼ (δ/p)Log ζ) | ACCEPT (constant c_± re-derived; numerically 10⁻¹⁹) | F5 |
| Lemma 1 (uniqueness) | ACCEPT WITH FIXES (typo in the exponent) | F3 |
| Lemma 2 (monodromy) | ACCEPT WITH FIXES (statement/proof mismatch in the error term) | F4 |
| Lemma 3 (seam_δ) | ACCEPT WITH FIXES (the (O5) polynomial bound near the seams) | F2, F8 |
| Prop 4 | ACCEPT WITH FIXES (inherits F2; the claim at 0 near the seams) | F2, F6 |
| Cor 5 | ACCEPT WITH FIXES (**MAJOR**: (iv) not proved; also the moments label) | F1, F7 |
| Rule C | ACCEPT WITH FIXES (pointers) | F9 |

## Findings

**F1 (MAJOR; scope; Cor 5, header table row "Cor 5", §0 last sentence).** Cor 5 states "Lemma H-d (i)–(iv) of JZC_M3a_Hd.md §3
holds" for p < 1. H-d (iv) is the a-priori bound: (F7) / Prop apriori for Q♮ with exponent |α|/2, i.e. G12 P2.4 for p < 1.
The proof of Cor 5 gives one sentence for it, "(iv) F_δD_W^{(α)} bounded near 0 (Paper 2 Prop apriori from (O5) near 0, Lemma 3
(iii)) times …". This has two problems.
- **The sentence is false as written.** |D_W^{(α)}(z)| ≍ |z|^{α/2±η} (Lemma szego (vi)), so F_δD_W^{(α)} is not bounded near 0
  when α < 0. The a-priori bound is a column statement that needs the Hurwitz sum bound and the lens-sector bound.
- **The status contradicts the repo.** JZC_M3a_H.md §4, item 2 of "still open", says "H-b′ for p < 1 (Paper 2 App C in the seam
  geometry) … OPEN". G3 §7 says "Inherited from H-d: G2 (App C, Lemma sumbound for the Hurwitz U)" remains. G12 P2.4 is stated
  for p > 1 only.

*Fix (either):*
- (a) **Restrict.** Change Cor 5 to "Lemma H-d (i)–(iii) … holds" and delete the "(iv) …" clause of its proof. Add to §7: "H-d
  (iv) (a-priori bound) for p < 1: open (expected from G12 L2.1 (p-free), L2.2, L2.3 and P2.4 with Lemma 3 (iii) for (O3)–(O5)
  near 0 and Prop 4 at ∞)". Keep the header table row "PROVED for the jump algebra".
- (b) **Prove it.** Add a Prop 4′ that runs G12 P2.4 for p < 1. The checks needed:
  - L2.1 is p-free (only T = n|z|^{−1/p} and spacing 1 are used).
  - In L2.2 with ϑ_lip = 𝗆πp/4, the points t ∈ δ − ℕ₀ lie on |arg s| = πp > ϑ_lip, and (eq:imtheta) holds for
    0 < ±arg z < πp.
  - L2.3 is p-free.
  - P2.4(i) uses (O5) near 0 for F_δ and (O3)–(O4) for H_n^δ (Lemma 3 (iii)).
  - P2.4(ii) at ∞ uses Prop 4.

  If (b) is chosen, update JZC_M3a_H.md §2 (H-b′ row) and §4 accordingly.

**F2 (MINOR, proof gap with a routine fix; Lemma 3 (iii) "the polynomial bound at ∞", used by Lemma 2 in Prop 4).** Lemma 2 needs
|F_δ|^{±1} ≤ C|z|^N on a **full** neighbourhood of ∞, including points near the seams Σ^s_±. Lemma 3 (iii) takes this from Paper
2's proof of Lemma seam (iv). That proof says only "In S_in ∩ {|z| ≥ n^p+δ′} … D, B_in, K and e^χ are bounded above and below by
powers of |z|" (app_outer.tex, last lines of (O5)). For e^χ this is not justified:
- Lemma corner (ii) gives |χ − χ(0)| ≤ C(1 + log|z|)², which is not a polynomial bound on e^χ.
- Lemma corner (ii) and dominated convergence apply only at distance ≥ τ|z| from the seams.
- Lemma corner (iii) is a statement near 0, not near ∞.

The claim is true, and it is the exact analogue of G12 P1.4(c)'s window argument.

*Fix:* add to Lemma 3 (ii) and (iii):
- "(ii′) For |ζ| ≥ 1, |χ_±^δ′(ζ)| ≤ C_n/|ζ|. Proof: dt/dζ = −t/(pζ); d/dt[j_δ + Log(1 − e^{−2πi(t−δ)})] = O(1/|t|) for |t| ≤ 2
  (L1.2(c) type: j_δ′ = (δ+½)/t + O(1 + |ln|t||)) and O(|t|^{−2}) for |t| ≥ 2; the elementary terms have derivatives O(1/|ζ|)."
- "(iii′) For fixed n, χ_δ is bounded on {|z| ≥ 2} uniformly up to the seams. Proof: for z near Σ^s_+ with nearest point z*,
  r = |z*|, split the Σ^s_+ integral at |ζ − z*| ≤ r/2. On the window, χ_+(ζ) = χ_+(z*) + O(|ζ − z*|C_n/r) by (ii′). The
  constant part times a logarithm with end points at comparable distances is bounded, since χ_+(z*) → 0. The Lipschitz part is
  O(C_n). Off the window, |ζ − z| ≥ (|ζ| + r)/C, and χ_+(ζ)/ζ is integrable. Σ^s_− is at distance ≥ |z|/C. Hence
  |F_δ|^{±1} ≤ C_n|z|^{N_n} for |z| ≥ X₁ + δ′."

Also record the Paper 2 sentence for math-pursuits FIXES (via a human; AGENTS.md Rule 1). This is a wording gap like the binetcut
one (G12 §4 item 6), and Paper 2's result is unaffected.

**F3 (MINOR/typo; Lemma 1 proof).** "At ∞, |G²| ≤ C|z|^{2N}". From |F_i|^{±1} ≤ C|z|^N, |G| ≤ C|z|^{2N}, so |G²| ≤ C|z|^{4N}.
*Fix:* "|G²|^{±1} ≤ C|z|^{4N}". Also add "and the same for G^{−2}". This is needed for "a polynomial without zeros", and it
holds because |F_i|^{∓1} also is bounded. The rest of the proof is correct:
- G² rather than G is used on 𝒵_n, which is right, since only F̃² is analytic on 𝒵_n by (O2);
- the extension across (e^{pc₀}n^p, ∞) needs no node there, which is why the outer radius exceeds X₁;
- removability at 0 is correct;
- G² constant implies G constant, since ℂ∖[0, ∞) is connected.

**F4 (MINOR; Lemma 2, statement vs proof).** The statement has error 1 + O(|z|^{−1/p}) + O(|z|^{−1}). The proof gives only
h = O(|z|^{−min(1,1/p)}log|z|). *Fix (either):*
- add the log to the statement, "1 + O(|z|^{−min(1,1/p)}log|z|) + O(|z|^{−1})"; or
- prove the log-free bound uniformly up to (R, ∞). Split h at x ∈ [|z|/2, 2|z|] and write t(x) = t(Re z) + O(|x − Re z|·
  n|z|^{−1−1/p}). The constant part gives t(Re z) times a bounded logarithm, and the rest is O(n|z|^{−1/p}). The pieces
  x < |z|/2 and x > 2|z| give O(n|z|^{−1}·∫_R^{|z|}x^{−1/p}dx + n|z|^{−1/p}).

Only "1 + o(1)" is used downstream, so this is cosmetic. Everything else in the proof is correct:
- the jump bookkeeping e^{2πit}e^{−2πiδ}·e^{2πiδ}·e^{−2πit} = 1 on (R, ∞);
- zero-free plus polynomially bounded gives G = Cz^m(1 + O(1/z)), uniformly in direction;
- z^m(−z)^δ = (−1)^m(−z)^{δ+m} for m ∈ ℤ with principal powers.

**F5 (MINOR; §0 last sentence, "F♮ … satisfies Paper 2's (O1)–(O5) with the lattice θ").** This overstates. F♮ satisfies (O1)
with the lattice θ, and (O5) at ∞. But F̃♮ = F̃_δ(−z)^{−δ} jumps across (0, 4c), so (O2) fails for F♮. (O2)–(O4) and (O5) near 0
hold for F_δ with κ_δ, which is exactly how H-d §3 and G12 P1.4 use them. *Fix:* "Hence F♮ = F_δ(−z)^{−δ} satisfies (O1) with
the lattice θ and (O5) at ∞, while (O2)–(O4) and (O5) near 0 hold for F_δ with κ_δ (Lemma 3 (iii)), as in G12 P1.4; and Lemma
H-d (i)–(iii) holds …" (see F1).

**F6 (MINOR; Prop 4, the claim at 0).** "F_δ(z) → (4c)^{−1/2}e^{χ_δ(0)} as z → 0 off the lens" uses χ → χ(0). Lemma corner (ii)
gives this only at distance ≥ τ₀|z| from the seams; near the seams Lemma corner (iii) gives boundedness only. The limit does
hold there too, by Lindelöf's theorem: F_δ is bounded, analytic across the seams, and has the same limit on two rays bracketing
the seam. But the memo does not say so, and (O5) needs only the boundedness. *Fix:* either add "(near the seams: boundedness by
Lemma corner (iii), and the limit by Lindelöf's theorem on the sector between two rays at distance τ₀|z| from Σ^s_±)", or
restrict the claim to dist(z, Σ^s_±) ≥ τ₀|z|, which is where the numerics (E) test it.

**F7 (MINOR; Cor 5 band factor, header table).** "Band-factor moments CONDITIONAL (Hurwitz's formula)" and "m_k(δ) =
ζ(−kp, 1+δ)/(kn^{kp})" are out of date relative to JZC_M3a_H.md §3.2. That section states the moments unconditionally as the
Fourier sums m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ), and makes the ζ(−kp, a) form Remark 3.3 (NOT QUOTED). *Fix:* in the table
and in Cor 5, "moments = the Fourier sums of H.md §3.2 (unconditional, via E_plt1 Lemma F.1 (ii)); their identification with
ζ(−kp, 1+δ)/(kn^{kp}) is H.md Remark 3.3 (NOT QUOTED)". Keep the existing caveat that F.1 (iv) was not re-derived for complex ℓ_±.

**F8 (MINOR; setting, header).** "s > 1" should be "1 < s < 1 + 2p". This is Paper 2's standing assumption, α ∈ (−1, 1), which
the frame (Lemma normalisation, Lemma szego, and Cor L2 once F1 (b) is done) uses. *Fix:* replace "s > 1" by "1 < s < 1 + 2p".

**F9 (MINOR; Rule C.2 bookkeeping).** The external inputs are (eq:binet-bound) at φ = π/2, applied at u = t − δ, and the
reflection formula (only for the "cosmetic" second form of λ_δ). Both are quoted correctly from Paper 2. The memo does not point
to RH/CITATIONS.md. *Fix:* add "Also used in: JZC_M3a_H_G3" lines:
- (DLMF) §5.11: 5.11.1 + §5.11(ii), n = 1, at u = t − δ = |δ| − i|t| on Σ^s_+, |ph u| < π/2, |u| ≥ |t| ≥ 1;
- (DLMF-5.5/5.11, Plan 54): 5.5.3 at z = −δ ∈ (0, 1).

Sokhotski–Plemelj in Lemma 2 is used as in Paper 2: real-analytic density, interior points of (R, ∞).

**I1 (INFO; Cor 5's phase identity).** Cor 5 repeats H-d's "[(−z)^{−δ}D_{x^{2δ}}] = (4c/Υ)^δe^{±iπδ}". G12 §5 (4) calls this
branch-ambiguous. It is in fact exact with principal branches in ℂ_± (arg Υ ∈ (0, π) in ℂ₊; see REVIEW_JZC_M3a_H_G12_A F3), so
no change is needed there beyond F1.

**I2 (INFO; numerics precision).** At p = 0.3, |ζ| = 10⁻⁶, the seam density needs about 25 extra digits in j_δ, since
|t| ≈ 4·10²⁰. My first dps-25 evaluation gave a spurious |χ_+| ≈ 3·10⁻⁴. At dps 70 I get |χ_+|/|ζ| = 0.633, consistent with
Lemma 3 (ii). The memo's §5 notes "extra digits in j_δ for |t| ≫ 1", and its p = 0.3 values are consistent with mine.

## Re-derivations

- **§2, the Log ζ coefficient.** (δ+½)/p [from −j_δ, Log t = ln n − (1/p)Log ζ] + (ϖ_δ + 1) − 1 − (½+δ). With
  ϖ_δ = (1 − 1/p)(½+δ) this is 0.
- **§2, the constant.**
  - Inputs: −j_δ → −(δ+½)Log t − LnΓ(−δ) + ½ln 2π; I re-derived this via r_δ = (δ+½)Log t + (−δ−½)ln(−δ) + δ + O(|t|log) and
    the definition of j at −δ.
  - Next, −ln(2|sin πδ|) − i(π/2 + πδ) − ln λ_δ, and +(½+δ)(ln 2πn + iπ), using arg(−ζ/2πn) = πp/2 − π.
  - The imaginary parts cancel, and the real part is −LnΓ(−δ) + (1+δ)ln 2π − ln(2|sin πδ|) − ln λ_δ = 0.
  - λ_δ = Γ(1+δ)(2π)^δ by reflection at −δ.
  - At δ = 0, λ₀ = 1 and ϖ₀ = ϖ, so B_in^0 = (1+z)^ϖ: Paper 2.
- **§0 constant.** c_+ = −δ ln n + lnΓ(1+δ) − iπδ, with Log ζ coefficient δ/p. Re-derived.
- **Lemma 3 (iii) side conditions.**
  - S_in ⊂ {Re z > 0}, so |1 + λ_δz| ≥ 1, and the zero −1 and the pole −1/λ_δ of B_in^δ lie in S_out.
  - min_{r∈[0,1]}|1 − re^{2πiδ}| > 0 for δ ∈ (−1, 0): it equals |sin 2πδ| if cos 2πδ > 0, and 1 otherwise. So s_δ > 0.
  - All constants of Lemma corner (i) remain n-free: for |t| < 1, |log|t|| ≤ (1/p)log|ζ| (since |ζ| > n^p), and the Möbius
    terms are n-free.
- **Prop 4.** In S_out, B_out^δK = (2πn)^{−½−δ}(−z)^{½+δ}(−z)^{−½}(1 + O(1/z)) with consistent principal branches. Then
  m = 0 and C_F = (2πn)^{−½−δ} from one ray, and Lemma 2 extends this to all directions, given F2.

## Independent verification (commands and outputs)

`…/scratchpad/venv/bin/python -B …/scratchpad/review/g3_spot.py` (mpmath, dps 25, n = 4, c = 1; my own quadrature of
(eq:chi) along both seams; not the repo's code):
- λ_δ, both forms agree to 3·10⁻²⁶ (p = 0.6 with δ = −0.5 and −0.25; p = 0.3 with δ = −0.8).
- Densities: |χ_+^δ(10¹⁰e^{iπp/2})| ≈ 4·10⁻¹¹ to 7·10⁻¹⁰ and |χ_+^δ(10²⁰e^{iπp/2})| ≈ 10⁻²⁰, so the decay is O(1/|ζ|) as
  claimed.
- Lattice-B density at |ζ| = 10²⁰ minus (δ/p)Log ζ − c_+: ≤ 1.2·10⁻¹⁹.
- Prop 4: F_δ(z)(−z)^{−δ}(2πn)^{½+δ} − 1 at |z| = 10⁸ and 10¹²:

  | (p, δ) | S_out ray (arg z = π/2), 10⁸ | 10¹² | S_in ray (arg z = πp/4), 10⁸ | 10¹² |
  |---|---|---|---|---|
  | (0.6, −0.5) | 3.1·10⁻⁹ | 3.1·10⁻¹³ | 3.1·10⁻⁹ | 3.1·10⁻¹³ |
  | (0.6, −0.25) | 1.6·10⁻⁸ | 1.6·10⁻¹² | 1.6·10⁻⁸ | 1.6·10⁻¹² |
  | (0.3, −0.8) | 2.7·10⁻⁸ | 2.7·10⁻¹² | 2.7·10⁻⁸ | 2.7·10⁻¹² |

  The rate is exactly O(1/|z|), with the same constant (2πn)^{−½−δ} in both sectors.
- Small ζ at dps 70 (p = 0.3, δ = −0.8): |χ_+|/|ζ| = 0.633, 0.633, 0.526 at |ζ| = 10⁻⁶, 10⁻³, 0.5.
- Repo outputs: m3a_g3_seam.out "ALL 81 CHECKS PASSED", m3a_g3_model.out "ALL 25 CHECKS PASSED". Both are newer than their .py
  files, and `sha256sum -c` against MANIFEST.sha256 gives OK. I did not re-run the repo scripts (slow), and I did not re-check
  the m3a_g3_model data provenance beyond the memo's statement (Rule X: the fits are of the actual Hurwitz measures).

Novelty: not assessed (outside remit). No RH claim is made or needed.
