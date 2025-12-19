from fastapi import FastAPI

from app.api.routers import main_router

app = FastAPI(
    title="Телефон-адрес Сервис",
    description="Микросервис для хранения и управления связками телефон-адрес.",
    version="1.0.0",
)

app.include_router(main_router)
