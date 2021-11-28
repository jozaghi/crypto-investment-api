import threading
import time
from flask_socketio import emit

from src.price_feed.price_feed_repository import PriceFeedRepository


def start(interval: int, price_feed_repository: PriceFeedRepository, app) -> None:
    def run_job(app):
        while True:
            latest_coin_prices = price_feed_repository.get_latest_prices()
            with app.app_context():
                for coin_price in latest_coin_prices:
                    emit("feed", coin_price.to_json(), namespace="", to=coin_price.coin_id)
            print("Job executed")
            time.sleep(interval)
    thread = threading.Thread(target=run_job, kwargs={'app': app})
    thread.start()

