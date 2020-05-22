import time
import schedule
import requests

def Tbot_sendtext(bot_msg):

	bot_token = '1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU'
	chat_ID = '935814583'
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+chat_ID+'&parse_mode=Markdown&text='+bot_msg

	response = requests.get(send_text)

	return response.json()


def drinkwater():
	msg = 'Hey baby, it has been 30 minutes, drink some water.'
	Tbot_sendtext(msg)

schedule.every(1).minutes.do(drinkwater)

while True:
	schedule.run_pending()
	time.sleep(1)