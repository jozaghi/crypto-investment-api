from dataclasses import dataclass
from datetime import datetime
import json


@dataclass
class CoinPrice:
    coin_id: str
    current_price: float
    date: datetime

    def to_json(self)->str:
        return json.dumps({
            'coinId': self.coin_id,
            'currentPrice': self.current_price,
            'date': self.date.isoformat()
        })
