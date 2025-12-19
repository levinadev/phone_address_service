from fastapi import APIRouter

from app.api.endpoints import address_router

main_router = APIRouter()

main_router.include_router(
    address_router,
    prefix="/phone-address",
    tags=["Телефон-адрес"],
)
