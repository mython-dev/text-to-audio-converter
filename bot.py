from telebot import *
from gtts import gTTS
from keyboard import *
import os


# Check for the presence of a file.

exists = True

i = 1

while exists:
    if os.path.exists(f'audio{i}.ogg'):
        i += 1
    else:
        exists = False

file = f'audio{i}.ogg'

token = '5821548679:AAGiqMydPtyu8xiD-vY8BPF1ve2l3BMlGB8'

# bot start:)

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
    bot.send_message(message.chat.id, f'Это Telegram бот, который может переводить аудио в текст.🙀\nВыберите на каком языке будет озвучивать🗣', reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: True)
def lang(call):
    if call.message:

        if call.data == 'russian':

            text_ru = bot.send_message(call.message.chat.id, 'Отправьте текст...📝')

            bot.register_next_step_handler(text_ru, send_audio_ru)

                        

        elif call.data == 'english':

            text_en = bot.send_message(call.message.chat.id, 'Send text...📝')

            bot.register_next_step_handler(text_en, send_audio_en)


    

def send_audio_ru(message):

    file = f'audio{i}.ogg'

    language_ru = "ru"

    audio = gTTS(text=message.text, lang=language_ru, slow=True)

    audio.save(file)

    send_file = open(file, 'rb')

    send_ru = bot.send_audio(message.chat.id, send_file)

    try:
        os.remove(file)   
    except FileNotFoundError:
        print('Нет такого файла.')

    
    # bot.register_next_step_handler(send_ru, send_audio_ru )



def send_audio_en(message):

    file = f'audio{i}.ogg'

    language_en = "en"

    audio = gTTS(text=message.text, lang=language_en, slow=False)

    audio.save(file)

    send_file = open(file, 'rb')

    send_en = bot.send_audio(message.chat.id, send_file)

    try:
        os.remove(file)   
    except FileNotFoundError:
        print('Нет такого файла.')

    
    # bot.register_next_step_handler(send_audio_en, send_audio_en)


bot.infinity_polling()


