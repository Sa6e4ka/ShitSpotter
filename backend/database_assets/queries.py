from .model import Shit
from .database import sessionlocal
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import select
from datetime import datetime
import pytz

JERUSALEM_TZ = pytz.timezone("Asia/Jerusalem")


def fetch_all_shit_entries() -> list[dict]:
    """
    Универсальный запрос всех данных для последующей фильтрации на уровне API.
    """
    session = sessionlocal()
    data = []
    try:
        query = select(Shit.id, Shit.lat, Shit.lng, Shit.timestamp)
        result = session.execute(query)

        for row in result:
            timestamp_utc = row.timestamp.replace(tzinfo=pytz.utc)
            timestamp_jerusalem = timestamp_utc.astimezone(JERUSALEM_TZ)

            data.append(
                {
                    "id": row.id,
                    "lat": row.lat,
                    "lng": row.lng,
                    "timestamp": timestamp_jerusalem.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
    except Exception as e:
        print(f"❌ Ошибка при запросе: {e}")
    finally:
        session.close()
    return data


def insert_data(probability, lat, lng, timestamp=None):
    # Открытие сессии
    session = sessionlocal()

    try:
        # Если timestamp не передан, используем текущее время (будет в UTC по умолчанию)
        if timestamp is None:
            timestamp = datetime.now(JERUSALEM_TZ)
            print(timestamp)

        # Создание новой записи для вставки
        new_dropping = Shit(
            lat=lat, lng=lng, timestamp=timestamp, probability=probability
        )

        # Добавление записи в сессию
        session.add(new_dropping)

        # Подтверждение изменений в базе данных
        session.commit()

        print(f"Record with ID {new_dropping.id} inserted successfully!")

    except SQLAlchemyError as e:
        # Обработка ошибок
        print(f"Error occurred: {e}")
        session.rollback()  # Откатить транзакцию при ошибке

    finally:
        session.close()  # Закрыть сессию


if __name__ == "__main__":

    coordinates = [
        [31.511505, 34.446485],
        [31.511475, 34.446452],
        [31.511520, 34.446395],
        [31.511490, 34.446370],
        [31.511525, 34.446440],
        [31.511510, 34.446330],
        [31.511495, 34.446480],
        [31.511470, 34.446410],
        [31.511530, 34.446460],
        [31.511485, 34.446350],
        [31.511515, 34.446370],
        [31.511460, 34.446390],
        [31.511540, 34.446415],
        [31.511475, 34.446435],
        [31.511490, 34.446395],
        [31.511505, 34.446365],
        [31.511520, 34.446425],
        [31.511480, 34.446420],
        [31.511495, 34.446440],
    ]
    for i in coordinates:
        insert_data(probability=0.999, lat=i[0], lng=i[1])
    # fetch_all_shit_entries()
