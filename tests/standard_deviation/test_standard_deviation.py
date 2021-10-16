import pytest

from algorithms import standard_deviation


@pytest.mark.parametrize(
    "tlist,tdeviation",
    [
        [[76, 84, 69, 92, 58, 89, 73, 97, 85, 77], 11.709],
        [[82, 93, 98, 89, 88], 5.958],
        [[43, 69, 51, 62, 49, 39, 47, 63, 59, 52], 9.571],
    ],
)
def test_standard_deviation(tlist, tdeviation):
    assert standard_deviation(tlist) == tdeviation
