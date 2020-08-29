import os
import json
import requests

from sqlalchemy import create_engine
from sqlalchemy import Column,String
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

from models import CoinGeckoCoin,CoinGeckoExchange


# setup db connection session
db_string = os.getenv("DB_STRING")
db = create_engine(db_string)  
base = declarative_base()
Session = sessionmaker(db)  
session = Session()

# deactivate current coin records
session.query(CoinGeckoCoin).update({CoinGeckoCoin.deactivated: True})

# get json coingecko coin list
response = requests.get("https://api.coingecko.com/api/v3/coins/list")
coins    = json.loads(response.text)

for coin in coins:
    coinObject = CoinGeckoCoin(coin['id'], coin['symbol'], coin['name'], True)
    session.merge(coinObject)

session.commit()

# deactivate current coin records
session.query(CoinGeckoExchange).update({CoinGeckoExchange.deactivated: True})

# get json coingecko exchange list
response = requests.get("https://api.coingecko.com/api/v3/exchanges")
exchanges = json.loads(response.text)

for exchange in exchanges:
    exchangeObject = CoinGeckoExchange(exchange['id'], exchange['name'], exchange['year_established'], exchange['country'], exchange['description'], exchange['url']
    , exchange['image'], exchange['has_trading_incentive'], exchange['trust_score'], exchange['trust_score_rank'], exchange['trade_volume_24h_btc'], exchange['trade_volume_24h_btc_normalized']
    , True)
    session.merge(exchangeObject)

session.commit()


# Read
#coins = session.query(CoinGeckoCoin)  
#for coin in coins:  
#    print(coin.symbol)
