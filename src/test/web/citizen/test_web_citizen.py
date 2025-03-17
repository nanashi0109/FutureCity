import pytest
import asyncio
import requests
import uvicorn

from src.model.citizen import Citizen
from src.data.citizens import CitizenData


def get_citizens():
    citizen1 = Citizen(id=0, name="name1", age=41, gender="male", social_rating="high")
    citizen2 = Citizen(id=1, name="name2", age=42, gender="famale", social_rating="low")
    citizen3 = Citizen(id=2, name="name3", age=43, gender="male", social_rating="medium")
    citizen4 = Citizen(id=3, name="name4", age=44, gender="famale", social_rating="high")
    
    return (citizen1, citizen2, citizen3, citizen4)


@pytest.fixture(scope="module", autouse=True)
def setup():
    server = asyncio.create_subprocess_exec(
        "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"
    )

    asyncio.sleep(1)

    yield

    server.close()


@pytest.fixture(scope="session", autouse=True)
def setup_citizens():
    citizens = CitizenData

    for citizen in get_citizens():
        asyncio.run(citizens.add(citizen))
    
    return citizens


@pytest.mark.parametrize("expected_result", [get_citizens])
def test_get_all(expected_result):
    data = requests.get("http://127.0.0.1:8000/citizen/all")
    json = data.json()

    for number in range(0, len(expected_result), 1):
        assert expected_result[number].id == json["citizens"][number].id 

