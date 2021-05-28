from datetime import datetime, date, time

def Time():
    now = datetime.now()
    return now.strftime("%I : %M %p") 
    #timestamp = datetime.now().strftime('%H:%M:%S.%f')
def HourAs12():
    now = datetime.now()
    return str(now.strftime("%I"))
def HourAs24():
    now = datetime.now()
    return int(now.strftime("%H"))
def Minute():
    now = datetime.now()
    return int(now.strftime("%M"))
def Date():
    return str(datetime.now().strftime("%d-%m-%Y"))
def Day():
    date = date.today()
    return str(date.strftime("%A"))
#print(Time(), HourAs12(),HourAs24(), Minute(),Date(),Day())
