from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import join_room, leave_room

from src.coin_info import coin_info_api
from src.price_feed import price_feed_job
from src.price_feed.price_feed_repository import PriceFeedRepository


app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('connect')
def on_connect():
    print('Server received connection')


@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    print('Join feed:', room)


@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    print('leave feed:', room)


@app.route('/')
def home():
    return '<h1>Hello world!!!</h1>'


app.register_blueprint(coin_info_api.blueprint)


if __name__ == '__main__':
    price_feed_repository = PriceFeedRepository(app.config['COIN_MARKET_CAP_API_KEY'])
    price_feed_job.start(
        app.config['PRICE_FEED_UPDATE_INTERVAL'],
        price_feed_repository,
        app
    )
    socketio.run(app)
