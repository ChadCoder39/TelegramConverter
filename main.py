import telebot
from telebot import types
import os
import string
import random



from App1 import API_KEY
from functions.generate_keyboard import generate_keyboard


bot = telebot.TeleBot(API_KEY)

# convertion options
options = {
    'Convert to PDF', 
    'Convert to DOCX', 
    'Convert to TXT', 
    'Convert to JPG',
    'Convert to PNG', 
    'Convert to MP3'
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Dear {message.from_user.first_name}, This bot is created for free file conversion. Just give him your files and choose desired format!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "FAQ and commands")


@bot.message_handler(content_types=['document', 'photo', 'audio', 'video', 'voice'])
def get_file(message):
    fileData = message.document or message.photo or message.audio or message.video or message.voice

    # extracting extension from filename
    fileExtension = fileData.file_name.split(".")[-1] # TODO fix for .filename (no ext)

    # gen keyboard with conversion options
    keyboard = generate_keyboard(fileExtension)

    # getting file
    file = bot.get_file(fileData.file_id)

    # downloading
    downloadedFile = bot.download_file(file.file_path)

    # saving
    with open(f"./assets/{''.join(random.choices(string.ascii_lowercase, k=12))}.{fileExtension}", 'wb') as new_file:
        new_file.write(downloadedFile)

    # sending the keyboards list to user
    bot.send_message(message.chat.id, 'Please select the desired conversion format:', reply_markup=keyboard)

    # dictionary for storing users file extension
    user_conversion_format = {}

    # operator /convert for accepting and launching the process of converting
    @bot.message_handler(func=lambda message: message.text in options)
    def handle_conversion_choice(message):
        user_conversion_format[message.chat.id] = message.text
        bot.send_message(message.chat.id, f'You have selected {message.text}. Converting...')

        # unique user id
        user_id = message.chat.id
        bot.send_message(message.chat.id, user_conversion_format[user_id])

        # deleting file
        file_path = f"./assets/{user_id}.{fileExtension}"
        if os.path.exists(file_path):
            os.remove(file_path)
        
        


bot.infinity_polling()

