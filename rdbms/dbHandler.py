from conf import conf
import pymysql

class DBHandler():

    def __init__(self):
        self.database = pymysql.connect(
            user=conf.DB_USER,
            passwd=conf.DB_PASSWORD,
            host=conf.DB_HOST,
            db=conf.DB_DATABASE,
            charset="utf8"
        )
