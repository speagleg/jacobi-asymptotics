# REVIEW_RH: Rule R second reading of research/G1/RH (HEAD aa044c4), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus). It edited no repo files.
- **Probes** (session scratchpad): sign_phitilde.py, testA_probe.py, testA_p1.py, testB_more.py.

**Overall: ACCEPT WITH FIXES at the PROOF SKETCH label only. §6.2–6.3 (D/E, global parametrix) REJECTED as stated for
p = 2.**

| Item | Verdict | Required fixes |
|---|---|---|
| §1 symmetrization, fold | ACCEPT WITH FIX | "equivalent" is proved only in one direction (γ ⇒ Law P); add the converse or say "implied by" |
| Lemma 1.1 | ACCEPT WITH FIX | p = 2 silently switches to the odd branch θ = πN/z; fix one convention and restate §§2–3 |
| r* | ACCEPT | (r*^{2/p} = 2π/B(½+1/p, ½), independently checked) |
| Lemma 2.1 | ACCEPT | — |
| Lemma 2.2 | ACCEPT WITH FIX | strictness on the saturated part needs a one-line argument (G2 B*(ii) gives only ≥) |
| Lemma 2.3 | ACCEPT WITH FIXES | **sign: φ̃ = φ ± iθ/N in ℂ±** (not ∓); **missing condition Re φ̃ > 0 (and Re φ̂ > 0) on band-lens contours** |
| §5, α | ACCEPT | state KV's hypothesis α > −½ ⟺ r > 1 |
| Lemma 3.1 | ACCEPT | "verified end to end" overstated: one node, one region, no left half, no △ region checked |
| §6.2–6.3 | **REJECT for p = 2** | (i) E's principal (z² − r*²)^{1/4} cuts along iℝ; (ii) D is one-sided, so a two-sided construction is needed for odd t = N/z; (iii) the data contradict the stated normalization: \|T₁₁(iy)\|·N is stable, i.e. N^{−1} = the square of the predicted N^{−1/2}, which suggests a two-sided D; p = 1 gives N^{−1/2}, as in WLXZ; (iv) w₀ ∝ (r*² − x²)^{1/p} |
| §6.4 | ACCEPT WITH FIX | p = 2 uses the non-principal odd branch; state it |
| Lemma 4.1 | ACCEPT WITH FIX | analyticity of the √ prefactor (substitution u = x² + (r*² − x²)v) |
| Lemma 4.2 | ACCEPT | sign of the conformal map relative to KV |
| Prop 4.3 | structure identified only | KV has no analytic h (absorbing it is Vanlessen [38]/KMVV, unread); the perturbation from the actual local jumps (upper-triangular entries, D̃² vs D̂²) must be estimated under conjugation by P ~ \|z\|^{−2α} |
| Lemma 4.4 | ACCEPT (NUMERICAL) | — |
| Lemma 5.1 | ACCEPT | — |
| Test A | ACCEPT WITH FIXES | it detects a wrong r*, but cannot see l or any normalization; "exponential precision" overstated |
| Test B | **Rule X: circular** | it re-parametrizes the Phase 0 data, and no RH prediction of k₀, k₁ is compared. Fits suggest k₀ = 1 − r − p/2 and k₁ ≈ −4α (p = 2) |
| Citations | FIX | WLXZ §§3–6 quotes must be recorded; BKMM excludes band edges and must not be cited for Airy |

**Missing for PROVED (beyond the document's list):**
1. behaviour at z = 0 (uniqueness; removability under P⁻¹);
2. a two-sided D and E for p = 2, and a re-derived global parametrix and w₀ that explain test A's N^{−1};
3. the θ branch convention for p = 2;
4. Re φ̃ > 0 and Re φ̂ > 0 on band-lens contours;
5. the origin perturbation estimate to the KV model, uniform up to 0 under conjugation by P;
6. Airy discs: √-factor analyticity, the E singularity, the vertical segments;
7. top end: the vertical segment at k_N, and small norm on a contour of length ~N^q (L¹/L² bounds);
8. the extraction formula, with k₀ and k₁ predicted analytically;
9. p = 1 runs of checks 3a, 3b, 5. (Probe: p = 1 test A converges at O(1/N), with N^{−1/2} scaling as in WLXZ.)

**Note.** RH_proof.md (commit 4f13aea, written after this HEAD) inherits issues 2, 3, 4 and the φ̃ sign. Its PROVED-mod-cite
label is withdrawn.

(Condensed from the reviewer's full report, as relayed in the session.)
