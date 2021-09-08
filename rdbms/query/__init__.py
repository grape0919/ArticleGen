
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import createQuery


INSERT_ARTICLE =\
"""
INSERT INTO NAVER_ARTICLES(URL, KEYWORD_ID, TITLE, CONTENT, LENGTH, CREATED_DATE) VALUES (%s, %s, %s, %s, %s, %s);
"""

INSERT_KEYWORD =\
"""
INSERT INTO KEYWORDS(KEYWORD) VALUES (%s);
"""

COUNT_NAVER_ARTICLE = \
"""
select B.KEYWORD kid, COUNT(0) count FROM NAVER_ARTICLES A
LEFT JOIN KEYWORDS B ON B.ID = A.KEYWORD_ID
group by kid;
"""

SELECT_KEYWORD_ID =\
"""
SELECT ID FROM KEYWORDS WHERE KEYWORD=%s;
"""

DELETE_NAVER_ARTICLES =\
"""
DELETE FROM NAVER_ARTICLES WHERE KEYWORD_ID=(SELECT KEYWORD_ID FROM KEYWORDS WHERE KEYWORD=%s);
"""

SELECT_NAVER_ARTICLES = \
"""
SELECT CONTENT FROM NAVER_ARTICLES WHERE KEYWORD_ID=(SELECT ID FROM KEYWORDS WHERE KEYWORD=%s) order by rand() LIMIT %s;
"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    