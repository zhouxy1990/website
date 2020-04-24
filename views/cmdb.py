# -*- coding:utf-8 -*-
# CREATE BY Zhou Xiangyu
from flask import Blueprint,current_app,render_template,request
import os
from models import cmdb as db

BASE_PATH = current_app.config.get("BASE_PATH")
cmdb = Blueprint("cmdb",__name__,
                 template_folder=os.path.join(BASE_PATH,"templates/cmdb"),
                 static_folder=os.path.join(BASE_PATH,"statics"),
                 )

@cmdb.route("/index",methods=["GET"])
def index():
    schema_info = db.getSchemaInfo()
    return render_template("index.html",infos=schema_info)

@cmdb.route("/detail",methods=["GET"])
def detail():
    id = request.args.get("id")
    detail_info = db.getDetailBySchemaId(id)
    page = current_app.config.get("PAGE_DICT").get(id)
    if not page :
        render_template("404.html")
    return render_template(page,detail_info=detail_info)