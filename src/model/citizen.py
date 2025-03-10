from pydantic import BaseModel


class Citizen(BaseModel):
    name: str             # Имя горожанина
    age: str              # Возраст горожанина
    gender: str           # Пол горожанина
    social_rating: str    # Социальный рейтинг