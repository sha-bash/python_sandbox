import telebot

token = "введите токен"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chatid, message.text)

bot.polling(non_stop=True)