import os
import telebot
from flask import Flask, request
from telebot import types
from data import *
from functions import *

bot = telebot.TeleBot(inflationBot_token)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def getMessage(message):
    bot.send_message(message.chat.id, start_text, parse_mode='Markdown')


@bot.message_handler(commands=['countries'])
def getMessage(message):
    bot.send_message(message.chat.id, countries_list)


@bot.message_handler(commands=['examples'])
def getMessage(message):
    bot.send_message(message.chat.id, example_text, parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def getMessage(message):
    keyboard = types.InlineKeyboardMarkup()
    url = 'https://github.com/russsik1/inflation_bot/tree/master'
    link = types.InlineKeyboardButton(text='README.md', url=url)
    keyboard.add(link)
    bot.send_message(message.chat.id, help_text, reply_markup=keyboard)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def getMessage(message):
    response = warningMessage
    request = message.text.split(' ')
    if request[0].lower() == 'inflation':
        if len(request) == 3:
            country = countryParser(request[1])
            start = dateParser(request[2])[0]
            end = dateParser(request[2])[1]
            response = CalculateInflationRate(country, start, end)
    elif request[0].lower() == 'price':
        if len(request) == 4:
            country = countryParser(request[2])
            start = dateParser(request[3])[0]
            end = dateParser(request[3])[1]
            response = CalculatePriceChange(country, start, end, request[4])
    elif request[0].lower() == 'value':
        if len(request) == 4:
            country = countryParser(request[2])
            start = dateParser(request[3])[0]
            end = dateParser(request[3])[1]
            response = CalculateValueChange(country, start, end, request[4])

    elif (request[0] + request[1]).lower() == 'getdenominations' or (request[0] + request[1]).lower() == 'getinflation':
        response = not_ready_text

    if '<!DOCTYPE html>' in response:
        response = warningMessage

    bot.send_message(message.chat.id, response)


# @server.route("/bot", methods=['POST'])
# def getMessage():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200
# 
# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url="https://inflationbot.herokuapp.com/bot")
#     return "!", 200
# 
# 
# server.run(host="0.0.0.0", port=os.environ.get('PORT', 5001))
# server = Flask(__name__)

bot.remove_webhook()
bot.polling()
