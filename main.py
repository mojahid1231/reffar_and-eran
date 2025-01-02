import time
import json
import telebot

##TOKEN DETAILS
TOKEN = "TRON"

BOT_TOKEN = "YOUR BOT TOKEN"
PAYMENT_CHANNEL = "@PAYMENTCHANNELUSERNAME" #add payment channel here including the '@' sign
OWNER_ID = 1194007250 #write owner's user id here.. get it from @MissRose_Bot by /id
CHANNELS = ["@CHECKCHANNEL"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"] 
              #you can add as many channels here and also add the '@' sign before channel username
Daily_bonus = 0.001 #Put daily bonus amount here!
Mini_Withdraw = 0.5  #remove 0 and add the minimum withdraw u want to set
Per_Refer = 0.0001 #add per refer bonus here

bot = telebot.TeleBot(BOT_TOKEN)

def check(id):
    for i in CHANNELS:
        check = bot.get_chat_member(i, id)
        if check.status != 'left':
            pass
        else:
            return False
    return True
bonus = {}

def menu(id):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('🆔 Account')
    keyboard.row('🙌🏻 Referrals', '🎁 Bonus', '💸 Withdraw')
    keyboard.row('⚙️ Set Wallet', '📊Statistics')
    bot.send_message(id, "*🏡 Home*", parse_mode="Markdown",
                     reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
   try:
    user = message.chat.id
    msg = message.text
    if msg == '/start':
        user = str(user)
        data = json.load(open('users.json', 'r'))
        if user not in data['referred']:
            data['referred'][user] = 0
            data['total'] = data['total'] + 1
        if user not in data['referby']:
            data['referby'][user] = user
        if user not in data['checkin']:
            data['checkin'][user] = 0
        if user not in data['DailyQuiz']:
