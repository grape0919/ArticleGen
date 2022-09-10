__all__ = [
    "query",
    "dbHandler"
]
import traceback
from rdbms.dbHandler import DBHandler
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


try:
    db_handler = DBHandler()
except Exception as e:
    traceback.print_exc(e)
    print("[ERROR] DB 에 연결을 실패하였습니다.")
    sys.exit()