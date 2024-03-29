INIT_QUERY = \
"""
DROP TABLE IF EXISTS GOOGLE_ARTICLES CASCADE;
DROP TABLE IF EXISTS NAVER_ARTICLES CASCADE;
DROP TABLE IF EXISTS KEYWORDS CASCADE;


CREATE TABLE KEYWORDS(
    ID INT NOT NULL AUTO_INCREMENT,
    KEYWORD NVARCHAR(50) NOT NULL,
    PRIMARY KEY(ID, KEYWORD)
);


CREATE TABLE NAVER_ARTICLES(
    ID INT NOT NULL AUTO_INCREMENT,
    URL NVARCHAR(1000) NOT NULL,
    KEYWORD_ID INT NOT NULL,
    TITLE TEXT,
    CONTENT TEXT,
    LENGTH INT,
    CREATED_DATE DATETIME,
    FOREIGN KEY (KEYWORD_ID) REFERENCES KEYWORDS (ID),
    UNIQUE KEY (ID, KEYWORD_ID),
    PRIMARY KEY(ID, URL)
);


CREATE TABLE GOOGLE_ARTICLES(
    ID INT NOT NULL AUTO_INCREMENT,
    URL NVARCHAR(1000) NOT NULL,
    KEYWORD_ID INT NOT NULL,
    TITLE TEXT,
    CONTENT TEXT,
    LENGTH INT,
    CREATED_DATE DATETIME,
    FOREIGN KEY (KEYWORD_ID) REFERENCES KEYWORDS (ID),
    UNIQUE KEY (ID, KEYWORD_ID),
    PRIMARY KEY(ID, URL)
);

CREATE INDEX idx_keyword ON KEYWORDS ( ID, KEYWORD );

CREATE INDEX idx_article_keyword1 ON NAVER_ARTICLES ( ID, KEYWORD_ID );

CREATE INDEX idx_article_keyword2 ON GOOGLE_ARTICLES ( ID, KEYWORD_ID );
"""