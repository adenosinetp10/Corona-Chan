import os
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
from strings import *
from stats import countrylist,global_stats

def start(update : Update, context : CallbackContext)-> None:
    say = update.message.reply_text
    user = update.message.from_user.full_name
    say(START.format(user),parse_mode = ParseMode.HTML,quote=False)
    say(HAPPY_FACE)

def search(update : Update, context : CallbackContext)-> None:
    say = update.message.reply_text
    query = ' '.join([i.capitalize() for i in context.args])
    if len(query) == 0:
        say(LEN_ZERO,parse_mode=ParseMode.HTML,quote=False)
    else:
        if countrylist(query) is False:
            say(COUNTRY_NOT_FOUND,parse_mode = ParseMode.HTML,quote=False)
        else:
            update.message.reply_photo(open('img.png','rb'),caption = countrylist(query),parse_mode = ParseMode.HTML,quote=False)

def help(update : Update, context : CallbackContext)-> None:
    user = update.message.from_user.full_name
    update.message.reply_animation(open('c_gif.gif','rb'),caption=HELP.format(user),parse_mode = ParseMode.HTML,quote=False)

def list(update : Update, context : CallbackContext)-> None:
    say = update.message.reply_text
    say(COUNTRY_LIST_1,parse_mode = ParseMode.HTML,quote=False)
    say(COUNTRY_LIST_2,parse_mode = ParseMode.HTML,quote=False)
    say(COUNTRY_LIST_3,parse_mode = ParseMode.HTML,quote=False)

def gstats(update : Update, context : CallbackContext)-> None:
    
    update.message.reply_photo(open('earth_chan.jpg','rb'),caption = global_stats(),parse_mode = ParseMode.HTML,quote=False)
    
    
            
if __name__ == "__main__":
    
    updater = Updater(os.environ.get("BOT_TOKEN",""))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start,run_async=True))
    dp.add_handler(CommandHandler("search",search,run_async=True))
    dp.add_handler(CommandHandler("help",help,run_async=True))
    dp.add_handler(CommandHandler("list",list,run_async=True))
    dp.add_handler(CommandHandler("global",gstats,run_async=True))

    updater.start_polling()
    updater.idle()
