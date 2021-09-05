from typing import Tuple
from crawler.data import engine_type


class Article():

    ID:int = -1
    URL:str = ""
    TITLE:str = ""
    ARTICLE:str = ""
    KEYWORD_ID:int = -1
    LENGTH:int = -1
    POSTDATE:str = ""
    CREATED_DATE:str = ""

    ENGINE:engine_type

    def __init__(self, ENGINE:engine_type, ID:int=-1, URL:str="", KEYWORD_ID:int = -1, TITLE:str=""
                    ,ARTICLE:str="", LENGTH:int=-1, POSTDATE:str="", CREATED_DATE:str = ""):
        self.ID = ID
        self.URL = URL
        self.KEYWORD_ID = KEYWORD_ID
        self.TITLE = TITLE.replace("'","\'")
        self.ARTICLE = ARTICLE.replace("'","\'")
        self.LENGTH = LENGTH
        self.POSTDATE = POSTDATE
        self.CREATED_DATE = CREATED_DATE
        self.ENGINE = ENGINE

    def to_tuple(self) -> Tuple[str, int, str, str, int, str]:#URL, KEYWORD_ID, TITLE, CONTENT, LENGTH, CREATED_DATE
        return (self.URL, self.KEYWORD_ID, self.TITLE, self.ARTICLE, self.LENGTH, self.POSTDATE)
class Keyword():

    ID:int = -1
    KEYWORD:str = ""

    def __init__(self, ID:int, KEYWORD:str):
        self.ID = ID
        self.KEYWORD = KEYWORD