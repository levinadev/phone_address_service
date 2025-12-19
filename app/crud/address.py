from app.core.redis_client import redis_client
from app.crud.base import BaseRedisCRUD


class PhoneAddressCRUD(BaseRedisCRUD):
    """
    CRUD для связки phone-address
    Интерфейс использует phone и address вместо key/value
    """

    async def get(self, phone: str) -> str | None:
        return await super().get(key=phone)

    async def create(self, phone: str, address: str) -> None:
        await super().create(key=phone, value=address)

    async def update(self, phone: str, address: str) -> None:
        await super().update(key=phone, value=address)

    async def delete(self, phone: str) -> None:
        await super().delete(key=phone)

    async def exists(self, phone: str) -> bool:
        return await super().exists(key=phone)


phone_address_crud = PhoneAddressCRUD(client=redis_client)
