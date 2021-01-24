import pytest

from sample_package import fibonacci


@pytest.mark.parametrize("num,value", [(1, 1), (3, 3), (9, 55), (11, 144)])
def test_fibonacci(num, value):
    assert fibonacci(num) == value
