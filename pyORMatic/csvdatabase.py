import pyORMatic
import csv

__author__ = 'Alex'

class CSVDatabase(pyORMatic.pyormatic.Pyormatic):

    def __init__(self):
        self.current_objs = dict()

    def get_fields(self, table, **kwargs):
        objs = list()
        with open(table + '.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for (line_number, row) in enumerate(reader):
                valid_object = True
                for (key, value) in row.iteritems():
                    if key in kwargs:
                        if kwargs[key] != value:
                            valid_object = False
                            break
                if valid_object:
                    obj = self.__create_object_from_query(row, line_number)
                    objs.append(obj)
                    self.current_objs[obj] = line_number
        return objs

    def put(self, table, *objs):
        edit_list = [obj for obj in objs if obj in self.current_objs]
        append_list = [obj for obj in objs if obj not in self.current_objs]
        with open(table + '.csv', newline='') as csvfile:
            writer = csv.DictWriter(csvfile)
            for (line_number, row) in enumerate(



    def __create_object_from_query(self, query_res, line_number):
        pass

    @property
    def database_name(self):
        pass

    @property
    def database_type(self):
        return "CSV"