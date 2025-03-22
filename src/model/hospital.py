from src.model.Citizen import Citizen
from pydantic import BaseModel

class Hospital(BaseModel):
    id: int
    name: str
    patients: list[Citizen]


