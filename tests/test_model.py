# import pytest
from src.detect import run_detection  # импорт функции инференса


def test_yolo_inference():
    img_path = "tests/sample.jpg"  # тестовое изображение
    result = run_detection(img_path)
    assert result is not None, "Модель не вернула результат"
