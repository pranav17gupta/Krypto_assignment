import apikey
import requests

headers = {
  'X-CMC_PRO_API_KEY' : apikey.key,
  'Accepts' : application/json'
}

params = {
  'start' : '1',
  'limit' : '5' ,
  convert : 'USD'
}

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'

json = requests.get(url, params=params, header=headers).json()

coins = json['data']

/*taking input from url*/
userid = request.args['userid']
price = request.args['price']
crypto = request.args['crypto']

/*checking the current price of cryptocurrency is equals to target price*/
for x in coins: 
  if x['current_price'] == price && x[id] == crypto:
    sendEmail(userid, crypto, price)
