from copy import *

__author__ = 'Alex'


class DatabaseObject:
    def __init__(self, table, line_number, **kwargs):
        self._table = table
        self._columns = deepcopy(kwargs)
        self._line_number = line_number

    def __getattr__(self, item):
        self._columns = self._table.get_fields(self._columns)
        if item in self._columns:
            return self._columns[item]
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        self._columns[key] = value

    def __eq__(self, other):
        if isinstance(other, DatabaseObject):
            return self._line_number == other._line_number \
                and self._table == other._table \
                and self._columns == other._columns
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self._table) ^ hash(self._columns)
