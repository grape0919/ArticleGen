from rdbms.dbHandler import DBHandler
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

__all__ = [
    "query",
    "dbHandler"
]

try:
    db_handler = DBHandler()
except:
    pass
    # print("[ERROR] DB 에 연결을 실패하였습니다.")
    # sys.exit()