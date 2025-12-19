from typing import Optional

from app.core.redis_client import redis_client


class PhoneAddressCRUD:
    @staticmethod
    async def get(phone: str) -> Optional[str]:
        return await redis_client.get(phone)

    @staticmethod
    async def create(phone: str, address: str) -> bool:
        exists = await redis_client.exists(phone)
        if exists:
            return False
        await redis_client.set(phone, address)
        return True

    @staticmethod
    async def update(phone: str, address: str) -> bool:
        exists = await redis_client.exists(phone)
        if not exists:
            return False
        await redis_client.set(phone, address)
        return True

    @staticmethod
    async def delete(phone: str) -> bool:
        deleted = await redis_client.delete(phone)
        return bool(deleted)
