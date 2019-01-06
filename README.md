# flask_tutorial

通过学习flask框架学习后端知识，选择flask的原因：

- 同时可以学习python
- flask轻巧，灵活，需要自己设定，更适合用来学习了解后端
- django更重，更适合快速开发，但也像rails一样更封闭些，不太适合初学

## 使用教程：

- [Python Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

## 使用环境：

- OSX 10.14.2
- shell zsh
- pyenv 1.2.8-5-gec9fb549
- virtualenv 16.1.0
- python 3.6.7

## 项目结构

```bash
blog
├── app/                  #项目文件夹
│   ├── templates/        #view层文件夹
│   │   └── layout.html     #layout
│   ├── __init__.py       #项目初始化
│   └── routes.py         #主页路由
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