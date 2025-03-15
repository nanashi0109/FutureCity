import pytest
import asyncio

from src.model.citizens import Citizen
from src.data.citizens import CitizenData


def get_citizens():
    citizen1 = Citizen(id=0, name="name1", age=41, gender="male", social_rating="high")
    citizen2 = Citizen(id=1, name="name2", age=42, gender="famale", social_rating="low")
    citizen3 = Citizen(id=2, name="name3", age=43, gender="male", social_rating="medium")
    citizen4 = Citizen(id=3, name="name4", age=44, gender="famale", social_rating="high")
    
    return (citizen1, citizen2, citizen3, citizen4)

@pytest.fixture()
def setup(scope="session"):
    citizens = CitizenData

    for citizen in get_citizens():
        asyncio.run(citizens.add(citizen))
    
    return citizens


@pytest.mark.parametrize("value, expected_result", [(0, "name1"), (1, "name2"), (2, "name3"), (3, "name4")])
def test_ctitzen_get_one(value, expected_result, setup):
    assert asyncio.run(setup.get_one(value)).name == expected_result  


@pytest.mark.parametrize("expected_result", [get_citizens()])
def test_ctitzen_get_all(expected_result, setup):
    global citizens

    result = asyncio.run(setup.get_all())
    for id in range(0, len(result), 1):
        assert result[id].id == expected_result[id].id 

# @pytest.mark.parametrize("value, expected_result", [(Citizen(id=5, name="name1", age=41, gender="male", social_rating="high"), 5), 
#                                                     (Citizen(id=6, name="name2", age=42, gender="famale", social_rating="low"), 6),
#                                                     (Citizen(id=7, name="name3", age=43, gender="male", social_rating="medium"), 7)])
# def test_citizen_add(value, expected_result):
#     asyncio.run(CitizenData.add(value))
#     assert asyncio.run(CitizenData.get_one(value.id)).id == expected_result.id


# @pytest.mark.parametrize(...)
# def test_citizen_remove():
#     pass

