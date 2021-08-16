from abc import ABC
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

    def api_url(self) -> str:
        return f"https://openapi.naver.com/v1/search/blog.json"

    def api_input_args(self) -> dict:
        return {
            "query":"",
            "display":10,
            "start":1
        }

    def crawling(self, keyword: str, num_of_article: int, start_page: int) -> ABCCrawler.URL_LIST:

        return super().crawling(keyword, num_of_article=num_of_article, start_page=start_page)

    def parse_article(self, url: TYPE_URL) -> TYPE_ARTICLE:
        return super().parse_article(url)
    
    def req_header(self, request: urllib.request.Request) -> urllib.request.Request:
        request.add_header("X-Naver-Client-Id",conf.NAVER_CLIENT_ID)
        request.add_header("X-Naver-Client-Secret",conf.NAVER_CLIENT_SECRET_ID)
        return request

    def getNaverSearch(self, keyword:str, numofarticle=10): # return 타입 : string / 네이버검색결과 컨텐츠
        encText = urllib.parse.quote(keyword)
        article_list = []

        print("Start craw : ", numofarticle)

        # if numofarticle <= 100: 

        resultMax = numofarticle
        url = f"https://openapi.naver.com/v1/search/blog.json?query={encText}&display={resultMax}&start=1" # json 결과
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

                    article_list.append(Article(frame_link, title, article, postdate))

                    time.sleep(0.1)
                else:
                     print("Not Found Frame :", link)
            print("!@#!@# article_list :", article_list)
            return article_list
        else:
            print("Error Code:", rescode)
        # except Exception as e:
        #     content = ""
        #     return content