
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
SELECT COUNT(0) FROM NAVER_ARTICLES WHERE KEYWORD_ID=(SELECT KEYWORD_ID FROM KEYWORDS WHERE KEYWORD=%s);
"""

SELECT_KEYWORD_ID =\
"""
SELECT ID FROM KEYWORDS WHERE KEYWORD=%s;
"""