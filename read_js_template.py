#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-
import os
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

        self._file_dir = ""
        self._file_contents = ""
        self._clean_file_contents = ""

    @abstractmethod
    def is_existent_file(self, input_path):
        raise NotImplementedError

    @abstractmethod
    def is_existent_path(self, input_path):
        raise NotImplementedError

    @abstractmethod
    def read_file(self):
        raise NotImplementedError

    @abstractmethod
    def get_data(self, input_path):
        self._set_file_dir(new_dir)
        self._read_file()
        return self._clean_file_contents



class Read_js:
    """doctest
    >>> to_extract_data = Read_js()
    >>> to_extract_data.get_data("jack_jsTest.js")
    "var: ['width', 'height', 'testtttt', 'aaaaaaa', 'goodfunction', 'area']\\nfunction: [' calculateArea', ' calculateArea']"
    >>> wrong_path = Read_js()
    >>> wrong_path.check_file_type("not_exist.js")
    You did not input any path or your input file is not existed
    """

    def __init__(self):
        self.fucntion_name = []
        self.var_name = []
        self.row_data = ''
        self.file = ''
        self.work_dir = ''
        self.input = ''

    # Jacks work
    def check_file_type(self, input_file):
        self.input = input_file
        if os.path.exists(input_file):
            try:
                assert os.path.isfile(self.input)
                self.work_dir = os.path.dirname(self.input)
                if self.input.startswith('/'):
                    self.file = self.input[len(self.work_dir)+1:]
                else:
                    self.file = self.input[len(self.work_dir):]
                try:
                    assert self.file.endswith('.js')
                    print("The current directory is: " + self.work_dir + "\n" +
                          "Your selected js file is: " +  self.file)
                    # return "The current directory is: " + work_dir + "\n" + \
                    #        "Your selected js file is: " + file
                except AssertionError:
                    print(self.input + " is not a js file, please re-select")

            except AssertionError:
                print("You might select a wrong path(i.e. a directory path), " 
                      "please re-enter a path of the js file you want to input")
        else:
            print("You did not input any path or your input file is not existed")

    def get_data(self, input_file):

        try:
            if path.exists(input_file):
                with open(input_file, "r") as source:
                    self.row_data = source.read()

                function = re.findall(r'function\s\w+', self.row_data, re.S) + re.findall(r'function\s\w+', self.row_data, re.S)
                var = re.findall(r'var\s\w+', self.row_data, re.S) + re.findall(r'const\s\w+', self.row_data, re.S) + re.findall(r'let\s\w+', self.row_data, re.S)

                for obj in function:
                    self.fucntion_name.append(obj.lstrip('function'))

                for obj in var:
                    self.var_name.append(re.sub('var|const|let| ', '', obj))
                    # var_all.append(obj.lstrip('var' or 'const' or 'let'))
                return 'var: ' + str(self.var_name) + '\n' + 'function: ' + str(self.fucntion_name)

            else:
                print("Your given python file does not exist in the current directory "
                      "or your input arguments were wrong. Please try again!")

        except Exception as err:
            print("Please try again! The exception is: ", err)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
