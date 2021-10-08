
def tomweather() : 
    
    import requests
    import json
    import datetime
    import numpy as np
    import os
    from dotenv import load_dotenv
    load_dotenv()
    weather_key = os.getenv('WEATHER_KEY')
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid={weather_key}&lang=kr'
    raw = requests.get(url)
    parsed = json.loads(raw.text)

    now = datetime.datetime.now()
    tom =  str(now.year) +'-'+ str(now.month).zfill(2) +'-'+ str(now.day+1).zfill(2)

    temp = np.array([]) #
    wind = np.array([]) #m/s
    hum = np.array([]) #%
    for i in parsed['list']:
        if tom in i['dt_txt'] :
            temp = np.append(temp, round(i['main']['temp']-273.15,2))
            wind = np.append(wind, i['wind']['speed'])
            hum = np.append(hum, i['main']['humidity'])
    return {'temp' : round(temp.mean(),2), 'wind' : round(wind.mean(),2), 'hum' : round(hum.mean(),2)}