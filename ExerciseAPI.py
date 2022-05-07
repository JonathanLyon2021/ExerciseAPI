import time, json, requests

# get tickets from various exchanges 
def btstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last'] # experiment replace last with other values

def bitfinex():
    bitFinexTick = requests.get('http://api.bitfinex.com/v1/ticker/xrpusd')
    return bitFinexTick.json()['last_price']

def coinbase():
    coinBaseTick = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
    return coinBaseTick.json()['data']['amount']

def kraken():
    krakenTick =requests.post('https://api.kraken.com/0/public/Ticker', data=json.dumps({"pair":"XXBTZUSD"}),headers={"content-type":"application/json"})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]

# get last btcusd bid and ask orders from bitstamp orderbook
#bid 
def btStampOrderBookLastBidPrice():
    bitStampOrderBookLastBidPrice = requests.get('https://www.bitstamp.net/api/v2/orderbook/last-book/btcusd/')
    return bitStampOrderBookLastBidPrice.json()['bids'][0][0]
def btStampOrderBookLastBidQuantity():
    btStampOrderBookLastBidQuantity = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return btStampOrderBookLastBidQuantity.json()['bids'][0][1]
    #ask
def btStampOrderBookLastAskPrice():
    btStampOrderBookLastAskPrice = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return btStampOrderBookLastAskPrice.json()['asks'][1][0]

def btStampOrderBookLastAskQuantity():
    bitStampOrderBookLastAskQuantity = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampOrderBookLastAskQuantity.json()['asks'][1][1]

while True:
    btStampUSDLive = float(btstamp())
    coinbUSDLive = float(coinbase())
    krakenUSDLive = float(kraken())
    bitfinexUSDLive = float(bitfinex())

    print (" --- ticker ---")
    print ("Bitstamp Price in USD =", btStampUSDLive)
    print ("Coinbase Price in USD =", coinbUSDLive)
    print ("Kraken Price in USD =", krakenUSDLive)
    print ("Bitfinex Price in USD =", bitfinexUSDLive)
    print (" ")

    btStampOrderBookLastBidP = float(btStampOrderBookLastBidPrice())
    btStampOrderBookLastBidQ = float(btStampOrderBookLastBidQuantity())
    btStampOrderBookLastAskP = float(btStampOrderBookLastAskPrice())
    btStampOrderBookLastAskQ = float(btStampOrderBookLastAskQuantity())

    print (" ---- bitstamp BTC/USD orders ----")
    print ("last bid:")
    print ("       price=", btStampOrderBookLastBidP)
    print ("       quantity=", btStampOrderBookLastBidQ)
    print ("last ask:")
    print ("       price=", btStampOrderBookLastAskP)
    print ("       quantity=", btStampOrderBookLastAskQ)
    print (" ")
    print (" ")
    print (" ")
    time.sleep(3) #120 equals two minutes
    print (" ")
    print (" ")
