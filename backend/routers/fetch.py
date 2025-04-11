from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict
from database_assets import fetch_all_shit_entries

fetch_router = APIRouter(prefix="/fetch", tags=["Fetching"])

# ------------------------------
# Response Models
# ------------------------------


class DroppingTableEntry(BaseModel):
    id: int
    coordinates: List[float]  # [latitude, longitude]
    timestamp: str


# ------------------------------
# Endpoints
# ------------------------------


@fetch_router.get(
    "/droppings",
    response_model=List[DroppingTableEntry],
    summary="Get all droppings for table view",
    description="Returns a list of all droppings including ID, coordinates, and timestamp for displaying in a table.",
)
def get_droppings_for_table():
    """
    Returns all detected droppings formatted for table view.
    """
    raw_data = fetch_all_shit_entries()
    data = [
        {
            "id": row["id"],
            "coordinates": [row["lat"], row["lng"]],
            "timestamp": row["timestamp"],
        }
        for row in raw_data
    ]
    return JSONResponse(content=data)


@fetch_router.get(
    "/mapcords",
    summary="Get coordinates for map view",
    description="Returns a dictionary of coordinates indexed by ID, suitable for rendering points on a map.",
)
def get_coordinates_for_map():
    """
    Returns coordinates of droppings for heatmap display.
    """
    raw_data = fetch_all_shit_entries()
    data = {row["id"]: [row["lat"], row["lng"]] for row in raw_data}
    return JSONResponse(content=data)
