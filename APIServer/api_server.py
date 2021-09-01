from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restful import Api, Resource, reqparse  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

req_parser = reqparse.RequestParser()
req_parser.add_argument('keyword', type=str)
req_parser.add_argument('numoftarget', type=str)
req_parser.add_argument('engine', type=str)
req_parser.add_argument('power', type=int)
class Article(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환

        args = req_parser.parse_args()
        print("!@#!@# args : ", args)

        return {"status": "success"}

class Renew(Resource):
    def get(self):
        try:
            args = req_parser.parse_args()

            return {""}
        except Exception as e:
            return {'error': str(e)}


class Renew_status(Resource):
    def get(self):
        return {"renew_status" : "running"}
        
api.add_resource(Article, '/article')
api.add_resource(Renew, '/dataset/renew')
api.add_resource(Renew_status, '/dataset/status')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
