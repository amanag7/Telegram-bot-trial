"""
	Telegram Bot made for Sikta to remind her to drink water regularly!
	Author: Aman Agrawal

"""

import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import threading

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
	""" Start message """
	msg = "Hey baby! I'm here.\nType /help for more commands."
	update.message.reply_text(msg)


def helpe(update: Update, context: CallbackContext) -> None:
	""" Display the help message """
	msg = """Hey sweetheart! Here's a list of commands for you:
			/start : to check if the bot is running.
			/help : to see the commands list.
			/set : to set the reminder in minutes as:
				\t/set <minutes>
			/unset : to stop the reminder.
			/drank : if you drank a lot of water already.
			/current : to show the current timer.
			/bae : to talk to your bae.
			/woof : to get a surprise.
			/stop : to stop the bot."""
	
	chat_id = update.message.chat_id
	if str(chat_id) == '935814583':
		msg += "\n/siktastart: to start sikta's timer.\n/siktastop: to stop sikta's timer."

	update.message.reply_text(msg)


def get_url():
	""" Getting the different dog pictures using API """
	contents = requests.get('https://random.dog/woof.json').json()    
	url = contents['url']
	return url

def bop(update: Update, context: CallbackContext) -> None:
	""" Displaying cute dog pictures """
	url=get_url()
	chat_id = update.message.chat_id
	context.bot.send_photo(chat_id=chat_id, photo=url)


def bae(update: Update, context: CallbackContext) -> None:
	""" To display a message to talk to me """
	chat_id = update.message.chat_id
	msg = "I'm missing you! <3 Text me : @sprshag"
	context.bot.send_message(chat_id=chat_id,text=msg)
	context.bot.send_message(chat_id='935814583',text="Hey, your girl wants to chat! Hit her up: @siktasharma")


def remove_job_if_exists(name, context):
	""" Remove a job with a given name. Returns whether job was removed. """
	current_jobs = context.job_queue.get_jobs_by_name(name)
	if not current_jobs:
		return False
	for job in current_jobs:
		job.schedule_removal()
	return True

def set_timer(update: Update, context: CallbackContext) -> None:
	""" Add a job to the queue """
	chat_id = update.message.chat_id
	try:
		# args[0] has the time for the timer in minutes
		global timer
		timer = int(context.args[0])*60
		if timer < 0:
			update.message.reply_text('Give it a positive number, baby.')
			return

		job_removed = remove_job_if_exists(str(chat_id), context)
		context.job_queue.run_repeating(drinkrem, interval=timer,context=chat_id,name=str(chat_id))

		text = "Timer successfully set!"
		if job_removed:
			text += "\nOld timer was removed.."
		update.message.reply_text(text)

	except(IndexError, ValueError):
		update.message.reply_text('Use it as: /set <minutes>')

def drinkrem(context):
	""" Displaying message periodically """
	job = context.job
	msg='Hey baby! Its been {} minutes, drink some water.'.format(int(timer/60))
	context.bot.send_message(job.context,text=msg)


def unset(update: Update, context: CallbackContext) -> None:
	""" To stop the timer """
	chat_id = update.message.chat_id
	job_removed = remove_job_if_exists(str(chat_id),context)

	msg = "Timer successfully stopped, darling.\nDon't forget to drink regularly!" if job_removed else "You have no active timer.\nSet one so I can remind you regularly!"
	update.message.reply_text(msg)


def drank(update: Update, context: CallbackContext) -> None:
	""" Drinking appreciation and timer reset """
	chat_id = update.message.chat_id

	job_removed = remove_job_if_exists(str(chat_id),context)
	context.job_queue.run_repeating(drinkrem, interval=timer,context=chat_id,name=str(chat_id))

	msg = 'Well done, darling! Keep going...'
	if job_removed:
		msg += ' Timer reset.'
	update.message.reply_text(msg)


def current(update: Update, context: CallbackContext) -> None:
	""" To show the current timer set """
	msg = "The current timer is: {} minutes".format(int(timer/60))
	msg += "\n You can use /drank to start the timer with this current time."
	update.message.reply_text(msg)


def siktastart(update: Update, context: CallbackContext) -> None:
	""" To start Sikta's timer from my side """
	chat_id = 752111336
	global timer
	
	job_removed = remove_job_if_exists(str(chat_id),context)
	context.job_queue.run_repeating(drinkrem, interval=timer,context=chat_id,name=str(chat_id))

	state = "reset " if job_removed else "started "
	msg = "Timer "+state+"by Mann for {} minutes".format(int(timer/60))
	context.bot.send_message(chat_id=chat_id, text=msg)
	update.message.reply_text("Starting her timer...")


def siktastop(update: Update, context: CallbackContext) -> None:
	""" To stop Sikta's timer from my side """
	chat_id = 752111336
	job_removed = remove_job_if_exists(str(chat_id),context)

	if job_removed:
		context.bot.send_message(chat_id=chat_id, text="Your timer has been stopped by me. Take care, baby...")

	warn = "Stopping her timer..." if job_removed else "No timer present"
	update.message.reply_text(warn)


def stop(update: Update, context: CallbackContext) -> None:
	""" To shutdown the bot """
	chat_id = update.message.chat_id

	job_removed = remove_job_if_exists(str(chat_id),context)
	update.message.reply_text("Stopping..")
	context.bot.send_message(chat_id='752111336', text="The bot has been stopped successfully.. Take care baby!")
	warning = "Hey, the bot has been stopped successfully!"  if job_removed else "Hey, the bot has been stopped! No active jobs."
	warning += "\nChat ID: {}".format(chat_id)
	context.bot.send_message(chat_id='935814583',text=warning)

	threading.Thread(target=shutdown).start()

def shutdown():
	updater.stop()
	updater.is_idle=False


def main():
	""" Main function """

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# answering different commands using functions
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('help', helpe))
	dp.add_handler(CommandHandler('woof',bop))
	dp.add_handler(CommandHandler('bae',bae))
	dp.add_handler(CommandHandler('set',set_timer))
	dp.add_handler(CommandHandler('unset',unset))
	dp.add_handler(CommandHandler('drank',drank))
	dp.add_handler(CommandHandler('current',current))
	dp.add_handler(CommandHandler('siktastart',siktastart))
	dp.add_handler(CommandHandler('siktastop',siktastop))
	dp.add_handler(CommandHandler('stop', stop))
	
	# Start the bot
	updater.start_polling()
	updater.idle()


timer = 3600

updater = Updater('1194260976:AAGqYFgCJeDNzKX_vqlTIgl9gfMf9VMwLYU',use_context=True)


if __name__=='__main__':
	main()