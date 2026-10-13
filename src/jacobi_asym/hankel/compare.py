"""Difference-ratio tool for Lemmas H4/H5 (item 11 PROOF.md section 7b)."""


def difference_ratio(f, g, a: float, b: float) -> float:
    if not a < b:
        raise ValueError("need a < b")
    return float((f(a) - f(b)) / (g(a) - g(b)))
