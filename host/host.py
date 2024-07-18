from typing import Dict

from flask import render_template, redirect, url_for
from flask.blueprints import Blueprint

from icecream import ic

from database import mongo
from utils.role import assign_roles

host_bp = Blueprint(
    "host_bp", __name__, url_prefix="/host", template_folder="templates"
)


@host_bp.route("/<code>")
def host(code: str):
    context: Dict = mongo.db.rooms.find_one_or_404({"host_code": int(code)})

    ic(context)

    return render_template(
        "host.html", code=code, context=context["players"], status=context["status"]
    )


@host_bp.route("/start-game/<code>", methods=["POST"])
def start_game(code: str):
    room = mongo.db.rooms.find_one_or_404({"host_code": int(code)})

    if len(room["players"]) < 6:
        return "Need at least 6 players to start the game", 400

    players = room["players"]
    assign_roles(players)

    for player in players:
        mongo.db.players.update_one(
            {"name": player["name"]}, {"$set": {"role": player["role"]}}
        )
        mongo.db.rooms.update_one(
            {"host_code": int(code), "players.player_id": player["player_id"]},
            {"$set": {"players.$.role": player["role"]}},
        )

    mongo.db.rooms.update_one({"host_code": int(code)}, {"$set": {"status": "started"}})

    return redirect(url_for("host_bp.host", code=code))


@host_bp.route("/end-game/<code>", methods=["POST"])
def end_game(code: str):
    mongo.db.rooms.delete_many({"host_code": int(code)})
    mongo.db.players.delete_many({"room_code": int(code)})

    return redirect(url_for("home_bp.index"))
