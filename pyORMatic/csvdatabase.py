import pyORMatic
import csv
from pyORMatic.databaseobject import DatabaseObject

__author__ = 'Alex'

class CSVDatabase(pyORMatic.pyormatic.Pyormatic):

    # Member variables


    def __init__(self):
        self._current_objs = dict()
        self._table_cache = dict()

    def get_fields(self, table, **kwargs):
        if table not in self._table_cache:
            self.__build_cache(table)
        return filter(lambda key: set(kwargs.items()).issubset(set(key.items())),
                      self._table_cache[table])

    def put(self, table, *objs):
        edit_list = [(self._current_objs[obj], obj) for obj in objs if obj in self._current_objs]
        append_list = [obj for obj in objs if obj not in self._current_objs]
        with open(table + '.csv', newline='') as csvfile:
            writer = csv.DictWriter(csvfile)
            for (line_number, row) in enumerate(writer):
                if line_number == edit_list[0][0]:

    def __build_cache(self, table):
        new_cache = list()
        with open(table + '.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            new_cache = [DatabaseObject(row) for row in reader]
        self._table_cache[table] = new_cache

    @property
    def database_name(self):
        pass

    @property
    def database_type(self):
        return "CSV"