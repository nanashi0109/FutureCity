from pydantic import BaseModel

class Route(BaseModel):
    id: int
    name: str | None = None
    count_stops: int
    