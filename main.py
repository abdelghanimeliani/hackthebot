from telegram.ext import *

import const as keys
import response as R

print("bda el bot")

def start_command(update,context):
    update.message.reply_text('type something to get sstarted')

def help_command(update,context):
    update.message.reply_text('if you want help chouf google')

def handle_message(update,context):
    text=str(update.message.text).lower()
    response = R.request_message(text)
    update.message.reply_text(response)

def main():
    updater=Updater(keys.apiKey)
    dp =updater.dispatcher
    dp.add_handler(CommandHandler("start" , start_command))
    dp.add_handler(CommandHandler("start", help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.start_polling()
    updater.is_idle


main()

