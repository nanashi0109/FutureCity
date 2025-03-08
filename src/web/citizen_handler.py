from fastapi import APIRouter, Body
from src.model.Citizen import Citizen
from src.data.CitizenData import CitizenData


router = APIRouter(prefix="/citizen")


@router.get("/")
def get_citizens():
    citizens = CitizenData.get_all()

    return {"status": "ok", "citizens": citizens}

@router.post("/add-citizen")
def add_citizen(citizen: Citizen):
    CitizenData.add(citizen)

    return {"status": "ok"}

@router.delete("/delete-citizen/{id}")
def delete_citizen(id: int = Body(embed=True)):
    CitizenData.remove(id)

    return {"status": "ok"}

@router.patch("/citizen/{id}")
def update_citizen(citizen: Citizen):
    CitizenData.update(citizen)

    return {"status": "ok"}
