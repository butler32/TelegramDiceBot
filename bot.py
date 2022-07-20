import random
import telebot
from telebot import types

bot = telebot.TeleBot('1765353729:AAEMjwPK9tBy0pDUSl9HBwZirM9JYtzFPbo')

random.seed()

@bot.message_handler(commands="/roll1")
def roll1(message):
    rand = int(random.randint(1, 6))
    bot.reply_to(message, f"Выпало {rand}")

@bot.message_handler(commands="/roll2")
def roll2(message):
    rand = int(random.randint(1, 6))
    num = rand
    rand = int(random.randint(1, 6))
    bot.reply_to(message, f"Выпало {num} + {rand}")

@bot.message_handler(commands="/roll3")
def roll3(message):
    rand = int(random.randint(1, 6))
    num1 = rand
    rand = int(random.randint(1, 6))
    num2 = rand
    rand = int(random.randint(1, 6))
    bot.reply_to(message, f"Выпало {num1} + {num2} + {rand}")

bot.polling()