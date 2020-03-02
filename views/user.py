# -*- coding:utf-8 -*-

from flask import Blueprint,session,request,render_template,current_app



#print(current_app.config['BASE_PATH'])
user=Blueprint("user",__name__,template_folder="../templates/user")

@user.route("/login",methods=["POST","GET"])
def login():
    user = request.form.get( "user" )
    pwd = request.form.get( "password" )
    if not user or not pwd :
        return render_template("login.html",error="user or pwd can not be null")
    else :
        session["user_info"] = user
    return "hello"

@user.route("/logout",methods=["POST","GET"])
def logout():
    del session["user_info"]
    return  "bye !"