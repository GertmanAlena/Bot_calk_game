from distutils.command.config import config
from markupsafe import Markup
from telegram import *
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackContext
from anecAPI import anecAPI
from calk import *
import telebot


def start(update, context):
    arg = context.args
    # arg = del_element(text)
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")

def exit_add(update, context):
    context.bot.send_message(
        update.effective_chat.id, f'Операция прервана')
    return ConversationHandler.END



        

