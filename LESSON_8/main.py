import telebot
from viloyatlar import *
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text=f"Salom \n{message.from_user.username}\nBu bot sizga O'zbekiston Respublikasidagi viloyatlar haqida malumotlarni topishga yordam beradi")

@bot.message_handler(commands=['viloyatlar'])
def viloyatlar(message):
    markup = InlineKeyboardMarkup()

    # Create buttons
    button1 = InlineKeyboardButton("Fargona", callback_data="fargona")
    button2 = InlineKeyboardButton("Namangan", callback_data="namangan")
    button3 = InlineKeyboardButton("Andijon", callback_data="andijon")
    button4 = InlineKeyboardButton("Samarqand", callback_data="samarqand")
    button5 = InlineKeyboardButton("Jizzax", callback_data="jizzax")
    button6 = InlineKeyboardButton("Buxoro", callback_data="buxoro")
    button7 = InlineKeyboardButton("Sirdaryo", callback_data="sirdaryo")
    button8 = InlineKeyboardButton("Surxondaryo", callback_data="surxondaryo")
    button9 = InlineKeyboardButton("Navoiy", callback_data="navoiy")
    button10= InlineKeyboardButton("Qashqadaryo", callback_data="qashqadaryo")
    button11 = InlineKeyboardButton("Xorazm", callback_data="xorazm")
    button12 = InlineKeyboardButton("Qoraqalpogiston", callback_data="qoraqalpogiston")
    button13 = InlineKeyboardButton("Toshkent", callback_data="toshkent")

    # Add buttons to the markup
    markup.add(button1, button2, button3,button4, button5, button6,button7, button8, button9,button10, button11, button12, button13)

    # Send the welcome message with the buttons
    bot.send_message(message.chat.id, "Viloyatni tanlang:", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "buxoro":
        bot.send_message(call.message.chat.id, buxoro())

    if call.data == "fargona":
        bot.send_message(call.message.chat.id, fargona())

    if call.data == "andijon":
        bot.send_message(call.message.chat.id, andijon())

    if call.data == "samarqand":
        bot.send_message(call.message.chat.id, samarqand())

    if call.data == "jizzax":
        bot.send_message(call.message.chat.id, jizzax())

    if call.data == "sirdaryo":
        bot.send_message(call.message.chat.id, sirdaryo())

    if call.data == "surxondaryo":
        bot.send_message(call.message.chat.id, surxondaryo())

    if call.data == "navoiy":
        bot.send_message(call.message.chat.id, navoiy())

    if call.data == "qashqadaryo":
        bot.send_message(call.message.chat.id, qashqadaryo())

    if call.data == "xorazm":
        bot.send_message(call.message.chat.id, xorazm())

    if call.data == "qoraqalpogiston":
        bot.send_message(call.message.chat.id, Qoraqalpogiston_Respublikasi())

    if call.data == "toshkent":
        bot.send_message(call.message.chat.id, toshkent())















bot.polling()