import functools
from app.help.helpers import check_existence, register_user, get_users
from flask import  Blueprint, render_template, request, session, flash, redirect, url_for, g

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")

@bp_auth.route("/login/", methods = ["GET", "POST"])
def login():
    if g.user is None:
        if request.method == "POST":
            email = request.form["email"].replace(' ', '')
            password = request.form["password"].replace(' ', '')

            if not check_existence(email):
                flash("Correo electronico no valido [555]")
                return redirect(url_for("auth.login"))

            user =  get_users(email)
            if not user["password"] == password:
                flash("Clave y correo electronico incorrecto")
                return redirect(url_for("auth.login"))

            session.clear()
            session["email"] = user["email"]

            #Lo redirrecionamos a home
            flash("Inicio de sesiónn correctamente")
            return redirect(url_for("home.home"))
        else:
            return render_template("auth.html")

def login_required(view):
    @functools.wraps(view)
    def wrapped_views(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_views

@bp_auth.before_app_request
def load_logged_in_user():
    user_id = session.get('email')
    if user_id is None:
        g.user = None
    else:
        g.user =  get_users(user_id)

@bp_auth.route("/register/", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"].replace(' ', '')
        password = request.form["password"].replace(' ', '')

        if check_existence(email):
            flash("Correo electronico no valido [555]")
            return redirect(url_for("auth.register"))

        if register_user(email, password):
            flash(f"Usuario {email} creado corectamente")
            return redirect(url_for("auth.login"))

    return render_template("register.html")