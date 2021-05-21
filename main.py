import logging
import json
import requests

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

import const as keys
import response as R

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

print("bda el bot")

# def start_command(update: Update,context: CallbackContext) -> None:
#     main_menu_keyboard = [[KeyboardButton('📝 Category')],
#                         [KeyboardButton('🛒 Cart')],
#                         [KeyboardButton('📦 Orders')]]
#     reply_kb_markup = ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard = True, one_time_keyboard = True)
#     context.bot.send_message(chat_id = update.message.chat_id, text = 'Products List', reply_markup=reply_kb_markup)

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('if you want help chouf google')

def product_command(update: Update, context: CallbackContext) -> None:
        context.bot.send_invoice(
        chat_id = update.message.chat_id, 
        title = "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops ", 
        description = "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday", 
        payload = "payload", 
        provider_token = keys.paymentToken,
        currency = "USD",
        prices = [LabeledPrice(label = 'Fjallraven', amount = 10900)],
        start_parameter = None,
        photo_url = "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
        photo_height=512,
        photo_width=512)


def category_command(update: Update, context: CallbackContext) -> None:
    categoriesurl = "https://fakestoreapi.com/products/categories"
    categoriesresponse = requests.get(categoriesurl)
    categories = json.loads(categoriesresponse.text)
    button_list = []
    for each in categories:
        button_list.append(InlineKeyboardButton(each, callback_data = each))
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

    productsUrl = "https://fakestoreapi.com/products/category/" + query.data
    productsResponse = requests.get(productsUrl)
    products = json.loads(productsResponse.text)
    button_list = []
    for each in products:
        button_list.append(InlineKeyboardButton(each['title'], callback_data = each['id']))
    reply_markup = InlineKeyboardMarkup(build_menu(button_list,n_cols=2))

    context.bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=reply_markup)

def handle_message(update: Update, context: CallbackContext) -> None:
    text=str(update.message.text).lower()
    response = R.request_message(text)
    update.message.reply_text(response)

def main():
    updater=Updater(keys.apiKey)
    dp =updater.dispatcher
    # dp.add_handler(CommandHandler("start" , start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("product", product_command))
    dp.add_handler(CommandHandler("category", category_command))
    dp.add_handler(CallbackQueryHandler(category_callback))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.start_polling()
    updater.is_idle

main()

