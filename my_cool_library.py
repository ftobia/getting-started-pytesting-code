
class Bunch(object):

    def __getitem__(self, name):
        return self.__dict__[name]

    def __setitem__(self, name, item):
        self.__dict__[name] = item

    def __delitem__(self, name):
        del self.__dict__[name]

    def __contains__(self, item):
        return item in self.__dict__

    def to_dict(self):
        return dict(self.__dict__)

