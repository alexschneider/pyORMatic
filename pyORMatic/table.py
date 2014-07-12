__author__ = 'Alex'


class Table:

    def __init__(self, database, table_name, primary_key):
        self._database = database
        self._table_name = table_name
        self._primary_key = primary_key

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __hash__(self):
        return hash(self._database.database_type()) ^ hash(self._table_name)

    def get_id(self, id):
        kwarg = {self._primary_key: id}
        return self._database.get_fields(self._table_name, **kwarg)

    def get_fields(self, **kwargs):
        return self._database.get_fields(self._table_name, kwargs)

    def put(self, *obj):
        return self._database.put(self._table_name, obj)

    @property
    def num_rows(self):
        pass