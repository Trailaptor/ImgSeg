import telebot
from telebot import types
import razmitie1

bot = telebot.TeleBot('5389920992:AAHcHtbo976RDP9jRzphineJrTNpIDM1yg0')

markup_none = types.ReplyKeyboardRemove(selective=False)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Скинь мне картикну и выбери что с ней сделать")


@bot.message_handler(commands=['help'])
def help_answer(message):
    bot.reply_to(message, "других команд нету.")


@bot.message_handler(content_types=['photo'])
def picture_interection(message):
    

    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open('photos/amount.txt', 'r') as am:
        SRC = 'photos/' + str(int(am.readlines()[-1])) + '.jpg'
    
    with open(SRC, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Исказить')
    btn2 = types.KeyboardButton('Фрагментировать')
    
    markup.add(btn1, btn2)
    # bot.send_message(message.chat.id, 'щас не будет работать, можете написать /help, там есть другие команды. Но там не интересно')
    bot.send_message(message.chat.id, 'Что мне сделать с твоей картикной?', reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def picture_ruine(message):
        if(message.text == "Исказить"):
            razmitie1.pic_ruining()
        elif(message.text == "Фрагментировать"):
            bot.send_message(message.chat.id, 'Функция пока не доступна')
        

        with open('photos/amount.txt', 'r') as am:
            SRCresult = 'photos/' + 'result' + str(int(am.readlines()[-1])) + '.jpg'
        ph = open(SRCresult, 'rb')
        bot.send_message(message.chat.id, 'Вот твоя фотка:', reply_markup=markup_none)
        bot.send_photo(message.chat.id, ph)

        with open('photos/amount.txt', 'a') as test:
            with open('photos/amount.txt', 'r') as tet:
                line = tet.readlines()[-1]
            test.write(str(int(line) + 1) + '\n')


bot.infinity_polling()
