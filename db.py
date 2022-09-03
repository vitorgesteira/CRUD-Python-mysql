import mysql.connector
from mysql.connector import errorcode, Error
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class DB:
    config = dotenv_values('.env')
    def __init__(self):
        host = DB.config.get("HOST")
        user = DB.config.get("USER")
        password = DB.config.get("PASSWORD")
        database = DB.config.get("DATABASE")
        self.__conexao = None

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

    def get_conexao(self):
        return self.__conexao