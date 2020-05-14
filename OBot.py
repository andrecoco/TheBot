import telegram
TOKEN = ""

from telegram.ext import Updater
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#SET ALL COMMAND_HANDLERS
from telegram.ext import CommandHandler
from Commands import *
start_handler       = CommandHandler('start', start)
dorimetor_handler   = CommandHandler('dorimetor', dorimetor)
dorimes_handler     = CommandHandler('dorimes', dorimes)
rolld20_handler     = CommandHandler('rolld20', rolld20)
doge_handler        = CommandHandler('doge', doge)
cat_handler         = CommandHandler('cat', cat)
birb_handler        = CommandHandler('birb', birb)
dolar_handler       = CommandHandler('dolar', pokeDolar)
euro_handler        = CommandHandler('euro', euro)
libra_handler       = CommandHandler('libra', libra)
iene_handler        = CommandHandler('iene', iene)
bitcoin_handler     = CommandHandler('bitcoin', bitcoin)
litecoin_handler    = CommandHandler('litecoin', litecoin)
ethereum_handler    = CommandHandler('ethereum', ethereum)
charada_handler     = CommandHandler('charada', charada)
hug_handler         = CommandHandler('hug', hug)
wink_handler        = CommandHandler('wink', wink)
pat_handler         = CommandHandler('pat', pat)
meme_handler        = CommandHandler('meme', meme)
sabedoria_handler   = CommandHandler('sabedoria', sabedoria)
sadanimesong_handler = CommandHandler('sadanimesong', sadanimesong)
acende_handler      = CommandHandler('acende', acende)

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

#NON COMMANDS
from telegram.ext import MessageHandler, Filters
dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'triste', re.IGNORECASE)), triste))
                        
                        

#START BOT
updater.start_polling()
updater.idle()
updater.stop()