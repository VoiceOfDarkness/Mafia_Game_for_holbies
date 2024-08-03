from typing import Dict

from bson import ObjectId
from flask import redirect, render_template, url_for
from flask.blueprints import Blueprint

from database import mongo
from utils.role import assign_roles
from websock import socketio

host_bp = Blueprint(
    "host_bp", __name__, url_prefix="/host", template_folder="templates"
)


@host_bp.route("/<code>")
def host(code: str):
    context: Dict = mongo.db.rooms.find_one_or_404({"host_code": code})

    return render_template(
        "host.html", code=code, context=context["players"], status=context["status"]
    )


@host_bp.post("/start-game/<code>")
def start_game(code: str):
    room = mongo.db.rooms.find_one_or_404({"host_code": code})

    if len(room["players"]) < 6:
        return "Need at least 6 players to start the game", 400

    players = room["players"]
    assign_roles(players)

    for player in players:
        mongo.db.players.update_one(
            {"name": player["name"]}, {"$set": {"role": player["role"]}}
        )
        mongo.db.rooms.update_one(
            {"host_code": code, "players.player_id": player["player_id"]},
            {"$set": {"players.$.role": player["role"]}},
        )

    mongo.db.rooms.update_one({"host_code": code}, {
                              "$set": {"status": "started"}})

    for player in players:
        if isinstance(player["player_id"], ObjectId):
            player["player_id"] = str(player["player_id"])

    socketio.emit("update_roles", {"players": players}, room=code)

    return redirect(url_for("host_bp.host", code=code))


@host_bp.post("/end-game/<code>")
def end_game(code: str):
    mongo.db.players.delete_many({"room_code": code})
    mongo.db.rooms.delete_many({"host_code": code})

    return redirect(url_for("home_bp.index"))

