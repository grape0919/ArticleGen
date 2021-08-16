
from typing import List
from nlp.posText import POSifiedText
from crawler.data.article_info import Article
from crawler.NaverCrawler import NaverCrawler
import markovify
import urllib.request
import urllib.parse
import json

class generator:

    @staticmethod
    def makeMarkov(mode = "file", srcPath = "textSource.txt", stLength = 15): # return 타입 : string / 섞은 후 컨텐츠
        text = ""
        print("src :", srcPath)

        if(mode == "file"):
            with open(srcPath, encoding="utf-8") as f:
                text = f.read()
        elif(mode == "str"):
            text = srcPath
        
        gen_doc = POSifiedText(text, state_size=3)
        text_model = gen_doc.compile() 

        # Print five randomly-generated sentences
        content = ""
        for i in range(stLength):
            makeSt = str(text_model.make_sentence())
            if(makeSt != "None"):
                content = content + makeSt
        return  content


    


if __name__ == "__main__":
    srcPath = "cont.txt"
    genor = NaverCrawler()
    contents:List[Article] = genor.getNaverSearch("선풍기", numofarticle=100)
    # print("!@#!@# cont = ", content)
    with open(srcPath, "w", encoding="UTF8") as file:
        for cont in contents:
            file.write(cont.ARTICLE + '\n')

    print("!@#!@# make article : ")
    new_article = generator.makeMarkov(mode="file", srcPath=srcPath)

    with open("article.txt", "w", encoding="UTF8") as file:
        file.write(new_article)
    print("!@#!@# article = ", new_article)
