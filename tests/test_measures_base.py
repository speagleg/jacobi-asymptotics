import numpy as np
import pytest
from jacobi_asym.measures import DiscreteMeasure, pure_power


def test_from_atoms_sorts_descending_and_keeps_pairs():
    mu = DiscreteMeasure.from_atoms([0.1, 0.5, 0.3], [1.0, 2.0, 3.0])
    assert np.array_equal(mu.atoms, [0.5, 0.3, 0.1])
    assert np.array_equal(mu.weights, [2.0, 3.0, 1.0])
    assert mu.N == 3 and mu.mass == pytest.approx(6.0)


def test_rejects_duplicates_nonpositive_nonfinite_mismatch():
    with pytest.raises(ValueError, match="duplicate"):
        DiscreteMeasure.from_atoms([0.5, 0.5], [1.0, 1.0])
    with pytest.raises(ValueError, match="positive"):
        DiscreteMeasure.from_atoms([0.5, -0.1], [1.0, 1.0])
    with pytest.raises(ValueError, match="positive"):
        DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 0.0])
    with pytest.raises(ValueError, match="finite"):
        DiscreteMeasure.from_atoms([0.5, np.nan], [1.0, 1.0])
    with pytest.raises(ValueError, match="length"):
        DiscreteMeasure.from_atoms([0.5, 0.1], [1.0])


def test_direct_constructor_rejects_unsorted():
    with pytest.raises(ValueError, match="decreasing"):
        DiscreteMeasure(np.array([0.1, 0.5]), np.array([1.0, 1.0]))


def test_arrays_are_read_only():
    mu = DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 1.0])
    with pytest.raises(ValueError):
        mu.atoms[0] = 9.0


def test_tail_is_merged():
    mu = DiscreteMeasure.from_atoms([0.5, 0.25], [1.0, 1.0], tail=([0.01, 0.02], [0.1, 0.1]))
    assert np.array_equal(mu.atoms, [0.5, 0.25, 0.02, 0.01])


def test_pure_power():
    mu = pure_power(2, 4, s=3, C=2.0)
    assert np.allclose(mu.atoms, 2.0 * np.arange(1, 5) ** -2.0)
    assert np.allclose(mu.weights, np.arange(1, 5) ** -3.0)
    mu2 = pure_power(1, 3)
    assert np.array_equal(mu2.weights, mu2.atoms)
