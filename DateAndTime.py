from datetime import datetime, date, time
date = date.today()
now = datetime.now()
def Time():
    return now.strftime("%I : %M %p") 
    #timestamp = datetime.now().strftime('%H:%M:%S.%f')
def HourAs12():
    return str(now.strftime("%I"))
def HourAs24():
    return int(now.strftime("%H"))
def Minute():
    return str(now.strftime("%M"))
def Date():
    return str(datetime.now().strftime("%d-%m-%Y"))
def Day():
    return str(date.strftime("%A"))
#print(Time(), HourAs12(),HourAs24(), Minute(),Date(),Day())
