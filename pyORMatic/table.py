__author__ = 'Alex'


class Table:

    def __init__(self, database_type, table_name, primary_key):
        self.database_type = database_type
        self.table_name = table_name
        self.primary_key = primary_key

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def get_id(self, id):
        kwarg = {self.primary_key: id}
        return self.database_type.get_fields(self.table_name, **kwarg)

    def get_fields(self, **kwargs):
        return self.database_type.get_fields(self.table_name, kwargs)

    def put(self, *obj):
        return self.database_type.put(self.table_name, obj)

    @property
    def num_rows(self):
        pass