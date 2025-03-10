from fastapi import APIRouter, Body
from fastapi.exceptions import HTTPException
from src.model.Citizen import Citizen
from src.data.CitizenData import CitizenData


router = APIRouter(prefix="/citizen")


@router.get("/")
def get_citizens():
    citizens = CitizenData.get_all()

    return {"status": "ok", "citizens": citizens}


@router.get("/{id}")
def get_one_citizen(id: int = Body(embed=True)):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, "Неверный id")

    citizen = CitizenData.get_one(id)

    if citizen is None:
        return HTTPException(404, "Горожанин не найден")

    return {"status": "ok", "citizen": citizen}


@router.post("/add")
def add_citizen(citizen: Citizen):
    CitizenData.add(citizen)

    return {"status": "ok"}


@router.delete("/delete/{id}")
def delete_citizen(id: int = Body(embed=True)):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, "Неверный id")

    CitizenData.remove(id)

    return {"status": "ok"}


@router.patch("/{id}")
def update_citizen(citizen: Citizen):
    CitizenData.update(citizen)

    return {"status": "ok"}
