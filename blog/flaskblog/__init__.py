from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

#创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)

#添加配置信息
app.config.from_object(Config)
#建立数据库关系
db = SQLAlchemy(app)

from flaskblog import routes,models