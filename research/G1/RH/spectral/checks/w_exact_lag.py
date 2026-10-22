"""w_exact helpers: exact large-n expansions for the Laguerre weight x^alpha e^{-x} with a branched tilt x^rho (JZC_W_exact.md §2).

Laguerre facts used (all elementary; each is re-checked numerically in w_exact_laguerre.py, Rule N):
  (L1) S_n := int_0^inf x^{alpha+rho} e^{-x} L_n^alpha(x)^2 dx = sum_{k=0}^n Gamma(lam+k+1)/k! [(-rho)_{n-k}/(n-k)!]^2, lam = alpha + rho;
       h_n = Gamma(n+alpha+1)/n!; m_n := <x^rho>_n = S_n/h_n. (Checked against direct quadrature and against rho = 1: 2n+alpha+1.)
  (L2) S_n = [x^n] Gamma(lam+1)(1-x)^{-lam-1} 2F1(-rho,-rho;1;x)  (Cauchy product of the two generating functions).
  (L3) Gauss connection formula (DLMF 15.8.4 / 15.10.21 with a = b = -rho, c = 1, c-a-b = 1+2rho):
       2F1(-rho,-rho;1;x) = C(2rho,rho) 2F1(-rho,-rho;-2rho;1-x) + (1-x)^{1+2rho} Gamma(-1-2rho)/Gamma(-rho)^2 2F1(1+rho,1+rho;2+2rho;1-x).
       NOT QUOTED from a read source here (Rule C): the formula is instead checked numerically below at several points.
  (L4) Singularity analysis (transfer [x^n](1-x)^{-g} = Gamma(n+g)/(Gamma(g) n!), termwise, the only dominant singularity being x = 1):
       NOT QUOTED (Flajolet-Odlyzko); the resulting two-series expansion of m_n is checked numerically to high precision.
Result: m_n = m_n^A + m_n^B with
  m_n^A = C(2rho,rho) sum_i (-rho)_i^2/((-2rho)_i i!) (lam+1-i)_i Gamma(n+alpha+rho+1-i)/Gamma(n+alpha+1)        (analytic in rho;
          poles at 2rho in {0,...,i-1})
  m_n^B = Phi sum_i (1+rho)_i^2/((2+2rho)_i i!) (alpha-rho-i)_i Gamma(n+alpha-rho-i)/Gamma(n+alpha+1),
          Phi = Phi_alpha(rho) := Gamma(-1-2rho)Gamma(alpha+rho+1)/(Gamma(-rho)^2 Gamma(alpha-rho))                   (branched).
Phi_nu(rho) is also the regularised Mellin moment int_0^inf y^rho J_nu(2 sqrt y)^2 dy (Weber-Schafheitlin; checked numerically)."""
import sympy as sp

al, rho, u = sp.symbols('alpha rho u')          # u = 1/N


def rf(x, k):
    r = sp.Integer(1)
    for j in range(k): r = r*(x + j)
    return r


def gamma_ratio_series(a, b, K):
    """Gamma(N+a)/Gamma(N+b) = N^{a-b} sum_{k<=K} r_k N^{-k}; from DLMF 5.11.8 (log Gamma(z+h) with Bernoulli polynomials)
    differenced; returns [r_0..r_K] (exact, symbolic). Checked numerically in w_exact_laguerre.py."""
    L = [sp.Integer(0)] + [(-1)**(k + 1)*(sp.bernoulli(k + 1, a) - sp.bernoulli(k + 1, b))/(k*(k + 1)) for k in range(1, K + 1)]
    E = [sp.Integer(1)]
    for k in range(1, K + 1):
        E.append(sp.expand(sum(j*L[j]*E[k - j] for j in range(1, k + 1))/k))
    return E


def ser_mul(A, B, K):
    return [sp.expand(sum(A[i]*B[k - i] for i in range(k + 1))) for k in range(K + 1)]


def sqrt_factor(K):
    """sqrt(1 - alpha^2 u^2/4) as coefficients in u"""
    s = sp.series(sp.sqrt(1 - al**2*u**2/4), u, 0, K + 1).removeO()
    return [s.coeff(u, k) for k in range(K + 1)]


def response_A(K, ladder=None):
    """natural-form analytic response G^A(N) = sum_k G_k N^{-k} of the Laguerre model (p = -1) to the normalised tilt
    exp(-mu z^rho / C(2rho,rho)), z = x/n:  G = (N/n)^{-(rho+1)} d/dmu (b_n/n), N = n + alpha/2.
    = -(1/2) sqrt(1 - alpha^2/(4N^2)) N^{-rho} (m_n - m_{n-1})/C(2rho,rho), restricted to m^A.
    ladder: optional replacement of the coefficient list coef_i (for controls)."""
    out = [sp.Integer(0)]*(K + 1)
    for i in range(K):
        coef = rf(-rho, i)**2/(rf(-2*rho, i)*sp.factorial(i))*rf(al + rho + 1 - i, i) if ladder is None else ladder(i)
        if coef == 0: continue
        R = gamma_ratio_series(al/2 + rho - i, al/2 + 1, K)       # Gamma(N+a)/Gamma(N+b), N^{rho-i-1}
        # term: -(1/2) coef (rho - i) u^{i+1} R(u)
        for k in range(K + 1 - (i + 1)):
            out[k + i + 1] += -sp.Rational(1, 2)*coef*(rho - i)*R[k]
    return [sp.factor(sp.together(x)) for x in ser_mul(out, sqrt_factor(K), K)]


def response_B(K):
    """branched response G^B(N) = N^{-2rho-2} sum_k GB_k N^{-k}, GB_k = PhiC * rational_k, PhiC := Phi_alpha(rho)/C(2rho,rho).
    Returns the rational parts [rat_k]."""
    out = [sp.Integer(0)]*(K + 1)
    for i in range(K + 1):
        coef = rf(1 + rho, i)**2/(rf(2 + 2*rho, i)*sp.factorial(i))*rf(al - rho - i, i)
        R = gamma_ratio_series(al/2 - rho - i - 1, al/2 + 1, K)    # N^{-rho-i-2}
        for k in range(K + 1 - i):
            out[k + i] += -sp.Rational(1, 2)*coef*(-rho - i - 1)*R[k]
    return [sp.factor(sp.together(x)) for x in ser_mul(out, sqrt_factor(K), K)]


def PhiC_residue(r0):
    """residue at rho = r0 (half-integer >= 1/2) of PhiC(rho) = Gamma(-1-2rho)Gamma(alpha+rho+1)Gamma(1+rho)^2/(Gamma(-rho)^2
    Gamma(alpha-rho)Gamma(1+2rho)); simple pole from Gamma(-1-2rho) at -1-2r0 = -m: Res_rho = (-1)^{m+1}/(2 m!)."""
    m = int(2*r0 + 1)
    return sp.factor((-1)**(m + 1)/(2*sp.factorial(m))*rf(al - r0, m)*sp.gamma(1 + r0)**2/(sp.gamma(-r0)**2*sp.gamma(1 + 2*r0)))
