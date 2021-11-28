import pytest
from datetime import datetime

from src.price_feed.price_feed_repository import PriceFeedRepository


def test_PriceFeedReposotory__given_empty_api_key__raise_value_exception():
    with pytest.raises(ValueError, match='coin_market_cap_api_key is required.'):
        PriceFeedRepository('')

def test_PriceFeedReposotory__pars_coin_market_cap_response__given_valid_response__return_valid_coin_price():
    api_response = {
        "data": [
            {
                "id": 1,
                "name": "Bitcoin",
                "symbol": "BTC",
                "quote": {
                    "USD": {
                        "price": 54814.97927559948,
                        "last_updated": "2021-11-27T18:30:02.000Z"
                    }
                }
            }
        ]
    }

    price_feed_repository = PriceFeedRepository('AAA')

    result = price_feed_repository.pars_coin_market_cap_response(api_response)

    assert len(result) == 1
    assert result[0].coin_id == 'BTC'
    assert result[0].current_price == 54814.97927559948
    assert result[0].date == datetime(2021, 11, 27, 18, 30, 2)


def test_PriceFeedReposotory__get_latest_prices__coin_market_cap_api_is_working():
    # coin market cap api integration test
    price_feed_repository = PriceFeedRepository('885cef66-883b-4245-9b42-888287c0722f')

    result = price_feed_repository.get_latest_prices()

    assert len(result) > 0
