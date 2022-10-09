from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
import bot_command as bc


bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

TITLE, TASK = 'title', 'task'

one_task = {
    'title': None,
    'description': None
}

start_handler = ConversationHandler(entry_points = [CommandHandler('start', bc.start)],
    states = {
        bc.go:[MessageHandler(Filters.regex('^(да|нет)$'), bc.start2)],
        bc.first_choice:[MessageHandler(Filters.regex('^(калькулятор|игра|выход)$'), bc.choise)],
        bc.start_game:[MessageHandler(Filters.text, bc.number_of_candies)],
        bc.heads_or_tails:[MessageHandler(Filters.regex('^(бросить манетку)$'), bc.rand)],
        bc.moves_user:[MessageHandler(Filters.text, bc.moves_game_user)],
        bc.test_test:[MessageHandler(Filters.text, bc.test), CommandHandler('no', bc.exit)],
        bc.moves_bot:[MessageHandler(Filters.text, bc.moves_game_bot)],
        bc.second_choice:[MessageHandler(Filters.regex('^(рациональные|комплексные)$'), bc.choise2)],
        bc.numb:[MessageHandler(Filters.text, bc.get_number)],
        bc.math:[MessageHandler(Filters.text, bc.result_num)],
        bc.ex:[MessageHandler(Filters.text, bc.exit)],
        
    },
    fallbacks=[CommandHandler('no', bc.exit)],
)

# start_handler = CommandHandler('start', bot_command.start)
dispatcher.add_handler(start_handler)
        
print('server started')
updater.start_polling()
updater.idle()
