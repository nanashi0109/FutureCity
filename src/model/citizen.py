from pydantic import BaseModel


class Citizen(BaseModel):
    name: str
    age: str
    gender: str
    social_rating: str