from pydantic import BaseModel


class Ore(BaseModel):
    name: str = 'iron'# Название руды
    date: str # Дата выработки
    weight: float  # Вес в килограммах, выработка за день
    color: str  # Цвет руды
    brand: str  # Марка руды
