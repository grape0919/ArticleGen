from crawler.data import engine_type
from datetime import datetime
from typing import List
from rdbms import query
from conf import conf
import pymysql
import pymysql.cursors

class DBHandler():

    _database = None

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
    
    def insert(self, sql, *args):
        self.db_cursor.execute(sql, (args))
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

    def insert_article(self, engine:engine_type, url:str, keyword_id:int, title:str, content:str, length:int):
        if engine == engine_type.NAVER:
            now = datetime.now()
            now.strftime('%Y-%m-%d %H:%M:%S')
            self.db_cursor.execute(query.INSERT_ARTICLE, (url, keyword_id, title, content, length, now))
            self.commit()
        else:
            print("!@#!@# 다른 엔진은 준비되지 않았습니다.")
        
    def multiple_insert_article(self,engine:engine_type, inputs:List[tuple[str, int, str, str, int]]):
        if engine == engine_type.NAVER:
            now = datetime.now()
            now.strftime('%Y-%m-%d %H:%M:%S')
            temp_inputs = []
            for i in inputs:
                temp = list(i)
                temp.append(now)
                print("!@#!@# debug : ", temp)
                temp_inputs.append(tuple(temp))

            print("!@#!@# debug : ", temp_inputs)
            self.db_cursor.executemany(query.INSERT_ARTICLE, temp_inputs)
            self.commit()
        else:
            print("!@#!@# 다른 엔진은 준비되지 않았습니다.")

    def count_article(self, engine:engine_type, keyword:str) -> int:
        if engine == engine_type.NAVER:
            count = self.select(query.COUNT_NAVER_ARTICLE, (keyword))
            return count
        else:
            print("!@#!@# 다른 엔진은 준비되지 않았습니다.")
            return 0

if __name__ == "__main__":
    handler = DBHandler()
    handler.init_db()
    # handler.insert_keywords("선풍기")
    # handler.multiple_insert_article(engine_type.NAVER, 
    #                         [("url1", 1, "선풍기 제목 1 ", "선풍기 글 1 ", 10),
    #                         ("url2", 1, "선풍기 제목 2 ", "선풍기 글 2 ", 10),
    #                         ("url3", 1, "선풍기 제목 3 ", "선풍기 글 3 ", 10),
    #                         ("url4", 1, "선풍기 제목 4 ", "선풍기 글 4 ", 10),
    #                         ("url5", 1, "선풍기 제목 5 ", "선풍기 글 5 ", 10)])