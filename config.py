from os import environ


class Config:
    COIN_MARKET_CAP_API_KEY = environ.get('COIN_MARKET_CAP_API_KEY', '885cef66-883b-4245-9b42-888287c0722f')
    PRICE_FEED_UPDATE_INTERVAL = 10
