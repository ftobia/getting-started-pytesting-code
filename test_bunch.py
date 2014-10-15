import pytest

from my_cool_library import Bunch


@pytest.fixture
def bunch():
    return Bunch()


@pytest.fixture
def full_bunch(bunch):
    bunch.foo = 'foo'
    bunch.bar = 'bar'
    bunch.baz = 'baz'
    return bunch


def test_contains(full_bunch):
    assert 'foo' in full_bunch


def test_hasattr(full_bunch):
    assert hasattr(full_bunch, 'foo')


def test_setattr(bunch):
    setattr(bunch, 'hello', 'world')
    assert bunch.hello == 'world'


def test_to_dict(full_bunch):
    assert full_bunch.to_dict() == {
        'foo': 'foo',
        'bar': 'bar',
        'baz': 'baz',
    }


def test_to_dict_makes_a_copy(full_bunch):
    d = full_bunch.to_dict()
    d['monkey'] = 'butler'
    assert 'monkey' in d
    assert 'monkey' not in full_bunch


class TestGetAndSet(object):

    def test_attr_attr(self, bunch):
        bunch.one = 'one'
        assert bunch.one == 'one'

    def test_attr_item(self, bunch):
        bunch.two = 'two'
        assert bunch['two'] == 'two'

    def test_item_attr(self, bunch):
        bunch['three'] = 'three'
        assert bunch.three == 'three'

    def test_item_item(self, bunch):
        bunch['four'] = 'four'
        assert bunch['four'] == 'four'


class TestDelete(object):

    def test_del_attr(self, full_bunch):
        del full_bunch.foo
        assert not hasattr(full_bunch, 'foo')

    def test_del_item(self, full_bunch):
        del full_bunch['bar']
        assert 'bar' not in full_bunch
