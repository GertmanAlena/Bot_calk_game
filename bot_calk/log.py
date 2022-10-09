from datetime import datetime as dt
import logging
from time import time

def data_recording(arg):

    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(f'{time} время \n')
        file.write('\n' + f'Пользователь {arg} вошёл в игру' + '\n')
        
def data_recording2(arg):

    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(f'{time} время \n')
        file.write('\n' + f'Пользователь {arg} выбрал калькулятор' + '\n')

#остальное записывается также. Времени нет ... но как делать поняла