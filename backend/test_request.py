import requests


def test_get_droppings():
    """
    Тестирует GET-запрос к /droppings
    """
    url = "http://localhost:8000/fetch/droppings"
    response = requests.get(url)
    print("GET /droppings Status Code:", response.status_code)
    print("GET /droppings Response JSON:", response.json())


def test_get_coordinates_for_map():
    """
    Тестирует GET-запрос к /mapcords
    """
    url = "http://localhost:8000/fetch/mapcords"
    response = requests.get(url)
    print("GET /mapcords Status Code:", response.status_code)
    print("GET /mapcords Response JSON:", response.json())


def test_insert_shit():
    """
    Тестирует POST-запрос к /insert_dropping
    """
    url = "http://localhost:8000/insert/insert_dropping"
    data = {
        "probability": 0.9,
        "lat": 12.345,
        "lng": 67.890,
        "timestamp": "2025-04-09T00:00:00",
    }
    response = requests.post(url, json=data)
    print("POST /insert_dropping Status Code:", response.status_code)
    print("POST /insert_dropping Response JSON:", response.json())


def test_upload_photo():
    """
    Тестирует POST-запрос к /upload_photo
    """
    url = "http://localhost:8000/insert/upload_photo"
    file_path = "utils/photo of me.jpg"  # Укажите путь к вашему файлу

    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "image/jpeg")}
        response = requests.post(url, files=files)

    print("POST /upload_photo Status Code:", response.status_code)
    print("POST /upload_photo Response JSON:", response.json()["url"])


if __name__ == "__main__":
    # Вызов всех тестов
    # test_get_droppings()
    # test_get_coordinates_for_map()
    # test_insert_shit()
    test_upload_photo()
