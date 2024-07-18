from flask import render_template, redirect, url_for, request
from flask.blueprints import Blueprint

import icecream

from utils.room_code import generate_room_code


from database import mongo

home_bp = Blueprint("home_bp", __name__, url_prefix="/", template_folder="templates")


@home_bp.route("/")
def index():
    return render_template("index.html")


@home_bp.route("/create_game", methods=["POST"])
def create_game():
    code = generate_room_code()

    mongo.db.rooms.insert_one({"host_code": code, "players": [], "status": "waiting"})
    return redirect(url_for("host_bp.host", code=code))


@home_bp.route("/join_game", methods=["POST"])
def join_game():
    code = request.form["room-code"]
    name = request.form["player-name"]

    room = mongo.db.rooms.find_one({"host_code": int(code)})
    player = mongo.db.players.find_one({"name": name})
    
    if not room:
        return "Room not found", 404

    if not player:
        player_id = mongo.db.players.insert_one(
            {"name": name, "room_code": code, "role": None}
        ).inserted_id

        mongo.db.rooms.update_one(
            {"host_code": int(code)},
            {"$push": {"players": {"player_id": player_id, "name": name, "role": None}}},
        )

    return redirect(url_for("player_bp.player", name=name))
