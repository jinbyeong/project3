from flask import Blueprint, render_template, request
import joblib


resultbp=Blueprint('result',__name__)

@resultbp.route('/result', method =['POST','GET'])
def index() : 
    if request.method == 'POST' :
        import joblib
        from prediction_app.function.func import tomweather
    
        loaded_model = joblib.load('lgbm.pkl')
        dic = tomweather()
        input_data = [dic['temp'],dic['wind'],dic['hum'],1] # 1 자리에 휴일 여부 받아서 예측
        result = loaded_model.predict(input_data)
        
        return render_template('result.html',prediction = result)
    
