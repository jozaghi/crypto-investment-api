from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from typing import Iterable

from src.common.util import parse_json_date_time


from src.price_feed.price_feed_schema import CoinPrice


class PriceFeedRepository:
    def __init__(self, coin_market_cap_api_key: str) -> None:
        if not coin_market_cap_api_key:
            raise ValueError('coin_market_cap_api_key is required.')
        self.coin_market_cap_api_key = coin_market_cap_api_key

    def pars_coin_market_cap_response(self, coin_price_response) -> Iterable[CoinPrice]:
        return [
            CoinPrice(
                coin_id=coin['symbol'],
                current_price=coin['quote']['USD']['price'],
                date=parse_json_date_time(coin['quote']['USD']['last_updated'])
            )
            for coin in coin_price_response['data']
        ]

    def get_latest_prices(self) -> Iterable[CoinPrice]:

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start': '1',
          'limit': '10',
          'convert': 'USD'
        }
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': self.coin_market_cap_api_key,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return self.pars_coin_market_cap_response(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            # todo log the exception
            print(e)
            return []
