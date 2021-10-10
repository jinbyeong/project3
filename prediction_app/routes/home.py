from flask import Blueprint, render_template, request
from prediction_app.function.func import tomweather


homebp=Blueprint('home',__name__)

@homebp.route('/',methods = ['GET','POST'])
def index() : 
    dic = tomweather()
    
    return render_template('index.html')
    
