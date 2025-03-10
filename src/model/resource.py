from pydantic import BaseModel
from src.model.citizen import Citizen

class Resource(BaseModel):
    name: str         # Название ресурса
    category : str    # Категория ресурса (дерево, железо, уголь ....)
    date: str         # Дата выработки
    weight: float     # Вес ресурса в килограммах, выработка за день
    color: str        # Цвет ресурса
    grade: str        # Марка ресурса
    citizen: Citizen  # Горожанин, занимающийся выработкой ресурса
