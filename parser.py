import requests
from bs4 import BeautifulSoup
import telegram
from telebot import types
from authorization import authorization
from Instructions import Instructions

bot_token = '6597827583:AAGCGNWxfEPQAcDUmZasaF0sufxOTzx-ZzI'

# Retrieve the content of the webpage
response = requests.get('https://www.advantshop.net/help/pages/add-product')
html_content = response.text

# Parsing the text using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')
parsed_text = soup.get_text()

bot = telegram.Bot(token=bot_token)

auth = authorization()
bot = auth.bot
bot.delete_webhook()

# Function to get instructions by category
def get_instructions_by_category(category):
    return Instructions.Category_of_question.get(category, [])

# Function to get URL by instruction name
def get_url_by_instruction(instruction):
    return Instructions.instruction_urls.get(instruction, None)

# Function to create instruction buttons
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
    btn1 = types.InlineKeyboardButton('DESIGN', callback_data='design')
    btn2 = types.InlineKeyboardButton('PRODUCTS', callback_data='products')
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "Hello! I'm your bot assistant from AdvantShop!")
    bot.send_message(chat_id, 'Choose a category:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    if call.data == 'design':
        markup = create_instruction_buttons('DESIGN')
        if markup:
            bot.send_message(chat_id, 'Instructions in DESIGN category:', reply_markup=markup)
        else:
            bot.send_message(chat_id, 'No instructions in DESIGN category')
    elif call.data == 'products':
        markup = create_instruction_buttons('PRODUCTS')
        if markup:
            bot.send_message(chat_id, 'Instructions in PRODUCTS category:', reply_markup=markup)
        else:
            bot.send_message(chat_id, 'No instructions in PRODUCTS category')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id
    text = message.text
    bot.send_message(chat_id, 'Please choose an option from the list above')
    bot.send_message(chat_id, parsed_text)
# Send message with parsed text
#bot.send_message(chat_id, parsed_text)

bot.polling(non_stop=True)
