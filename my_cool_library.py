
class Bunch(object):

    def __getitem__(self, name):
        return self.__dict__[name]

    def __setitem__(self, name, item):
        self.__dict__[name] = item

    def __delitem__(self, name):
        del self.__dict__[name]

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def to_dict(self):
        return dict(self.__dict__)


def chunkify(iterable, chunk_size):
    return_value = []
    acc = []
    for item in iterable:
        acc.append(item)
        if len(acc) == chunk_size:
            return_value.append(acc)
            acc = []
    if acc:
        return_value.append(acc)
    return return_value


def is_listy(x):
    from collections import Sized, Iterable, Mapping
    return (isinstance(x, Sized) and
            isinstance(x, Iterable) and
            not isinstance(x, (Mapping, type(b''), type(u''))))
