from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, BaseFilter)
from telegram import ReplyKeyboardMarkup
import telegram
import random
import time
import logging
updater = Updater(token='')
bot=telegram.Bot(token="")
dispatcher=updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG)

End=["Cum in her face", "Cum on tits", "Cum in her mouth", "Cum in her feet", "Cum in her pussy", "Cum in her ass"]
Preliminares_for_her=["Lick her pussy for 1 minute", "Lick and suck her tits for 30 seconds", "Finger her pussy for 1 minute"]
Preliminares_for_him=["Suck his dick for 1 minute","Suck her balls for 30 seconds", "Lick his nipple for 30 seconds", "Footjob for 1 minute", "Handjob for 1 minute"]
Position=["photo/69.jpg", "photo/missionary.jpg", "photo/cowgirl.jpg",  "photo/reverse.jpg", "photo/spoon.jpg", "photo/thefusion.jpg", "photo/doggy.jpg", "photo/thecat.jpg", "photo/thelapdance.jpg", "photo/hesquatthrust.jpg", "photo/thepretzel.jpg", "photo/theanvil.jpg", "photo/thebellyflop.jpg", "photo/squatthruster.jpg", "photo/kitchenconfidential.jpg", "photo/wheelbarrowatrest.jpg", "photo/crouchingtiger.jpg"]

def start(bot, update):
    reply_keyboard = [['Preliminares for her', 'Preliminares for him', 'Position', "End"]]
    bot.send_message(chat_id=update.message.chat_id, text=
        "Hello, welcome on the Sex Roulette Bot!\n"
        "\n"
        "Other command:\n"
        "/feedback\n"
        "/donations\n"
        "My website: domestic.pythonanywhere.com\n"
        "\n"
        "Choose the step from keyboard.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard))
start_handler=CommandHandler("start", start)
dispatcher.add_handler(start_handler)

def feedback(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Write me your feedback")
    update.message.forward(chat_id_group)
feed_handler=CommandHandler("feedback", feedback)
dispatcher.add_handler(feed_handler)



def donations(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="If you appreciate the bot, consider making a small donation to keep the development active. It will be greatly appreciated.\n"
    "bitcoincash:qqykq7adrqssm2e2gmz6ln440tup2qxuhqndwwlqfj")
don_handler=CommandHandler("donations", donations)
dispatcher.add_handler(don_handler)




class Filter_one(BaseFilter):
    def filter(self, message):
        return 'End' in message.text
filter_one_ = Filter_one()
def end(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=random.choice(End))
one_handler = MessageHandler(filter_one_, end)
dispatcher.add_handler(one_handler)

class Filter_two(BaseFilter):
    def filter(self, message):
        return 'Position' in message.text
filter_two_ = Filter_two()
def position(bot, update):
    f=random.choice(Position)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(f, "rb"))
two_handler = MessageHandler(filter_two_, position)
dispatcher.add_handler(two_handler)

class Filter_three(BaseFilter):
    def filter(self, message):
        return 'Preliminares for him' in message.text
filter_three_ = Filter_three()
def for_him(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=random.choice(Preliminares_for_him))
three_handler = MessageHandler(filter_three_, for_him)
dispatcher.add_handler(three_handler)

class Filter_four(BaseFilter):
    def filter(self, message):
        return 'Preliminares for her' in message.text
filter_four_ = Filter_four()
def for_her(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=random.choice(Preliminares_for_her))
four_handler = MessageHandler(filter_four_, for_her)
dispatcher.add_handler(four_handler)



updater.start_polling()
while True:
    time.sleep(2)
updater.idle()
