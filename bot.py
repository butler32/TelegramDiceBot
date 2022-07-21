import random
import telebot

bot = telebot.TeleBot('1765353729:AAEMjwPK9tBy0pDUSl9HBwZirM9JYtzFPbo')

random.seed()

if __name__ == '__main__':
	@bot.message_handler(commands="/roll1")
	def roll1(message):
		num1 = int(random.randint(1, 6))
		bot.reply_to(message, f"Выпало {num1}")

	@bot.message_handler(commands="/roll2")
	def roll2(message):
		num1 = int(random.randint(1, 6))
		num2 = int(random.randint(1, 6))
		bot.reply_to(message, f"Выпало {num1} + {num2}")

	@bot.message_handler(commands="/roll3")
	def roll3(message):
		num1 = int(random.randint(1, 6))
		num2 = int(random.randint(1, 6))
		num3 = int(random.randint(1, 6))
		bot.reply_to(message, f"Выпало {num1} + {num2} + {num3}")

	bot.polling()

