
import asyncio
import aiomysql
import configparser
import pymysql
from time import time

from validate_data import Data_to_db

class MySQL:
    def __init__(self):
        self.__connection = None
        self.__cursor = None
        self.__pool = None

        # DB
        self._sql_hostname = None
        self._sql_username = None
        self._sql_password = None
        self._sql_main_database = None
        self._sql_port = 0
        self._sql_loop = None
        self._sql_max_size = 0
        self._sqL_echo = None

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    def build_db_config(self):
        config = configparser.ConfigParser()
        config.read('db.ini')
        self._sql_hostname = config['mysql_local']['host']
        self._sql_username = config['mysql_local']['user']
        self._sql_password = config['mysql_local']['passwd']
        self._sql_main_database = config['mysql_local']['db']
        self._sql_port = int(config['mysql_local']['port'])
        self._sql_loop = config['mysql_local']['loop']

    async def aaa(self):
        print("Connection established...")
        try:
            self.__connection = await aiomysql.connect(host=self._sql_hostname,
                                   user=self._sql_username,
                                   password=self._sql_password,
                                   db=self._sql_main_database,
                                   port=3306)
            print("Connected to a MySQL server!")
        except pymysql.err.InternalError as e1:
            code, msg = e1.args
            if code == 1049:
                print('Your setting database: ' + self._sql_main_database, 'not exists')
            else:
                print("Please try again! The exception is: ", e1)

        except pymysql.err.OperationalError as e2:
            code, msg = e2.args
            if code == 1045:
                print('User not exists, Please try again!')
            else:
                print("Please try again! The exception is: ", e2)

        except Exception as err:
            print("Please try again! The exception is: ", err)


    async def create_connection(self, db_config):
        print("Connection established...")
        try:
            self.__connection = await aiomysql.connect(**db_config)
            print("Connected to a MySQL server!")
        except pymysql.err.InternalError as e1:
            code, msg = e1.args
            if code == 1049:
                print('Your setting database:' + self._sql_main_database, ' not exists, Please try again!')
            else:
                print("Please try again! The exception is: ", e1)

        except pymysql.err.OperationalError as e2:
            code, msg = e2.args
            if code == 1045:
                print('User: ' + self._sql_username, 'not exists, Please try again!')
            else:
                print("Please try again! The exception is: ", e1)

        except Exception as err:
            print("Please try again! The exception is: ", err)

    def disconnect_connection(self):
        self.__connection.close()
        print("Disconnected from the MySQL server!")

    async def create_connection_pool(self, db_pool_config):
        print("Connection established...")
        try:
            self.__pool = await aiomysql.create_pool(**db_pool_config)
            print(f"Create a connection pool {self.__pool} for a MySQL server!")

        except Exception as err:
            print("Please try again! The exception is: ", err)

    async def get_pool_connection(self):
        self.__connection = await self.__pool.acquire()
        print(f"Get a pool connection {self.__connection}!")

    def release_pool_connection(self, conn=None):
        if conn:
            self.__pool.release(conn)
        else:
            self.__pool.release(self.__connection)

    async def disconnect_pool(self):
        self.__pool.close()
        await self.__pool.wait_closed()
        print("Close the connection pool for the MySQL server!")

    async def create_cursor(self):
        self.__cursor = await self.__connection.cursor()
        return f"Create a new cursor object {self.__cursor} using the connection {self.__connection}!"

    async def close_cursor(self):
        await self.__cursor.close()
        return f"Close the cursor {self.__cursor}!"

    async def create_db(self, db_name):
        await self.__cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        return f"Database {db_name} created!"

    async def drop_db(self, db_name):
        await self.__cursor.execute(f"DROP DATABASE {db_name}")
        return f"Database {db_name} dropped!"

    async def process_query(self, query):
        await self.__cursor.execute(query)
        return f'Query "{query}" processed!'

    async def insert_records(self, query, data):
        print("Your data is inserting...")
        return await self.__cursor.executemany(query, data)

    async def fetch_all_records(self, query):
        await self.process_query(query)
        return await self.__cursor.fetchall()

    async def insert_dd(self, query, data):
        return await self.__cursor.execute(query, data)


async def show_db_info(loop):
    DB_CONFIG = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "hadooper",
        "password": "Test1234",
        "loop": loop
    }

    try:
        mysql = MySQL()

        await mysql.create_connection(DB_CONFIG)
        await mysql.create_cursor()

        query = "SELECT VERSION()"
        msg = await mysql.process_query(query)
        print(msg)

        result = await mysql.fetch_all_records(query)
        print(f'MySQL Database version: {result[0]}')

        await mysql.connection.commit()
        await mysql.close_cursor()
        mysql.disconnect_connection()

    except Exception as err:
        print(err)


async def show_db_class(loop):
    DB_CONFIG = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "hadooper",
        "password": "Test1234",
        "loop": loop
    }

    try:
        mysql = MySQL()

        await mysql.create_connection(DB_CONFIG)
        await mysql.create_cursor()

        query = "SELECT * from uml_resource.Class;"
        msg = await mysql.process_query(query)
        print(msg)

        result = await mysql.fetch_all_records(query)
        print('Class table data: \n', result)

        await mysql.connection.commit()
        await mysql.close_cursor()
        mysql.disconnect_connection()

    except Exception as err:
        print(err)


async def show_db_method(loop):
    DB_CONFIG = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "hadooper",
        "password": "Test1234",
        "loop": loop
    }

    try:
        mysql = MySQL()

        await mysql.create_connection(DB_CONFIG)
        await mysql.create_cursor()

        query = "SELECT * from uml_resource.Method;"
        msg = await mysql.process_query(query)
        print(msg)

        result = await mysql.fetch_all_records(query)
        print('Method table data: \n', result)

        await mysql.connection.commit()
        await mysql.close_cursor()
        mysql.disconnect_connection()

    except Exception as err:
        print(err)


async def show_db_attr(loop):
    DB_CONFIG = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "hadooper",
        "password": "Test1234",
        "loop": loop
    }

    try:
        mysql = MySQL()

        await mysql.create_connection(DB_CONFIG)
        await mysql.create_cursor()

        query = "SELECT * from uml_resource.Attribute;"
        msg = await mysql.process_query(query)
        print(msg)

        result = await mysql.fetch_all_records(query)
        print('Attribute table data: \n', result)

        await mysql.connection.commit()
        await mysql.close_cursor()
        mysql.disconnect_connection()

    except Exception as err:
        print(err)



async def show_db_all(loop):
    DB_CONFIG = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "hadooper",
        "password": "Test1234",
        "loop": loop
    }

    try:
        mysql = MySQL()

        await mysql.create_connection(DB_CONFIG)
        await mysql.create_cursor()

        query = "SELECT * from uml_resource.all_class;"
        msg = await mysql.process_query(query)
        print(msg)

        result = await mysql.fetch_all_records(query)
        return result

        await mysql.connection.commit()
        await mysql.close_cursor()
        mysql.disconnect_connection()

    except Exception as err:
        print(err)

async def process_transaction(mysql):
    if mysql.connection.get_autocommit():
        return

    try:
        await mysql.connection.begin()

        sql_query = 'CREATE DATABASE uml_resource;'
        msg = await mysql.process_query(sql_query)
        print(msg)


        sql_query = 'USE uml_resource;'
        msg = await mysql.process_query(sql_query)
        print(msg)

        sql_query = "CREATE TABLE IF NOT EXISTS `all_class` (`class_id` int(11) NOT NULL, `class_name` VARCHAR(45), `method_num` int(11), `attr_num` int(11))"
        msg = await mysql.process_query(sql_query)
        print(msg)

        sql_query = "CREATE TABLE IF NOT EXISTS `Class` (`class_id` int(11) NOT NULL, `class_name` varchar(45) DEFAULT NULL, PRIMARY KEY (`class_id`));"
        msg = await mysql.process_query(sql_query)
        print(msg)

        sql_query = "CREATE TABLE IF NOT EXISTS `Method` (`method_id` int(11) NOT NULL, `class_id` int(11) NOT NULL, `method_name` varchar(45) DEFAULT NULL, PRIMARY KEY (`method_id`));"
        msg = await mysql.process_query(sql_query)
        print(msg)

        sql_query = "CREATE TABLE IF NOT EXISTS `Attribute` (`attr_id` int(11) NOT NULL,`class_id` int(11) NOT NULL, `attr_name` varchar(45) DEFAULT NULL, PRIMARY KEY (`attr_id`));"
        msg = await mysql.process_query(sql_query)
        print(msg)

        data_all = [
            [1, 'CycleLog', 16, 4],
            [2, 'Ride', 4, 7]
        ]
        sql_query = "INSERT INTO all_class (class_id, class_name, method_num, attr_num) VALUES (%s, %s, %s, %s)"
        msg = await mysql.insert_records(sql_query, data_all)
        print(msg)

        my_data = Data_to_db()
        data_name = my_data.extract_name()
        sql_query = "INSERT INTO Class (class_id, class_name) VALUES (%s, %s)"
        msg = await mysql.insert_records(sql_query, data_name)
        print(msg)

        my_data = Data_to_db()
        data_method = my_data.extract_method()
        sql_query = "INSERT INTO Method (method_id, class_id, method_name) VALUES (%s, %s, %s)"
        msg = await mysql.insert_records(sql_query, data_method)
        print(msg)

        my_data = Data_to_db()
        data_attr = my_data.extract_attr()
        sql_query = "INSERT INTO Attribute (attr_id, class_id, attr_name) VALUES (%s, %s, %s)"
        msg = await mysql.insert_records(sql_query, data_attr)
        print(msg)

        await mysql.connection.commit()

    except Warning as w:
        pass

    except Exception as err:
        print(err)
        await mysql.connection.rollback()
        raise err

    finally:
        mysql.release_pool_connection()


async def demonstrate_connection_pool(loop):
    DB_POOL_CONFIG = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "hadooper",
        "password": "Test1234",
        "loop": loop,
        "maxsize": 100,
        "echo": True
    }
    try:
        mysql = MySQL()

        msg = await mysql.create_connection_pool(DB_POOL_CONFIG)
        print(msg)

        msg = await mysql.get_pool_connection()
        print(msg)

        msg = await mysql.create_cursor()
        print(msg)

        await process_transaction(mysql)

        msg = await mysql.close_cursor()
        print(msg)

        msg = await mysql.disconnect_pool()
        print(msg)

    except Exception as err:
        print(err)
        raise err


async def add_data(loop):
    print("You are running db_add_data...")
    await demonstrate_connection_pool(loop)


def test_connection():
    user = 'wrong_user'
    db = 'wrong_db'
    try:

        pymysql.connect(host="127.0.0.1",
                        user="hadooper",
                        passwd="Test1234",
                        db=db
        )
        pymysql.cursors()

        query = "SELECT VERSION()"
        msg = pymysql.cursors.Cursor.execute(query)
        print(msg)

        pymysql.connections.Connection.close()

    except pymysql.err.InternalError as e1:
        code, msg = e1.args
        if code == 1049:
            print('Your setting database:' + db, ' not exists, Please try again!')
        else:
            print("Please try again! The exception is: ", e1)

    except pymysql.err.OperationalError as e2:
        code, msg = e2.args
        if code == 1045:
            print('User: ' + user, 'not exists, Please try again!')
        else:
            print("Please try again! The exception is: ", e1)

    except Exception as err:
        print(err)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main(loop))
    print(result)
    loop.close()


