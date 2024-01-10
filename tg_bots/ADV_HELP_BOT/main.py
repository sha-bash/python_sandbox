import telebot
from telebot import types
from authorization import authorization
from Instructions import Instructions

auth = authorization()
bot = auth.bot
bot.delete_webhook()

# Функция для получения инструкций по категории
def get_instructions_by_category(category):
    return Instructions.Category_of_question.get(category, [])

# Функция для получения URL по названию инструкции
def get_url_by_instruction(instruction):
    return Instructions.instruction_urls.get(instruction, None)

# Функция для создания кнопок инструкции
def create_instruction_buttons(category):
    instructions = get_instructions_by_category(category)
    markup = types.InlineKeyboardMarkup()
    for instruction in instructions:
        url = get_url_by_instruction(instruction)
        if url:
            btn = types.InlineKeyboardButton(instruction, url=url)
            markup.add(btn)
    return markup

@bot.message_handler(commands=['start'])
def start_menu(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('ДИЗАЙН', callback_data='design')
    btn2 = types.InlineKeyboardButton('ТОВАРЫ', callback_data='products')
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "Добрый день! Я Ваш бот-помощник от компании AdvantShop!")
    bot.send_message(chat_id, 'Выберите категорию вопроса:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    if call.data == 'design':
        markup = create_instruction_buttons('ДИЗАЙН')
        if markup:
            bot.send_message(chat_id, 'Инструкции в категории ДИЗАЙН:', reply_markup=markup)
        else:
            bot.send_message(chat_id, 'В категории ДИЗАЙН нет инструкций')
    elif call.data == 'products':
        markup = create_instruction_buttons('ТОВАРЫ')
        if markup:
            bot.send_message(chat_id, 'Инструкции в категории ТОВАРЫ:', reply_markup=markup)
        else:
            bot.send_message(chat_id, 'В категории ТОВАРЫ нет инструкций')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id
    text = message.text
    bot.send_message(chat_id, 'Пожалуйста, выберите пункт из списка наверху')

bot.polling(non_stop=True)
