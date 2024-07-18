from flask import render_template
from flask.blueprints import Blueprint

from database import mongo

player_bp = Blueprint(
    "player_bp", __name__, url_prefix="/player", template_folder="templates"
)


@player_bp.route("/<name>")
def player(name: str):
    player = mongo.db.players.find_one_or_404({"name": name})

    return render_template("player.html", player=player)
