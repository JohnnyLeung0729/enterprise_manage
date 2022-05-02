import json

from flask import Blueprint, render_template, request
from flask_restful import Api, Resource

from ext import db
from models.Enterprise import Enterprise
from util.models import dict2user

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


# 添加管理企业信息    /add_enterprise
class AddEnterprise(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'datas[new_id - 1]'}


api.add_resource(AddEnterprise, '/add_enterprise')


# 查看在管企业清单   /list_enterprise
class ListEnterprise(Resource):
    def get(self):
        enters = Enterprise.query.all()
        print(enters)
        return {'code': 200, 'msg': 'ok', 'success': 'datas[new_id - 1]'}


api.add_resource(ListEnterprise, '/list_enterprise')


# 管理员用户登录   /login_user
class LoginUser(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'datas[new_id - 1]'}


api.add_resource(LoginUser, '/login_user')


# 添加管理员用户   /add_user
class AddUser(Resource):
    def post(self):
        u = request.get_json()
        us = json.dumps(u)
        user = json.loads(us, object_hook=dict2user)
        print(user)

        db.session.add(user)
        db.session.commit()
        return {'code': 200, 'msg': 'ok', 'success': 'datas[new_id - 1]'}


api.add_resource(AddUser, '/add_user')
