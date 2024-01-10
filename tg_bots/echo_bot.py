import telebot

token = "6350792761:AAHlqpuEiN9v3CzkkdAA4My3xxAIrY7xZ_U"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chatid, message.text)

bot.polling(non_stop=True)