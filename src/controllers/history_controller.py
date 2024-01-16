from flask import Blueprint, jsonify
from models.history_model import HistoryModel
import json

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def get_history():
    history_data = HistoryModel.list_as_json()
    return jsonify(json.loads(history_data)), 200
    # json.loads transforma a string json em um objeto python
