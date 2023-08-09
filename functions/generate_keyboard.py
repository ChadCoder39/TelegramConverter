from telebot import types


def generate_keyboard(extension):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Convert to PDF'))
    keyboard.add(types.KeyboardButton('Convert to DOCX'))
    keyboard.add(types.KeyboardButton('Convert to TXT'))
    keyboard.add(types.KeyboardButton('Convert to JPG'))
    keyboard.add(types.KeyboardButton('Convert to PNG'))
    keyboard.add(types.KeyboardButton('Convert to MP3'))

    return keyboard