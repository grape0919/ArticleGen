
from generate_article import generator
from rdbms import db_handler
import crawler
from crawler import get_crawler
from crawler.data import engine_type
from flask_restful import Resource, reqparse  # Api 구현을 위한 Api 객체 import
from APIServer import api


req_parser = reqparse.RequestParser()
req_parser.add_argument('keyword', type=str)
req_parser.add_argument('num_of_target', type=str)
req_parser.add_argument('mode', type=str)
req_parser.add_argument('engine', type=str)
req_parser.add_argument('power', type=int)

class Generate_Article(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환

        args = req_parser.parse_args()

        engine = "naver"
        display = 1
        mode = "spin"
        power = 1

        try:
            engine = args['engine']
        except:
            pass

        engine = engine.lower()

        try:
            display = args['num_of_target']
            display = int(display)
        except:
            pass
        try:
            mode = args['mode']
        except:
            pass
        try:
            power = args['power']
        except:
            pass
        try:
            keyword = args['keyword']
        except:
            print("[ERROR] 생성에 사용할 문서가 없습니다.")
            return {"error" : "wrong keyword."}
            
        if engine == "naver":
            base_articles = db_handler.get_naver_articles(keyword, power)
            if base_articles:
               base_articles = "\n".join([ a['CONTENT'] for a in base_articles ])
            else :
                print("!@#!@# 수집된 문서가 없습니다.")
                return {"error" : "we don't have crawled documents. You must request crawling document first."}

        new_articles = []

        doc_generator = generator()

        for i in range(display):
            new_article = doc_generator.makeMarkov(base_articles)

            if mode == "spin":
                new_article = doc_generator.make_synonym(new_article)
        
            new_articles.append({
                "articleNo":i,
                "articleText":new_article,
                "articleLen":len(new_article)})

        return new_articles

class Renew(Resource):
    # TODO : async 처리 필요 
    def get(self):
        # try:
        args = req_parser.parse_args()

        engine = args['engine']
        engine = engine[0].upper() + engine[1:].lower()
        keyword = args['keyword']
        num_of_target = args['num_of_target']

        if args['mode'] and args['mode'] == 'clear':
            db_handler.delete_article(keyword = keyword)
    
        crawler = get_crawler(engine)

        if not keyword or not num_of_target:
            return {"error":"wrong input"}

        try:
            article_list = crawler.proc(keyword = keyword, num_of_target = int(num_of_target))
        except:
            {"error":"Failed crawling"}
        try:
            if article_list:
                db_handler.multiple_insert_article(engine_type(engine.upper()), keyword ,article_list)
        except:
            {"error":"Failed data insert into db"}

        return {"status":"success"}

        # except Exception as e:
        #     print("[ERROR] ", e)
        #     return {'error': str(e)}


class Renew_status(Resource):
    '''
    article renew 가 async로 작동하기 때문에 다음 작업을 위한 작업상태확인이 필요
    '''
    def get(self):
        return {"renew_status" : "running", "process" : "70% "}

class Count_article(Resource):
    def get(self):
        try:
            args = req_parser.parse_args()

            engine = args['engine']
            engine = engine_type(engine.upper())
            if engine == engine_type.NAVER:
                count = db_handler.count_naver_article(engine)
            else:
                return {"error":"wrong input"}

            return {'count': count}
        except Exception as e:
            return {'error':str(e)}
        
        

api.add_resource(Generate_Article, '/article')
api.add_resource(Count_article, '/article/count')
api.add_resource(Renew, '/dataset/renew')
api.add_resource(Renew_status, '/dataset/status')
