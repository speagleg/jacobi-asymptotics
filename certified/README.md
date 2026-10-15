# Certified numerics (Plan 58)

Every check here is **CERTIFIED** in the sense of [VERIFICATION_POLICY.md](../VERIFICATION_POLICY.md) (Rule N): Arb
ball arithmetic (python-flint 0.9.0) over every operation, exact rational inputs, and no truncation that is not
bounded inside Arb itself. Everything that is *not* certified is marked as such below and in the scripts. A finite
check never certifies an asymptotic or "for all n" statement; those remain theorems (or not) in `research/` and the
papers.

The suite lives at the top level, not under `papers/*/checks`, because it serves README.md, THEOREMS.md and both
papers, and because those `checks/` folders hold the NUMERICAL (mpmath) versions of the same comparisons, which are
kept unchanged. The library code is in `src/jacobi_asym/certify/` (`constants.py`, `moments.py`, `report.py`).

Run from the repository root (each script prints `midpoint +/- radius` enclosures, one `[PASS]/[FAIL]` line per
check, and a final `RESULT:` line; the stored `.out` files are the outputs, reproduced byte-for-byte by
`pytest -m slow tests/test_certified.py`):

```bash
.venv/bin/python -I certified/c01_constants.py       > certified/c01_constants.out       # ~3 s
.venv/bin/python -I certified/c02_lommel.py          > certified/c02_lommel.out          # ~8 s (N = 300)
.venv/bin/python -I certified/c03_zeta_hankel.py     > certified/c03_zeta_hankel.out     # ~3 s (n <= 30)
.venv/bin/python -I certified/c04_monien_density.py  > certified/c04_monien_density.out  # ~1 s
.venv/bin/python -m pytest tests/test_certified.py   # fast subset (~3 s); add -m slow for the full scripts
```

## What a PASS means

Three kinds of check occur, and they certify different things.

| Kind | PASS means (rigorously) |
|---|---|
| **rounding** (`rounds to`, `truncated`) | every point of the enclosure lies within half a unit of the last printed digit (resp. in the truncation interval) of the quoted decimal. This certifies the quoted digits. |
| **overlap** of two enclosures (closed form vs computation, two closed forms) | \|x − y\| ≤ rad(x) + rad(y). This is a certified *bound on the difference* (radii are printed; typically 10⁻⁷⁰ to 10⁻²⁰⁰⁰), not a proof that x = y. |
| **[exact]** | exact symbolic algebra (sympy) on closed forms: an identity or polynomial inequality valid for all n (or p) at once. |

## Certified claims

### c01 — Law-P constants (Arb, 256 bits)
Source: README, THEOREMS.md notation, Paper 1 Table `tab:constants` and §5 text, `research/G1/RH/zeta`.

* c(1) = ½ and c(2) = π²/16: enclosures of c(1) contain ½ and of c(2) overlap π²/16 (radius < 10⁻⁷⁶); **[exact]**
  sympy `gammasimp` proves both identities, and c(½) = √6/6, u_s(½) = 3/8.
  c(2) = 0.616850275068084913677155687492 ± 4.4·10⁻⁷⁷.
* Paper 1 Table `tab:constants`, all 21 entries c(p), u_s = 2I(p)/π, κ_p = 3p/2 + log c(p) for
  p ∈ {½, 1, 3/2, 2, 3, 4, 6}: each printed value is the correctly **rounded** value (rounding check). Also
  2I(p)/π overlaps (4c(p))^(−1/p) for each p. (The Monte Carlo column is NUMERICAL and not checked.)
* Paper 1 §5 text "3a/2 + log c(a) equals 0.806853…, 2.516871…, 4.127795…, 5.696954…": rounding check passes.
  Note: these are *rounded*, not truncated (κ₁ = 0.80685281…, κ₃ = 4.12779464…), although "…" often signals
  truncation.
* κ₂ = 3 + log(π²/16) = 2.516871049459019110617926 ± 1.1·10⁻⁷⁶ (overlap).
* Smooth-ζ constant: κ = −2(log(π/2) − (1 − log 2)) = −0.289459771698800348286854702706 ± 2.2·10⁻⁷⁷.
  The identity κ = −2(log c)′(2) is checked two independent ways: (log c)′(p) from the hand-differentiated closed form
  log(π/2) − log I(p) + p⁻¹(ψ(1/p+½) − ψ(1/p+1)), and from Taylor-mode differentiation of log c(2 + t) in `arb_series`
  (no hand derivative); both give 0.144729885849400174143427351353 ± 4.3·10⁻⁷⁷ and overlap −κ/2.
  ψ(3/2) − ψ(1) overlaps 2 − 2 log 2. Quoted decimals certified: −0.28946 (README, rounded), −0.289459… (RH_zeta_close,
  truncated), −0.2894597717 (check_z_kappa.out, rounded), 0.14473 (REVIEW_RHzeta, rounded).

### c02 — Lommel closed form for σ₂,₂ (Paper 2, Remark `rem:pure-lommel`)
* Moments m_j = ζ(2j + 2), j < 600: Arb's rigorous `zeta`, each overlapping the exact Bernoulli formula
  ζ(2m) = (−1)^{m+1}B_{2m}(2π)^{2m}/(2(2m)!).
* a_n and b_n² for 0 ≤ n < 300 by the Chebyshev algorithm in ball arithmetic (16384 bits, chosen automatically by
  precision doubling until every coefficient has ≥ 128 relative bits). Every ball contains the exact coefficient of
  σ₂,₂: the moments are exact values, so there is no truncation; ill-conditioning can only widen balls.
* Result: for every 1 ≤ n < 300 the computed balls overlap a_n = 2π²/((4n+1)(4n+5)) and
  b_n² = π⁴/((4n+1)²(4n−1)(4n+3)), with **certified max relative difference ≤ 4.5·10⁻²⁰⁹² (a_n) and ≤ 2.3·10⁻²⁰⁹⁷
  (b_n²)**; a₀ overlaps π²/15 and B₀ = m₀ overlaps π²/6. This replaces the mpmath check
  (`papers/paper2/checks/lommel_check.py`, n ≤ 9, 90 digits, NUMERICAL) by a certified one for n < 300. It does not
  prove the closed form for all n; that is the derivation in the Remark.
* Independent route for n ≤ 12: b_n² = D_{n+1}D_{n−1}/D_n² with `arb_mat.det`, overlapping the Chebyshev values.
* **[exact]** from the closed form, for all n ≥ 1: n²b_n/c(2) = 1 − 1/(2n) + O(n⁻²); a_n/(2b_n) = 1 − 1/n + O(n⁻²)
  (1/n coefficient −p/2 = −1); a_n/(2b_n) < 1 because (4n+5)² − (4n−1)(4n+3) = 32n + 28 > 0; n²b_n < c(2) because
  (4n+1)²(4n−1)(4n+3) − (4n)⁴ = 256m³ + 800m² + 816m + 269 with n = m + 1.

### c03 — Hankel determinants of zeta values (Paper 1, Corollary `cor:zeta`, Remark `rem:bs`)
* H_n(a, b) = det_{1≤i,j≤n} ζ(a(i+j)+b) for n ≤ 30 and (a, b) ∈ {(1,0), (1,1), (3/2,0), (2,−2), (2,0), (2,2), (3,0)}:
  certified enclosures with ≥ 100 relative bits, all certified positive (e.g. H₃₀(1,0) =
  1.053157850466278084626429·10⁻¹⁰⁵⁵ ± 4.5·10⁻¹¹⁰⁶; values for n ∈ {1, 2, 3, 5, 8, 12, 30} are in the .out file).
* Baricz–Štampach closed forms at a = 2, b ∈ {−2, 0, 2} (as quoted in Paper 1 Remark `rem:bs`; exact rational × power
  of π): overlap with the direct determinants for every 1 ≤ n ≤ 30, certified max relative difference ≤ 1.6·10⁻¹⁵⁸,
  2.2·10⁻¹⁵⁵, 3.2·10⁻¹⁵² respectively. (Upgrade of the NUMERICAL `papers/paper1/checks/bs_check.py`, n ≤ 8.)
* **Not certified (illustration only):** the comparison of (log H_n + a n² log n)/n² with κ_a. The printed values are
  enclosures, but no finite n certifies the o(n²) limit, which is a theorem of Paper 1 (Corollary `cor:zeta`).

### c04 — Monien's p = 1 density vs ρ* (Paper 1, Remark on a = 1; `papers/paper1/checks/monien_check.py`)
* At the 11 sample points x ∈ {1/10, …, 10⁴} (exact rationals; branch of min(1, 1/(2x)) decided exactly), Monien's
  density 2/π(atan(1/r) − r/(2x)) overlaps ρ*(x) = I_{min(1,1/(2x))}(3/2, 1/2): certified max |difference| ≤ 4.5·10⁻⁷⁴.
* **Not certified:** the total-mass check ∫ρ* = 1 of `monien_check.py` (improper integral; would need a rigorous
  quadrature with a tail bound), and the identity for all x (proved in Paper 1, not here).

## Not certified, and why
* Paper 2 Table `tab:numerics` (`papers/paper2/checks/table2.py`), `check_p55_strip.py`, G1/G3′ numerics: they use
  truncated measures with 10⁵–10⁶ atoms plus a quadrature of the continuous tail in long double; certifying them
  would need a rigorous bound for the effect of the tail on b_n (a perturbation bound for the Jacobi matrix), which is
  not available in the toolkit. They stay NUMERICAL.
* Paper 1 Monte Carlo column of `tab:constants`, `positivity_sanity.py` (oscillatory improper integral) and
  `airy_check.py` (pointwise check of an analytic construction): NUMERICAL.
* Fitted asymptotic coefficients (e.g. the 10⁶⁰ fit κ ≈ −0.289472, d₁, e₁): NUMERICAL by nature.
* Asymptotic laws (Law P, the averaged law, RH_ζ): theorems, not numbers; nothing here certifies them.
