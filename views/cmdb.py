# -*- coding:utf-8 -*-
# CREATE BY Zhou Xiangyu
from flask import Blueprint,current_app,render_template
import os
from models import cmdb as db

BASE_PATH = current_app.config.get("BASE_PATH")
cmdb = Blueprint("cmdb",__name__,template_folder=os.path.join(BASE_PATH,"templates/cmdb"))

@cmdb.route("/index",methods=["GET"])
def index():
    schema_info = db.getSchemaInfo()
    return render_template("index.html",infos=schema_info)