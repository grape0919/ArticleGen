
from typing import NewType

TYPE_URL = NewType('URL', str)
TYPE_TITLE = NewType('TITLE', str)
TYPE_ARTICLE = NewType('ARTICLE', str)
TYPE_POSTDATE = NewType('POST', str)

class Article():

    URL:TYPE_URL = ""
    TITLE:TYPE_TITLE = ""
    ARTICLE:TYPE_ARTICLE = ""
    POSTDATE:TYPE_POSTDATE = ""


    def __init__(self, URL:TYPE_URL, TITLE:TYPE_TITLE,
                    ARTICLE:TYPE_ARTICLE, POSTDATE:TYPE_POSTDATE):
        self.URL = URL
        self.TITLE = TITLE
        self.ARTICLE = ARTICLE
        self.POSTDATE = POSTDATE
