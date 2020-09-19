import os
import telegram
from dotenv import load_dotenv
load_dotenv()

def sendTelegramMessage(msg):
    #msg = 'Hello btc world!'
    # use token generated in first step
    telegram_token   = os.getenv('TELEGRAM_API_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_API_CHAT_ID')
    bot = telegram.Bot(token=telegram_token)
    status = bot.send_message(chat_id=telegram_chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)