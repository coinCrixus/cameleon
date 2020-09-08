import os
import telegram
from dotenv import load_dotenv
load_dotenv()

msg = 'Hello btc world!'
# use token generated in first step
bot = telegram.Bot(token=os.getenv('TELEGRAM_API_TOKEN'))
status = bot.send_message(chat_id="@olafbtcalerts", text=msg, parse_mode=telegram.ParseMode.HTML)

print(status)

