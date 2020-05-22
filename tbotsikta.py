import time
import schedule
import requests
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler
import re
import threading

def get_url():
	contents = requests.get('https://random.dog/woof.json').json()    
	url = contents['url']
	return url

def bop(bot,update):
	url=get_url()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)

# def Tbot_sendtext(bot_msg):

# 	bot_token = '1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU'
# 	chat_ID = update.message.chat_id
# 	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+chat_ID+'&parse_mode=Markdown&text='+bot_msg

# 	response = requests.get(send_text)

# 	return response.json()


def drinkwater(bot,update):
	msg = 'Hey baby, it has been 30 minutes, drink some water.'
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id,text=msg)	

def bae(bot,update):
	msg = "He's missing you! <3 Go text him : @sprshag"
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id,text=msg)

# schedule.every(30).minutes.do(drinkwater)

# while True:
# 	schedule.run_pending()
# 	time.sleep(1)

def shutdown():
	updater.stop()
	updater.is_idle=False

def stop(bot,update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id,text="Hey! I've stopped successfully. Take care!")
	bot.send_message(chat_id='935814583',text="Hey, the bot has been stopped!")
	threading.Thread(target=shutdown).start()

def start(bot,update):
	msg = "Hey baby! I'm still awake. Type /help for more commands."
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id,text=msg)

def helpe(bot,update):
	msg = "Hey sweetheart. Here's a list of commands for you:\n/start : to check if the bot is running.\n/woof : to get a surprise.\n/drink : to remind yourself to do something important.\n/bae : to talk to your bae.\n/help : to see the commands list.\n/stop : to stop the bot.\n"
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id,text=msg)

def main():
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('woof',bop))
	dp.add_handler(CommandHandler('drink',drinkwater))
	dp.add_handler(CommandHandler('stop', stop))
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('help', helpe))
	dp.add_handler(CommandHandler('bae',bae))
	updater.start_polling()
	updater.idle()
	

updater = Updater('1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU')


if __name__=='__main__':
	main()