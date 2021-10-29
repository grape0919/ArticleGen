import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crawler.ABCCrawler import ABCCrawler
from NaverCrawler import NaverCrawler

def get_crawler(engine_prefix:str = "Naver") -> ABCCrawler:

    crawler_name = engine_prefix+'Crawler'

    crawler_class = getattr(sys.modules[__name__+"."+crawler_name], crawler_name)
    obj = crawler_class()

    return crawler_class
