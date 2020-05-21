import telegram

#Read Token
f = open("config/token", "r")
TOKEN = f.readline()

from telegram.ext import Updater
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#SET ALL COMMAND_HANDLERS
from telegram.ext import CommandHandler, Filters, InlineQueryHandler
from Commands import *
test_handler        = CommandHandler('test', test, filters=~Filters.update.edited_message)
start_handler       = CommandHandler('start', start, filters=~Filters.update.edited_message)
dorimetor_handler   = CommandHandler('dorimetor', dorimetor, filters=~Filters.update.edited_message)
dorimes_handler     = CommandHandler('dorimes', dorimes, filters=~Filters.update.edited_message)
rolld20_handler     = CommandHandler('rolld20', rolld20, filters=~Filters.update.edited_message)
doge_handler        = CommandHandler('doge', doge, filters=~Filters.update.edited_message)
cat_handler         = CommandHandler('cat', cat, filters=~Filters.update.edited_message)
birb_handler        = CommandHandler('birb', birb, filters=~Filters.update.edited_message)
dolar_handler       = CommandHandler('dolar', pokeDolar, filters=~Filters.update.edited_message)
euro_handler        = CommandHandler('euro', euro, filters=~Filters.update.edited_message)
libra_handler       = CommandHandler('libra', libra, filters=~Filters.update.edited_message)
iene_handler        = CommandHandler('iene', iene, filters=~Filters.update.edited_message)
bitcoin_handler     = CommandHandler('bitcoin', bitcoin, filters=~Filters.update.edited_message)
litecoin_handler    = CommandHandler('litecoin', litecoin, filters=~Filters.update.edited_message)
ethereum_handler    = CommandHandler('ethereum', ethereum, filters=~Filters.update.edited_message)
charada_handler     = CommandHandler('charada', charada, filters=~Filters.update.edited_message)
hug_handler         = CommandHandler('hug', hug, filters=~Filters.update.edited_message)
wink_handler        = CommandHandler('wink', wink, filters=~Filters.update.edited_message)
pat_handler         = CommandHandler('pat', pat, filters=~Filters.update.edited_message)
meme_handler        = CommandHandler('meme', meme, filters=~Filters.update.edited_message)
sabedoria_handler   = CommandHandler('sabedoria', sabedoria, filters=~Filters.update.edited_message)
sadanimesong_handler = CommandHandler('sadanimesong', sadanimesong, filters=~Filters.update.edited_message)
acende_handler      = CommandHandler('acende', acende, filters=~Filters.update.edited_message)
#inline_handler      = InlineQueryHandler(inline_function)
inline_handler      = InlineQueryHandler(meme_generator)

dispatcher.add_handler(test_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(dorimetor_handler)
dispatcher.add_handler(dorimes_handler)
dispatcher.add_handler(rolld20_handler)
dispatcher.add_handler(doge_handler)
dispatcher.add_handler(cat_handler)
dispatcher.add_handler(birb_handler)
dispatcher.add_handler(dolar_handler)
dispatcher.add_handler(euro_handler)
dispatcher.add_handler(libra_handler)
dispatcher.add_handler(iene_handler)
dispatcher.add_handler(bitcoin_handler)
dispatcher.add_handler(litecoin_handler)
dispatcher.add_handler(ethereum_handler)
dispatcher.add_handler(charada_handler)
dispatcher.add_handler(hug_handler)
dispatcher.add_handler(wink_handler)
dispatcher.add_handler(pat_handler)
dispatcher.add_handler(meme_handler)
dispatcher.add_handler(sabedoria_handler)
dispatcher.add_handler(sadanimesong_handler)
dispatcher.add_handler(acende_handler)
dispatcher.add_handler(inline_handler)

#NON COMMANDS
from telegram.ext import MessageHandler
dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'triste', re.IGNORECASE)), triste))

#START BOT
updater.start_polling()
updater.idle()
updater.stop()