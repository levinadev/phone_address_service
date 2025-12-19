class BaseRedisCRUD:
    """
    Базовые CRUD-методы для Redis
    """

    def __init__(self, client):
        self.client = client

    async def get(self, key: str) -> str:
        """
        Получение значения по ключу
        """
        return await self.client.get(key)

    async def create(self, key: str, value: str) -> None:
        """
        Создание ключа в Redis
        """
        await self.client.set(key, value)

    async def update(self, key: str, value: str) -> None:
        """
        Обновление значения по ключу
        """
        await self.client.set(key, value)

    async def delete(self, key: str) -> None:
        """
        Удаление ключа
        """
        await self.client.delete(key)

    async def exists(self, key: str) -> bool:
        """
        Проверка существования ключа
        """
        return bool(await self.client.exists(key))
