import requests


def get_exchange_rate(currency):
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': currency})
    currency_and_price = response.json()
    price = round(float(currency_and_price['price']), 2)
    return str(price)
