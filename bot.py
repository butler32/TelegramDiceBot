import random
import telebot
import Config
from telebot import types
import re

bot = telebot.TeleBot(Config.TOKEN)

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






@bot.message_handler(regexp="asdroll\s+\d+\s*")
def handle_message(message):
    num = int(re.search(r"(\d+)", message.text).group(0))
    rand = int(random.randint(1, num))
    bot.reply_to(message, f"Выпало {rand}")

@bot.message_handler(regexp="/attack(\s+\d+){5}\s*")
def handle_message(message):
    numbers = re.findall(r"(\d+)", message.text)
    num = re.findall(r"(\d+)", message.text)
    d20 = random.randint(1, 20)
    i = int(num[2])
    if d20 == 1:
        bot.reply_to(message, "Критический промах!")
    elif d20 == 20:
    	bot.reply_to(message, "Крит!")
    	damage = random.randint(1, int(num[3]))
    	while i > 1:
    		damage += random.randint(1, int(num[3]))
    		i -= 1
    	damage += int(num[4])
    	damage += random.randint(1, int(num[3]))
    	while i > 1:
    		damage += random.randint(1, int(num[3]))
    		i -= 1
    	damage += int(num[4])
    	bot.reply_to(message, f"{damage} урона")
    elif (d20 + int(num[0])) >= int(num[1]):
    	damage = random.randint(1, int(num[3]))
    	while i > 1:
    		damage += random.randint(1, int(num[3]))
    		i -= 1
    	damage += int(num[4])
    	bot.reply_to(message, f"{damage} урона")
    else:
        bot.reply_to(message, "Не попал")
        
bot.polling()