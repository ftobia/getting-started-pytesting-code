import pytest

from my_cool_library import chunkify


@pytest.mark.parametrize('input,chunk_size,expected', [
    pytest.mark.empty(([], 0, [])),
    pytest.mark.empty(([], 1, [])),
    pytest.mark.empty(([], 10, [])),
    ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
    ([1, 2, 3, 4, 5], 3, [[1, 2, 3], [4, 5]]),
    ('ABC', 1, [['A'], ['B'], ['C']]),
    ('ABCDE', 2, [['A', 'B'], ['C', 'D'], ['E']]),
    (xrange(5), 2, [[0, 1], [2, 3], [4]]),
])
def test_chunkify(input, chunk_size, expected):
    assert chunkify(input, chunk_size) == expected


@pytest.mark.foo
@pytest.mark.empty
def test_nothing_in_particular():
    # This test doesn't actually test anything :(
    pass
