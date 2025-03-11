from pydantic import BaseModel


class Citizen(BaseModel):
    name: str
    age: int
    gender: str
    education: str | None
    social_rating: str

