import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Contact, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import time

texts = '''Grüße Dich %s,  
 
herzlich Willkommen bei der Gemeinschaft "Chemtrailfreier Himmel - Holen wir uns den sauberen Himmel zurück!" hier auf Telegram. https://t.me/chemtrailfreier_himmel  
 
Wir sind eine Gruppe von aufgeklärten Menschen, die nicht mehr tatenlos, der Umweltverschmutzung durch Chemtrails und Wettermanipulation, zusehen wollen. 
 
Lade auch Du Freunde und Bekannte in diese Gruppe ein, damit wir möglichst viele sind, die darüber Bescheid wissen. Bitte mache auch wie wir Aufklärung über die Chemtrails da draußen, denn nur gemeinsam können wir den Himmel wieder Chemtrailfrei bekommen. 
 
Wenn Du Fotos und Videobeweise über die Chemtrails Einsätze hast, dann kannst Du deine Beweise hier in der Gruppe veröffentlichen.  
 
Bitte beachte jedoch unsere Regeln, wie Du richtig Fotos und sonstige Beweise veröffentlichst. 
 
Klicke auf den unteren Knopf „Hierher klicken“ und mache Dich mit den Gruppenregeln vertraut.'''


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='704412135:AAGJXWDDZ5PxlS1Tx4nUTGjNb2671-RT9nQ')
dispatcher = updater.dispatcher
def start(bot, update):
    message = update.message
    if update.message.new_chat_members != []:
        M_I = message.message_id
        button = [[InlineKeyboardButton('Hierher klicken', url = 'https://telegra.ph/Gruppenregeln-für-die-Chemtrailfreier-Himmel-Telegram-Gruppe-03-03')]]
        keyboard = InlineKeyboardMarkup(button)
        bot.send_message(message.chat.id,texts %(message.from_user.first_name),reply_markup=keyboard)
        time.sleep(90)
        bot.delete_message(message.chat_id, M_I)
        bot.delete_message(message.chat_id, M_I + 1)
    elif update.message.left_chat_member != []:
        time.sleep(20)
        M_I = message.message_id
        bot.delete_message(message.chat_id, M_I)
    else:
        pass
start_handler = MessageHandler(Filters.all, start)
dispatcher.add_handler(start_handler)
updater.start_polling(timeout=5, clean=True)
