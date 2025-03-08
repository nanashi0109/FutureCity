from pydantic import BaseModel


class Wood(BaseModel):

    weight: float  # Вес древесины на м3
    color: str  # Цвет древесины
    bark: bool  # Наличие коры
    density: float  # Плотность древесины
    humidity: int  # Влажность - содержание влаги в дереве
    thermal: float  # Теплопроводность
