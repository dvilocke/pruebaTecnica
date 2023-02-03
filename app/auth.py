from flask import  Blueprint, render_template, request, session, flash, redirect, url_for, g

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")

@bp_auth.route("/login/", methods = ["GET", "POST"])
def login():
    return render_template("auth.html")

@bp_auth.route("/register/", methods = ["GET", "POST"])
def register():
    return render_template("register.html")