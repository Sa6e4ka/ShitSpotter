from sqlalchemy import Column, Integer, Float, DateTime, func
from .database import Base


class Shit(Base):
    __tablename__ = "shit_storage"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    probability = Column(Float, nullable=True)
