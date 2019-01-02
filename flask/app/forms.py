from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[InputRequired(message='请输入名户名')])
    password = PasswordField('密码',validators=[InputRequired(message='请输入密码')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')