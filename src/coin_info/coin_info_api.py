from flask import Blueprint
from src.coin_info.coin_info_repository import CoinInfoRepository
from flask import jsonify

blueprint = Blueprint(name='coin_api', url_prefix='/coins', import_name=__name__)


@blueprint.route('/', methods=['GET'])
def get_coin_list():
    coin_info_repository = CoinInfoRepository()
    coin_list = coin_info_repository.get_coins()
    return jsonify(results=coin_list)
