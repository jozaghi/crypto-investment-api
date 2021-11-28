from dataclasses import dataclass
from datetime import datetime


@dataclass
class Coin:
    id: str
    symbol: str
    name: str
    icon: str


