
def tomweather() : 
    
    import requests
    import json
    import datetime
    import numpy as np
    import os
    from dotenv import load_dotenv

    load_dotenv()    
    weather_key = os.environ.get('WEATHER_KEY')
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

def dbinsert(userlog) :
    import psycopg2
    import os
    from dotenv import load_dotenv
    import pandas as pd

    load_dotenv()

    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    database = os.environ.get('DB_NAME')


 
    df = pd.read_csv('data.csv')

    conn = psycopg2.connect(database = database,host=host,password=password,user=user,port=5432)
    cur = conn.cursor()
    cur.execute("INSERT INTO userlog (log_date, p_temp, p_wind, p_hum, p_isholiday, p_count) VALUES (%s, %s, %s, %s, %s, %s);",(userlog[0],userlog[1],userlog[2],userlog[3],userlog[4],userlog[5]))
	

    conn.commit()
    conn.close()
    return print("complete!")

