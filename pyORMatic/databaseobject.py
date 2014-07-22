from collections.abc import MutableMapping
from copy import *

__author__ = 'Alex'


class DatabaseObject(MutableMapping):
    def __init__(self, table, **kwargs):
        self.__table = table
        self.__columns = deepcopy( )

    def __getattr__(self, item):
        self.__columns = self.__table.get_fields(self.__columns)
        if item in self.__columns:
            return self.__columns[item]
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        self.__columns[key] = value

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __setitem__(self, key, value):
        return self.__setattr__(key, value)

    def __delitem__(self, key):
        del self.__columns[key]

    def __iter__(self):
        return NotImplemented

    def __len__(self):
        return len(self.__columns)

    def __eq__(self, other):
        if isinstance(other, DatabaseObject):
            return self.__table == other.__table \
               and self.__columns == other.__columns
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.__table) ^ hash(self.__columns)
