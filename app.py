from flask import Flask, render_template
from flask_socketio import join_room

from config import Config
from database import mongo
from home.home import home_bp
from host.host import host_bp
from player.player import player_bp
from websock import socketio

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)
mongo.init_app(app)
socketio.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(host_bp)
app.register_blueprint(player_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on('join_room')
def handle_join_room(data):
    room = data['room']
    join_room(room)


if __name__ == "__main__":
    socketio.run(app, debug=True)
