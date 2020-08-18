import sqlite3
from sqlite3 import Error


class MySqlite:

    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connection(self):
        return self.__connection

    def cursor(self):
        return self.__cursor

    def close_connection(self):
        self.__connection.close()
        print("DB connection closed...")

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        try:
            self.__connection = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            print("DB connection established...")

    def commit_changes(self):
        self.__connection.commit()

    def create_cursor(self):
        self.__cursor = self.__connection.cursor()

    def close_cursor(self):
        self.__cursor.close()

    def execute_query(self, query):
        self.__cursor.execute(query)

    def fetch_one(self, query):
        self.execute_query(query)
        return self.__cursor.fetchone()

    def fetch_all(self, query):
        self.execute_query(query)
        return self.__cursor.fetchall()

    def execute_blob(self, sql, data):
        self.__cursor.execute(sql, [sqlite3.Binary(data)])


if __name__ == '__main__':  # For testing functions without using in main program

    mysqlite = MySqlite()

    mysqlite.create_connection(r"pythonsqlite.db")
    mysqlite.create_cursor()

    print("fetchall:")
    result = mysqlite.fetch_all("SELECT * FROM testData")
    for r in result:
        print(r)

    mysqlite.close_connection()
