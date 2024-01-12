from src.models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict) -> None:
        super().__init__(data)  # inicializa o construtor da classe pai
        # com o dict recebido
