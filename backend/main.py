from fastapi import FastAPI
from routers import insert_router, fetch_router
from fastapi.middleware.cors import CORSMiddleware

# Инициализация FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(insert_router)
app.include_router(fetch_router)
