import telegram
import os
import sys
import db

def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    """Handler for unhandled exceptions that will write to the logs"""
    if issubclass(exc_type, KeyboardInterrupt):
        # call the default excepthook saved at __excepthook__
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    print("Unhandled exception", exc_type, exc_value, exc_traceback)

sys.excepthook = handle_unhandled_exception

################

#Read Token
TOKEN = os.getenv("TOKEN")
PORT = int(os.environ.get('PORT', 5000))

from telegram.ext import Updater
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

#SETUP DB
db.setup()

#SET ALL COMMAND_HANDLERS
from telegram.ext import CommandHandler, Filters, InlineQueryHandler
from Commands import *

command_handlers = []
command_handlers.append(CommandHandler('start', start, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('dorimetor', dorimetor, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('dorimes', dorimes, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('rolld20', rolld20, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('doge', doge, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('cat', cat, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('birb', birb, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('dolar', pokeDolar, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('euro', euro, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('libra', libra, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('iene', iene, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('bitcoin', bitcoin, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('litecoin', litecoin, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('ethereum', ethereum, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('charada', charada, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('hug', hug, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('wink', wink, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('pat', pat, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('meme', meme, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('sabedoria', sabedoria, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('sadanimesong', sadanimesong, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('acende', acende, filters=~Filters.update.edited_message))
#command_handlers.append(CommandHandler('weather', weather, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('shame', shame, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('resumo', resumo, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('barbixas', barbixas, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('dbtest', db_test, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('dbprint', db_printa_msgs, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('dbrestart', db_restart, filters=~Filters.update.edited_message))
command_handlers.append(CommandHandler('dbclearesumo', db_clear_resumo, filters=~Filters.update.edited_message))
#command_handlers.append(InlineQueryHandler(inline_function))
#command_handlers.append(InlineQueryHandler(meme_generator))

for handler in command_handlers:
    dispatcher.add_handler(handler)

#NON COMMANDS
from telegram.ext import MessageHandler
dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'triste', re.IGNORECASE)), triste))
dispatcher.add_handler(MessageHandler(~Filters.update.edited_message, db_insere_msg))

#START BOT
heroku_link = os.getenv("HEROKU_LINK")
updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook(heroku_link + TOKEN)

updater.idle()