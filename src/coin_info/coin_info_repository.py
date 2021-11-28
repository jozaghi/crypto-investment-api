from typing import List

from src.coin_info.coin_info_schema import Coin


class CoinInfoRepository:
    def get_coins(self) -> List[Coin]:
        # todo replace with database call
        return [
            Coin(
                id='BTC',
                symbol='BTC',
                name='Bitcoin',
                icon='https://cdn.icon-icons.com/icons2/1487/PNG/512/8369-bitcoin_102502.png'
            ),
            Coin(
                id='ETH',
                symbol='ETH',
                name='Ethereum',
                icon='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/220px-Ethereum-icon-purple.svg.png'
            ),
            Coin(
                id='BNB',
                name='Binance',
                symbol='BNB',
                icon='https://cryptocoin.news/wp-content/wpmowebp/wp-content/uploads/2019/04/binance-coin.webp'
            ),
        ]
