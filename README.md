# flask_tutorial

通过学习flask框架学习后端知识，选择flask，同时可以学习python。

主流python框架：

- flask：插件式，轻巧，灵活，需要自己设定，更适合用来学习了解后端
- Bottle：原型开发，学习Web框架组织以及构建简单个人应用的完美解决方案。
- django：全栈式，更重，更适合快速开发，但也像rails一样更封闭些，不太适合初学
- Tornado：异步网络库，据说配置正确，它可以处理10,000多个并发连接
- TurboGears：数据驱动的全栈Web应用程序框架。
- Pyramid：主要目标是尽可能以最小的复杂性进行操作。
- CherryPy：极简主义，待研究。

## 分支说明：

- virtualenv：
  - [Flask从入门到做出一个博客的大型教程](https://blog.csdn.net/u014793102/article/details/80372815)
- blog：
  - [Python Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

## 使用环境：

- OSX 10.14.2
- shell zsh
- pyenv 1.2.8-5-gec9fb549
- virtualenv 16.1.0
- python 3.6.7

## 开始项目

- 安装插件：

```shell
virtualenv --no-site-packages venv
source venv/bin/activate
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
pip install pymysql
pip install flask_login
```

- 启动flask：

```shell
source venv/bin/activate  #使用virtualenv进入虚拟环境
cd flask/                 #打开flask文件夹
flask run                 #启动flask
deactivate                #切出虚拟环境
```