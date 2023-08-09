import telebot
from telebot import types

from App1 import API_KEY

ABOUT_TEXT = """This bot is created for free file conversion.
Just give him your files and choose desired format!"""

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, ABOUT_TEXT)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "FAQ and commands")


bot.infinity_polling()

