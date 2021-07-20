from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''Hai {member.full_name} , \n\n`Iam a Simple Welcome Bot. Add me to your group and make me as admin.\n\n👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz) ''')

def help(updater,context):
 updater.message.reply_text("➠ `Add Me To Group`\n\nMake Admin Me\n\n👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz)")\
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hai {member.full_name} , Welcome to ln Support\n\n💖Thank💖You💖For💖Joining💖')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
