import asyncio
import aiomysql


class MySQL:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    async def create_connection(self, db_config):
        self.__connection = await aiomysql.connect(**db_config)
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

    def execute_blob(self, sql, data):
        self.__cursor.process_query(sql, [sqlite3.Binary(data)])


async def testing_connection():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root'
    }

    mysql = MySQL()

    try:

        await mysql.create_connection(db_config)

    except Exception as err:
        print(err)


async def main():
    await testing_connection()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    result = loop.run_until_complete(main())
    print(result)

    loop.close()
