import logging
import json
import requests

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, ConversationHandler

import const as keys
import response as R

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/start 🛒 - start shopping\n /help ❓ - display commands help')

def start_command(update: Update, context: CallbackContext) -> None:
    categoriesurl = "https://fakestoreapi.com/products/categories"
    categoriesresponse = requests.get(categoriesurl)
    categories = json.loads(categoriesresponse.text)
    button_list = []
    for each in categories:
        button_list.append(InlineKeyboardButton(each, callback_data = 'c+' + each))
    reply_markup = InlineKeyboardMarkup(build_menu(button_list,n_cols=2))
    context.bot.send_message(chat_id=update.message.chat_id, text='Choose from the following',reply_markup=reply_markup)

def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def category_callback(update: Update, context: CallbackContext):
    query = update.callback_query

    productsUrl = "https://fakestoreapi.com/products/category/" + query.data[2:]
    productsResponse = requests.get(productsUrl)
    products = json.loads(productsResponse.text)
    button_list = []
    for each in products:
        button_list.append(InlineKeyboardButton(each['title'], callback_data = 'p+' + str(each['id'])))
    reply_markup = InlineKeyboardMarkup(build_menu(button_list,n_cols=2))

    context.bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=reply_markup)

def products_callback(update: Update, context: CallbackContext) :
    query = update.callback_query
    productUrl = "https://fakestoreapi.com/products/" + query.data[2:]
    productResponse = requests.get(productUrl)
    product = json.loads(productResponse.text)
    def num(s):
        try:
            return int(s)
        except ValueError:
            return float(s)
    context.bot.send_invoice(
        chat_id = query.message.chat_id, 
        title = product['title'], 
        description = product['description'], 
        payload = "128", 
        provider_token = keys.paymentToken,
        currency = "USD",
        prices = [LabeledPrice(label = product['title'], amount = num(product['price']) * 100)],
        start_parameter = None,
        photo_url = product['image'],
        photo_height=512,
        photo_width=512)

def handle_message(update: Update, context: CallbackContext) -> None:
    text=str(update.message.text).lower()
    response = R.request_message(text)
    update.message.reply_text(response)

def main():
    updater=Updater(keys.apiKey)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CallbackQueryHandler(category_callback, pattern='^(c+)'))
    dp.add_handler(CallbackQueryHandler(products_callback, pattern='^(p+)'))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.start_polling()
    updater.is_idle

main()

