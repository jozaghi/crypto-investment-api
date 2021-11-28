from datetime import datetime


class Coin:
    id: str
    name: str
    icon: str


class CoinPrice:
    coin: Coin
    current_price: float
    date: datetime
