from http import HTTPStatus

from fastapi import HTTPException

from app.crud.address import PhoneAddressCRUD


async def check_phone_exists(phone: str) -> None:
    """
    Проверяет, существует ли телефон в Redis.
    Если не найден — бросает HTTPException 404.
    """
    address = await PhoneAddressCRUD.get(phone)
    if address is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Телефон не найден"
        )


async def check_phone_duplicate(phone: str) -> None:
    """
    Проверяет, что телефон ещё не существует в Redis.
    Если существует — бросает HTTPException 409.
    """
    address = await PhoneAddressCRUD.get(phone)
    if address is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail="Телефон уже существует"
        )
