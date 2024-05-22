import telebot
from telebot import types
from time import sleep
import random
import json
import os

with open('history.json', 'r') as json_file:
    data = json.load(json_file)

app = telebot.TeleBot("6406531245:AAF2F2coXQnbto48OkYxSDFPnJvX9LSoW8o")
blocker = 0

delete_markup = telebot.types.ReplyKeyboardRemove()

@app.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Угадай число(1-100)")
    button2 = types.KeyboardButton("Поделить число на 1")
    button3 = types.KeyboardButton("Конвертер валют")
    button4 = types.KeyboardButton("Угадай мой ник")
    markup.add(button1, button2, button3, button4)
    app.send_message(message.chat.id, text="Выбери игру".format(message.from_user), reply_markup=markup)
    
@app.message_handler(content_types=['text'])
def func(message):
    global blocker
    if blocker == 0:
        blocker = 1
        if(message.text == "Угадай число(1-100)"):
            
            sent_message = app.send_message(message.chat.id, text="Угадай число от 1 до 100", reply_markup=delete_markup)
            app.register_next_step_handler(sent_message, digit_handler)
            
        elif(message.text == "Поделить число на 1"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Последние 10 запросов")
            markup.add(button1)
            sent_message = app.send_message(message.chat.id, text="Какое число поделить?", reply_markup=markup)
            app.register_next_step_handler(sent_message, auto_divider)
            
        elif(message.text == "Конвертер валют"):
            sent_message = app.send_message(message.chat.id, text="Введите сумму", reply_markup=delete_markup)
            app.register_next_step_handler(sent_message, prof_converter)
        elif(message.text == "Угадай мой ник"):
            app.send_message(message.chat.id, text="Ваш ник: {0.first_name}".format(message.from_user))
        else:
            app.send_message(message.chat.id, text="Такого еще нет.".format(message.from_user))
        blocker = 0
    
    
def digit_handler(message):
    global blocker
    if blocker == 0:
        blocker += 1
        digit = message.text
        digit_text = str(digit)
        try:
            digit_num = int(digit)
        except:
            digit_num = 73210031616321
        the_right_digit = random.randint(1, 100)
        
        if(digit_text == 'Треугольник' or digit_num == the_right_digit):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Угадай число(1-100)")
            button2 = types.KeyboardButton("Поделить число на 1")
            button3 = types.KeyboardButton("Конвертер валют")
            button4 = types.KeyboardButton("Угадай мой ник")
            markup.add(button1, button2, button3, button4)
            app.send_message(message.chat.id, text="ТЫ ПОБЕДИЛ!".format(message.from_user), reply_markup=markup)
        elif digit_num == 73210031616321:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Угадай число(1-100)")
            button2 = types.KeyboardButton("Поделить число на 1")
            button3 = types.KeyboardButton("Конвертер валют")
            button4 = types.KeyboardButton("Угадай мой ник")
            markup.add(button1, button2, button3, button4)
            app.send_message(message.chat.id, text="Это даже не число... Хоть попробуй!!", reply_markup=markup)
        else:
            app.send_message(message.chat.id, text="О НЕТ, ТЫ ПРОИГРАЛ!".format(message.from_user))
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Угадай число(1-100)")
            button2 = types.KeyboardButton("Поделить число на 1")
            button3 = types.KeyboardButton("Конвертер валют")
            button4 = types.KeyboardButton("Угадай мой ник")
            markup.add(button1, button2, button3, button4)
            app.send_message(message.chat.id, text="Верное число было: " + str(the_right_digit), reply_markup=markup)
        blocker = 0
    
def auto_divider(message):
    with open('history.json', 'r') as json_file:
        data = json.load(json_file)
    global blocker
    if blocker == 0:
        blocker += 1
        try:
            answer = message.text
        
            last_ten = ''
            if answer == 'Последние 10 запросов':
                blocker = 1
                for i in data:
                    last_ten += i['data'] + '\n'
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1 = types.KeyboardButton("Угадай число(1-100)")
                button2 = types.KeyboardButton("Поделить число на 1")
                button3 = types.KeyboardButton("Конвертер валют")
                button4 = types.KeyboardButton("Угадай мой ник")
                app.send_message(message.chat.id, text='Последние 10 запросов:\n' + last_ten.format(message.from_user), reply_markup=markup)
                blocker = 0
            else:
                answer = int(message.text)
                app.send_message(message.chat.id, text="Это может занять какое-то время...".format(message.from_user))
                json_data = str(answer) + '/1' + ' = ' + str(answer)

                sleep(2)
                app.send_message(message.chat.id, text="Это сложнее чем кажется!".format(message.from_user))
                photos = os.listdir('photo')
                photo_name = random.choice(photos)
                sleep(4)
                photo = open('photo/' + photo_name, 'rb')
                app.send_photo(message.chat.id, photo)
                sleep(6)
                app.send_message(message.chat.id, text="Извлекаю кубический корень...".format(message.from_user))
                sleep(2)
                app.send_message(message.chat.id, text="Секундочку...".format(message.from_user))
                sleep(5)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1 = types.KeyboardButton("Угадай число(1-100)")
                button2 = types.KeyboardButton("Поделить число на 1")
                button3 = types.KeyboardButton("Конвертер валют")
                button4 = types.KeyboardButton("Угадай мой ник")
                markup.add(button1, button2, button3, button4)
                data.append({'data': json_data})
                with open('history.json', 'w') as json_file:
                    json.dump(data, json_file)
                app.send_message(message.chat.id, text='Итак ' + str(answer) + ' делёное на 1 равно ' + str(answer).format(message.from_user), reply_markup=markup)
                blocker = 0
        except Exception as e:
            print(e)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Угадай число(1-100)")
            button2 = types.KeyboardButton("Поделить число на 1")
            button3 = types.KeyboardButton("Конвертер валют")
            button4 = types.KeyboardButton("Угадай мой ник")
            app.send_message(message.chat.id, text='ОЙОЙОЙОЙ SOMETHING WENT WRONG! Пиши вследующий раз цифры, бал1.'.format(message.from_user), reply_markup=markup)
            blocker = 0

def prof_converter(message):
    global blocker
    if blocker == 0:
        blocker += 1
        global summa
        summa = message.text
        if isinstance(summa, int):
            sent_message = app.send_message(message.chat.id, text="Из какой валюты конвертируем?")
            app.register_next_step_handler(sent_message, prof_converter_final)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Угадай число(1-100)")
            button2 = types.KeyboardButton("Поделить число на 1")
            button3 = types.KeyboardButton("Конвертер валют")
            button4 = types.KeyboardButton("Угадай мой ник")
            markup.add(button1, button2, button3, button4)
            app.send_message(message.chat.id, text='Имей совесть! Хоть тут напиши число.', reply_markup=markup)
        blocker = 0
        
        
def prof_converter_final(message):
    global blocker
    if blocker == 0:
        blocker += 1
        value = message.text
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Угадай число(1-100)")
        button2 = types.KeyboardButton("Поделить число на 1")
        button3 = types.KeyboardButton("Конвертер валют")
        button4 = types.KeyboardButton("Угадай мой ник")
        markup.add(button1, button2, button3, button4)
        app.send_message(message.chat.id, text='Итак ' + summa + value + ' это немного больше чем 0₽', reply_markup=markup)   
        blocker = 0
        

app.polling()