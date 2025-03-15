import pytest
import time
import subprocess
import requests

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
    response = requests.get("http://127.0.0.1:8000/citizen")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "citizens": []}
    