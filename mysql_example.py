#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import re
import os
import pymysql
from checkfiles import CheckDirectory


class LinkDb:
    func_all = []
    imp_arr = []

    def __init__(self):
        pass

    def get_file(self, cmd_file):
        file_name = CheckDirectory.check_file(self, cmd_file)
        file = open(file_name)
        file1 = file.read()
        imp = re.findall(r"import\s\w+", file1, re.S)
        func = re.findall(r"def\sdo\w+", file1, re.S)

        for i in func:
            j = i.strip('def')
            self.func_all.append(j)

        print(self.func_all)

        for i in imp:
            j = i.strip('import')
            self.imp_arr.append(j)
        print(self.imp_arr)

    def link_mysql_save(self):
        mydb = pymysql.connect(host="127.0.0.1", user="root", passwd="1234", database="class")
        cursor = mydb.cursor()
        sql_table = ("CREATE TABLE content ( packages VARCHAR(25), features VARCHAR(25))")
        try:
            cursor.execute(sql_table)
            for d, f in zip(self.func_all,self.imp_arr):
                sql = "INSERT INTO content (packages, features) VALUES (%s, %s)"
                val = (f, d)
                cursor.execute(sql, val)
                mydb.commit()
                #db.commit()

        except:
            mydb.rollback()
        mydb.close()

    def check_link_db(self):
        mydb = pymysql.connect(host="127.0.0.1", user="root", passwd="1234", database="class")

        if (mydb):

            print("Connection successful")
        else:
            # Terminate
            print("Connection unsuccessful")

    def load_mysql_data(self):
        db = pymysql.connect(host="127.0.0.1", user="root", passwd="1234", database="class")
        cursor = db.cursor()
        sql_query = ("Select*from content")
        try:
            # Execute the SQL command
            cursor.execute(sql_query)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                Packages = row[0]
                features = row[1]
                print("Packages  = %s ,features = %s" % \
                      (Packages, features))
        except:
            print("Error: unable to fetch data")


"""
if __name__ == '__main__':
    LinkDb().get_file("/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py")
    LinkDb().link_mysql_save()
    LinkDb().load_mysql_data()
    LinkDb().check_link_db()
"""