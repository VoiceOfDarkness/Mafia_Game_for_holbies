from flask import Flask

from config import Config
from database import mongo
from home.home import home_bp
from host.host import host_bp
from player.player import player_bp

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)
mongo.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(host_bp)
app.register_blueprint(player_bp)

if __name__ == "__main__":
    app.run()
