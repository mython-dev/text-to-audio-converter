from telebot import types

markup = types.InlineKeyboardMarkup()

markup.row_width = 1

lang_ru = types.InlineKeyboardButton('Русский', callback_data='russian')

langu_en = types.InlineKeyboardButton('English', callback_data='english')

markup.add(lang_ru, langu_en)
