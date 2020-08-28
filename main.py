#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

<<<<<<< HEAD
# import packages

# import cmd
# import re
# import os


# Edan coding area
=======
# Jack imports
import asyncio
import os
# import cmd
# import re
import visitorTest
from read_js import Read_js
from mysql import MySQL, main1, main2, main3
import pyodbc
>>>>>>> readJS_test

# Edan imports
from cmd import Cmd
# import argparse  # currently not using argparse
from converter import Converter
from json_loader import JsonLoader


class CommandLineInterface(Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = ">>> "
        self.intro = "This program will generate a class diagram from your JavaScript source code. " \
                     "Type help for a list of commands."
        jloader = JsonLoader('help_file.json')
        try:
            jloader.open_file()
        except FileNotFoundError:
            print('There is no help file.')
        self.jloader = jloader

<<<<<<< HEAD
    def do_uml(self, arg):
        con = Converter()
        con.visit(con.extract_data(con))
        con.convert_to_dot()
=======
    def do_extract_data(self, arg):
        con = Converter()
        con.visit(con.extract_data(con))
>>>>>>> readJS_test

    def do_choose_system_type(self, arg):
        """ -w for Windows, -m for Mac"""
        if arg == "-w":
            print('Windows Selected')
        elif arg == "-m":
            print('Mac Selected')

    def help_choose_system_type(self):
        print(self.jloader.get_help_text('choose_system_type'))

    def do_exit(self):
        """Exit the program"""
        return True

<<<<<<< HEAD
=======
    def do_uml(self, arg):
        try:
            raw_data = arg.split()
            input_file = raw_data[0]
            Read_js().check_file_type(input_file)

            con = Converter()
            con.load_data(input_file)
            con.visit(con.extract_data(con))
            con.convert_to_dot()

        except Exception as err:
            print(err)





    # Jack uncompleted coding
    def do_read_js(self, arg):
        chk = Read_js()
        chk.check_file_type(arg)

    def do_pwd(self, arg):
        print(os.getcwd())

    def do_db_connect(self, arg):
        loop = asyncio.get_event_loop()
        try:
            result = loop.run_until_complete(main1())
            print(result)
        except Exception as e:
            print(e)

        # finally:
        #     loop.close()

    def do_db_btf_info(self, arg):
        loop = asyncio.get_event_loop()
        try:
            result = loop.run_until_complete(main3())
            print(result)
        except Exception as e:
            print(e)
        # finally:
        #     loop.close()

    def do_tb_select_all(self, arg):
        loop = asyncio.get_event_loop()
        try:
            result = loop.run_until_complete(main2())
            print(result)
        except Exception as e:
            print(e)
        # finally:
        #     loop.close()

>>>>>>> readJS_test

if __name__ == '__main__':
    import sys

    cli = CommandLineInterface()
    sys_exit_code = cli.cmdloop()
    print('Exiting with code: {!r}'.format(sys_exit_code))
<<<<<<< HEAD
    sys.exit(sys_exit_code)

# Jack coding area

# print("hello world")
#
# print("testing")
#
# A = 1 + 2
# print(A)
#
#
# def check_file(self, input_file):
#     """
#     >>> a = CheckDirectory()
#     >>> a.check_file('/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py')
#     'ppp_cmd.py'
#     """
#
#     if os.path.isfile(input_file):
#         work_dir = os.path.dirname(input_file)
#         file = input_file[len(work_dir) + 1:]
#
#         return file
#
#     else:
#         work_dir = input_file
#         file = "*.py"
#
#         return file
#
# if __name__ == '__main__':
#
#     file1 = open(check_file("/Users/jimmy/py/pythonClassProject2020/cmd_test.py")).read()
#     imp = re.findall(r"var\s\w+", file1, re.S)
#     func = re.findall(r"function\sdo\w+", file1, re.S)
#
#     for i in func:
#         j = i.strip('function')
#         func_all.append(j)
#     print(self.func_all)
#
#     for i in imp:
#         j = i.strip('var')
#         imp_arr.append(j)
=======
    sys.exit(sys_exit_code)
>>>>>>> readJS_test
