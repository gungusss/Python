from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

cmc = CoinMarketCapAPI('ecbcd302-0924-48c8-8a55-fa8b33093a65')

r = cmc.tools_priceconversion(symbol='BTC')

print(r.data)

