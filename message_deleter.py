import telebot
import random
from datetime import datetime

bot = telebot.TeleBot( "TOKEN" )

@bot.message_handler( commands = ['start', 'help'] )
def send_welcome( message ):
	bot.reply_to(message, "STRING")

# Deletes 5 or 10 messages including the received message
def annihilation( message ):
	chat_id = message.chat.id
	message_id = message.message_id
	bot_usr = bot.get_me()

	max_removed = 0
	random.seed( datetime.now() )
	coin_flip = random.randint( 0, 1 )
	if coin_flip == 0:
		max_removed = 5
	else:
		max_removed = 10

	removed = 0
	count = 0
	for i in range(0, 100):
		if not ( message.from_user == bot_usr ):
			bot.delete_message( chat_id, message_id - count )
			removed = removed + 1

		if removed == max_removed:
			break

		count = count + 1

# Deletes messages if COMPARE_STRING is in text
@bot.message_handler( func = lambda m: True )
def message_deleter( message ):
	if "COMPARE_STRING" in message.text.lower():
		bot.reply_to( message, "STRING" )

		try:
			annihilation( message )
		except:
			pass

bot.polling()