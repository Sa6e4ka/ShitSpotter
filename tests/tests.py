from fastapi.testclient import TestClient
from main import app  # Ваш FastAPI app
import subprocess
from utils import delete_file_from_s3


# Тестирование GET эндпоинтов
def test_get_droppings_for_table():
    client = TestClient(app)
    response = client.get("fetch/droppings")
    assert response.status_code == 200


def test_get_coordinates_for_map():
    client = TestClient(app)
    response = client.get("fetch/mapcords")
    assert response.status_code == 200


# Тестирование POST эндпоинтов
def test_insert_shit():
    client = TestClient(app)
    drop_data = {
        "probability": 0.9,
        "lat": 12.34,
        "lng": 56.78,
    }
    response = client.post("insert/insert_dropping", json=drop_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Record inserted successfully!"}


# Тестирование загрузки фото
def test_upload_photo():
    client = TestClient(app)
    with open("utils\photo of me.jpg", "rb") as file:
        response = client.post(
            "insert/upload_photo", files={"file": ("photo.jpg", file, "image/jpeg")}
        )
    assert response.status_code == 200
    assert "url" in response.json()  # Проверяем наличие url в ответе
    delete_file_from_s3(object_key=response.json()["url"])  # Удаляем файл


def test_requirements_installed():
    """
    Проверяет, что все зависимости из requirements.txt установлены.
    """
    try:
        result = subprocess.run(
            ["pip", "check"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        assert (
            result.returncode == 0
        ), f"pip check failed: {result.stdout + result.stderr}"
    except subprocess.CalledProcessError as e:
        assert False, f"Dependency check failed: {e.stdout + e.stderr}"
