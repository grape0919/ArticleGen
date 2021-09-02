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
        self.TITLE = TITLE
        self.ARTICLE = ARTICLE
        self.LENGTH = LENGTH
        self.POSTDATE = POSTDATE
        self.CREATED_DATE = CREATED_DATE
        self.ENGINE = ENGINE

class Keyword():

    ID:int = -1
    KEYWORD:str = ""

    def __init__(self, ID:int, KEYWORD:str):
        self.ID = ID
        self.KEYWORD = KEYWORD