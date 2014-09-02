import os
import shutil
import tempfile
from pyormatic import Pyormatic
import pickle
import itertools

__author__ = 'alex'


class PickleDatabase(Pyormatic):

    def __init__(self, name, directory):
        super().__init__(name, directory)
        self.__cache = dict()
        self.__initialize_cache()
    @property
    def database_type(self):
        return 'pickle'

    def get_fields(self, table, **kwargs):
        if table not in self.__cache:
            return list()
        if len(kwargs) == 0:
            return self.__cache[table]
        return filter(lambda x: all(item in x.items() for item in kwargs.items()), self.__cache[table])

    def put(self, table, *objs):
        chain = itertools.chain(*objs)
        if table not in self.__cache:
            self.__cache[table] = list()
        self.__cache[table].extend(chain)
        self.__flush_cache(table)

    def delete(self, table, *objs):
        chain = itertools.chain(*objs)
        for obj in chain:
            if obj in self.__cache[table]:
                self.__cache[table].remove(obj)
        self.__flush_cache(table)

    def __flush_cache(self, table):
        t = tempfile.NamedTemporaryFile(delete=False) # Defaults to binary mode - for any loading, ensure that binary mode is selected
        pickle.dump(self.__cache[table], t)
        tmp_file_name = t.name
        t.close()
        shutil.copy(tmp_file_name, self.database_directory + '/' + table + '.' + self.database_type)

    def __initialize_cache(self):
        current_dir_files = list()
        for root, dirs, files in os.walk(self.database_directory):
            current_dir_files.extend(files)
            break # We only want the files in the current directory
        for file in current_dir_files:
            self.__initialize_file_cache(file)

    def __initialize_file_cache(self, file):
        with open(self.database_directory + '/' + file, 'rb') as f:
            self.__cache[os.path.splitext(file)[0]] = pickle.load(f)
