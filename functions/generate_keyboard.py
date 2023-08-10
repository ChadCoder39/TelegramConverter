from telebot import types

keys_config = {}
keys_config['txt']  = ['pdf', 'docx']
keys_config['pdf']  = ['txt', 'docx']
keys_config['docx'] = ['pdf', 'txt']
keys_config['jpg']  = ['png']
keys_config['png']  = ['jpg']
keys_config['mp4']  = ['mp3']


default_str = 'Convert to'


def generate_keyboard(extension):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
    for ext in keys_config[extension]:
        keyboard.add(types.KeyboardButton(f"{default_str} {str(ext).upper()}"))

    return keyboard