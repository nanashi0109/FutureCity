from fastapi import APIRouter, Body
from fastapi.exceptions import HTTPException
from src.model.school import School as SchoolModel
from src.data.school import School as SchoolData

router = APIRouter(prefix='/school')

@router.get('/')
def get_schools():
    schools = SchoolData.get_all()

    return {'status': 'ok', 'schools': schools}

@router.get('/{id}')
def get_one_school(id: int = Body(embed=True)):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, 'Некорректный id.')
    
    school = SchoolData.get_one(id)

    if school is None:
        return HTTPException(404, 'Школа не найдена.')
    
    return {'status': 'ok', 'school': school}

@router.post('/add')
def add_school(school: SchoolModel):
    SchoolData.add(school)

    return {'status': 'ok'}

@router.post('/delete/{id}')
def delete_school(id: int = Body(embed=True)):
    try:
        id = int(id)
    except ValueError:
        return HTTPException(400, 'Некорректный id.')
    
    SchoolData.remove(id)

    return {'status': 'ok'}

@router.patch('/school/{id}')
def update_school(school: SchoolModel):
    SchoolData.update(school)

    return {'status': 'ok'}