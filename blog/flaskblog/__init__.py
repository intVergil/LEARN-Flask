from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)

#添加配置信息
app.config.from_object(Config)
#建立数据库关系
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes,models