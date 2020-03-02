# -*- coding:utf-8 -*-
from flask import Flask,current_app
from .import  account
from . import user

app=Flask(__name__)
settings = app.config.from_object("configs.BaseConfig")
print(settings)
app.register_blueprint(account.account)
app.register_blueprint(user.user)
