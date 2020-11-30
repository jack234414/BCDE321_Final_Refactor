#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-
import re
import os.path
from os import path
from abc import ABCMeta, abstractmethod


class ReadFileTemplate(metaclass=ABCMeta):
    def __init__(self):
        self.file_name = ''
        self.work_dir = ''
        self.input = ''

        self.fucntion_name = []
        self.var_name = []
        self.row_data = ''

    @abstractmethod
    def is_existent_path(self, input_path):
        raise NotImplementedError

    @abstractmethod
    def is_existent_file(self, input_path):
        raise NotImplementedError

    @abstractmethod
    def read_file(self, input_path):
        raise NotImplementedError

    @abstractmethod
    def get_data(self, input_path):
        self.read_file(input_path)


class ReadNormalFile:
    def __init__(self, normal_file_template: ReadFileTemplate):
        self.normal_file_template = normal_file_template

    def return_is_existent_path(self, input_path):
        return self.normal_file_template.is_existent_path(input_path)

    def return_is_existent_file(self, input_path):
        return self.normal_file_template.is_existent_file(input_path)

    def receive_data(self, input_path):
        return self.normal_file_template.read_file(input_path)

    def receive_var_and_func(self, input_path):
        return self.normal_file_template.get_data(input_path)

class ReadJS(ReadFileTemplate):

    def is_existent_path(self, input_path):
        if os.path.exists(input_path):
            return True
        else:
            print("You did not input any path or your input file is not existed")

    def is_existent_file(self, input_path):
        try:
            assert os.path.isfile(input_path)
            return True

        except AssertionError:
            print("You might select a wrong path(i.e. a directory path), "
                  "please re-enter a path of the js file you want to input")

    def set_dir(self, input_path):
        self.work_dir = os.path.dirname(input_path)
        if self.work_dir.startswith('/'):
            self.file_name = input_path[len(self.work_dir) + 1:]
        else:
            self.file_name = input_path[len(self.work_dir):]

    def is_js_file(self, input_path):
        try:
            assert self.file_name.endswith('.js')
            return "Your selected js file is: " + self.file_name

        except AssertionError:
            print(self.input + " is not a js file, please re-select")

    def read_file(self, input_path):
        js_file = open(input_path, "r")
        self.row_data = js_file.read()
        return self.row_data

    def get_data(self, input_path):
        function = re.findall(r'function\s\w+', self.row_data, re.S) + re.findall(r'function\s\w+', self.row_data, re.S)
        var = re.findall(r'var\s\w+', self.row_data, re.S) + re.findall(r'const\s\w+', self.row_data,
                                                                        re.S) + re.findall(r'let\s\w+', self.row_data, re.S)
        for obj in function:
            self.fucntion_name.append(obj.lstrip('function'))

        for obj in var:
            self.var_name.append(re.sub('var|const|let| ', '', obj))

        return 'var: ' + str(self.var_name) + '\n' + 'function: ' + str(self.fucntion_name)

# if __name__ == "__main__":
#     a = ReadNormalFile(ReadJS())
#     a.return_is_existent_file("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/jack_jsTest.js")
#     print(a.return_is_existent_file("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/jack_jsTest.js"))
#
#     a.return_is_existent_file("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/jack_jsTest")
#
#     a.receive_data("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/jack_jsTest.js")
#     print(a.receive_data("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/jack_jsTest.js"))