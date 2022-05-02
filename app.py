from flask import Flask

from ext import db
from models.Enterprise import Enterprise
from admin.admin import admin as admin_blueprint
from front.front import front as front_blueprint
from util import crypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Ly818379@localhost:3306/entermanagesys"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(admin_blueprint)
app.register_blueprint(front_blueprint)

db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    enters = Enterprise.query.all()

    print(enters[0])
    return enters[0].nsrsbh


if __name__ == '__main__':
    app.run()
