from pydantic import BaseModel
from src.model.citizens import Citizen

class Transport(BaseModel):
    id: int
    name: str
    type: str
    status: str | None = None
    driver: Citizen | None = None
    