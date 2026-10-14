# G1 citations

Citation gate (AGENTS.md rule 4): read on 2026-10-13 from the arXiv PDFs.

## (BKMM) Baik–Kriecherbauer–McLaughlin–Miller — READ (abstract and §1)

arXiv:math/0212149v1, "Uniform asymptotics for polynomials orthogonal with respect to a general class of discrete
weights and universality results for associated ensembles: announcement of results".

> "We compute the pointwise asymptotics of orthogonal polynomials with respect to a general class of pure point
> measures supported on finite sets as both the number of nodes of the measure and also the degree of the orthogonal
> polynomials become large. … In particular, we consider nodes that are not necessarily equally spaced. The asymptotic
> results are given with error bound for all points in the complex plane except for a finite union of discs of
> arbitrarily small but fixed radii."
>
> (§1) "Let N ∈ ℕ be fixed, and consider N distinct real nodes x_{N,0} < x_{N,1} < ⋯ < x_{N,N−1} to be given."

> (§1.3.1) "The nodes lie in a bounded open interval (a, b) and are distributed with a density ρ0(x). … The density
> function ρ0(x) is real analytic in a complex neighborhood of the closed interval [a, b]"; and (§1.3.2) "VN(x) may be
> taken to be a real analytic function defined in a neighborhood G of the closed interval [a, b]".
>
> (§1.4.2) "Definition 3 (Saturated regions). A saturated region Γ is an open subinterval of [a, b] of maximal length
> in which dμ^c_min/dx ≡ ρ0(x)/c, and thus the minimizer realizes the upper constraint."

**Relevance.** This is the Riemann–Hilbert route to pointwise asymptotics for discrete orthogonal polynomials,
including saturated regions, but on finite node sets in a bounded interval with real-analytic node density and
potential. It does not cover infinitely many nodes accumulating at 0.

## (WLXZ) Wu–Lin–Xu–Zhao — READ (abstract and §1)

arXiv:1410.3948v1, "Uniform asymptotics for discrete orthogonal polynomials on infinite nodes with an accumulation
point".

> "In this paper, we develop the Riemann-Hilbert method to study the asymptotics of discrete orthogonal polynomials on
> infinite nodes with an accumulation point. To illustrate our method, we consider the Tricomi-Carlitz polynomials
> f_n^{(α)}(z) where α is a positive parameter."

**Relevance.** Infinite nodes accumulating at 0 are handled, but only for one explicit family (Tricomi–Carlitz; nodes
±(k+α)^{−1/2}, i.e. p = 1 in the squared variable), whose recurrence coefficients are explicit anyway. This is the
only accumulating case found in the literature read.

## (Simon) Simon 2004 — READ (§1 notation, §3 in full: Theorems 3.1, 3.2, Proposition 3.3, Lemma 3.4 and proofs)

B. Simon, "Ratio asymptotics and weak asymptotic measures for orthogonal polynomials on the real line", J. Approx.
Theory 126 (2004); preprint mp_arc 03-341 (file `simon_ratios.TEX`, AMS-LaTeX source, fetched from
web.ma.utexas.edu/mp_arc on 2026-10-14 and read; Plan 42). Quotes are verbatim from the TeX source, modulo TeX markup ({\rm{(}} → "(", equation labels dropped).

Conventions (§1; note: Simon's b is the **diagonal** and a the **off-diagonal** parameter, the reverse of G1's a_n, b_n,
and his indices start at 1):

> "we suppose henceforth that $d\mu$ is nontrivial, that is, not supported on a finite set, and we will also assume
> throughout that $\mu(\bbR)=1$."
>
> "$x P_n(x) = P_{n+1}(x) + b_{n+1} P_n (x) + a_n^2 P_{n-1}(x)$" (1.1); "$x p_n(x) =a_{n+1} p_{n+1}(x) + b_{n+1} p_n(x)
> + a_n p_{n-1}(x)$" (1.3).

§3:

> "Let $d\mu_n =p_n^2 \, d\mu$. In this section, the main theorems are
>
> Theorem 3.1. Suppose $b_n\to b \qquad a_{2n}\to a \qquad a_{2n+1}\to c$ (3.1) for $b\in\bbR$, $a,c\in [0,\infty)$.
> Then as $n\to\infty$, $d\mu_n$ has a weak limit $d\rho_{b;a,c} (x)$, and for every $\ell$, $\int x^\ell\, d\mu_n \to
> \int x^\ell\, d\rho_{b;a,c}(x)$ (3.2)"
>
> "Theorem 3.2. Suppose for $\ell=1,2$, and $4$, $\lim_{n\to\infty} \, \int x^\ell d\mu_n =A_\ell$. Then for some
> $a,b,c$, (3.1) holds. Moreover, $A_1, A_2, A_4$ determine $b$, $a+c$, $\abs{a-c}$ (i.e., they determine $b$ and the
> unordered pair $(a,c)$)."
>
> (Remark 2 after Thm 3.1) "We will see below that $d\rho_{b';a',c'}=d\rho_{b;a,c}$ implies $b'=b$ and either $a'=a$,
> $c'=c$, or $a'=c$, $c'=a$."
>
> "Proposition 3.3. $\int x^\ell \, d\mu_n =\sum_{\rho\in Q_{n,\ell}} W(\rho)$ where $Q_{n,\ell}$ is the set of all
> paths of length $\ell$ with $\rho_0 =\rho_\ell =n$."
>
> (proof of Thm 3.2) "$\lim_{n\to\infty}\, a_{n+1}^2 + a_n^2 =A_2$ (3.10) … $\lim_{n\to\infty}\, a_{n+2}^2 a_{n+1}^2
> + a_n^2 a_{n-1}^2 = A_4 - A_2^2$ (3.11) … $\abs{a^2 -c^2} = \sqrt{3A_2^2 - 2A_4}$ (3.13)" (after reducing to
> $A_1 = 0$, $b_n \to 0$).

**Hypotheses vs use.** Simon's theorems are for a *fixed* measure (fixed Jacobi parameters) and unscaled μ_n. G1 §3.13
(Lemma RL) needs the n^p-rescaled ν_n, whose moments are those of the n-dependent matrix n^pJ, so Theorems 3.1–3.2 are
**not applied**; Lemma RL re-proves the scaled statement by the same path-sum argument (Proposition 3.3 is re-proved
there as (M)). The citation is for attribution only. In G1's notation, Simon's (3.10)–(3.11) are §3.13's (∗) and (∗∗),
and the arcsine target is the case 3A_2² − 2A_4 = 0 (centred A_2 = 2β², A_4 = 6β⁴).
