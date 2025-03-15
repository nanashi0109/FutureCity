import pytest
import asyncio

from fastapi import APIRouter, Body

@pytest.fixture(scope='module', autouse=True)
def setup():
    server = asyncio.create_subprocess_exec('uvicorn', 'main.app', '--host', '127.0.0.1', '--port', '8000')

    asyncio.sleep(2)

    yield None

    server.close()


def test_get_all(setup):
    result = get('/')
    assert result == []