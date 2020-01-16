1.安装Django：pip install Django
2.使用Pycharm创建Django项目   (  或者使用Django自带的命令安装： django-admin startproject 项目名  )
3.运行命令：python manage.py runserver 127.0.0.1:8080

项目目录
website   项目的容器
├── db.sqlite3
├── manage.py 管理Django项目执行的文    (一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。)。
├── readme.txt
├── templates 模板引擎
└── website
    ├── __init__.py 一个空文件，告诉 Python 该目录是一个 Python 包。
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── settings.cpython-37.pyc
    │   ├── urls.cpython-37.pyc
    │   └── wsgi.cpython-37.pyc
    ├── settings.py  Django 项目的设置/配置。
    ├── urls.py  请求路径映射配置文件
    └── wsgi.py  一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。