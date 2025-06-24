import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
# PORT = os.getenv("db_port")
DBNAME = os.getenv("DBNAME")

# Construct the SQLAlchemy connection string
DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:6543/{DBNAME}?sslmode=require"
)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# if __name__ == "__main__":
#     try:
#         engine.connect()
#         print("✅ Подключение успешно!")
#     except Exception as e:
#         print(f"❌ Не удалось подключиться к БД: {e}")
