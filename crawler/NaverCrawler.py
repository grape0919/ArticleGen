import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from crawler.data.crawl_info import Url_info
import re
# import re
import urllib.parse
import urllib.request
import requests
import json
import time

from conf import conf
from ABCCrawler import ABCCrawler

from bs4 import BeautifulSoup

from data.article_info import *
class NaverCrawler(ABCCrawler):

    def __init__(self):
        super().__init__()

    def _ENGINE_TYPE(self) -> engine_type:
        return engine_type.NAVER

    def _api_url(self) -> str:
        return f"https://openapi.naver.com/v1/search/blog.json"

    def _api_input_params(self) -> dict:
        return {
            "query" : None,
            "display" : 100,
            "start" : 1
        }

    def _crawling_urls(self, keyword:str, num_of_target:int) -> ABCCrawler.URL_LIST:

        encText = urllib.parse.quote(keyword)
        url_list = []

        try:
            cnt = 0
            for i in range(int(num_of_target/100)+1, 0, -1):
                resultMax = 100
                if i == 1 :
                    resultMax = num_of_target%100

                self.set_param("query", encText)
                self.set_param("display", resultMax)
                self.set_param("start", i)

                response = self._request()
                rescode = response.getcode()
                if(rescode == 200):
                    response_body = response.read()
                    result = json.loads(response_body)
                    items = result['items']
                    for item in items:
                        link = item["link"]
                        title = item["title"]
                        postdate = item["postdate"]

                        url_list.append(Url_info(link, title, postdate))

                        cnt += 1

                    time.sleep(0.1)
                else:
                    print("Error Code:", rescode)
                    return None
            
            print("[INFO] success craw url : ", cnt)
        except Exception as e:
            print("[ERROR] NaverCrawler._crawling_urls : ", e)
            return None

        return url_list

    def _parse_article(self, url:Url_info) -> str:
        response = requests.get(url.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        frame = soup.find('iframe', {'id':'mainFrame'})
        if frame:
            frame_link = frame['src']

            frame_link = "https://blog.naver.com/"+frame_link
            response = requests.get(frame_link)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p', {'class':'se-text-paragraph'})

            article = []
            for pa in paragraphs:
                article.append(str(pa.getText()).strip().strip("\u200b"))

            article = re.sub('[\\s]+', ' ', str(" ".join(article)))

            return Article(engine_type.NAVER, None, frame_link, url.title, article, len(article), url.postdate)

        else:
            print("Not Found Frame :", url)
            return None

    def _req_header(self, request: urllib.request.Request) -> urllib.request.Request:
        request.add_header("X-Naver-Client-Id",conf.NAVER_CLIENT_ID)
        request.add_header("X-Naver-Client-Secret",conf.NAVER_CLIENT_SECRET_ID)
        return request

    def getNaverSearch(self, keyword:str, numofarticle=10): # return 타입 : string / 네이버검색결과 컨텐츠
        encText = urllib.parse.quote(keyword)
        article_list = []

        try:
            for i in range(int(numofarticle/100)+1, 0, -1):
                resultMax = 100
                if i == 1 :
                    resultMax = numofarticle%100

                url = f"https://openapi.naver.com/v1/search/blog.json?query={encText}&display={resultMax}&start={i}" # json 결과
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id",conf.NAVER_CLIENT_ID)
                request.add_header("X-Naver-Client-Secret",conf.NAVER_CLIENT_SECRET_ID)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                if(rescode == 200):
                    response_body = response.read()
                    result = json.loads(response_body)
                    items = result['items']
                    i = 0
                    for item in items:
                        i+=1
                        print("craw ", i)
                        link = item["link"]
                        title = item["title"]
                        postdate = item["postdate"]

                        response = requests.get(link)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        frame = soup.find('iframe', {'id':'mainFrame'})
                        if frame:
                            frame_link = frame['src']

                            frame_link = "https://blog.naver.com/"+frame_link
                            response = requests.get(frame_link)
                            soup = BeautifulSoup(response.text, 'html.parser')
                            paragraphs = soup.find_all('p', {'class':'se-text-paragraph'})

                            article = []
                            for pa in paragraphs:
                                article.append(str(pa.getText()).strip().strip("\u200b"))

                            article = re.sub('[\\s]+', ' ', str(" ".join(article)))

                            article_list.append(Article(engine_type.NAVER, None, frame_link, title, article, len(article), postdate))

                            time.sleep(0.1)
                        else:
                            print("Not Found Frame :", link)
                    return article_list
                else:
                    print("Error Code:", rescode)
            
        except Exception as e:
            return print("[ERROR] ", e)