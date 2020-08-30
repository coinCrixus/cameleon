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

class CoinGeckCoinData(Base):
    __tablename__ = 'coingecko_coindata'
    id                              = Column(String, primary_key=True)
    asset_platform_id               = Column(String)
    public_notice                   = Column(String)
    homepage                        = Column(String)
    twitter_screen_name             = Column(String)
    telegram_channel_identifier     = Column(String)
    image_url_thumb                 = Column(String)
    image_url_small                 = Column(String)
    image_url_large                 = Column(String)
    country_origin                  = Column(String)
    sentiment_votes_up_percentage   = Column(Numeric)
    sentiment_votes_down_percentage = Column(Numeric)
    market_cap_rank                 = Column(Numeric)
    coingecko_rank                  = Column(Numeric)
    coingecko_score                 = Column(Numeric)
    developer_score                 = Column(Numeric)
    community_score                 = Column(Numeric)
    liquidity_score                 = Column(Numeric)
    public_interest_score           = Column(Numeric)
    twitter_followers               = Column(Numeric)
    telegram_channel_user_count     = Column(Numeric)
    created_at                      = Column(DateTime(timezone=True), default=func.now())
    updated_at                      = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    deactivated                     = Column(Boolean, default=False)

    def __init__(self, id, asset_platform_id,public_notice,homepage,twitter_screen_name,telegram_channel_identifier,image_url_thumb,image_url_small,image_url_large
                ,country_origin,sentiment_votes_up_percentage,sentiment_votes_down_percentage,market_cap_rank,coingecko_rank,coingecko_score,developer_score
                ,community_score,liquidity_score,public_interest_score,twitter_followers,telegram_channel_user_count,deactivated):
        self.id                                 = id
        self.asset_platform_id                  = asset_platform_id
        self.public_notice                      = public_notice
        self.homepage                           = homepage
        self.twitter_screen_name                = twitter_screen_name
        self.telegram_channel_identifier        = telegram_channel_identifier
        self.image_url_thumb                    = image_url_thumb
        self.image_url_small                    = image_url_small
        self.image_url_large                    = image_url_large
        self.country_origin                     = country_origin
        self.sentiment_votes_up_percentage      = sentiment_votes_up_percentage
        self.sentiment_votes_down_percentage    = sentiment_votes_down_percentage
        self.market_cap_rank                    = market_cap_rank
        self.coingecko_rank                     = coingecko_rank
        self.coingecko_score                    = coingecko_score
        self.developer_score                    = developer_score
        self.community_score                    = community_score
        self.liquidity_score                    = liquidity_score
        self.public_interest_score              = public_interest_score
        self.twitter_followers                  = twitter_followers
        self.telegram_channel_user_count        = telegram_channel_user_count
        self.deactivated                        = deactivated

class CoinGeckCoinTag(Base):
    __tablename__ = 'coingecko_cointag'
    coin_id         = Column(String, primary_key=True)
    tag_group_id    = Column(String, primary_key=True)
    tag_id          = Column(String, primary_key=True)
    created_at                      = Column(DateTime(timezone=True), default=func.now())
    updated_at                      = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    deactivated                     = Column(Boolean, default=False)
    
    def __init__(self, coin_id, tag_group_id , tag_id, deactivated):
        self.coin_id        = coin_id
        self.tag_group_id   = tag_group_id
        self.tag_id         = tag_id
        self.deactivated    = deactivated
        