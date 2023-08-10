from telebot import types


def generate_keyboard(extension):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    if extension == 'txt':
        keyboard.add(types.KeyboardButton('Convert to PDF'))
        keyboard.add(types.KeyboardButton('Convert to DOCX'))
    elif extension == 'pdf':
        keyboard.add(types.KeyboardButton('Convert to TXT'))
        keyboard.add(types.KeyboardButton('Convert to DOCX'))
    elif extension == 'docx':
        keyboard.add(types.KeyboardButton('Convert to PDF'))
        keyboard.add(types.KeyboardButton('Convert to TXT'))
    elif extension == 'jpg':
        keyboard.add(types.KeyboardButton('Convert to PNG'))
    elif extension == 'png':
        keyboard.add(types.KeyboardButton('Convert to JPG'))
    elif extension == 'mp4':
        keyboard.add(types.KeyboardButton('Convert to MP3'))

    return keyboard