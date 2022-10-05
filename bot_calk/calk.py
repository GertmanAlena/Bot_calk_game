from unittest import result
from bot_command import *

numb1 = ''
def get_number(message):
    global numb1   #тут ведённый пример
    numb1 = message.text
    number = []   # тут положили цифры
    alem = []   # тут положили знаки
    temp_num = ''   # тут склеиваем цифры
    numb1 += '='
    for char in numb1:
        if char.isdigit():
            temp_num += char
        else:
            number.append(temp_num)
            alem.append(char)
            temp_num = ''
    bot_api_version.register_next_step_handler(number, alem[:-1], calk)
    return number, alem[:-1]

def pop_insert_list(number_list, index_alem, num, oper_list):
    number_list.pop(index_alem)
    number_list.pop(index_alem)
    number_list.insert(index_alem, num)
    oper_list.pop(index_alem)

def calk(oper_list, number_list):
    global numb2
    global numb3
    operators_list = ['/', '*', '-', '+']
    priority_list = [1, 1, 2, 2]
    unite_list = list(zip(priority_list, operators_list))

    operators = {
    '*': lambda x, y: int(x)*int(y),
    '/': lambda x, y: int(x)/int(y),
    '+': lambda x, y: int(x)+int(y),
    '-': lambda x, y: int(x)-int(y)
    }
    for i in unite_list:                
        if i[0] == 1:           # i в (1, '/'), (1, '*')
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
                                pop_insert_list(number_list, index_alem, num, oper_list)
                             

                    if j in '*':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            pop_insert_list(number_list, index_alem, num, oper_list)
    for i in unite_list:    
        if i[0] == 2:           
            for j in oper_list:
                
                if j == i[1]:
                    index_alem = oper_list.index(j)
                   
                    if j in '-':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            pop_insert_list(number_list, index_alem, num, oper_list)
                    if j in '+':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            pop_insert_list(number_list, index_alem, num, oper_list)
    bot_api_version.register_next_step_handler(number_list, result_num)
    return number_list