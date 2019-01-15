class Config(object):
    #设置密匙要没有规律，别被人轻易猜到哦
    SECRET_KEY = 'fc250564dbff802c0f210ff226a04323'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'