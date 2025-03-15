from pydantic import BaseModel


class Citizen(BaseModel):
    id: int = None
    name: str
    age: int
    gender: str
    education: str | None = None
    social_rating: str

