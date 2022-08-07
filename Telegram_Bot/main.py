import logging  # return logs
from telegram.ext import *
import responses  # return responses


APT_KEY = "5427165954:AAGBfJxxQWAwtdqLgnDVoGF07YB1AxTQAqo"


# set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) # not important line
logging.info("Starting bot")


def start_command(update,context):
    update.message.reply_text("Hello there! I\'m a bot. What\'s up?")

def help_command(update,context):
    update.message.reply_text("Try typing anything and i will do my best to respond")
    
def custom_command(update,context):
    update.message.reply_text("This is cusotm command, you can do any thing you want")


def handle_massage(update,context):
    text = str(update.message.text).lower()
    response = responses.get_responses(text)
    logging.info(f"User: %s, Message: %s", update.message.chat.id,text)
    
    
    # bot responses
    update.message.reply_text(response)

def error(update,context):
    logging.error("Update caused error: %s", context.error)


if __name__ == '__main__':
    updater = Updater(APT_KEY, use_context=True)
    dp = updater.dispatcher
    
    # commands
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("custom", custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_massage))
    
    # log all errors
    dp.add_error_handler(error)

    # run the bot
    updater.start_polling(1)  # check update every 1 seconds
    updater.idle() # wait for updates


