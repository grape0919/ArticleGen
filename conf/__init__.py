
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import Config

conf:Config = Config()
conf.load()
