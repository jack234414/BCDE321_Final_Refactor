#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

import pyodbc

import asyncio

class MSSQL:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    async def create_connection(self, connection_string):
        self.__connection = pyodbc.connect(connection_string)
        print("Connection established...")

    def close_connection(self):
        self.__connection.close()

    async def create_cursor(self):
        self.__cursor = await self.__connection.cursor()

    async def close_cursor(self):
        await self.__cursor.close()

    async def process_query(self, query):
        await self.__cursor.execute(query)
        return f'Query "{query}" processed!'

    async def insert_records(self, query, data):
        return await self.__cursor.executemany(query, data)

    async def fetch_all_records(self, query):
        await self.process_query(query)
        return await self.__cursor.fetchall()

    async def fetch_one(self, query):
        await self.process_query(query)
        return await self.__cursor.fetchone()

async def testing_connection():
    connection_string = "Driver={ODBC Driver 17 for SQL Server};" \
                        "Server=tcp:ara-db-test.database.windows.net,1433;" \
                        "Database=UML_Resource;" \
                        "Uid=ara-admin;" \
                        "Pwd=Test1234;" \
                        "Encrypt=yes;" \
                        "TrustServerCertificate=no;" \
                        "Connection Timeout=30;"
    mssql = MSSQL()
    try:

        await mssql.create_connection(connection_string)
        print("connection build successfully")

    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)

async def main():
    await testing_connection()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    result = loop.run_until_complete(main())
    print(result)

    connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:ara-db-test.database.windows.net,1433;Database=UML_Resource;Uid=ara-admin;Pwd=Test1234;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    con = pyodbc.connect(connection_string)
    print(con)

    query_I = "INSERT INTO dbo.js_Input (class_name, function_name, var_num) VALUES (?, ?, ?);"
    query_S = "SELECT * FROM dbo.js_Input"
    params = [('Cyclelog', 'addRide', 4)]

    cur = con.cursor()
    cur.executemany(query_I, params)

    cur.execute(query_S)

    con.commit()
    loop.close()


# server = 'tcp:aratesting.database.windows.net,1433'
# database = 'JStoUML'
# username = 'jack'
# password = 'Test1234'
# driver= '{ODBC Driver 17 for SQL Server}'
#
# with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM dbo.testdb")

# connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:ara-db-test.database.windows.net,1433;Database=UML_Resource;Uid=ara-admin;Pwd=Test1234;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
# con = pyodbc.connect(connection_string)
# print(con)
#
# cur = con.cursor()
# cur.execute("select 1+1 as sum")
# rows = cur.fetchall()
# print(rows)
# con.commit()


# cnxn = pyodbc.connect(
#     'DRIVER={Devart ODBC Driver for SQLAzure};'
#     'Server=;'
#     'Database=JStoUML;'
#     'Port=1433;'
#     'User ID=jack;'
#     'Password=Test1234')
#
# cursor = cnxn.cursor()
# cursor.execute("INSERT INTO EMP (column1, column2, column3) VALUES ('a333', 'Scott', 'Manager')")

# cursor = cnxn.cursor()
# cursor.execute("SELECT * FROM EMP")
# row = cursor.fetchone()
# while row:
#     print(row)
#     row = cursor.fetchone()

