import asyncio
import sqlite3
from database import sql_queries
from sqlite3 import Error

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

        self.loop = asyncio.get_running_loop()

    def sql_create_tables(self):
        if self.connection:
            print('database connected successfully')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)

    def sql_insert_user_command(self, telegram_id, username, first_name,
                                last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name,)
        )
        self.connection.commit()

    def sql_select_ban_user_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (telegram_id,)
        ).fetchall()

    def select_username(self, username):
        result = []
        query = f"""SELECT * FROM users WHERE username='{username}';"""

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
        except Error as e:
            print(e)
            return result

    async def async_select_username(self, username):
        return await self.loop.run_in_executor(None, self.select_username, username)

    def select_first_name(self, first_name):
        result = []
        query = f"""SELECT * FROM users WHERE first_name='{first_name}';"""

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
        except Error as e:
            print(e)
            return result

    async def async_select_first_name(self, first_name):
        return await self.loop.run_in_executor(None, self.select_first_name, first_name)

    def sql_update_ban_user_count_command(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_insert_ban_user_command(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, 1,)
        )
        self.connection.commit()

    def sql_insert_user_form_command(self, telegram_id, nickname, bio,
                                     age, occupation, married, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, age, occupation, married, photo,)
        )
        self.connection.commit()

    def sql_select_user_form_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "occupation": row[5],
            "married": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchall()

