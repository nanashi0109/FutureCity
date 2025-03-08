from pydantic import BaseModel


class Iron(BaseModel):

    name: str  # Название руды
    weight: float  # Вес в килограммах
    color: str  # Цвет руды
    brand: str  # Марка руды
