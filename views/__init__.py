# -*- coding:utf-8 -*-
from flask import Flask
from configs import BaseConfig,DBConfig
app=Flask(__name__)
app.config.from_object(BaseConfig)
app.config.from_object(DBConfig)
app.app_context().push()

from . import  account
from . import user
from . import cmdb
app.register_blueprint(account.account)
app.register_blueprint(user.user)
app.register_blueprint(cmdb.cmdb)

