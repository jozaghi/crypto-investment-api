from datetime import datetime

from src.price_feed.price_feed_schema import CoinPrice


def test_CoinPrice__to_json__creates_valid_json():
    coin_price = CoinPrice(
        coin_id='BTC',
        current_price=5000,
        date=datetime(2021, 11, 26, 20, 20, 20, 111)
    )

    result = coin_price.to_json()

    assert result == '{"coinId": "BTC", "currentPrice": 5000, "date": "2021-11-26T20:20:20.000111"}'

