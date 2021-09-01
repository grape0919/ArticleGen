from rdbms.dbHandler import DBHandler
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

__all__ = [
    "query",
    "dbHandler"
]