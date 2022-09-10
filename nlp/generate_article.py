import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.getcwd()))

from typing import List
from posText import POSifiedText
from crawler.data.article_info import Article
from crawler.NaverCrawler import NaverCrawler

def list_split(listA, n):
    return [tuple(listA[i:i+n]) for i in range(len(listA))]
class generator:

    _model:POSifiedText
    def makeMarkov(self, text = "", stLength = 15): # return 타입 : string / 섞은 후 컨텐츠
        
        text_model = self.generate_model(text)
        content = ""
        for i in range(stLength):
            makeSt = str(text_model.make_sentence())
            if(makeSt != "None"):
                content = content + makeSt
        return  content

    def generate_model(self, text, state_size:int = 2) -> POSifiedText:
        self._model = POSifiedText(text, state_size=state_size)
        text_model = self._model.compile()
        return text_model

    @property
    def get_model(self):
        return self._model

    def make_synonym(self, content):
        model = self.get_model
        key_list = list(list_split(model.word_split(content), model.state_size+1))
        synonym_result = []
        for k in key_list:
            item_list:dict = model.chain.model.get(tuple(k[:model.state_size]))
            if item_list and len(item_list) > 1:
                if k[-1] != list(item_list.keys())[1] and \
                    item_list.get(list(item_list.keys())[1]) > len(self.get_model.chain.model.keys())/10000:
                    synonym_result.append((k[-1],list(item_list.keys())[1]))
                else :
                    synonym_result.append(k[-1])
            else :
                synonym_result.append(k[-1])
        
        return self.get_model.word_join(synonym_result)


if __name__ == "__main__":
    srcPath = "cont.txt"
    with open(srcPath, encoding="utf-8") as f:
        text = f.read()
    genor = NaverCrawler()
    
    contents:List[Article] = genor.proc(keyword="선풍기", num_of_target=250)
    # print("!@#!@# cont = ", content)
    with open(srcPath, "w", encoding="UTF8") as file:
        for cont in contents:
            file.write(cont.ARTICLE + '\n')

    print("!@#!@# make article : ")
    doc_generator = generator()
    new_article = doc_generator.makeMarkov(text)

    with open("article.txt", "w", encoding="UTF8") as file:
        file.write(new_article)
    print("!@#!@# article = ", new_article)
    
    sentences_size = len(doc_generator.get_model.sentence_split(text))
    print("!@#!@# sn = ", doc_generator.make_synonym(new_article))

    # print(list_split(doc_generator.get_model.word_split(new_article), doc_generator.get_model.state_size))
    