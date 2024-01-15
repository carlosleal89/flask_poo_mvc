from flask import Blueprint, jsonify, request, render_template
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator


language_controller = Blueprint("language_translate", __name__)


@language_controller.route("/", methods=["GET"])
def index():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )


@language_controller.route("/", methods=["POST"])
def translate_text():
    request_data = request.json
    text_to_translate = request_data.get("text_to_translate", "")
    # o segundo parametro é o que retorna caso a chave nao exista
    translate_from = request_data.get("translate_from", "")
    translate_to = request_data.get("translate_to", "")

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
        ).translate(
        text_to_translate
    )

    return jsonify({"translated": translated}), 201
