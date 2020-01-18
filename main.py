import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def voice(update, context):
	if update.message.text == 'власть':
		cite = "Злой Артес: Я получил власть, которая и не снилась моему отцу!"
		button_list = [
			[InlineKeyboardButton(cite, callback_data='EvilArthasPissed3')]
		]
		reply_markup = InlineKeyboardMarkup(button_list)
		context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите фразу", reply_markup=reply_markup)
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text='Такой фразы пока у меня нет :(')


def cb_handler(update, context):
	if update.callback_query.data == 'EvilArthasPissed3':
		context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('sounds/EvilArthasPissed3.ogg', 'rb'))


def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
	print('Starting bot...')
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	token = open('token.txt', mode='r').readline()
	updater = Updater(token, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(MessageHandler(Filters.text, voice))
	dp.add_handler(CallbackQueryHandler(cb_handler))
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()
	print('Bot finished working.')


if __name__ == '__main__':
	main()
