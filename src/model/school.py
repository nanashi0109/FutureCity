from pydantic import BaseModel

from citizen import Citizen

class School(BaseModel):
    id: int
    name: str
    students: list[Citizen]
    teachers: list[Citizen]