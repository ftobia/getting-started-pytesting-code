import pytest

from my_cool_library import chunkify


@pytest.mark.parametrize('input,chunk_size,expected', [
    ([], 0, []),
    ([], 1, []),
    ([], 10, []),
    ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
    ([1, 2, 3, 4, 5], 3, [[1, 2, 3], [4, 5]]),
    ('ABC', 1, [['A'], ['B'], ['C']]),
    ('ABCDE', 2, [['A', 'B'], ['C', 'D'], ['E']]),
    (xrange(5), 2, [[0, 1], [2, 3], [4]]),
])
def test_chunkify(input, chunk_size, expected):
    assert chunkify(input, chunk_size) == expected


def test_chunk_size_cannot_be_negative():
    with pytest.raises(ValueError) as cm:
        chunkify([1, 2, 3], -2)
    assert str(cm.value) == 'Chunk size cannot be negative'
