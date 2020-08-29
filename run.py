import os
import json
import requests

from sqlalchemy import create_engine
from sqlalchemy import Column,String
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

from models import CoinGeckoCoin,CoinGeckoExchange,CoinGeckoTicker


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
    coinObject = CoinGeckoCoin(coin['id'], coin['symbol'], coin['name'], False)
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
    , False)
    session.merge(exchangeObject)

session.commit()

# loop through exchanges and get tickers
#exchanges = session.query(CoinGeckoExchange).filter(CoinGeckoExchange.deactivated == False)
exchanges = session.query(CoinGeckoExchange).all()

for exchange in exchanges:
    print("processing exchange [{}]".format(exchange.name))
    pagenr = 1
    while pagenr > 0:
        request_url = "https://api.coingecko.com/api/v3/exchanges/{}/tickers?include_exchange_logo=true&page={}".format(exchange.id,pagenr)
        response = requests.get(request_url)
        try:
            tickers = json.loads(response.text)['tickers']
        
            if len(tickers) == 0 :
                pagenr = 0
            else:
                pagenr += 1
                for ticker in tickers:
                    tickerObject = CoinGeckoTicker(exchange.id
                    , ticker['coin_id'], ticker.get('target_coin_id','default')
                    , ticker['base'], ticker['target']
                    , ticker['last'], ticker['volume']
                    , ticker['converted_last']['btc']
                    , ticker['converted_last']['eth']
                    , ticker['converted_last']['usd']
                    , ticker['converted_volume']['btc']
                    , ticker['converted_volume']['eth']
                    , ticker['converted_volume']['usd']
                    , ticker['trust_score'], ticker['bid_ask_spread_percentage'], ticker['timestamp']
                    , ticker['last_traded_at'], ticker['last_fetch_at'], ticker['is_anomaly']
                    , ticker['is_stale'], ticker['trade_url'],False)
                    session.merge(tickerObject)
                session.commit()
        except:
            pagenr = 0
            print(response)

    


# Read
#coins = session.query(CoinGeckoCoin)  
#for coin in coins:  
#    print(coin.symbol)
