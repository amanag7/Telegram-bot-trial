import time
import schedule
import requests
from telegram.ext import Updater, CommandHandler
import re

def get_url():
	contents = requests.get('https://random.dog/woof.json').json()    
	url = contents['url']
	return url

def bop(bot,update):
	url=get_url()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)

def Tbot_sendtext(bot_msg):

	bot_token = '1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU'
	chat_ID = update.message.chat_id
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+chat_ID+'&parse_mode=Markdown&text='+bot_msg

	response = requests.get(send_text)

	return response.json()


def drinkwater():
	msg = 'Hey baby, it has been 30 minutes, drink some water.'
	Tbot_sendtext(msg)

# schedule.every(30).minutes.do(drinkwater)

# while True:
# 	schedule.run_pending()
# 	time.sleep(1)

def main():
	updater = Updater('1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU')
	dp = updater.dispatcher
	dp.add_handler(CommandHamdler('woof',bop))
	updater.start_polling()
	updater.idle()
	drinkwater()

if __name__=='__main__':
	main()