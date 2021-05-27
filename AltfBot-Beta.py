from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import xlrd
import os

TOKEN = os.environ["TOKEN"]
from datetime import datetime, time, date
#TOKEN = None

"""with open("token.txt") as f:
    TOKEN = f.read().strip()"""
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

#Just logging ignore..
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hello {user.mention_markdown_v2()}\!')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm AltfBot! Whatsup?")

def hi(update, context):
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!')
def beta(update, context):
    user = update.effective_user
    update.message.reply_markdown_v2(fr'{user.mention_markdown_v2()} You can Join the Beta Group through the link below\!')
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://t.me/joinchat/ttfV8gOEzWljNTI1")
def schedule(update, context):
    wb = xlrd.open_workbook('classSchedulle.xls')
    sheet = wb.sheet_by_index(0)
    # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = 1, 2, 3, 4, 5, 6
    from datetime import time, datetime, date
    now = datetime.now()
    hour = int(now.strftime("%H"))
    date = date.today()
    day = date.strftime("%A")
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
        y = 0
        session = {}
        for x in range(8):
            y += 1
            session[x] = sheet.cell_value(dayy, y)
    format = f"session 1 : {session[0]}\nsession 2: {session[1]}\nsession 3: {session[2]}\nsession 4: {session[3]}\nsession 5: {session[5]}\nsession 6: {session[6]}\nsession 7: {session[7]}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=format)
def enna(update, context):
    try:
        if context.args[0] == "class":
            ########Code for schedule
	        # import xlrd
            # To open Workbook
            wb = xlrd.open_workbook('classSchedulle.xls')
            sheet = wb.sheet_by_index(0)
            # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = 1, 2, 3, 4, 5, 6
            from datetime import time, datetime, date
            now = datetime.now()
            hour = int(now.strftime("%H"))
            minute = int(now.strftime("%M"))
            date = date.today()
            day = date.strftime("%A")
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
                elif hour == 15:
                    session = sheet.cell_value(dayy, 7)
                elif hour == 16:
                    session = sheet.cell_value(dayy, 8)
                elif hour>16:
                    session = '5 mani mela class irukathu (mostly!)'
               
                if minute>45 and hour != 13 and hour<15 and hour>9:
                    session = session + " session has ended at " + str(hour) + ":" + str(minute)
            ########
        elif context.args[0] == "date":
            from datetime import date, datetime
            date = datetime.now().strftime("%d-%m-%Y")
            #context.bot.send_message(chat_id=update.effective_chat.id, text=str(datentime))
            session = str(date)
        elif context.args[0] == "time":
            from datetime import datetime,time
            now = datetime.now()
            time = now.strftime("%I : %M %p") 
            #timestamp = datetime.now().strftime('%H:%M:%S.%f')
            session = str(time)
        elif context.args[0] == "day":
            from datetime import date
            day = date.today()
            session = str(day.strftime("%A"))
        else:
            session = "puriyala"
    except (IndexError, ValueError):
        context.bot.send_message(chat_id=update.effective_chat.id, text="/enna Command Arguments: \n\t1. class\n\t2. date\n\t3. time")
        session = "/enna command ku arguments onume pass panala!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=session)

def next(update, context):
    try:
        if context.args[0] == "class":
            ########Code for schedule
	        # import xlrd
            # To open Workbook
            wb = xlrd.open_workbook('classSchedulle.xls')
            sheet = wb.sheet_by_index(0)
            #Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = 1, 2, 3, 4, 5, 6
            from datetime import time, datetime, date
            now = datetime.now()
            hour = int(now.strftime("%H"))
            hour = hour+1
            date = date.today()
            day = date.strftime("%A")
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
                    session = "Lunch time! Go eat!"
                elif hour == 14:
                    session = sheet.cell_value(dayy, 6)
                elif hour == 15:
                    session = sheet.cell_value(dayy, 7)
                elif hour == 16:
                    session = sheet.cell_value(dayy, 8)
                elif hour>16:
                    session = '5 mani mela class irukathu (mostly)'
                
            ########
        
        else:
            session = "puriyala"
    except (IndexError, ValueError):
        context.bot.send_message(chat_id=update.effective_chat.id, text="/next Command Arguments: \n\t class")
        session = "/next command ku arguments onume pass panala!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=session)
# For errors
def unknown(update, context):
     msg = "correct aah sollu."
     update.message.reply_text(msg)
def sollu(update, context):
    msg = str(update.message.text)
    start = 0
    stop = 5
    # Remove charactes from index 0 to 5
    if len(msg) > stop :
        msg = msg[0: start:] + msg[stop + 1::]
    update.message.reply_text(msg)

def whoami(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    #user = update.effective_user
    whoami = "chat_id : {}\n user_id : {}\nfirstname : {}\nlastname : {}\nusername : {}". format(chat_id,user['id'],first_name, last_name , user['username'])
    #update.message.reply_markdown_v2(whoami)
    #update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!')    
    #update.message.reply_markdown_v2(fr'chat_id \: {chat_id} and firstname \: {first_name} lastname \: {last_name}  username {username}')
    #context.bot.send_message(chat_id=update.effective_chat.id, text=whoami)
    update.message.reply_text(whoami)

#calling everytime /start is called
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#for hi command
start_handler = CommandHandler('hi', hi)
dispatcher.add_handler(start_handler)
#for beta command
start_handler = CommandHandler('beta', beta)
dispatcher.add_handler(start_handler)
#for enna command
enna_handler = CommandHandler('enna', enna)
dispatcher.add_handler(enna_handler)
#for schedule command
schedule_handler = CommandHandler('schedule', schedule)
dispatcher.add_handler(schedule_handler)
#for sollu command
sollu_handler = CommandHandler('sollu', sollu)
dispatcher.add_handler(sollu_handler)
#for next handler 
next_handler = CommandHandler('next', next)
dispatcher.add_handler(next_handler)
#for whoami handler
whoami_handler = CommandHandler('whoami', whoami)
dispatcher.add_handler(whoami_handler)
# for errors handler
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()



#-----------------------------------------------------------#
#seperate functions bellow
