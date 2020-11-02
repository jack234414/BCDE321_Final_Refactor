#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

from converter import Converter
import json
from pickler import *


class Data_to_db:

    def __init__(self):
        # Initialize property
        self._class_id = []
        self._class_names = []
        self._class_methods = []
        self._class_attrs = []
        self._class_methods_num = []
        self._class_attr_num = []
        self._data = Pickler.use_pickle(Pickler)

    def print_pickle(self):
        print(self._data)

    def extract_id(self):
        with open('result.json') as uml_resource:
            data = json.load(uml_resource)
            for key in data:
                self._class_id.append("".join(filter(str.isdigit, key)))
            return self._class_id

    def extract_name(self):
        with open('result.json') as uml_resource:
            data = json.load(uml_resource)
            for key, value in data.items():
                self._class_names.append([data[key]["classname"]])
            self._class_names[0].insert(0, 1)
            self._class_names[1].insert(0, 2)

        return self._class_names

    def extract_method(self):
        temp_list = []
        with open('result.json') as uml_resource:
            data = json.load(uml_resource)
            for key, value in data.items():
                temp_list.append(data[key]["classmethod"])

            for i in range(1, len(data.keys())+1):
                for value in temp_list[i-1]:
                    self._class_methods.append([i] + [value])

            for i in range(0, len(self._class_methods)):
                self._class_methods[i].insert(0, i+1)

        return self._class_methods

    def extract_attr(self):
        temp_list = []
        with open('result.json') as uml_resource:
            data = json.load(uml_resource)
            for key, value in data.items():
                temp_list.append(data[key]["attributes"])

            for i in range(1, len(data.keys())+1):
                for value in temp_list[i-1]:
                    self._class_attrs.append([i] + [value])

            for i in range(0, len(self._class_attrs)):
                self._class_attrs[i].insert(0, i+1)

        return self._class_attrs

    def method_num_count(self):
        print(self._class_methods[0])
        self._class_methods_num.append(len(self._class_methods[0]))
        self._class_methods_num.append(len(self._class_methods[1]))
        print(self._class_methods_num)

    def attr_num_count(self):
        self._class_attr_num.append(len(self._class_attrs[0]))
        self._class_attr_num.append(len(self._class_attrs[1]))
        print(self._class_attr_num)

    # def dumpclean(self, obj):
    #     for p_id, p_info in obj.items():
    #         self._class_id.append("".join(filter(str.isdigit, p_id)))
    #
    #         for key in p_info:
    #             if key == "classname":
    #                 self._class_names.append(p_info[key])
    #             elif key == "classmethod":
    #                 self._class_methods.append(p_info[key])
    #             else:
    #                 self._class_attr.append(p_info[key])
    #
    #             if key == "classmethod":
    #                 self._class_methods.append(list(p_info[key]))
    #             self._class_attr = list(p_info[key] & {'attributes'})
    #
    # def get_everything(obj):
    #     for p_id, p_info in obj.items():
    #         print("\nClass ID:", p_id)
    #         for key in p_info:
    #             print(key + ':', p_info[key])

# if __name__ == '__main__':
#     da = Data_to_db()
#
#     # da.print_pickle()
#
#     da.method_num_count()
#     da.attr_num_count()