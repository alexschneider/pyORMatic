from abc import *

__author__ = 'Alex'


class Pyormatic():
    __metaclass__ = ABCMeta
    @abstractmethod
    def get_fields(self, table, **kwargs):
        pass

    @abstractmethod
    def put(self, table, *objs):
        pass

    @abstractmethod
    def delete(self, table, objs):
        pass

    @property
    def database_name(self):
        return self.__name

    @property
    def database_directory(self):
        return self.__directory

    @property
    @abstractmethod
    def database_type(self):
        pass

    @staticmethod
    def construct_database(database_type, database_name, database_directory):
        if database_type == "json":
            from jsondatabase import JSONDatabase
            return JSONDatabase(database_name, database_directory)
        else:
            raise NotImplementedError
    def __init__(self, name, directory):
        self.__name = name
        self.__directory = directory


if __name__ == "main":
    pass
    # unit tests
