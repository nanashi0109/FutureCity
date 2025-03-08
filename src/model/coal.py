from pydantic import BaseModel


class Coal(BaseModel):

    weight: float  # Вес в килограммах
    color: str  # Цвет руды
    brand: str  # Марка руды
    structure: bool  # Структура: однородна / не однородна
    shine: bool  # Блеск: да / нет
