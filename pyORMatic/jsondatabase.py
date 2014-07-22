import os
import shutil
import tempfile
from databaseobject import DatabaseObject
from pyormatic import Pyormatic
import json

__author__ = 'alex'

class JSONDatabase(Pyormatic):

    def __init__(self, name, directory):
        super().__init__(name, directory)
        self.__cache = dict()
        self.__initialize_cache()

    @property
    def database_type(self):
        return 'json"'

    def get_fields(self, table, **kwargs):
        return filter(lambda x: all(item in x.items() for item in kwargs.items()), self.__cache[table])

    def put(self, table, *objs):
        self.__cache[table].extend(objs)
        self.__flush_cache(table)

    def delete(self, table, *objs):
        for obj in objs:
            if obj in self.__cache[table]:
                self.__cache[table].remove(obj)

    def __flush_cache(self, table):
        t = tempfile.NamedTemporaryFile(delete=False)
        json.dump(self.__cache[table], t, separators=(',', ':'))
        tmp_file_name = t.name
        t.close()
        shutil.copy(tmp_file_name, self.database_directory + table + '.' + self.database_type)

    def __initialize_cache(self):
        current_dir_files = list()
        for root, dirs, files in os.walk(self.database_directory):
            current_dir_files.extend(files)
            break # We only want the files in the current directory
        for file in current_dir_files:
            self.__initialize_file_cache(file)

    def __initialize_file_cache(self, file):
        with open(file) as f:
            self.__cache[os.path.basename(file)] = json.load(f, object_hook=DatabaseObject)