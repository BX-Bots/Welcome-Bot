from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''π·ππ , \n\nπΈππ  π  ππππππ  πππππππ  π±ππ.  π°ππ  ππ  ππ  π’πππ  πππππ  πππ  ππππ  ππ  ππ  πππππ\n\nπ² πΌπππππππππ  π±π’ : @BX_Botz ''')

def help(updater,context):
 updater.message.reply_text("β  π°ππ  πΌπ  ππ  πΆππππ\n\nβ  πΌπππ  π°ππππ  πΌπ\n\nπ² πΌπππππππππ  π±π’ : @BX_Botz")\
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hai {member.full_name} , Welcome to ln Support\n\nπThankπYouπForπJoiningπ')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
