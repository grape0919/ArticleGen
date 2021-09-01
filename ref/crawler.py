import urllib.parse
import urllib.request
import json

from conf.config import Config

def getNaverSearch(keyword, numofarticle): # return 타입 : string / 네이버검색결과 컨텐츠
    encText = urllib.parse.quote(keyword)

    if numofarticle <= 100: 

        resultMax = numofarticle
        url = f"https://openapi.naver.com/v1/search/blog.json?query={encText}&display={resultMax}&start=101" # json 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",Config.NAVER_CLIENT_ID)
        request.add_header("X-Naver-Client-Secret",Config.NAVER_CLIENT_SECRET_ID)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            result = json.loads(response_body)
            items = result['items']
            for item in items:
                link = item["link"]
                title = item["title"]
                description = item["description"]

                #db insert

        else:
            print("Error Code:" + rescode)
        # except Exception as e:
        #     content = ""
        #     return content