from flask import Flask

#创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc250564dbff802c0f210ff226a04323'

from app import routes