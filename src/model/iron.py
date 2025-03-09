from pydantic import BaseModel


class Iron(BaseModel):
    name: str # Название руды
    date: str # Дата выработки
    weight: float  # Вес в килограммах, выработка за день
    color: str  # Цвет руды
    brand: str  # Марка руды
