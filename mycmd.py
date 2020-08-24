#!/usr/local/bin/Python3.6

# -*- coding: utf-8 -*-
import os
import sys
import mycmd
import ast
import subprocess
from os import environ, pathsep, path
from sqlite import MySqlite
from datetime import datetime
from extractData import ExtractData
from validate_data import ValidateData
from mysql_example import LinkDb
from checkfiles import CheckDirectory
import re
import shelve
from mysql import MySQL
import cmdAdapter
import asyncio
from jsonTesting import JsonData
from argparse import ArgumentParser
import re
from pieChart import CreatePieChart
from strategy import *
from draw_UML import SvgSite, FigSite, DotSite
from coverage import *

os.environ["PATH"] += os.pathsep + './wavi-master/bin'
dir_path = os.path.dirname(os.path.realpath(__file__))
wavi_path = os.path.join(dir_path, "wavi-master/bin", "")
os.environ["PATH"] += os.pathsep + os.pathsep.join(wavi_path)

class CustomStream(object):
    async def readline(self):
        return await sys.stdin.readline()

    def write(self, msg):
        sys.stdout.write(msg)

    def flush(self):
        pass


MyAsyncShell = type('MyAsyncShell', (mycmd.Cmd,), {
    'cmdloop': cmdAdapter.adapter_cmdloop,
    'use_rawinput': False,
    'stdin': CustomStream(),
    'stdout': CustomStream()
})


class CLI(mycmd.Cmd):  # MyAsyncShell - This is not working bugged !!!

    def __init__(self):
        mycmd.Cmd.__init__(self)
        self.prompt = "==>>>"
        self.intro = "This program can generate class diagrams from your source codes, type help for a list of commands"
        json = JsonData('helpfiledata.json')
        try:
            json.open_file()
        except FileNotFoundError:
            print('Help data file cannot be opened...')
        self.__json = json

    def do_get_all_source_files(self, arg):
        arguments = arg.split()

        if len(arguments) != 0:

            if path.isdir(arguments[0]):
                files = []
                for file in os.listdir(arguments[0]):
                    if file.endswith(".py"):
                        print(os.path.join(arguments[0], file))
                        files.append(os.path.join(arguments[0], file))

                if len(arguments) == 3 and arguments[1] == "-a":
                    if arguments[2] == "svg" or arguments[2] == "dot" or arguments[2] == "fig":
                        for file in files:
                            self.do_uml_diagram(file + " " + arguments[2])
                    else:
                        print("Incorrect output format entered")
            else:
                print("Directory not valid")

    def help_get_all_source_files(self):
        print(self.__json.get_help_text('getAllSourceFiles'))

    def do_shelve(self, cmd_file):
        """input an absoluat"""
        file_name = CheckDirectory.check_file(self, cmd_file)
        print(file_name)
        file = open(file_name)
        file1 = file.read()
        imp = re.findall(r"import\s\w+", file1, re.S)
        s = shelve.open("test")
        s['package'] = imp
        print(s['package'])
        s.close()

    def do_choose_system(self, arg):
        """ please input -w or -m  to tell us your operation system, Windows or Mac"""
        if arg == "-w":
            print('Windows lover')
        elif arg == "-m":
            print('Mac lover')

    def help_choose_system(self):
        print(self.__json.get_help_text('choose_system'))

    def do_exit(self, *args):
        """leave this programme"""
        return True

    def do_uml_diagram(self, args):
        """PLEASE input full path and can have
         options on two different diagram types """
        # try:
        #     raw_data = args.split()
        #     input_file = raw_data[0]
        #     file_type = raw_data[1]
        #     if file_type == '-svg':
        #         svg = SvgSite(input_file)
        #         svg.run_all()
        #         return True
        #     elif file_type == '-fig':
        #         fig = FigSite(input_file)
        #         fig.run_all()
        #         return True
        #     elif file_type == '-dot':
        #         dot = DotSite(input_file)
        #         dot.run_all()
        #         return True
        #     else:
        #         print(" You only have 3 options which are svg, dot and fig in the file types")
        #         return False
        # except:
        #     pass
        os.environ["PATH"] += os.pathsep + './wavi-master/bin'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        wavi_path = os.path.join(dir_path, "wavi-master/bin", "")
        os.environ["PATH"] += os.pathsep + os.pathsep.join(wavi_path)

        command = "/Users/hadooper/uml_test/wavi-master/bin/wavi /Users/hadooper/js-test uml-test.svg"
        subprocess.run(command, cwd="/Users/hadooper", shell=True)
        #
        # raw_data = args.split()
        # wavi = raw_data[0]
        # file_type = raw_data[1]
        # try:
        #     os.path.isdir(input_file)
        #     os.path.isfile(input_file)
        #     work_dir = os.path.dirname(input_file)
        #     file = input_file[len(work_dir) + 1:]
        #
        # except FileNotFoundError:
        #     print("wrong path, try again")
        #
        # else:
        #
        #     if file_type == 'svg':
        #         command = "pyreverse {0} -o svg -p diagram".format(file)
        #         print("input_dir:{0} input_file:{1}".format(work_dir, file))
        #         print("command:" + command)
        #         subprocess.run(command, cwd=work_dir, shell=True)
        #     elif file_type == 'fig':
        #         command = "pyreverse {0} -o fig -p diagram".format(file)
        #         print("input_dir:{0} input_file:{1}".format(work_dir, file))
        #         print("command:" + command)
        #         subprocess.run(command, cwd=work_dir, shell=True)
        #     elif file_type == 'dot':
        #         command = "pyreverse {0} -o dot -p diagram".format(file)
        #         print("input_dir:{0} input_file:{1}".format(work_dir, file))
        #         print("command:" + command)
        #         subprocess.run(command, cwd=work_dir, shell=True)
        #     else:
        #         print(" You only have 3 options which are svg, dot and fig in the file types")

    def help_uml_diagram(self):
        print(self.__json.get_help_text('uml_diagram'))

    def do_extract_data(self, args):
        """This can load a cmd interface file and extract data from it"""

        ExtractData().get_data(args)

    def help_extract_data(self):
        print(self.__json.get_help_text('extractData'))

    def do_validate_data(self, args):
        try:
            path = True
            ValidateData().check_file(args)
        except Exception as err:
            print(err)
            path = False
        return path

    def help_validate_data(self):
        print(self.__json.get_help_text('ValidateData'))

    def do_chart(self, args):
        """input a full path of your file, then add -t for
        generate a table or add -b for generate a bar chart"""
        raw_data = args.split()
        input_file = raw_data[0]
        chart = raw_data[1]
        if chart == "-t":
            con = Context(Table(input_file))
            con.chart()
            path = True
        elif chart == "-b":
            con2 = Context(Bar(input_file))
            con2.chart()
            path = True
        else:
            print("Please choose a table or bar chart")
            path = False
        return path

    def help_bar_chart(self):
        print(self.__json.get_help_text('bar_chart'))

    def do_mysql(self, arg):
        """this can check weather the db links.
        please make sure your Mysql have a database which is
        host="127.0.0.1", user="root", passwd="1234", database="class """

        LinkDb().check_link_db()

        return True

    def do_save_data(self, args):
        """this can save data to MySql database.
        please make sure your Mysql have a database which is
        host="127.0.0.1", user="root", passwd="1234", database="class"""
        try:
            path = True
            LinkDb().get_file(args)
            LinkDb().link_mysql_save()
        except:
            print("wrong path, try again")
            path = False
        return path

    def do_load_data(self, arg):
        """This can laod data from MySql database.
         please make sure your Mysql have a database which is host="127.0.0.1", user="root",
         passwd="1234", database="class"""
        try:
            LinkDb().load_mysql_data()
        except FileNotFoundError:
            print("cannot load data from the database")

    def do_print_file(self, path):
        """Takes one parameter: file path. Takes a file and then prints it to the console"""
        try:

            fileObj = open(path, 'r')
            print(fileObj.read())

        except FileNotFoundError:

            print("No file found at: '" + path + "'")

    def do_generate_dot(self, args):
        """Takes one parameter: source code file path. This command turns the source
        code file into a dot file of the program structure"""

        arguments = args.split()

        if len(arguments) == 1:

            print("correct number")
            print(arguments[0])

            try:
                open(arguments[0], 'r').read()

            except FileNotFoundError:

                print("No file found at: '" + arguments[0] + "'")

            command = 'pyreverse -o dot ' + arguments[0] + ' -p componentplain '
            return subprocess.call(command)


        else:

            print("Wrong num of args, please try again")

    def do_save_file_to_local_database(self, arg):
        """Saves a file to the database server"""
        save_file_to_local_database(arg)

    def do_get_file_from_local_database(self, arg):
        get_file_from_local_database(arg)

    async def do_test_save_to_database_server(self):
        loop = asyncio.get_event_loop()

        result = loop.run_until_complete(saveServer())
        print(result)

        loop.close()

    def do_generate_pie_chart(self, file):

        try:
            with open(file, 'r') as file:
                file_data = file.read().replace('\n', '')
        except FileNotFoundError:
            print("No such file found")

        else:

            ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
            valid_extensions = ['.py']
            if not ext.lower() in valid_extensions:
                print('Unsupported file extension, only accepts .py files')
            else:
                num_classes = 0
                num_functions = 0
                num_attribute = 0

                regex = r"class"

                matches = re.finditer(regex, file_data, re.MULTILINE)
                for _ in matches:
                    num_classes += 1

                regex = r"def"

                matches = re.finditer(regex, file_data, re.MULTILINE)
                for _ in matches:
                    num_functions += 1

                regex = r"self.*="

                matches = re.finditer(regex, file_data, re.MULTILINE)

                for _ in matches:
                    num_attribute += 1

                labels = 'Classes', 'Functions', 'Attributes'
                sizes = [num_classes, num_functions, num_attribute]
                pie = CreatePieChart(labels, sizes, file)
                pie.generate_pie_chart()

    def help_generate_pie_chart(self):
        print(self.__json.get_help_text('generatePieChart'))


async def save_server():
    await save_file_to_database_server("Components.txt")


def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def save_file_to_local_database(path):
    conn = MySqlite()
    conn.create_connection(r"pythonsqlite.db")
    conn.create_cursor()

    try:

        fileData = convertToBinaryData(path)
        sql = """INSERT INTO testData (fileName, fileData, fileSaveDate) VALUES ("{}", ?, "{}")""".format(path,
                                                                                                          datetime.now())
        conn.execute_blob(sql, fileData)
        print("File inserted into db...")

    except FileNotFoundError:

        print("File path does not exist")

    conn.commit_changes()
    conn.close_cursor()
    conn.close_connection()


def get_file_from_local_database(filename):
    conn = MySqlite()
    try:
        conn.create_connection(r"pythonsqlite.db")
    except Exception as err:
        print("Cannot connect to local db: " + err)
    conn.create_cursor()
    sql = """SELECT fileData FROM testData WHERE fileName = "{}" """.format(filename)
    result = conn.fetch_all(sql)
    print(result)


async def save_file_to_database_server(path):
    conn = MySQL()
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root'
    }
    try:

        await conn.create_connection(db_config)
        fileData = convertToBinaryData(path)

    except FileNotFoundError:

        print("File path not found...")

    except Exception as err:

        print(err)

    else:

        await conn.create_cursor()
        sql = """INSERT INTO testData (fileName, fileData, fileSaveDate) VALUES ("{}", ?, "{}")""".format(path,
                                                                                                          datetime.now())
        await conn.execute_blob(sql, fileData)
        await conn.commit()
        await conn.close_cursor()
        await conn.close_connection()


def add_args():
    parser = ArgumentParser()
    parser.add_argument("-s", "--SourceCodePath", help="path to input source code file")
    parser.add_argument("-f", "--FileType", help="set output file type"
                                                 "supported file types: svg, dot, fig")
    return parser.parse_args()




if __name__ == '__main__':
    # CLI().cmdloop()
    # -s C:/Users/TimDesk/PycharmProjects/pythonClassProject2020/test4.py -f svg (EXAMPLE command line args)

    args = add_args()

    if args.SourceCodePath and args.FileType:

        CLI.do_uml_diagram("", "{}".format(args.SourceCodePath) + " {}".format(args.FileType))

    else:

        loop = asyncio.get_event_loop()
        loop.run_until_complete()
        loop.close()


