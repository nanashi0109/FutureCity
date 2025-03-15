from fastapi import APIRouter, Body
from src.model.hospital import Hospital
from src.data.hospital import Hospitals

router = APIRouter(prefix = '/hospital')

@router.get('/')
def get_hospitals():
    hospitals = Hospitals.get_all()

    return {'status': 'ok','hospitals': hospitals}

@router.post('/add')
def add_hospital(hospital : Hospital):
    Hospitals.update(hospital)

    return {'status': 'ok'}

@router.delete('/delete/{id}')
def delete_hospital(id: int):
    Hospitals.delete(id)

    return {'status': 'ok'}

@router.patch('/hospital/{id}')
def update_hospital(hospital: Hospital):
    Hospitals.update(hospital)

    return {'status': 'ok'}



