from modules.DateAndTime import *
import xlrd
# To open Workbook for class schedule
wb = xlrd.open_workbook('classSchedulle.xls')
sheet = wb.sheet_by_index(0)

def TimeTable():
    now, hour, minute, day = datetime.now(), int(HourAs24()), int(Minute()), Day() 
    temp = "other Days"
    if day == 'Monday':
        dayy = 1
    elif day == 'Tuesday':
        dayy = 2
    elif day == 'Wednesday':
        dayy = 3
    elif day == 'Thursday':
        dayy = 4
    elif day == 'Friday':
        dayy = 5
    elif day == 'Saturday':
        dayy = 6
    else:
        temp = "Sunday"
        session = 'inaiku Leave uh'
    #example for understanding ::print(sheet.cell_value(monday, 8))
    if temp != "Sunday":
        if hour<9:
            session = "Class usually starts at 9 AM"
        elif hour == 9:
            session = sheet.cell_value(dayy, 1)
        elif hour == 10:
            session = sheet.cell_value(dayy, 2)
        elif hour == 11:
            session = sheet.cell_value(dayy, 3)
        elif hour == 12:
            session = sheet.cell_value(dayy, 4)
        elif hour == 13:
            session = "Lunch time! poi sapudu!"
        elif hour == 14:
            session = sheet.cell_value(dayy, 6)
        elif hour>16:
            session = '5 mani mela class irukathu (mostly!)'

    return str(session)
