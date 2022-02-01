from os import environ


class Config:
    COIN_MARKET_CAP_API_KEY = environ.get('COIN_MARKET_CAP_API_KEY', '')
    PRICE_FEED_UPDATE_INTERVAL = 10
