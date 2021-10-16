import pytest

from algorithms import mean


@pytest.mark.parametrize(
    "tlist,tmean",
    [
        [[1, 2, 3], 2.0],
        [[8, 4, 6, 3, 9], 6.0],
    ],
)
def test_mean(tlist, tmean):
    assert mean(tlist) == tmean
