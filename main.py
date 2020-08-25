#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

# Jack imports
import os
# import cmd
# import re
import visitorTest
from read_js import Read_js

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

    def do_extract_data(self, arg):
        con = Converter()
        con.visit(con.extract_data(con))

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

    def do_uml(self, arg):
        con = Converter()
        con.visit(con.extract_data(con))
        con.convert_to_dot()

    # Jack uncompleted coding
    def do_read_js(self, arg):
        chk = Read_js()
        chk.check_file_type(arg)

    def do_pwd(self, arg):
        print(os.getcwd())


if __name__ == '__main__':
    import sys

    cli = CommandLineInterface()
    sys_exit_code = cli.cmdloop()
    print('Exiting with code: {!r}'.format(sys_exit_code))
    sys.exit(sys_exit_code)