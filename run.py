import os
import json
import requests
import time
import logging

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column,String
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

from models import CoinGeckoCoin,CoinGeckoExchange,CoinGeckoTicker,CoinGeckoCoinData,CoinGeckoCoinTag

# logging
logging.basicConfig(filename='example.log',level=os.getenv('LOG_LEVEL'),format='%(asctime)s - %(levelname)s:%(message)s', datefmt='%d-%b-%y %H:%M:%S')

# setup db connection session
db_string = os.getenv("DB_STRING")
db = create_engine(db_string)  
base = declarative_base()
Session = sessionmaker(db)  
session = Session()

# deactivate current coin records
session.query(CoinGeckoCoin).update({CoinGeckoCoin.deactivated: True})

# get json coingecko coin list
print("{} updating coingecko coin list".format(datetime.now()))
logging.info("Updating coingecko coin list")
response = requests.get("https://api.coingecko.com/api/v3/coins/list")
coins    = json.loads(response.text)

for coin in coins:
    coinObject = CoinGeckoCoin(coin['id'], coin['symbol'], coin['name'], False)
    session.merge(coinObject)

session.commit()


# get json coingeck coin data
print("{} updating coingecko coin data".format(datetime.now()))
logging.info("Updating coingecko coin data")

# loop through coins and get coin data
coins = session.query(CoinGeckoCoin).filter(CoinGeckoCoin.deactivated == False).all()
for coin in coins:
    print("{} processing coin [{}]".format(datetime.now() ,coin.id))
    request_url = "https://api.coingecko.com/api/v3/coins/{}?localization=false&tickers=false&market_data=false&developer_data=false&sparkline=true".format(coin.id)
    exit = False
    loops = 0
    time.sleep(0.15)
    while exit == False and loops < 20:
        loops+=1
        time.sleep(0.01)
        response = requests.get(request_url)
        try:
            if response.status_code == 429:
                print('Http code 429, trying again in 5 seconds')
                time.sleep(5)
            elif response.status_code == 200:
                coinData = json.loads(response.text)
                coinDataObject = CoinGeckoCoinData(
                    coin.id,
                    coinData.get('asset_platform_id'),
                    coinData.get('public_notice'),
                    coinData.get('links').get('homepage')[0],
                    coinData.get('links').get('twitter_screen_name'),
                    coinData.get('links').get('telegram_channel_identifier'),
                    coinData.get('image').get('thumb'),
                    coinData.get('image').get('small'),
                    coinData.get('image').get('large'),
                    coinData.get('country_origin'),
                    coinData.get('sentiment_votes_up_percentage'),
                    coinData.get('sentiment_votes_down_percentage'),
                    coinData.get('market_cap_rank'),
                    coinData.get('coingecko_rank'),
                    coinData.get('coingecko_score'),
                    coinData.get('developer_score'),
                    coinData.get('community_score'),
                    coinData.get('liquidity_score'),
                    coinData.get('public_interest_score'),
                    coinData.get('community_data').get('twitter_followers'),
                    coinData.get('community_data').get('telegram_channel_user_count'),
                    False)
                session.merge(coinDataObject)
                

                categories = coinData.get('categories')

                for cat in categories:
                    coinTagObject = CoinGeckoCoinTag(coin.id,'categories',cat,True)
                    session.merge(coinTagObject)
                
                session.commit()
                exit = True
            else:
                print("Error, httpcode {}".format(response.status_code))
                exit = True
        except Exception as e:
            logging.error(e)
            print("Error {}".format(e) )
            exit = True
            



# deactivate current coin records
session.query(CoinGeckoExchange).update({CoinGeckoExchange.deactivated: True})

# get json coingecko exchange list
print("{} updating coingecko exchange list".format(datetime.now() ) )
logging.info("Updating coingecko exchange list")
response = requests.get("https://api.coingecko.com/api/v3/exchanges")
exchanges = json.loads(response.text)

for exchange in exchanges:
    exchangeObject = CoinGeckoExchange(exchange['id'], exchange['name'], exchange['year_established'], exchange['country'], exchange['description'], exchange['url']
    , exchange['image'], exchange['has_trading_incentive'], exchange['trust_score'], exchange['trust_score_rank'], exchange['trade_volume_24h_btc'], exchange['trade_volume_24h_btc_normalized']
    , False)
    session.merge(exchangeObject)

session.commit()

# loop through exchanges and get tickers
exchanges = session.query(CoinGeckoExchange).all()

for exchange in exchanges:
    print("{} processing exchange [{}]".format(datetime.now() ,exchange.name))
    logging.info("processing exchange [{}]".format(exchange.name))

    time.sleep(1)
    pagenr = 1
    while pagenr > 0:
        request_url = "https://api.coingecko.com/api/v3/exchanges/{}/tickers?include_exchange_logo=true&page={}".format(exchange.id,pagenr)
        response = requests.get(request_url)
        print("{}                         \___ {}".format(datetime.now() , request_url))
        try:
            if response.status_code == 429:
                print('Http code 429, trying againg in 2 seconds')
                time.sleep(2)
            elif response.status_code == 200:
                tickers = json.loads(response.text)['tickers']
        
                if len(tickers) == 0 :
                    pagenr = 0
                else:
                    pagenr += 1
                    for ticker in tickers:
                        tickerObject = CoinGeckoTicker(exchange.id
                        , ticker['base'], ticker['target']
                        , ticker['coin_id'], ticker.get('target_coin_id','default')
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
            else:
                print("Error, httpcode {}".format(response.status_code))
                pagenr = 0
        except Exception as e:
            logging.error(e)
            print("Error {}".format(e) )
            pagenr = 0
            
    


# Read
#coins = session.query(CoinGeckoCoin)  
#for coin in coins:  
#    print(coin.symbol)
