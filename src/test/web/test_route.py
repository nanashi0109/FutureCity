import pytest
import time
import subprocess
import requests
from src.model.transport_network.route import Route

# Эта фикстура будет вызвана один раз перед началом выполнения тестов в данном модуле
# И второй раз после выполнения всех тестов (чтоб закрыть сервер)
@pytest.fixture(scope="module", autouse=True)
def setup():
    # Запускаем uvicorn как отдельный процесс (как будто бы через консоль)
    server = subprocess.Popen(
        ["uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", "8000"]
    )

    # Ждём запуск сервера
    for _ in range(50):
        try:
            requests.get("http://127.0.0.1:8000/")
            break
        except requests.ConnectionError:
            time.sleep(0.1)
    else:
        # Падаем с грустинкой если сервер не запустился
        server.terminate()
        raise ConnectionError("Server failed to start 😢 😭 😢 😿 😥 😓 😪 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 😞 😟 😔 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 😾 💢 👿 😈 🤒 🤕")

    # Прерываем работу функции setup (на время выполнения тестов)
    yield None

    # После выполнения тестов setup автоматически вызывается с этой точки 
    # И завершает работу сервера
    server.terminate()


def test_some():
    response = requests.get("http://127.0.0.1:8000/route")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "routes": []}

def test_add_route():
    response = requests.post("http://127.0.0.1:8000/route/add-route", data= Route(id= 1, name='Route 1', count_stops=5, count_transport_on_line=0))
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_update_route():
    response = requests.patch("http://127.0.0.1:8000/route/update-route/{1}", data= Route(id= 1, name='Route 11', count_stops=51, count_transport_on_line=2))
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_delete_route():
    response = requests.delete("http://127.0.0.1:8000/route/delete-route/{1}")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
