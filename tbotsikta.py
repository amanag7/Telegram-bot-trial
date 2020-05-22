import time
import schedule
import requests
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler, CallbackContext
import telegram
import threading

def get_url():
	contents = requests.get('https://random.dog/woof.json').json()    
	url = contents['url']
	return url

def bop(update,context):
	url=get_url()
	chat_id = update.message.chat_id
	context.bot.send_photo(chat_id=chat_id, photo=url)

# def Tbot_sendtext(bot_msg):

# 	bot_token = '1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU'
# 	chat_ID = update.message.chat_id
# 	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+chat_ID+'&parse_mode=Markdown&text='+bot_msg

# 	response = requests.get(send_text)

# 	return response.json()


def drinkwater(update,context):
	msg = 'Well done, darling! I am proud of you! Keep going!'
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text=msg)

def drinkrem(context):
	msg='Hey baby! Its been 30 minutes, drink some water.'
	context.bot.send_message(chat_id=context.job.context,text=msg)

def startreminder(update,context):
	context.bot.send_message(chat_id=update.message.chat_id,text='Starting the reminder to run every 30 minutes.')
	context.job_queue.run_repeating(drinkrem,1800,context=update.message.chat_id,first=0)


def bae(update,context):
	msg = "I'm missing you! <3 Text me : @sprshag"
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text=msg)

# schedule.every(30).minutes.do(drinkwater)

# while True:
# 	schedule.run_pending()
# 	time.sleep(1)

def shutdown():
	updater.stop()
	updater.is_idle=False

def stop(update,context):
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text="Hey! I've stopped successfully. Take care!")
	context.bot.send_message(chat_id='935814583',text="Hey, the bot has been stopped!")
	threading.Thread(target=shutdown).start()

def start(update,context):
	msg = "Hey baby! I'm still awake. Type /help for more commands."
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text=msg)

def helpe(update,context):
	msg = "Hey sweetheart. Here's a list of commands for you:\n/start : to check if the bot is running.\n/reminder: to start/reset the reminder for something important.\n/woof : to get a surprise.\n/drank : if you drank a lot of water already.\n/bae : to talk to your bae.\n/help : to see the commands list.\n/stop : to stop the bot.\n"
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text=msg)

def main():
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('woof',bop))
	dp.add_handler(CommandHandler('drank',drinkwater))
	dp.add_handler(CommandHandler('stop', stop))
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('help', helpe))
	dp.add_handler(CommandHandler('bae',bae))
	dp.add_handler(CommandHandler('reminder',startreminder))
	updater.start_polling()
	updater.idle()
	

updater = Updater('1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU',use_context=True)


if __name__=='__main__':
	main()