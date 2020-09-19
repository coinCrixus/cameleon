from huobi import HuobiRestClient
client = HuobiRestClient(access_key='frbghq7rnm-004dc987-fb3baeb8-04c86', secret_key='ff053cec-06dec3aa-3a15eecf-39e65')
trades = client.market_history_trade(symbol='ethusdt').data
trades
print(trades)
#help(HuobiRestClient)

kline = client.market_history_kline(symbol='btcusdt').data
kline = client.market_history_kline(symbol='btcusdt').data
kline = client.market_history_kline(symbol='btcusdt').data
print(kline)


#help(HuobiRestClient)
