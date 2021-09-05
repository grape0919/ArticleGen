
from rdbms import db_handler
import crawler
from crawler import get_crawler
from crawler.data import engine_type
from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restful import Api, Resource, reqparse  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

req_parser = reqparse.RequestParser()
req_parser.add_argument('keyword', type=str)
req_parser.add_argument('num_of_target', type=str)
req_parser.add_argument('engine', type=str)
req_parser.add_argument('power', type=int)
class Article(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환

        args = req_parser.parse_args()
        print("!@#!@# args : ", args)

        engine = args['engine']
        engine = engine.lower()
        
        return {"status": "success"}

class Renew(Resource):
    # TODO : async 처리 필요
    def get(self):
        # try:
        args = req_parser.parse_args()

        engine = args['engine']
        engine = engine[0].upper() + engine[1:].lower()
    
        crawler = get_crawler(engine)

        keyword = args['keyword']
        num_of_target = args['num_of_target']

        if not keyword or not num_of_target:
            return {"error":"wrong input"}
        article_list = crawler.proc(keyword = keyword, num_of_target = int(num_of_target))
        if article_list :
            print("!@#!@# complete craw")

            pass # db insert

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

            count = db_handler.count_article(engine, args['keyword'])
            return {'count': count}
        except Exception as e:
            return {'error':str(e)}
        
        
api.add_resource(Article, '/article')
api.add_resource(Count_article, '/article/count')
api.add_resource(Renew, '/dataset/renew')
api.add_resource(Renew_status, '/dataset/status')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)