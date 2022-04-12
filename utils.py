import requests
import json
from config import currencies

class ConvertionException(Exception):
    pass

class CrypConverter:
    @staticmethod
    def convert(curr1: str, amount: str, curr2: str):

        if curr1 == curr2:
            raise ConvertionException(f'Одинаковые валюты {curr1}!')

        try:
            curr1_ticker = currencies[curr1][0]
        except KeyError:
            raise ConvertionException(f'Невозможно обработать валюту {curr1}')

        try:
            curr2_ticker = currencies[curr2][0]
        except KeyError:
            raise ConvertionException(f'Невозможно обработать валюту {curr2}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Невозможно обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={curr1_ticker}&tsyms={curr2_ticker}')
        base = json.loads(r.content)[currencies[curr2][0]]

        return base