from pydantic import BaseModel

class Type_Transoprt(BaseModel):
    id: int
    name: str
    status: str | None = None
    