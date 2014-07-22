__author__ = 'Alex'


class Table:

    def __init__(self, database, table_name):
        self.__database = database
        self.__table_name = table_name

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __hash__(self):
        return hash(self.__database.database_type()) ^ hash(self.__table_name)

    def get_fields(self, **kwargs):
        return self.__database.get_fields(self.__table_name, kwargs)

    def put(self, *objs):
        return self.__database.put(self.__table_name, objs)

    def delete(self, *objs):
        return self.__database.delete(self.__table_name, objs)