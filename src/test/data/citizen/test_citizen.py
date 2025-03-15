import pytest

from src.model.citizen import Citizen
from src.data.citizens import CitizenData

class TestCitizens:
    pass


def create_citizens():
    citizen1 = Citizen("name1", 41, "male", None, "high")
    citizen2 = Citizen("name2", 42, "female", None, "low")
    citizen3 = Citizen("name3", 43, "male", None, "middle")
    citizen4 = Citizen("name4", 44, "female", None, "high")
    
    CitizenData.add(citizen1)
    CitizenData.add(citizen2)
    CitizenData.add(citizen3)
    CitizenData.add(citizen4)


# @pytest.mark.parametrize("expected_result", [...])
# def test_ctitzen_get_all(expected_result):
#     assert CitizenData.get_all() == expected_result

@pytest.mark.parametrize("value, expected_result", [(1, "name1"), (2, "name2"), (3, "name3"), (4, "name4")])
def test_ctitzen_get_all(value, expected_result):
    assert CitizenData.get_one(value).name == expected_result