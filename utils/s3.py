import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os
from dotenv import load_dotenv

load_dotenv()


# Настроим клиент S3
def create_s3_client():
    try:
        s3_client = boto3.client("s3")
        return s3_client
    except (NoCredentialsError, PartialCredentialsError):
        print("Ошибка: Пожалуйста, настройте свои AWS креды.")
        return None


# Функция для загрузки файла
def upload_file_to_s3(file_path: str, s3_object_name: str):
    s3_client = create_s3_client()
    if s3_client:
        try:
            # Загружаем файл
            with open(file_path, "rb") as file_data:
                s3_client.upload_fileobj(
                    file_data, os.environ.get("S3_BUCKET_NAME"), s3_object_name
                )
            print(
                f"Файл {file_path} успешно загружен в {os.environ.get("S3_BUCKET_NAME")}/{s3_object_name}"
            )
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}")
    else:
        print("Не удалось создать клиента S3.")


# Функция для получения списка объектов в бакете
def list_files_in_bucket():
    s3_client = create_s3_client()
    if s3_client:
        try:
            response = s3_client.list_objects_v2(
                Bucket=os.environ.get("S3_BUCKET_NAME")
            )
            if "Contents" in response:
                for obj in response["Contents"]:
                    print(f"Файл: {obj['Key']}")
            else:
                print(f"В бакете {os.environ.get("S3_BUCKET_NAME")} нет файлов.")
        except Exception as e:
            print(f"Ошибка при получении списка файлов: {e}")
    else:
        print("Не удалось создать клиента S3.")


def delete_file_from_s3(object_key: str) -> bool:
    """
    Удаляет файл из указанного S3-бакета.

    :param bucket_name: Название бакета
    :param object_key: Путь к файлу внутри бакета (ключ)
    :return: True, если файл успешно удалён, иначе False
    """
    s3_cliest = create_s3_client()
    if s3_cliest:
        try:
            s3_cliest.delete_object(
                Bucket=os.environ.get("S3_BUCKET_NAME"), Key=object_key
            )
            print(
                f"Deleted {object_key} from bucket {os.environ.get("S3_BUCKET_NAME")}"
            )
            return True
        except Exception as e:
            print(f"Error deleting object: {e}")
            return False
    else:
        print("Не удалось создать S3 клиент")


# Пример использования
# if __name__ == "__main__":
#     upload_file_to_s3("utils/photo of me.jpg", "photo.jpg")
# list_files_in_bucket("your-bucket-name")
