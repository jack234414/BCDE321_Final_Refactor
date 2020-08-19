#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

# import packages

import cmd
import re
import os


# Edan coding area

# from cmd import Cmd
# import argparse
# from converter import Converter
# from json_loader import JsonLoader
#
#
# class CommandLineInterface(Cmd):
#
#     def __init__(self):
#         super().__init__()
#         self.prompt = ">>> "
#         self.intro = "This program will generate a class diagram from your JavaScript source code. " \
#                      "Type help for a list of commands."
#         jloader = JsonLoader('help_file.json')
#         try:
#             jloader.open_file()
#         except FileNotFoundError:
#             print('There is no help file.')
#         self.jloader = jloader
#
#     def do_extract_data(self, arg):
#         con = Converter()
#         con.visit(con.extract_data(con))
#
#
#     def do_choose_system_type(self, arg):
#         """ -w for Windows, -m for Mac"""
#         if arg == "-w":
#             print('Windows Selected')
#         elif arg == "-m":
#             print('Mac Selected')
#
#     def help_choose_system_type(self):
#         print(self.jloader.get_help_text('choose_system_type'))
#
#     def do_exit(self):
#         """Exit the program"""
#         return True
#
#
# if __name__ == '__main__':
#     import sys
#
#     cli = CommandLineInterface()
#     sys_exit_code = cli.cmdloop()
#     print('Exiting with code: {!r}'.format(sys_exit_code))
#     sys.exit(sys_exit_code)

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