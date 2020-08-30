from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class CoinGeckoCoin(Base):
    __tablename__ = 'coingecko_coin'
    id          = Column(String, primary_key=True) 
    symbol      = Column(String)
    name        = Column(String)
    created_at  = Column(DateTime(timezone=True), default=func.now())
    updated_at  = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    deactivated = Column(Boolean, default=False)

    def __init__(self, id, symbol, name, deactivated):
        self.id          = id
        self.symbol      = symbol
        self.name        = name
        self.deactivated = deactivated

class CoinGeckoExchange(Base):
    __tablename__ = 'coingecko_exchange'
    id                              = Column(String, primary_key=True)
    name                            = Column(String)
    year_established                = Column(Integer)
    country                         = Column(String)
    description                     = Column(String)
    url                             = Column(String)
    image                           = Column(String)
    has_trading_incentive           = Column(Boolean)
    trust_score                     = Column(Integer)
    trust_score_rank                = Column(Integer)
    trade_volume_24h_btc            = Column(Numeric)
    trade_volume_24h_btc_normalized = Column(Numeric)
    created_at                      = Column(DateTime(timezone=True), default=func.now())
    updated_at                      = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    deactivated                     = Column(Boolean, default=False)

    def __init__(self, id, name, year_established, country, description, url, image, has_trading_incentive, trust_score, trust_score_rank,trade_volume_24h_btc
                , trade_volume_24h_btc_normalized, deactivated):
        self.id                              = id
        self.name                            = name
        self.year_established                = year_established
        self.country                         = country
        self.description                     = description
        self.url                             = url
        self.image                           = image
        self.has_trading_incentive           = has_trading_incentive
        self.trust_score                     = trust_score
        self.trust_score_rank                = trust_score_rank
        self.trade_volume_24h_btc            = trade_volume_24h_btc
        self.trade_volume_24h_btc_normalized = trade_volume_24h_btc_normalized
        self.deactivated                     = deactivated

class CoinGeckoTicker(Base):
    __tablename__ = 'coingecko_ticker'
    exchange_id          = Column(String, primary_key=True)
    base_currency        = Column(String, primary_key=True)
    target_currency      = Column(String, primary_key=True)
    base_coin_id         = Column(String)
    target_coin_id       = Column(String)
    last_price           = Column(Numeric)
    volume               = Column(Numeric)
    converted_last_btc   = Column(Numeric)
    converted_last_eth   = Column(Numeric)
    converted_last_usd   = Column(Numeric)
    converted_volume_btc = Column(Numeric)
    converted_volume_eth = Column(Numeric)
    converted_volume_usd = Column(Numeric)
    trust_score          = Column(String)
    bid_ask_spread_perc  = Column(Numeric)
    timestamp            = Column(DateTime)
    last_traded_at       = Column(DateTime)
    last_fetch_at        = Column(DateTime)
    is_anomaly           = Column(Boolean)
    is_stale             = Column(Boolean)
    trade_url            = Column(String)
    created_at           = Column(DateTime(timezone=True), default=func.now())
    updated_at           = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    deactivated          = Column(Boolean, default=False)

    def __init__(self, exchange_id, base_currency, target_currency, base_coin_id, target_coin_id, last_price, volume, converted_last_btc, converted_last_eth, converted_last_usd
            , converted_volume_btc, converted_volume_eth, converted_volume_usd, trust_score, bid_ask_spread_perc, timestamp, last_traded_at, last_fetch_at
            , is_anomaly, is_stale, trade_url, deactivated):
        self.exchange_id          = exchange_id
        self.base_currency        = base_currency
        self.target_currency      = target_currency
        self.base_coin_id         = base_coin_id
        self.target_coin_id       = target_coin_id
        self.last_price           = last_price
        self.volume               = volume
        self.converted_last_btc   = converted_last_btc
        self.converted_last_eth   = converted_last_eth
        self.converted_last_usd   = converted_last_usd
        self.converted_volume_btc = converted_volume_btc
        self.converted_volume_eth = converted_volume_eth
        self.converted_volume_usd = converted_volume_usd
        self.trust_score          = trust_score
        self.bid_ask_spread_perc  = bid_ask_spread_perc
        self.timestamp            = timestamp
        self.last_traded_at       = last_traded_at
        self.last_fetch_at        = last_fetch_at
        self.is_anomaly           = is_anomaly
        self.is_stale             = is_stale
        self.trade_url            = trade_url
        self.deactivated          = deactivated