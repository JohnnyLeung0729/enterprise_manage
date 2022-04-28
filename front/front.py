from flask import Blueprint, render_template
from flask_restful import Api, Resource

front = Blueprint('front', __name__, template_folder='views')

api = Api(front)

datas = [{'id': 1, 'name': 'xag', 'age': 18}, {'id': 2, 'name': 'xingag', 'age': 19}]


@front.route('/index')
def index():
    return render_template('index.html')

# 测试接口，restful_API
class EnterpriseView(Resource):
    def get(self):
        return {'code': 200, 'msg': 'success', 'data': datas}


api.add_resource(EnterpriseView, '/enterprise')


# 添加管理企业信息
class Add_Enterprise(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'datas[new_id - 1]'}


api.add_resource(Add_Enterprise, '/add_enterprise')