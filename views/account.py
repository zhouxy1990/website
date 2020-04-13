# -*- coding:utf-8 -*-
from flask import Blueprint,session,redirect


account = Blueprint("account",__name__,url_prefix="/acc")

@account.route("/balance",methods=["GET"])
def balance():
    return "10 yuan"

@account.before_request
def process_request():
    if session.get("user_info"):
        return None
    return redirect("/login")


