import pytest
import asyncio
import requests
import uvicorn

from src.model.school import School
from src.data.schools import Schools
from src.model.Citizen import Citizen

def get_schools():
    student1 = Citizen(name="Иван Иванов", age="15", gender="Мужской", education="Среднее", social_rating="Высокий")
    student2 = Citizen(name="Мария Петрова", age="14", gender="Женский", education="Среднее", social_rating="Средний")
    student3 = Citizen(name="Алексей Сидоров", age="16", gender="Мужской", education="Среднее", social_rating="Низкий")

    teacher1 = Citizen(name="Ольга Васильева", age="45", gender="Женский", education="Высшее", social_rating="Высокий")
    teacher2 = Citizen(name="Дмитрий Николаев", age="50", gender="Мужской", education="Высшее", social_rating="Средний")

    school1 = School(
        id=1,
        name="Школа №1",
        students=[student1, student2],
        teachers=[teacher1]
    )

    school2 = School(
        id=2,
        name="Школа №2",
        students=[student3],
        teachers=[teacher2]
    )

    school3 = School(
        id=3,
        name="Школа №3",
        students=[],
        teachers=[]
    )

    return (school1, school2, school3)

@pytest.fixture(scope='module', autouse=True)
def setup():
    server = asyncio.create_subprocess_exec(
        'uvicorn', 'main:app', '--host', '127.0.0.1', '--port', '8000'
    )

    asyncio.sleep(1)

    yield

    server.close()

@pytest.fixture(scope='session', autouse=True)
def setup():
    schools = Schools

    for school in get_schools():
        asyncio.run(schools.create(school))

    return schools

@pytest.mark.parametrize('expected_result', [get_schools()])
def test_get_all(expected_result):
    data = requests.get('http://127.0.0.1:8000/schools/all')
    json = data.json()

    for number in range(0, len(expected_result), 1):
        assert expected_result[number].id == json['schools'][number].id