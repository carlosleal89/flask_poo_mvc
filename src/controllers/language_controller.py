from flask import Blueprint, request, render_template
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator


language_controller = Blueprint("language_controller", __name__)


@language_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

    else:
        text_to_translate = "O que deseja traduzir?"
        translate_from = "pt"
        translate_to = "en"

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
        ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
