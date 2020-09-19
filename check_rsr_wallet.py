import os
import json
import requests
import sendMessageTelegramChannel



# rsr wallet
contract = '0x8762db106B2c2A0bccB3A80d1Ed41273552616E8'
address  = '0xdc2a3e304a4d48e9d93b351596d0d97314d5df7d'

#contract = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
#address  = '0x7e2c8909b4e3bace1cb371a3a176562b43fe4964'
offset   = 100
sort   = 'asc'

url = 'https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={}&address={}#tokentxns&page=1&offset={}&sort={}'.format(contract,address,offset,sort)
print(url)
response = requests.get(url)

with open('check_rsr_last_block.txt', 'r') as f:
    lines = f.read().splitlines()
    check_rsr_last_block = lines[-1]
    print(check_rsr_last_block)

try:
    if response.status_code != 200:
                print('Http code 429, trying again in 5 seconds')
                
    elif response.status_code == 200:
        json = json.loads(response.text)
        result = json.get('result')
        for txn in result:
            blockNumber = txn.get('blockNumber')
            txnHash = txn.get('hash')
            tokens = int(txn.get('value')) / (10**int(txn.get('tokenDecimal')))
            print('blocknumber{} ,tokens {}'.format(blockNumber,tokens) )
        lastBlockNumber = blockNumber
        if lastBlockNumber != check_rsr_last_block:
            txnUrl = 'https://etherscan.io/tx/{}'.format(txnHash)
            sendMessageTelegramChannel.sendTelegramMessage('RSR wallet check: last transaction seen blockNumber {} tokens {}, see {}'.format(blockNumber,tokens,txnUrl))

except Exception as exc:
            print("Error {}".format(exc) )
            exit = True