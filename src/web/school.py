from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.model.school import School as SchoolModel
from src.data.schools import School as SchoolData

import asyncio

router = APIRouter(prefix='/school')

@router.get('/all')
def get_schools():
    schools = asyncio.run(SchoolData.get_all())

    return {'status': 'ok', 'schools': schools}

@router.get('/{id}')
def get_one_school(id: int):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, 'Некорректный id.')
    
    school = asyncio.run(SchoolData.get_one(id))

    if school is None:
        return HTTPException(404, 'Школа не найдена.')
    
    return {'status': 'ok', 'school': school}

@router.post('/add')
def add_school(school: SchoolModel):
    SchoolData.add(school)

    return {'status': 'ok'}

@router.post('/delete/{id}')
def delete_school(id: int):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, 'Некорректный id.')
    
    asyncio.run(SchoolData.remove(id))

    return {'status': 'ok'}

@router.patch('/school/{id}')
def update_school(school: SchoolModel):
    asyncio.run(SchoolData.update(school))

    return {'status': 'ok'}