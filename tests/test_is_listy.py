import pytest

from my_cool_library import is_listy


@pytest.fixture(params=[
    [], [1],
    (), (1,),
    set(), {1},
    frozenset(), frozenset([1]),
    xrange(0), xrange(2),
    bytearray(), bytearray(1),
    buffer(''), buffer('x'),
])
def listy_thing(request):
    return request.param


@pytest.fixture(params=[
    u'', u'foo',
    b'', b'foo',
    {}, {'a': 'b'},
    iter([]), (i for i in range(2)),
    0, 1,
    False, True,
    object, object()
])
def non_listy_thing(request):
    return request.param


def test_is_listy(listy_thing):
    assert is_listy(listy_thing) is True


def test_is_not_listy(non_listy_thing):
    assert is_listy(non_listy_thing) is False
