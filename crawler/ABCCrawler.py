

from abc import ABCMeta, abstractclassmethod, abstractmethod, abstractproperty
from argparse import ArgumentParser
from markovify.text import ParamError

from requests import api
from crawler.data.crawl_info import Url_info
from typing import List, NewType

import urllib.request

from data.article_info import *

import time
class ABCCrawler(metaclass=ABCMeta):
    
    '''
    크롤러 추상 클래스
    요청 : NAVER, GOOGLE
    해당 클래스를 구현하는 것으로 다른 사이트의 article을 수집하여 해당 api에서 사용할 수 있다.
    '''

    __params:dict = {}

    def __init__(self):
        self.__params = self._api_input_params(self)

    @abstractclassmethod
    def _api_input_params(self)->dict:
        ...

    @classmethod
    def set_param(self, key, value):
        if key in self._api_input_params(self):
            self.__params.update({key:value})
        else :
            print("[ERROR] 잘못된 파라메터입니다. : ", key)
            print("[ERROR] 파라메터 리스트 (None은 필수 파라메터입니다.) : ", self._api_input_params(self))

        print("!@#!@# set param : ", key, " : ", value)
        print("!@#!@# param : ", self.__params)

    def __check_validate(self):
        print("!@#!@# 요청 파라메터 : ", self.__params)
        for k, v in self.__params.items():
            if not v :
                return False
        
        return True
            

    @abstractclassmethod
    def _api_url(self)->str:
        ...

    @property
    def api_url(self)->str:
        return self._api_url()

    @abstractclassmethod
    def _ENGINE_TYPE(self) -> engine_type:
        ...
    
    @property
    def ENGINE_TYPE(self) ->engine_type:
        return self._ENGINE_TYPE()

    def __init__(self):
        pass

    @abstractclassmethod
    def _crawling_urls(self, keyword:str, num_of_target:int) -> List[Url_info]:
        '''
        crawling article
        @param dynamic param each son classes
        return url_list
        '''
        ...

    @abstractmethod
    def _req_header(self, request:urllib.request.Request)->urllib.request.Request:
        ...

    def _request(self):

        if self.__check_validate(self):

            url = str(self._api_url(self))
            url += "?"
            for k, v in self.__params.items():
                url += "&" + str(k) + "=" + str(v)

            print("!@#!@# request : ", url)
            request = urllib.request.Request(url)
            self._req_header(self, request)
            response = urllib.request.urlopen(request)

            self.__params = self._api_input_params(self)
            return response

        else:
            print("[ERROR] 요청 파라매터가 적절하지 않습니다. ")

    @abstractclassmethod
    @abstractmethod
    def _parse_article(self, url:str) -> Article:
        '''
        parsing article in some page
        @param url : article url
        return article text
        '''
        ...

    @classmethod
    def proc(self, keyword:str, num_of_target:int) -> List[Article]:
        
        url_list = self._crawling_urls(self, keyword=keyword, num_of_target=num_of_target)
        articles = []
        for url in url_list:
            if url:
                article = self._parse_article(self, url)
        
                if article :
                    articles.append(article)

        return articles


    