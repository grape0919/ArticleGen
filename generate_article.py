import markovify
import urllib.request
import urllib.parse
import json

class generator:
    def __init__(self, client_id = 'iLSTcLpJKsaBETLkEHOq', client_secret = '_SBXwc4_ht'):
        self.client_id = client_id 
        self.client_secret = client_secret

    

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
    # print("!@#!@# cont = ", content)
    with open("cont.txt", "w", encoding="UTF8") as file:
        file.write(content)

    # article = genor.makeMarkov("str", content)

    # with open("article.txt", "w", encoding="UTF8") as file:
    #     file.write(article)
    # print("!@#!@# article = ", article)