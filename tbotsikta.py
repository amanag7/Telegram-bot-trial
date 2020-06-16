import requests
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler, CallbackContext
import threading

def get_url():
	contents = requests.get('https://random.dog/woof.json').json()    
	url = contents['url']
	return url

def bop(update,context):
	url=get_url()
	chat_id = update.message.chat_id
	context.bot.send_photo(chat_id=chat_id, photo=url)

def drinkwater(update,context):
	msg = 'Well done, darling! I am proud of you! Keep going!'
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text=msg)

def drinkrem(context):
	msg='Hey baby! Its been {} minute(s), drink some water.'.format(timer/60)
	context.bot.send_message(chat_id=context.job.context,text=msg)

def startreminder(update,context):
	context.bot.send_message(chat_id=update.message.chat_id,text='Starting the reminder to run every {} minute(s).'.format(timer/60))
	context.job_queue.tick()
	context.job_queue.run_repeating(drinkrem,interval=timer,context=update.message.chat_id)

def stoprem(update,context):
	context.bot.send_message(chat_id=update.message.chat_id,text="The reminder has been stopped, but don't forget to drink water darling.")
	context.job_queue.stop()

# def settimer(update,context):
# 	global timer
# 	timin = ''.join(context.args)
# 	timer = int(timin)*60
# 	context.bot.send_message(chat_id=update.message.chat_id,text="You'll get reminder every {} minute(s) now.".format(timin))

def bae(update,context):
	msg = "I'm missing you! <3 Text me : @sprshag"
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text=msg)

def shutdown():
	updater.stop()
	updater.is_idle=False

def stop(update,context):
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text="Hey! I've stopped successfully. Take care!")
	context.bot.send_message(chat_id='935814583',text="Hey, the bot has been stopped! Chat ID: {}".format(chat_id))
	threading.Thread(target=shutdown).start()

def start(update,context):
	msg = "Hey baby! I'm still awake. Type /help for more commands."
	chat_id = update.message.chat_id
	context.bot.send_message(chat_id=chat_id,text=msg)

def helpe(update,context):
	msg = "Hey sweetheart. Here's a list of commands for you:\n/start : to check if the bot is running.\n/reminder : to start/reset the reminder for something important.\n/woof : to get a surprise.\n/drank : if you drank a lot of water already.\n/bae : to talk to your bae.\n/help : to see the commands list.\n/stop : to stop the bot.\n"
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
	#dp.add_handler(CommandHandler('settimer',settimer))
	dp.add_handler(CommandHandler('reminder',startreminder,pass_job_queue=True))
	#dp.add_handler(CommandHandler('stopreminder',stoprem,pass_job_queue=True))
	updater.start_polling()
	updater.idle()
	
timer = 1800

updater = Updater('1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU',use_context=True)


if __name__=='__main__':
	main()