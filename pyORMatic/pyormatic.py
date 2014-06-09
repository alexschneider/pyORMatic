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
    def __create_object_from_query(self, query_res):
        pass

    @property
    @abstractmethod
    def database_name(self):
        pass

    @property
    @abstractmethod
    def database_type(self):
        pass


    @staticmethod
    def construct_database(database_type):
        raise NotImplemented


if __name__ == "main":
    pass
    # unit tests
