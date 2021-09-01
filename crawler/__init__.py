from crawler.ABCCrawler import ABCCrawler
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from NaverCrawler import NaverCrawler
from GoogleCrawler import GoogleCrawler

def get_crawler(engine_prefix:str = "Naver") -> ABCCrawler:

    crawler_class = getattr(sys.modules['crawler'], engine_prefix+'Job')

    return crawler_class()
