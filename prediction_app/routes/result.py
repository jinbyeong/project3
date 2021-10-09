from flask import Blueprint, render_template, request
import joblib


resultbp=Blueprint('result',__name__)

@resultbp.route('/result', methods =['POST','GET'])
def index() : 
    if request.method == 'POST' :
        import joblib        
        from prediction_app.function.func import tomweather,dbinsert
        import datetime
        

        date = datetime.datetime.now()
        log = str(date) 
        form_data = request.form
        
        f = open('./prediction_app/lgbm.pkl','rb')
        loaded_model = joblib.load(f)
        dic = tomweather()
        input_data = [[dic['temp'],dic['wind'],dic['hum'],int(form_data['holiday'])]]
        result = loaded_model.predict(input_data)
        f.close()
        userlog = [log,dic['temp'],dic['wind'],dic['hum'],int(form_data['holiday']),round(result[0])]
        dbinsert(userlog)
        return render_template('result.html',prediction = round(result[0]))
        
