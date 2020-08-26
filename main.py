#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

# Jack imports
import asyncio
import os
# import cmd
# import re
import visitorTest
from read_js import Read_js
from mssql_test import MSSQL, main
import pyodbc

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
        result = loop.run_until_complete(main())
        print(result)

    def do_db_select_all(self, arg):
        db_select_all()

def db_select_all():
    conn = MSSQL()
    connection_string = "Driver={ODBC Driver 17 for SQL Server};" \
                        "Server=tcp:ara-db-test.database.windows.net,1433;" \
                        "Database=UML_Resource;" \
                        "Uid=ara-admin;" \
                        "Pwd=Test1234;" \
                        "Encrypt=yes;" \
                        "TrustServerCertificate=no;" \
                        "Connection Timeout=30;"
    try:
        conn.create_connection(connection_string)
        print("connection build successfully")

    except Exception as err:

        print(err)

    else:
        conn.create_cursor()
        sql = "SELECT * FROM dbo.js_Input"
        conn.process_query(sql)

        # row = cursor.fetch_one()
        # while row:
        #     print(str(row[0]) + " " + str(row[1]))
        #     row = cursor.fetch_one(sql)

        print(conn.process_query(sql))

        conn.create_cursor()
        # row = conn.fetch_one(sql)
        for row in conn.fetch_all_records(sql):
            print(row)
        # while row:
        #     print (str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]))
        #     row = conn.fetchone()

        conn.close_cursor()
        conn.close_connection()


if __name__ == '__main__':
    import sys

    cli = CommandLineInterface()
    sys_exit_code = cli.cmdloop()
    print('Exiting with code: {!r}'.format(sys_exit_code))
    sys.exit(sys_exit_code)