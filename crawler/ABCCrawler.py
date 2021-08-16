

from abc import ABCMeta, abstractmethod, abstractproperty
from typing import List, NewType

from conf import conf

import urllib.request

from data.article_info import *

class ABCCrawler(metaclass=ABCMeta):
    
    URL_LIST = NewType('URL_LIST', List[TYPE_URL])
    ARTICLE_LIST = NewType('ARTICLE_LIST', List[Article])

    @property
    @abstractmethod
    def api_input_args(self)->dict:
        ...

    @property
    @abstractmethod
    def api_url(self)->str:
        ...

    def __init__(self):
        pass

    @abstractmethod
    def crawling(self, api_input_args:api_input_args) -> URL_LIST:
        '''
        crawling article
        @param keyword
        @param num_of_article
        return url_list
        '''
        ...

    @abstractmethod
    def req_header(self, request:urllib.request.Request)->urllib.request.Request:
        ...

    def request(self):
        url = self.api_url
        url += "?"
        for arg in self.api_input_args.keys():
            url += "&" + str(arg) + "" + str(self.api_input_args[arg])

        request = urllib.request.Request(url)
        self.req_header(request)
        response = urllib.request.urlopen(request)
        return response

    @abstractmethod
    def parse_article(self, url:TYPE_URL) -> Article:
        '''
        parsing article in some page
        @param url : article url
        return article text
        '''
        ...

    def proc(self, api_input_args:api_input_args):
        '''
        
        '''
        url_list = self.crawling(api_input_args)
        for url in url_list:
            article = self.parse_article(url)
            self.insertArticle(url, article)
        

    def insertArticle(self, article:Article):
        '''
        function for insert article in database
        '''
        pass

    