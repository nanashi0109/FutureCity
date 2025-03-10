from fastapi import APIRouter, Body
from src.model.transport_network.transports import Transport
from src.data.transports import Transports


router = APIRouter(prefix="/transport")


@router.get("/")
def get_transports():
    transports = Transports.get_all_transports()

    return {"status": "ok", "transports": transports}

@router.post("/add-transport")
def add_transport(transport: Transport):
    Transports.create_transport(transport)

    return {"status": "ok"}

@router.delete("/delete-transport/{id}")
def delete_transport(id: int = Body(embed=True)):
    Transports.delete_transport(id)

    return {"status": "ok"}

@router.patch("/transport/{id}")
def update_transport(transport: Transport):
    Transports.update(transport)

    return {"status": "ok"}