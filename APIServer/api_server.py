from crawler.GoogleCrawler import GoogleCrawler
from crawler.data import engine_type
from crawler.NaverCrawler import NaverCrawler
from sys import argv
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

        return {"status": "success"}

class Renew(Resource):
    # TODO : async 처리 필요
    def get(self):
        try:
            args = req_parser.parse_args()
            print("!@#!@# args : ", args)

            engine:str = args['engine']
            engine = engine.upper()

            

            if engine == engine_type.NAVER.name or engine == str(engine_type.NAVER.value):
                crawler = NaverCrawler()
            elif engine == engine_type.GOOGLE.name or engine == str(engine_type.GOOGLE.value):
                
                crawler = GoogleCrawler()


            article_list = crawler.proc(args['keyword'], args['num_of_target'])
            if article_list :
                print("!@#!@# complete craw")

                pass # db insert

            return {"status":"success"}

        except Exception as e:
            return {'error': str(e)}


class Renew_status(Resource):
    '''
    article renew 가 async로 작동하기 때문에 다음 작업을 위한 작업상태확인이 필요
    '''
    def get(self):
        return {"renew_status" : "running", "process" : "70% "}
        
api.add_resource(Article, '/article')
api.add_resource(Renew, '/dataset/renew')
api.add_resource(Renew_status, '/dataset/status')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
