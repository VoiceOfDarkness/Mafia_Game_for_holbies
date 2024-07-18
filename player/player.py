from bson.objectid import ObjectId
from flask import render_template
from flask.blueprints import Blueprint

from database import mongo

player_bp = Blueprint(
    "player_bp", __name__, url_prefix="/player", template_folder="templates"
)


@player_bp.route("/<id>")
def player(id: str):
    oid = ObjectId(id)
    player = mongo.db.players.find_one_or_404({"_id": oid})

    return render_template("player.html", player=player)
