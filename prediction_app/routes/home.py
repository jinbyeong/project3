from flask import Blueprint
from prediction_app.function.func import tomweather


homebp=Blueprint('home',__name__)

@homebp.route('/')
def index() : 
    dic = tomweather()
    
    return f"{dic}"
    
