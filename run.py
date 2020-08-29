import os
import json
import requests

from sqlalchemy import create_engine
from sqlalchemy import Column,String
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

from models import CoinGeckoCoin


# setup db connection session
db_string = os.getenv("DB_STRING")
db = create_engine(db_string)  
base = declarative_base()
Session = sessionmaker(db)  
session = Session()

# get json coingecko coin list
response = requests.get("https://api.coingecko.com/api/v3/coins/list")
coins    = json.loads(response.text)

for coin in coins:
    coinObject = CoinGeckoCoin(coin['id'], coin['symbol'], coin['name'])
    session.merge(coinObject)

session.commit()


# Read
#coins = session.query(CoinGeckoCoin)  
#for coin in coins:  
#    print(coin.symbol)
