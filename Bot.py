import telebot
from telebot import types
import razmitie1
import segm, savings

TOKEN = '5787558909:AAGuC1T6YiseDq1j7-NnHdDFw0_QqcspP08'

bot = telebot.TeleBot(TOKEN)

markup_none = types.ReplyKeyboardRemove(selective=False)


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Скинь мне картикну и выбери что с ней сделать\nТолько не кликай много раз на кнопки, пожалуйста")


@bot.message_handler(commands=['help'])
def help_answer(message):
    bot.send_message(message.chat.id, "Просто скинь мне фотку. Любую")


@bot.message_handler(content_types=['photo'])
def picture_interection(message):

    print('Скинули картинку', message.chat.username)

    global downloaded_file

    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Исказить')
    btn2 = types.KeyboardButton('Фрагментировать')
    btn3 = types.KeyboardButton('Демотивировать')

    markup.add(btn1, btn2)

    # bot.send_message(message.chat.id, 'щас не будет работать, можете написать /help, там есть другие команды. Но там не интересно')
    bot.send_message(message.chat.id, 'Что мне сделать с твоей картикной?', reply_markup=markup)


    # Искажение
    @bot.message_handler(regexp='Исказить')
    def picture_ruining(m):

        bot.send_message(m.chat.id, 'Подождите', reply_markup=markup_none)

        with open(savings.ruin_save(), 'wb') as new_file:
            new_file.write(downloaded_file)

        razmitie1.pic_ruining()

        ph = open(savings.ruin_send(), 'rb')
        bot.send_message(m.chat.id, 'Вот твоя фотка:')
        bot.send_photo(m.chat.id, ph)

        with open('ruin/amount.txt', 'a') as test:
            with open('ruin/amount.txt', 'r') as tet:
                line = tet.readlines()[-1]
            test.write(str(int(line) + 1) + '\n')


    # Фрагментация
    @bot.message_handler(regexp='Фрагментировать')
    def pictrue_fragment(me):

        bot.send_message(me.chat.id, "Подождите.", reply_markup=markup_none)

        with open(savings.segm_save(), 'wb') as new_file:
            new_file.write(downloaded_file)

        segm.pic_segment()

        ph = open(savings.segm_send(), 'rb')
        bot.send_message(me.chat.id, 'Вот твоя фотка:')
        bot.send_photo(me.chat.id, ph)

        with open('segm/amount.txt', 'a') as test:


bot.infinity_polling()