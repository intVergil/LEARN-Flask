# flask_tutorial

通过学习flask框架学习后端知识，选择flask的原因：

- 同时可以学习python
- flask轻巧，灵活，需要自己设定，更适合用来学习了解后端
- django更重，更适合快速开发，但也像rails一样更封闭些，不太适合初学

## 使用教程：

- Flask从入门到做出一个博客的大型教程（<https://blog.csdn.net/u014793102/article/details/80372815>）

## 使用环境：

- OSX 10.14.2
- shell zsh
- pyenv 1.2.8-5-gec9fb549
- virtualenv 16.1.0
- python 3.6.7
- Flask 1.0.2
- flask-wtf

## 项目结构

```shell
flask
├── app                   #项目文件夹
│   ├── templates         #view层
│       ├── base.html     #layout
│       └── index.html    #模版内容
│   ├── __init__.py       #项目初始化
│   └── routes.py         #主页路由
└── myblog.py             #项目入口
```

## 开始项目

- 启动flask：

```shell
source venv/bin/activate  #使用virtualenv进入虚拟环境
cd flask/                 #打开flask文件夹
flask run                 #启动flask
deactivate                #切出虚拟环境
```

## 学习笔记

### 1. 准备PYTHON环境

- #### pyenv : 管理python版本

  1. 安装pyenv

     `git clone git://github.com/yyuu/pyenv.git ~/.pyenv`

  2. 设置path（使用bash的话，于“.bash_profile”）

     ```shell
     echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
     echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
     echo 'eval "$(pyenv init -)"' >> ~/.zshrc
     ```

  3. 使用pyenv安装python 

     ```shell
     pyenv install --list  #查看所有版本
     pyenv install 3.6.7   #安装某版本
     pyenv rehash          #安装后更新一下
     pyenv global 3.6.7    #指定版本
     ```

     - 安装遇到问题
     ```shell
       yan53074@intVergil  ~   master ●  pyenv install 3.6.7
       python-build: use openssl from homebrew
       python-build: use readline from homebrew
       Downloading Python-3.6.7.tar.xz...
       -> https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz
       Installing Python-3.6.7...
       python-build: use readline from homebrew

       BUILD FAILED (OS X 10.14.2 using python-build 1.2.8-5-gec9fb549)

       Inspect or clean up the working tree at /tmp/python-build.20181224002925.28632
       Results logged to /tmp/python-build.20181224002925.28632.log

       Last 10 log lines:
         File "/private/tmp/python-build.20181224002925.28632/Python-3.6.7/Lib/ensurepip/__main__.py", line 5, in <module>
           sys.exit(ensurepip._main())
         File "/private/tmp/python-build.20181224002925.28632/Python-3.6.7/Lib/ensurepip/__init__.py", line 204, in _main
           default_pip=args.default_pip,
         File "/private/tmp/python-build.20181224002925.28632/Python-3.6.7/Lib/ensurepip/__init__.py", line 117, in _bootstrap
           return _run_pip(args + [p[0] for p in _PROJECTS], additional_paths)
         File "/private/tmp/python-build.20181224002925.28632/Python-3.6.7/Lib/ensurepip/__init__.py", line 27, in _run_pip
           import pip
       zipimport.ZipImportError: can't decompress data; zlib not available
       make: *** [install] Error 1
     ```

     - 解决方案1（失败）:

       `brew install zlib`

     - 解决方案2（失败）:

       `xcode-select --install`

     - 解决方案3（成功）：

       `CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install -v 3.6.7`

- #### virtualenv : 分离项目依赖版本

  1. `pip install virtualenv`

  2. 使用方法：

     ```shell
     #1.首先创建项目目录
     $ mkdir flask_tutorial
     $ cd flask_tutorial

     #2.创建项目的虚拟环境
     $ virtualenv --no-site-packages venv #会创建一个不带其他pip包的干净虚拟环境

     #3.切换到虚拟环境
     $ source venv/bin/activate
     (venv) yan53074@intVergil:/flask_tutorial$  # (venv)表示该项目处于虚拟环境中

     #4. 切出虚拟环境
     (venv) yan53074@intVergil:/myproject$ deactivate
     ```

### 2. 配置.gitignore

由于Python执行后产生的缓存文件也会加入到git，需要手动设置.gitignore不上传哪些文件。

- 注意：已push的部分已经加入管理行列，需要手动删除。

```.gitignore
# Python
__pycache__

# MAC
.DS_Store
```

### 3. 使用WTFORM制作表单

由于浏览器默认的require渲染会覆盖WTF的require，教程中的写法无法自定义验证反馈，需要将浏览器默认的require关闭。

- 在每一项表单中添加(required=False)属性

```html
  <p>
      {{ form.username.label }}<br>
      {{ form.username(size=32,required=False) }}<br>
      {% for error in form.username.errors %}
          <span style="color: red;">[{{ error }}]</span>
      {% endfor %}
  </p>
```

### 4. 数据库

使用flask插件链接model和数据库：

- flask-sqlalchemy
- flask-migrate
- pymysql