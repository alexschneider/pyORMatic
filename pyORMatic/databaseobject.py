from collections.abc import MutableMapping
from copy import *

__author__ = 'Alex'


class DatabaseObject(MutableMapping):
    def __init__(self, table, **kwargs):
        self._table = table
        self._columns = deepcopy(kwargs)

    def __getattr__(self, item):
        self._columns = self._table.get_fields(self._columns)
        if item in self._columns:
            return self._columns[item]
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        self._columns[key] = value
        self._table.put(self)

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __setitem__(self, key, value):
        return self.__setattr__(key, value)

    def __delitem__(self, key):
        return NotImplemented

    def __iter__(self):
        return NotImplemented

    def __len__(self):
        return len(self._columns)

    def __eq__(self, other):
        if isinstance(other, DatabaseObject):
            return self._table == other._table \
               and self._columns == other._columns
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self._table) ^ hash(self._columns)
