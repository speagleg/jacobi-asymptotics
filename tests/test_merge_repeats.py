import numpy as np
import pytest
from jacobi_asym.measures.lfun import merge_repeats, model_zeros


def test_merge_repeats_sets_pairs_equal_and_preserves_order():
    g = model_zeros(10)
    h = merge_repeats(g, [2, 5])
    assert h[3] == g[2] and h[6] == g[5]
    assert np.all(np.diff(h) >= 0)
    assert np.array_equal(np.delete(h, [3, 6]), np.delete(g, [3, 6]))


def test_merge_repeats_rejects_adjacent_overlap():
    with pytest.raises(ValueError):
        merge_repeats(model_zeros(10), [2, 3])
