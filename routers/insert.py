from fastapi import APIRouter, HTTPException
from utils import DroppingCreate, upload_file_to_s3
from database_assets import insert_data
from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
from uuid import uuid4
import os

insert_router = APIRouter(prefix="/insert")


@insert_router.post("/insert_dropping")
def insert_shit(drop: DroppingCreate):
    """
    Добавление новой записи от робота или пользователя
    """
    try:
        insert_data(drop.probability, drop.lat, drop.lng, drop.timestamp)
        return {"message": f"Record inserted successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting dropping: {e}")


@insert_router.post("/upload_photo")
def upload_photo(file: UploadFile = File(...)):
    try:

        # Создаем временное имя файла
        temp_filename = f"{uuid4()}.jpg"
        temp_path = (
            f"./tmp/{temp_filename}"  # Используем локальный путь для временного файла
        )

        # Проверим, существует ли директория для сохранения временных файлов
        if not os.path.exists("./tmp"):
            os.mkdir("./tmp")

        # Сохраняем файл временно
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Передаем имя файла (ключ) для загрузки в S3
        upload_file_to_s3(file_path=temp_path, s3_object_name=temp_filename)

        # Логируем успешную загрузку
        print(f"File uploaded to S3: {temp_filename}")

        os.remove(temp_path)
        return {"message": "File uploaded successfully!", "url": temp_filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")
