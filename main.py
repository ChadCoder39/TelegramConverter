import telebot
from telebot import types
import os
import string
import random

from App1 import API_KEY



bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Dear {message.from_user.first_name}, This bot is created for free file conversion. Just give him your files and choose desired format!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "FAQ and commands")


@bot.message_handler(content_types=['document', 'photo', 'audio', 'video', 'voice'])
def get_file(message):
    fileData = message.document

    # extracting extension from filename
    fileExtension = fileData.file_name.split(".")[-1]
    
    # getting file
    file = bot.get_file(fileData.file_id)

    # downloading
    downloadedFile = bot.download_file(file.file_path)

    # saving
    with open(f"./assets/{''.join(random.choices(string.ascii_lowercase, k=12))}.{fileExtension}", 'wb') as new_file:
        new_file.write(downloadedFile)


    
    


bot.infinity_polling()

