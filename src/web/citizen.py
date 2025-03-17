from fastapi import APIRouter, Body
from fastapi.exceptions import HTTPException

import asyncio

from src.model.citizen import Citizen
from src.data.citizens import CitizenData


router = APIRouter(prefix="/citizen")


@router.get("/all")
def get_citizens():
    citizens = asyncio.run(CitizenData.get_all())

    return {"status": "ok", "citizens": citizens}


@router.get("/{id}")
def get_one_citizen(id: int):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, "Неверный id")

    citizen = asyncio.run(CitizenData.get_one(id))

    if citizen is None:
        return HTTPException(404, "Горожанин не найден")

    return {"status": "ok", "citizen": citizen}


@router.post("/add")
def add_citizen(citizen: Citizen):
    asyncio.run(CitizenData.add(citizen))

    return {"status": "ok"}


@router.delete("/delete/{id}")
def delete_citizen(id: int):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, "Неверный id")

    asyncio.run(CitizenData.remove(id))

    return {"status": "ok"}


@router.patch("/{id}")
def update_citizen(citizen: Citizen):
    asyncio.run(CitizenData.update(citizen))

    return {"status": "ok"}
