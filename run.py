import os
import configparser
from sqlalchemy import create_engine
from sqlalchemy import Column,String
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

from models import CoinGeckoCoin

db_string = os.getenv("DB_STRING")

db = create_engine(db_string)  
base = declarative_base()

Session = sessionmaker(db)  
session = Session()

# Create 
coin = CoinGeckoCoin('reserve0121','RSR','Reserve protocol')
session.merge(coin)  
session.commit()

# Read
coins = session.query(CoinGeckoCoin)  
for coin in coins:  
    print(coin.symbol)



