# blog分支

- 参考教程：[Python Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

## 项目结构

```bash
blog
├── app/                  #项目文件夹
│   ├── templates/        #view层文件夹
│   │   └── layout.html     #layout
│   ├── __init__.py       #项目初始化
│   ├── routes.py         #主页路由
│   └── forms.py          #表单文件
└── flaskblog.py          #项目入口
```

## 开始项目`

- 启动flask：

```bash
$ source venv/bin/activate  #使用virtualenv进入虚拟环境
$ cd flask/                 #打开flask文件夹
$ flask run                 #启动flask
$ deactivate                #切出虚拟环境
```

## 学习笔记

### 1. Getting Started

```bash
$ export FLASK_APP=flaskblog      #指定启动文件
$ export FLASK_DEBUG=1            #开启debut模式
```

### 2. Templates

#### 渲染html

```python
#blog/app/routes.py
from flask import render_template                      #使用render_template方法
...
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)   #指定模版文件，传入数据
```

#### Layout模版

- 设置layout模版：`{% block content %}{% endblock %}`
- 使用指定layout模版：`{% extends "layout.html" %} {% block content %}{% endblock content%}`

#### static文件引入

- 设置PATH：`url_for('static', filename='main.css')`

### 3. Form and User input

使用flask-wtf，基本流程：

- 创建表单：forms.py              #class 表单名
- 创建路由：routes.py             #form = 表单名(), render_template(posts=posts)
- 创建模版：templates/*.html      #{{ form.栏目名(required=False) }}

使用flash，基本流程：

- 添加flash至模版：templates/layout.html    #`{% with messages = get_flashed_messages(with_categories=true) %}{% endwith %}`
- 添加flash规则：routes.py                  #`flash(f'反馈信息 {form.栏目名.data}!', 'success')`
  - 跳转其他页面显示flash信息：                 #`return redirect(url_for('home'))`

### 4. Database with Flask-SQLAlchemy

使用Flask-SQLAlchemy创建数据库，这里使用sqlite

### 5. Package Structure

整理文件，不过我一开始就整理好了。