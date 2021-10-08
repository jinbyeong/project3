from flask import Blueprint
from prediction_app.function.func import tomweather


bp=Blueprint('home',__name__,url_prefix='/home')

@bp.route('/')
def index() : 
    dic = tomweather()
    
    return f"{dic['temp']}"
    
