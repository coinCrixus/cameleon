from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

#class Student(Base):
#    __tablename__ = 'students'
#    name = Column(String)
#    seq = Column(Integer, primary_key=True)
#
#    def __init__(self, name):
#        self.name = name

class CoinGeckoCoin(Base):
    __tablename__ = 'coingecko_coin'
    id     = Column(String, primary_key=True) 
    symbol = Column(String)
    name   = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    def __init__(self, id, symbol, name):
        self.id     = id
        self.symbol = symbol
        self.name   = name

class CoinGeckoExchange(Base):
    __tablename__ = 'coingecko_exchange'
    id      = Column(String, primary_key=True)
    name    = Column(String)
    year_established = Column(Integer)
    country = Column(String)
    description = Column(String)
    url = Column(String)
    image = Column(String)
    has_trading_incentive = Column(Boolean)
    trust_score = Column(Integer)
    trust_score_rank = Column(Integer)
    trade_volume_24h_btc = Column(Numeric)
    trade_volume_24h_btc_normalized = Column(Numeric)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    def __init__(self, id, name, year_established, country, description, url, image, has_trading_incentive, trust_score, trust_score_rank,trade_volume_24h_btc
                , trade_volume_24h_btc_normalized):
        self.id     = id
        self.symbol = symbol
        self.name   = name
