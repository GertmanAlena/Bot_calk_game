from random import randint
from telegram import BotCommand, Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackContext
import log


go, go_end, first_choice, start_game, heads_or_tails, moves_user, moves_bot, second_choice,\
     numb, math, test_test, ex = range(12)

number = []
alem = []
max = 4
min = 1

def start(update,_):
    log.data_recording(update.effective_user.first_name)
    reply_keyboard = [['да', 'нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}! идём дальше?', reply_markup=markup_key,)
    return go

def start2(update,_):
   
    if update.message.text == 'да':
        reply_keyboard = [['калькулятор', 'игра', 'выход']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(f'{update.effective_user.first_name}! выбирай', reply_markup=markup_key,)
        return first_choice
    if update.message.text == 'нет':
        update.message.reply_text(f'{update.effective_user.first_name}! Пока')
    return ConversationHandler.END


def choise(update,_):
    if update.message.text == 'калькулятор':
        log.data_recording2(update.effective_user.first_name)
        reply_keyboard = [['рациональные', 'комплексные']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(f'{update.effective_user.first_name}! выбирай', reply_markup=markup_key,)
        return second_choice
    if update.message.text == 'игра': 
        update.message.reply_text(f'{update.effective_user.first_name}!\n'
            'с каким количеством конфет будем играть?')
        return start_game
    if update.message.text == 'выход': 
        update.message.reply_text(f'{update.effective_user.first_name}! Пока')
    return ConversationHandler.END
    

def choise2(update,_):
    # text = update.message.text
    if update.message.text == 'рациональные':
        update.message.reply_text(f'введите пример')
        return numb
    # else: 
    #     update.message.reply_text(f'введите пример')
    #     x = complex( update.message.reply_text("Введите первое комплексное число: "))
    #     y = complex( update.message.reply_text("Введите второе комплексное число: "))
    #     oper =  update.message.reply_text("Введите математическую операцию: (+, -, *, /)")
    #     res = 0
    # if oper == '+':
    #     res = x+y
    #     return res
    # elif oper == '-':
    #     res = x-y
    #     return res  
    # elif oper == '*':
    #     res = x*y
    #     return res
    # elif oper == '/':
    #     res = x/y
    #     return res 
    # update.message.reply_text(f'ответ {res} ещё посчитаем?')
       

def get_number(update, _):
    reply_keyboard = [['да', 'нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    number = []
    alem = []
    global number_list
    number_list = []
    global numb1   #тут введённый пример
    numb1 = update.message.text
    # global number    # тут положили цифры
    # global alem    # тут положили знаки
    temp_num = ''   # тут склеиваем цифры
    numb1 += '='
    for char in numb1:
        if char.isdigit():
            temp_num += char
        else:
            number.append(temp_num)
            alem.append(char)
            temp_num = ''
    # update.message.reply_text(f'Я тут, {update.effective_user.first_name}! получилось {number} и {alem[:-1]}')

    operators_list = ['/', '*', '-', '+']
    priority_list = [1, 1, 2, 2]
    unite_list = list(zip(priority_list, operators_list))
                                        # [(1, '/'), (1, '*'), (2, '-'), (2, '+')]  
    operators = {
    '*': lambda x, y: int(x)*int(y),
    '/': lambda x, y: int(x)/int(y),
    '+': lambda x, y: int(x)+int(y),
    '-': lambda x, y: int(x)-int(y)
    }
    oper_list = alem[:-1]
    number_list = number
    
    for i in unite_list:        # i в (1, '/'), (1, '*'), (2, '-'), (2, '+')
        if i[0] == 1:           # [(1, '/')  6-2*4-6
            for j in oper_list: # ['-', '+', '*', '=']
                if j == i[1]:
                    index_alem = oper_list.index(j)
                    if j in ' /':
                        while j in oper_list:
                            if int(number_list[index_alem+1]) == 0:
                                print("нельзя делить на ноль") 
                                break
                            else:    
                                num = operators[j](number_list[index_alem], number_list[index_alem+1])
                                number_list.pop(index_alem)
                                number_list.pop(index_alem)
                                number_list.insert(index_alem, num)
                                oper_list.pop(index_alem)
                    if j in '*':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            number_list.pop(index_alem)
                            number_list.pop(index_alem)
                            number_list.insert(index_alem, num)
                            oper_list.pop(index_alem)
    for i in unite_list:    # i в (1, '/'), (1, '*'), (2, '-'), (2, '+')
        if i[0] == 2:            # i в (2, '-'), (2, '+')
            for j in oper_list:  # ['-', '+', '*', '=']
                
                if j == i[1]:
                    index_alem = oper_list.index(j)
                   
                    if j in '-':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            number_list.pop(index_alem)
                            number_list.pop(index_alem)
                            number_list.insert(index_alem, num)
                            oper_list.pop(index_alem)
                    if j in '+':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            number_list.pop(index_alem)
                            number_list.pop(index_alem)
                            number_list.insert(index_alem, num)
                            oper_list.pop(index_alem)
    update.message.reply_text(f'ответ {number_list} ещё посчитаем?')
    update.message.reply_text(f'{update.effective_user.first_name}! хватит или хотите продолжить?\n'
                                    , reply_markup=markup_key,)
    return go

def result_num(update,_):
    text = update.message.text
    if text.lower() == 'да':
        return go
    elif text.lower() == 'нет':
        return ex
    else:
        update.message.reply_text(update.effective_chat.id, 'я тебя не понимаю')

def exit(update, _):
    update.message.reply_text(update.effective_chat.id, f'Операция прервана')
    return ConversationHandler.END


def pop_insert_list(number_list, index_alem, num, oper_list):
    number_list.pop(index_alem)
    number_list.pop(index_alem)
    number_list.insert(index_alem, num)
    oper_list.pop(index_alem)

def number_of_candies(update, _):
    global total_sweets
    total_sweets = int(update.message.text)
    reply_keyboard = [['бросить манетку']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(f'{update.effective_user.first_name}! теперь бросим манетку\n'
                            'кто ходит первым', reply_markup=markup_key,)   
   
    return heads_or_tails

def rand(update,_):
    global total_sweets
    global step_bot
    first_step = randint(1, 2)
    if first_step == 1:
        update.message.reply_text(f'{update.effective_user.first_name},ты начинашь игру!!!\n'
        'сколько конфет ты берёшь?')
        # number_of_candies = player_step(number_of_candies, min, max)
        return moves_user   
    if first_step == 2:  #  вызывает функцию, длля бота
        update.message.reply_text(f'{update.effective_user.first_name},игру начинает Бот!!')
        # moves_game_bot(update, context)
        
        step_bot = randint(1, max)
        total_sweets = total_sweets - step_bot
        update.message.reply_text(f' БОТТ взял {step_bot} осталось {total_sweets} конфет \n'
        'Берите конфеты!!')
        # return moves_user
        return moves_bot

def test(update, context):
    
    context.bot.send_message(update.effective_chat.id, "сколько конфет берёшь?")
    return moves_user

def moves_game_user(update, context):   
    global total_sweets
    global max
    step_player = int(update.message.text)
   
    if step_player >= total_sweets or step_player <= 0 or step_player > max:
        context.bot.send_message(update.effective_chat.id,'попробуйте еще. ')
        step_player = int(update.message.text)
        return test(update, context)
    
    else:
        total_sweets = total_sweets - step_player
        context.bot.send_message(update.effective_chat.id,f'Вы взяли {step_player}, осталось {total_sweets} конфет\n'
        'теперь ходит бот!')
        return moves_game_bot(update, context)


def moves_game_bot(update, context):
    global total_sweets
    if total_sweets == min:
        reply_keyboard = [['да', 'нет']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        context.bot.send_message(update.effective_chat.id,f' Бот проиграл!!')
        update.message.reply_text(f'{update.effective_user.first_name}! хватит или хотите продолжить?\n'
                                    , reply_markup=markup_key,)
        return go
    if total_sweets == max+max+3: 
        step_bot = max-1
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' ББот взял {step_bot} осталось {total_sweets} конфет \n'
        'Берите конфеты!!')
        return moves_user
    if total_sweets > max+3: 
        step_bot = randint(1, max)
        total_sweets = total_sweets - step_bot
        update.message.reply_text(f' БОТТ взял {step_bot} осталось {total_sweets} конфет \n'
        'Берите конфеты!!')
        return moves_user
    if total_sweets > max*3+1: 
        step_bot = min+1
        total_sweets = total_sweets - step_bot
        update.message.reply_text(f' БОТТ взял {step_bot} осталось {total_sweets} конфет \n'
        'Берите конфеты!!')
        return moves_user
    if total_sweets == max+3: 
        step_bot = min
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' БОт взял {step_bot} осталось {total_sweets} конфет \n'
        'Берите конфеты!!')
        return moves_user
    if total_sweets == max:
        reply_keyboard = [['да', 'нет']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        
        step_bot = max-1
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' боТ взял {step_bot} осталось {total_sweets} конфет \n'
        'ВЫ ПРОИГРАЛИ!!')
        update.message.reply_text(f'{update.effective_user.first_name}! хватит или хотите продолжить?\n'
                                    , reply_markup=markup_key,)
        return go
    if total_sweets == max+1:
        reply_keyboard = [['да', 'нет']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        step_bot = max
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' БОТ взял {step_bot} осталось {total_sweets} конфет \n'
        'ВЫ ПРОИГРАЛИ!!')
        update.message.reply_text(f'{update.effective_user.first_name}! хватит или хотите продолжить?\n'
                                    , reply_markup=markup_key,)
        return go
    if total_sweets == max*3:
        step_bot = min
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' бот взял {step_bot} осталось {total_sweets} конфет \n'
        'Берите конфеты!!')
        return moves_user
    if total_sweets == max*2+2:
        step_bot = max
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' бот взял {step_bot} осталось {total_sweets} конфет \n'
        'Берите конфеты!!')
        return moves_user
    if total_sweets == min+1:
        reply_keyboard = [['да', 'нет']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        step_bot = min
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' бот взял {step_bot} осталось {total_sweets} конфет \n'
        'Бот выиграл!!')
        update.message.reply_text(f'{update.effective_user.first_name}! хватит или хотите продолжить?\n'
                                    , reply_markup=markup_key,)
        return go
    if total_sweets == max-1:
        reply_keyboard = [['да', 'нет']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        step_bot = 2
        total_sweets = total_sweets - step_bot
        context.bot.send_message(update.effective_chat.id,f' бот взял {step_bot} осталось {total_sweets} конфет \n'
        'Бот выиграл!!')
        update.message.reply_text(f'{update.effective_user.first_name}! хватит или хотите продолжить?\n'
                                    , reply_markup=markup_key,)
        return go
    if total_sweets == 1:
        reply_keyboard = [['да', 'нет']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        context.bot.send_message(f'осталась {total_sweets} конфета \n'
        'Бот выиграл!!')
        update.message.reply_text(f'{update.effective_user.first_name}! хватит или хотите продолжить?\n'
                                    , reply_markup=markup_key,)
        return go


