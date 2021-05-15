from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import xlrd
from datetime import datetime, time, date
updater = Updater(token='1898176973:AAHDlqEBBegfpeTb5cJ1yo8lwxNvofWHkd0', use_context=True)

dispatcher = updater.dispatcher

#Just logging ignore..
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm AltfBot! Whatsup?")

def enna(update, context):
    try:
        if context.args[0] == "class":
            ########Code for schedule
	   # import xlrd
            # To open Workbook
            wb = xlrd.open_workbook('classSchedulle.xls')
            sheet = wb.sheet_by_index(0)
            #Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = 1, 2, 3, 4, 5, 6
            from datetime import time, datetime, date
            #from dateutil.tz import gettz
            #now = datetime.now(tz=gettz('Asia/Kolkata'))
            now = datetime.now()
            hour = int(now.strftime("%H"))
            date = date.today()
            day = date.strftime("%A")

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
                session = 'inaiku Leave uh'
            #example for understanding ::print(sheet.cell_value(monday, 8))
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
                session = "Lunch time! Go eat!"
            elif hour == 14:
                session = sheet.cell_value(dayy, 6)
            elif hour == 15:
                session = sheet.cell_value(dayy, 7)
            elif hour == 16:
                session = sheet.cell_value(dayy, 8)
            elif hour>16:
                session = '4 mani mela class irukathu (mostly)'
            ########
        elif context.args[0] == "date":
            from datetime import date

            datentime = date.today()
            #context.bot.send_message(chat_id=update.effective_chat.id, text=str(datentime))
            session = str(datentime)
        elif context.args[0] == "time":
            from datetime import datetime,time
            now = datetime.now()
            #time = now.strftime("%H : %M") 
            #timestamp = datetime.now().strftime('%H:%M:%S.%f')
            from dateutil.tz import gettz
            time = datetime.now(tz=gettz('Asia/Kolkata'))
            time = time.strftime("%H : %M")
            session = str(time)
        else:
            session = "puriyala"
    except (IndexError, ValueError):
        context.bot.send_message(chat_id=update.effective_chat.id, text="/enna Command Arguments: \n\t1. class\n\t2. date\n\t3. time")
        session = "/enna command ku arguments onume pass panala!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=session)

# For errors
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(context.args))
    context.bot.send_message(chat_id=update.effective_chat.id, text="this command was confidential htf did u know?")
#calling everytime /start is called
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#for enna command
enna_handler = CommandHandler('enna', enna)
dispatcher.add_handler(enna_handler)
#for echo 
echo_handler = CommandHandler('echo', echo)
dispatcher.add_handler(echo_handler)
# for errors
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()



#-----------------------------------------------------------#
#seperate functions bellow
