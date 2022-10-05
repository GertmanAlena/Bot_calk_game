from distutils.command.config import config
import imp
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
from anecAPI import anecAPI
from bot_command import *
import telebot

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

TITLE, TASK = 'title', 'task'

one_task = {
    'title': None,
    'description': None
}

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', bot_command.start)],

        states={
            TITLE:[MessageHandler(Filters.text, add_title), CommandHandler('no', exit_add)],
            TASK: [MessageHandler(Filters.text, add_task),
               CommandHandler('no', bot_command.exit_add)]
               },
        fallbacks=[CommandHandler('no', exit_add)]
)

