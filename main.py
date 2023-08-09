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

    # custom keyboard with conversion options
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Convert to PDF'))
    keyboard.add(types.KeyboardButton('Convert to DOCX'))
    keyboard.add(types.KeyboardButton('Convert to TXT'))
    keyboard.add(types.KeyboardButton('Convert to JPG'))
    keyboard.add(types.KeyboardButton('Convert to PNG'))
    keyboard.add(types.KeyboardButton('Convert to MP3'))

    # sending the keyboards list to user
    bot.send_message(message.chat.id, 'Please select the desired conversion format:', reply_markup=keyboard)

    # getting file
    file = bot.get_file(fileData.file_id)

    # dictionary for storing users file extension
    user_conversion_formats = {}

    # Storing the file extension
    user_context = {'file_extension': fileExtension}

    # Saving user's preferred conversion format
    user_conversion_formats[message.chat.id] = {}

    # downloading
    downloadedFile = bot.download_file(file.file_path)

    # saving
    with open(f"./Assets/{''.join(random.choices(string.ascii_lowercase, k=12))}.{fileExtension}", 'wb') as new_file:
        new_file.write(downloadedFile)

    # operator /convert for accepting and launching the process of converting
    @bot.message_handler(func=lambda message: message.text in {'Convert to PDF', 'Convert to DOCX', 'Convert to TXT', 'Convert to JPG',
                                              'Convert to PNG', 'Convert to MP3'})
    def handle_conversion_choice(message):
        user_conversion_formats[message.chat.id] = {'file_extension': fileExtension, 'conversion_format': message.text}
        bot.send_message(message.chat.id, f'You have selected {message.text}. Please proceed by clicking /convert.')

    # converting(hello for saving file)
    @bot.message_handler(commands=['help'])
    def convertinon(message):
        user_id = message.chat.id
        if user_id in user_conversion_formats:
            print("hello")


bot.infinity_polling()

