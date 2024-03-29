from flask import Blueprint, request, render_template
from models.language_model import LanguageModel
from models.history_model import HistoryModel
from deep_translator import GoogleTranslator


language_controller = Blueprint("language_controller", __name__)


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
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    # o segundo parametro é o que retorna caso a chave nao exista
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    HistoryModel(
        {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to
        }
    ).save()

    translated = GoogleTranslator(
        source=translate_from, target=translate_to,
        ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/reverse", methods=["POST"])
def reverse_text_translate():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    reverse_translated = GoogleTranslator(
        source=translate_from, target=translate_to,
        ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=reverse_translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
