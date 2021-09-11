import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crawler.ABCCrawler import ABCCrawler
from NaverCrawler import NaverCrawler
from GoogleCrawler import GoogleCrawler

def get_crawler(engine_prefix:str = "Naver") -> ABCCrawler:

    crawler_name = engine_prefix+'Crawler'

    crawler_class = getattr(sys.modules[__name__+"."+crawler_name], crawler_name)
    print("!@#!@# crawler_class : ", crawler_class)
    obj = crawler_class()
    print("!@#!@# obj : ", obj)

    return crawler_class
