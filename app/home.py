from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from app.auth import login_required
import requests
import random
bp_menu = Blueprint('home', __name__)

api = "70489895cb00438eb17a94daf6c20b15"

@bp_menu.route('/')
@login_required
def home():
    #Hacemos la petición
    url = ('https://newsapi.org/v2/top-headlines?'
           'pageSize=4&'
           'sources=abc-news&'
           'apiKey=70489895cb00438eb17a94daf6c20b15')
    response = requests.get(url)
    response = response.json()["articles"]
    return render_template("notice.html", notices = response)

@bp_menu.route('/cali/', methods = ["GET"])
@login_required
def cali():
    #No me dejas consultar porque toca que pagar
    y = "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=e1308dcbce732dbd5810045e28460c12"
    x = "https://api.openweathermap.org/data/3.0/onecall?lat=3.43722&lon=-76.5225&&appid=e1308dcbce732dbd5810045e28460c12"
    response = requests.get(y)
    response = response.json()
    return "hola mundo"


@bp_menu.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('auth.login'))