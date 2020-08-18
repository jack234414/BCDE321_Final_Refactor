#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

# import packages

import cmd
import re
import os


# Edan coding area


#------------------------------Sexy function1------------------------------


#------------------------------Sexy function2------------------------------


# Jack coding area

print("hello world")

print("testing")

A = 1 + 2
print(A)


def check_file(self, input_file):
    """
    >>> a = CheckDirectory()
    >>> a.check_file('/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py')
    'ppp_cmd.py'
    """

    if os.path.isfile(input_file):
        work_dir = os.path.dirname(input_file)
        file = input_file[len(work_dir) + 1:]

        return file

    else:
        work_dir = input_file
        file = "*.py"

        return file

if __name__ == '__main__':

    file1 = open(check_file("/Users/jimmy/py/pythonClassProject2020/cmd_test.py")).read()
    imp = re.findall(r"var\s\w+", file1, re.S)
    func = re.findall(r"function\sdo\w+", file1, re.S)

    for i in func:
        j = i.strip('function')
        func_all.append(j)
    print(self.func_all)

    for i in imp:
        j = i.strip('var')
        imp_arr.append(j)