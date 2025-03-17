import pytest
import asyncio

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

@pytest.fixture(scope='session')
def setup():
    schools = Schools

    for school in get_schools():
        asyncio.run(schools.create(school))

    return schools

@pytest.mark.parametrize('value, expected_result', [(1, 'Школа №1'), (2, 'Школа №2'), (3, 'Школа №3')])
def test_schools_get_one(value, expected_result, setup):
    assert asyncio.run(setup.get_one(value)).name == expected_result

@pytest.mark.parametrize('expected_result', [get_schools()])
def test_schools_get_all(expected_result, setup):
    global schools

    result = asyncio.run(setup.get_all())
    for id in range(0, len(result), 1):
        assert result[id].id == expected_result[id].id

@pytest.mark.parametrize('value, expected_result', 
    [
        (School(id=4, name="Школа №4", students=[], teachers=[]), True),
        (School(id=5, name="Школа №5", students=[], teachers=[]), True),
    ],
)
def test_schools_create(value, expected_result, setup):
    result = asyncio.run(setup.create(value))
    assert result == expected_result

    added_school = asyncio.run(setup.get_one(value.id))
    assert added_school.name == value.name

@pytest.mark.parametrize('value, expected_result', 
    [
     (1, True),
     (2, True),
     (10, False)                        
    ])
def test_schools_delete(value, expected_result, setup):
    result = asyncio.run(setup.delete(value))
    assert result == expected_result

@pytest.mark.parametrize(
    'value, expected_result',
    [
        (School(id=1, name="Лицей №1", students=[], teachers=[]), True),
        (School(id=2, name="Гимназия №2", students=[], teachers=[]), True),
        (School(id=10, name="Школа №10", students=[], teachers=[]), False),
    ],
)
def test_schools_update(value, expected_result, setup):
    result = asyncio.run(setup.update(value))
    assert result == expected_result