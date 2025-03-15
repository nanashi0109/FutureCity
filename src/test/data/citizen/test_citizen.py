import pytest
import asyncio

from src.model.citizen import Citizen
from src.data.citizens import CitizenData


async def add_citizen_in_data():
    citizen1 = Citizen(name="name1", age=41, gender="male", education=None, social_rating="high")
    citizen2 = Citizen(name="name2", age=42, gender="famale", education=None, social_rating="low")
    citizen3 = Citizen(name="name3", age=43, gender="male", education=None, social_rating="medium")
    citizen4 = Citizen(name="name4", age=44, gender="famale", education=None, social_rating="high")
    
    await CitizenData.add(citizen1)
    await CitizenData.add(citizen2)
    await CitizenData.add(citizen3)
    await CitizenData.add(citizen4)

asyncio.run(add_citizen_in_data())


@pytest.mark.parametrize("value, expected_result", [(0, "name1"), (1, "name2"), (2, "name3"), (3, "name4")])
def test_ctitzen_get_one(value, expected_result):
    assert asyncio.run(CitizenData.get_one(value)).name == expected_result  


# @pytest.mark.parametrize("expected_result", [...])
# def test_ctitzen_get_all(expected_result):
#     assert CitizenData.get_all() == expected_result
