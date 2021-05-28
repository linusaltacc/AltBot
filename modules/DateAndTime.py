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
def Day():
    return str(date.today().strftime("%A"))
def Date():
    return str(datetime.now().strftime("%d-%m-%Y"))
#print(Time(), HourAs12(),HourAs24(), Minute(),Date(),Day())
