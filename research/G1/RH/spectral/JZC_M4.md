# JZC M4: the second-order layer — the natural index N = n + α/2 − Z(0) (Plan JZC, milestone M4; first results)

Status (2026-10-21): NOT REVIEWED. Labels per VERIFICATION_POLICY.md.

| # | Statement | Label |
|---|---|---|
| Identity N.1 | E2's d₂(p, s) = p(p+1)δ_N²/2 + f₂(p, α), δ_N := α/2 + ½, f₂ := −(p+2)α²/8 + (p+1)/12, α := (s−1)/p − 1 | PROVED (algebra) |
| Prop N.2 | Bessel-zero (Lommel) measures, p = s = 2 (α = −½): n²b_n/c = (n/N)²·(1 − 1/(4N²))^{−1/2} exactly, N = n + μ/2 = n + α/2 − Z(0) | PROVED (from the Lommel closed form, SPEC §3.10) |
| Conj S1-N | n^pb_n/c = (n/N)^p·F_{p,α}(N; Z), N := n + α/2 − Z(0). F has no 1/N term; its integer layer is even in 1/N; its N⁻² coefficient is f₂; the spectral terms (zeta layer, poles) appear as functions of N | CONJECTURE (NUMERICAL: m4_natural_index.out, 7 lattices; S1′, rule H, S1⁗ as instances) |

## 1. The identity

E2 Theorem E2.1: d₂ = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12. With α = (s−1)/p − 1, s − 1 = p(α + 1) and s − 1 − p = pα.
- The first term is (p+1)p(α+1)²/8 = p(p+1)δ_N²/2, with δ_N = (α+1)/2.
- The second term is −(p+2)α²/8.
So **d₂ = p(p+1)δ_N²/2 + f₂**. The first term is exactly the n⁻² term produced by the index shift n → n + δ_N in (n/N)^p:
(1 + δ/n)^{−p} = 1 − pδ/n + p(p+1)δ²/(2n²) − …

The 1/n term of the same shift is −pδ_N = −p(α + 1)/2 = −(s − 1)/2 = d₁. So **the lattice's d₁ and the (s − 1)² part of d₂ are a
single index shift by δ_N = α/2 + ½**, and f₂ is what is left.

## 2. The natural index

For a regular spectrum, d₁ = −pα/2 + pZ(0) (S1) = −p(α/2 − Z(0)). So the shift is N = n + α/2 − Z(0). It has two parts:
- **α/2: the hard-edge shift.** The band [0, 4c] has a hard edge at 0 with Jacobi exponent α (the model weight z^α). As for
  Laguerre (b_n = √(n(n + α)) = N√(1 − α²/(4N²)), N = n + α/2) and Jacobi (rational in 2n + α + β + 1) polynomials, the hard
  edge shifts the natural index by α/2. The soft edge (Airy) is symmetric and contributes no shift.
- **−Z(0): the spectral shift.** The regularised count of the nodes (S1), i.e. the Hurwitz offset δ in rule H.

**Proposition N.2 (Bessel zeros; exact).** The Lommel closed form (SPEC §3.10) is n²b_n/c = 4n²/((2n + μ)√((2n + μ)² − 1)). With
N := n + μ/2 this is (n/N)²·(1 − 1/(4N²))^{−1/2}. For these measures p = 2 and s = 2, so α = −½, and Z(0) = −μ/2 − ¼ (SPEC §3.9).
Hence α/2 − Z(0) = μ/2: the natural index. The bare function F = (1 − 1/(4N²))^{−1/2} = 1 + 1/(8N²) + 3/(128N⁴) + … has
- no 1/N term;
- only even powers;
- N⁻² coefficient 1/8 = f₂(2, −½) = −4·(1/4)/8 + 3/12. ∎
(At μ = ½, the lattice λ = (πk)², this gives d₂ = 3·(1/16) + 1/8 = 5/16 = E3's d₂(2, 2), as noted in SPEC §3.9.)

## 3. Conjecture S1-N and evidence

**Conjecture S1-N.** For a regular spectrum, n^pb_n/c = (n/N)^p·F_{p,α}(N; Z) with N = n + α/2 − Z(0), where:
- the integer layer of F is 1 + f₂N⁻² + f₄N⁻⁴ + …: even, with no N⁻¹ and no N⁻³ term;
- f₂ = −(p+2)α²/8 + (p+1)/12;
- the spectral terms are those of S1′/S1″ written in N: ε_jN^{−1−jp}, pole terms pRW(q)π cot(πq)N^{−1−pq};
- the Jacobian-tilt term of S1⁗ (SPEC §3.15) is a separate first-order density effect.

Its instances:
- **S1′ (I)** (the integer layer is the lattice's at n + δ) and **rule H** (both layers at n + δ, with Hurwitz ζ). These are
  S1-N with Z(0) = ζ(0, a) = ½ − a, i.e. −Z(0) = ½ + δ.
- **S1⁗'s shift term** (the pole term evaluated at n + δ_eff, δ_eff = (s − 1)/(2p)). This is S1-N's δ_N for the lattice, since
  (s − 1)/(2p) = (α + 1)/2. The identification there came from data; here it is structural.

**New test: no N⁻³ term** (`checks/m4_natural_index.py`, `checks/m4_natural_index.out`). Plan 62 lattice coefficients are mapped
to F(N) = (N/n)^p·n^pb_n/c. The script subtracts 1 + f₂N⁻² + Σε_jN^{−1−jp} and fits the remainder in powers of 1/N, with
nuisance exponents (4, 5, 2 + jp, 3 + jp). Results:

| p | s | α | N⁻¹ residual | N⁻² residual | N⁻³ residual (spread) |
|---|---|---|---|---|---|
| 1.5 | 2 | −⅓ | −4·10⁻¹¹ | +1.5·10⁻⁷ | −3.0·10⁻⁴ (2·10⁻⁴) |
| 1.5 | 3 | +⅓ | +5·10⁻¹¹ | −1.6·10⁻⁷ | +3.2·10⁻⁴ (2·10⁻⁴) |
| 1.25 | 2 | −0.2 | +4·10⁻¹¹ | −1.5·10⁻⁷ | +5.2·10⁻⁴ (4·10⁻⁴) |
| 2.5 | 2 | −0.6 | −2·10⁻¹¹ | +5·10⁻⁸ | −6·10⁻⁵ (6·10⁻⁵) |
| 3 | 2 | −⅔ | +2·10⁻¹² | −4·10⁻⁹ | +2.3·10⁻⁶ (5·10⁻⁷) |
| 1.5 | 2.5 | 0 | +2·10⁻¹² | −7·10⁻⁹ | +1.3·10⁻⁵ (2·10⁻⁵) |
| 2 | 3 | 0 | −2·10⁻¹³ | +4·10⁻¹⁰ | −3·10⁻⁷ (3·10⁻⁷) |

- The N⁻¹ and N⁻² rows re-confirm E2's d₁ and d₂ (PROVED) in natural form.
- The N⁻³ row is the new content. It is zero to ≤ 5·10⁻⁴, against lattice d₃ values of order 0.1–1 (for example −0.267 at
  p = 1.5, s = 2). At α = 0 it is ≤ 10⁻⁵.
- *Open.* The residual at p = 1.5 flips sign with α (−3.0·10⁻⁴ at α = −⅓, +3.2·10⁻⁴ at α = +⅓, both about 1.5 spreads), and p = 3
  shows 2·10⁻⁶ at about 4 spreads. This could be a small odd-in-α N⁻³ coefficient, or an unmodelled nuisance term. Higher-
  precision runs would settle it.

**What S1-N buys.** It halves the unknowns of the integer layer, since only the even f_{2k}(p, α) remain. It unifies d₁, rule H and
the S1⁗ shift. And it gives M3/M4 a precise target: the Riemann–Hilbert analysis should produce exactly the shift α/2 (hard-edge
Bessel parametrix of order α) and −Z(0) (the Γ normalisation of the interpolation), with the soft edge contributing only even
terms.

## 4. Open

- Derive N from the Riemann–Hilbert data. Candidates: the hard-edge parametrix gives α/2; the outer scalar j_δ (Bernoulli
  polynomials B_{k+1}(−δ), SPEC §3.1) gives −Z(0).
- f₄(p, α), and a closed form for F_{p,α} (p = 2, α = −½: (1 − 1/(4N²))^{−1/2}).
- The possible small odd-in-α N⁻³ term.
- How the Jacobian-tilt term of S1⁗ fits the natural form.
