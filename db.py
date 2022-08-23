import mysql.connector
from mysql.connector import errorcode, Error
import dotenv
import os

class DB:
    dotenv.load_dotenv(dotenv.find_dotenv())
    def __init__(self):
        host = os.getenv("HOST")
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        database = os.getenv("DATABASE")

        try:
            self.__conexao = mysql.connector.connect(host=host, user=user, password=password, database=database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def ExecuteSQL(self, sql, select=False):
        try:
            cursor = self.__conexao.cursor()
            cursor.execute(sql)
            if not select:
                self.__conexao.commit()
            return cursor
        except Error as err:
            print("SQL Error: ", err)
            return False

