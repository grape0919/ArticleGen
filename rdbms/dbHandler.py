from datetime import datetime
from rdbms import query
from conf import conf
import pymysql
import pymysql.cursors

class DBHandler():

    _conn = None

    def __init__(self):
        self._database = pymysql.connect(
            user=conf.DB_USER,
            passwd=conf.DB_PASSWORD,
            host=conf.DB_HOST,
            port=conf.DB_PORT,
            db=conf.DB_DATABASE,
            charset="utf8"
        )

    @property
    def db_cursor(self):
        return self._database.cursor(pymysql.cursors.DictCursor)

    def select(self, sql):
        self.db_cursor.execute(sql)
        return self.db_cursor.fetchall()
    
    def insert(self, sql):
        self.db_cursor.execute(sql)
        self.commit()

    def commit(self):
        self._database.commit()

    def init_db(self):
        for q in self.split_multi_query(query.createQuery.INIT_QUERY):
            q = q.strip()
            if q :
                self.db_cursor.execute(q)
                self.commit()
        
    def split_multi_query(self, sqls:str):
        return sqls.split(";")

    def insert_keywords(self, keyword):
        self.db_cursor.execute(query.INSERT_KEYWORD, keyword)
        self.commit()

    def insert_article(self, engine:str, url:str, keyword_id:int, title:str, content:str, length:int):
        if engine == "NAVER":
            now = datetime.now()
            now.strftime('%Y-%m-%d %H:%M:%S')
            self.db_cursor.execute(query.INSERT_ARTICLE, (url, keyword_id, title, content, length, now))
            self.commit()
        else:
            print("!@#!@# 다른 엔진은 준비되지 않았습니다.")
        
    

if __name__ == "__main__":
    hendler = DBHandler()
    hendler.init_db()
    hendler.insert_keywords("선풍기")
    hendler.insert_article("NAVER", "url", 1, "선풍기 제목 1 ", "선풍기 글 1 ", 10)