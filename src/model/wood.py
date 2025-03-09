from pydantic import BaseModel


class Wood(BaseModel):
    name: str # Название древесины
    date: str # Дата выработки
    weight: float  # Вес древесины на м3 в килограммах, выработка за день
    color: str  # Цвет древесины
    brand: str  # Марка древесины
