from pydantic import BaseModel

class Transport(BaseModel):
    id: int
    name: str
    type: str
    status: str | None = None
    # driver: Citizen | None = None
    