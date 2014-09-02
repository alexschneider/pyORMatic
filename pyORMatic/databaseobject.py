from collections.abc import MutableMapping
from copy import *

__author__ = 'Alex'


class DatabaseObject(MutableMapping):
    def __init__(self, *args, **kwargs):
        self.__columns = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, item):
        return self.__columns[item]

    def __setitem__(self, key, value):
        self.__columns[key] = value

    def __delitem__(self, key):
        del self.__columns[key]

    def __iter__(self):
        return NotImplemented

    def __len__(self):
        return len(self.__columns)

    def __eq__(self, other):
        if isinstance(other, DatabaseObject):
            return self.__columns == other.__columns # Comparing two identical rows from two different tables may be a problem here
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.__columns)

    def __repr__(self):
        return str(self.__columns)
