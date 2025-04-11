from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import pytz

JERUSALEM_TZ = pytz.timezone("Asia/Jerusalem")


class DroppingCreate(BaseModel):
    probability: Optional[float] = None
    lat: float
    lng: float
    timestamp: Optional[datetime] = datetime.now(JERUSALEM_TZ)
