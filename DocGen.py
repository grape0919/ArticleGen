import markovify
import urllib.request
import urllib.parse
import json

class articlesGenerator:
    def __init__(self, client_id = 'iLSTcLpJKsaBETLkEHOq', client_secret = '_SBXwc4_ht'):
        self.client_id = client_id 
        self.client_secret = client_secret

    def getNaverSearch(self, keyword): # return 타입 : string / 네이버검색결과 컨텐츠
        encText = urllib.parse.quote(keyword)
        resultMax = 100
        url = f"https://openapi.naver.com/v1/search/blog?query={encText}" # json 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",self.client_id)
        request.add_header("X-Naver-Client-Secret",self.client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            result = json.loads(response_body)
            content = ""
            for r in result['items']:
                content = content + r["description"]
            filterList = ["<b>", "</b>", "...", "..", "[", "]", "(", ")", "{", "}", "18", "토토", "년"]
            for fItem in filterList:
                content = content.replace(fItem, "")
            return content
        else:
            print("Error Code:" + rescode)
        # except Exception as e:
        #     content = ""
        #     return content

    def makeMarkov(self, mode = "file", srcPath = "textSource.txt", stLength = 15): # return 타입 : string / 섞은 후 컨텐츠
        text = ""
        if(mode == "file"):
            with open(srcPath, encoding="utf-8") as f:
                text = f.read()
        elif(mode == "str"):
            text = srcPath
        # Build the model.
        text_model = markovify.Text(text)
        text_model = text_model.compile() 

        # Print five randomly-generated sentences
        content = ""
        for i in range(stLength):
            makeSt = str(text_model.make_sentence())
            if(makeSt != "None"):
                content = content + makeSt
            #print(text_model.make_sentence())
        return  content


if __name__ == "__main__":
    genor = articlesGenerator()
    content = genor.getNaverSearch(keyword="선풍기")
    print("!@#!@# cont = ", content)
    with open("cont.txt", "w", encoding="UTF8") as file:
        file.write(content)

    article = genor.makeMarkov("str", content)

    with open("article.txt", "w", encoding="UTF8") as file:
        file.write(article)
    print("!@#!@# article = ", article)