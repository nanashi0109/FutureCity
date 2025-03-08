from pydantic import BaseModel


class Cityzen(BaseModel):
    name: str
    age: str
    social_rating: str
