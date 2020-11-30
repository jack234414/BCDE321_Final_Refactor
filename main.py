#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

# Jack imports
import os
import sys
import subprocess
import asyncio

from mmmmsql import add_data, show_db_info, show_db_class, show_db_method, show_db_attr, test_connection
from validate_data import Data_to_db
from pickler import Pickler
from my_plot_strategy import *
from read_js_template import *

# Edan imports
from cmd import Cmd
from converter import Converter
from json_loader import JsonLoader

os.environ["PATH"] += os.pathsep + './wavi-master/bin'
dir_path = os.path.dirname(os.path.realpath(__file__))
wavi_path = os.path.join(dir_path, "wavi-master/bin")
os.environ["PATH"] += os.pathsep + wavi_path

class CommandLineInterface(Cmd):

    def __init__(self, dir=os.getcwd()):
        Cmd.__init__(self, dir)
        self.dir = dir
        self.prompt = ">>" + dir + ">> "
        self.hosts = []
        self.connections = []
        self.con = Converter()
        self.loop = asyncio.get_event_loop()
        self.intro = "This program will generate a class diagram from your JavaScript source code. " \
                     "Type help for a list of commands."
        jloader = JsonLoader('help_file.json')
        # self.do_load_data("JSTest2.js")  # test
        try:
            jloader.open_file()
        except FileNotFoundError:
            print('There is no help file.')
        self.jloader = jloader

    # Edan's work below
    def default(self, arg):
        print(arg, 'is an incorrect command, type help or ? to see the command list')

    def do_create_pickle(self, arg):
        self.con.make_pickle()

    def help_create_pickle(self):
        print(self.jloader.get_help_text('create_pickle'))

    def do_exit(self, arg):
        return True

    def help_exit(self):
        print(self.jloader.get_help_text('exit'))

    def do_load_data(self, arg):
        try:
            raw_data = arg.split()
            input_file = raw_data[0]
            Read_js().check_file_type(input_file)

            self.con.load_data(input_file)

        except IndexError:
            print('You should follow the format, please try {help load_data} to find the use.')

        except Exception as e:
            print(e)

    def help_load_data(self):
        print(self.jloader.get_help_text('load_data'))

    def do_extract_data(self, arg):
        try:
            self.con.visit(self.con.extract_data(self.con))
        except Exception as e:
            print(e)

    def help_extract_data(self):
        print(self.jloader.get_help_text('extract_data'))

    def do_convert_to_uml(self, arg):
        try:
            if self.con is not None:
                self.con.convert_to_uml()
            else:
                print("Please try to extract data first.")

        except Exception as e:
            print(e)

    def help_convert_to_uml(self):
        print(self.jloader.get_help_text('convert_to_uml'))

    """Jack's work above"""
    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print(self.jloader.get_help_text('EOF'))

    def do_read_js(self, arg):
        chk = Read_js()
        chk.check_file_type(arg)

    def help_read_js(self):
        print(self.jloader.get_help_text('read_js'))

    def do_js_parser(self, input_file):
        my_data = Read_js()
        print(my_data.get_data(input_file))

    def help_js_parser(self):
        print(self.jloader.get_help_text('js_parser'))

    def do_pwd(self, arg):
        if len(arg) > 1:
            print('Please check <help pwd> to follow up the format')
        else:
            print(os.getcwd())

    def help_pwd(self):
        print(self.jloader.get_help_text('pwd'))

    def do_use_pickle(self, arg):
        pickle_data = Data_to_db()
        pickle_data.print_pickle()
        # self.con.load_data("JStest1.js")
        # self.con.visit(self.con.extract_data(self.con))
        # self.con.convert_to_uml()
        # self.con.make_pickle()
        # my_pickler = Pickler()
        # print(my_pickler.convert(my_pickler.use_pickle()))

    def help_use_pickle(self):
        print(self.jloader.get_help_text('se_pickle'))

    def do_delete_pickle(self, arg):
        my_pickler = Pickler()
        my_pickler.delete_pickle(arg)

    def help_delete_pickle(self):
        print(self.jloader.get_help_text('delete_pickle'))

    def do_db_connect(self, arg):
        try:
            result = self.loop.run_until_complete(show_db_info(self.loop))
            print(result)
        except Exception as e:
            print(e)

    def help_db_connect(self):
        print(self.jloader.get_help_text('db_connect'))

    def do_test_db(self, arg):
        try:
            test_connection()

        except Exception as e:
            print(e)

    def do_db_add_data(self, arg):
        try:
            result = self.loop.run_until_complete(add_data(self.loop))
            print(result)
        except Exception as e:
            print(e)

    def help_db_add_data(self):
        print(self.jloader.get_help_text('db_add_data'))

    def do_db_table_select(self, arg):

        try:
            raw_data = arg.split()
            db = raw_data[0]

            if len(raw_data) == 1:
                try:
                    if db == '-c':
                        result = self.loop.run_until_complete(show_db_class(self.loop))
                        print(result)
                    elif db == '-m':
                        result = self.loop.run_until_complete(show_db_method(self.loop))
                        print(result)
                    elif db == '-a':
                        result = self.loop.run_until_complete(show_db_attr(self.loop))
                        print(result)
                    else:
                        print('The table you choose is not existed in the database,'
                              ' please try {help table_select} to check the existed tables')

                except Exception as e:
                    print(e)

            elif len(raw_data) != 1:
                print('Only 1 argument allowed, please try {help table_select} to follow up the format')
            else:
                print("Please at the least entre 1 argument as an option. Try again !")

        except IndexError as ie:
            print("Please at the least entre 1 argument as an option. Try again !")

    def help_db_table_select(self):
        print(self.jloader.get_help_text('db_table_select'))

    def do_draw_chart(self, arg):
        diagram_data = DiagramData()
        data = diagram_data.load_from_db()

        try:
            raw_data = arg.split()
            diagram_type = raw_data[0]

            if len(raw_data) == 1:
                try:
                    if diagram_type == '-b':
                        diagram_creator = ImageContext(BarImageStrategy())
                        diagram_creator.produce_image(data)
                    elif diagram_type == '-p':
                        diagram_creator = ImageContext(PieImageStrategy())
                        diagram_creator.produce_image(data)
                    else:
                        print('The table you choose is not existed in the database,'
                              ' please try {help table_select} to check the existed tables')

                except Exception as e:
                    print(e)

            elif len(raw_data) != 1:
                print('Only 1 argument allowed, please try {help table_select} to follow up the format')
            else:
                print("Please at the least entre 1 argument as an option. Try again !")

        except IndexError as e:
            print("Please at the least entre 1 argument as an option. Try again !")


    def help_draw_chart(self):
        print(self.jloader.get_help_text('draw_chart'))

    def do_validate_data(self, arg):
        v_data = Data_to_db()

        try:
            raw_data = arg.split()
            opt = raw_data[0]

            if len(raw_data) == 1:
                try:
                    if opt == '-c':
                        print(v_data.extract_name())
                    elif opt == '-m':
                        print(v_data.extract_method())
                    elif opt == '-a':
                        print(v_data.extract_attr())
                    else:
                        print(
                            'The data you choose is not existed in the extracted data, '
                            'please try {help validate_data} to check the existed tables')

                except Exception as e:
                    print(e)

            elif len(raw_data) != 1:
                print('Only 1 argument allowed, please try {help validate_data} to follow up the format')
            else:
                print("Please at the least entre 1 argument as an option. Try again !")

        except IndexError as ie:
            print("Please at the least entre 1 argument as an option. Try again !")

    def help_validate_data(self):
        print(self.jloader.get_help_text('validate_data'))

    def do_wavi(self, arg):
        try:
            raw_data = arg.split()
            input_file = raw_data[0]

            command = "wavi {0} uml-test.svg".format(input_file)
            print("Your wavi directory is: " + wavi_path)
            subprocess.run(command, cwd=dir_path, shell=True)

        except IndexError:
            print('You should follow the format, please try {help wavi} to find the use.')

        except Exception as e:
            print(e)

    def help_wavi(self):
        print(self.jloader.get_help_text('wavi'))


    # Jack's work (11.Amount of checking for pre- and post- conditions of methods)
    def preloop(self):
        """Initialization"""
        Cmd.preloop(self)  # sets up command completion
        self._hist = []  # No history yet
        self._locals = {}  # Initialize execution namespace for user
        self._globals = {}

    # Jack's work (11.Amount of checking for pre- and post- conditions of methods)
    def postloop(self):
        """Finish up everything"""
        Cmd.postloop(self)
        print("The application will now exit!")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':

    cli = CommandLineInterface()

    try:
        # Jack's work (1.Support command-line arguments)
        if len(sys.argv) > 1:
            cli.onecmd(' '.join(sys.argv[1:]))
        else:
            sys_exit_code = cli.cmdloop()
            print('Exiting with code: {!r}'.format(sys_exit_code))
            sys.exit(sys_exit_code)

    # Jack's work (10.Exception handling)
    except KeyboardInterrupt as e:
        print("\nProgram aborted by user\n")