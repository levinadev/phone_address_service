from typing import Annotated

from pydantic import BaseModel, Field, constr

DESC_PHONE = "Номер телефона клиента"
EXAMPLE_PHONE = "+7-999-123-45-67"

DESC_ADDRESS = "Адрес клиента"
EXAMPLE_ADDRESS = "г. Москва, ул. Пушкина, д. 10, кв. 5"

PhoneStr = Annotated[
    str,
    Field(
        pattern=r"^\+7-\d{3}-\d{3}-\d{2}-\d{2}$",
        description=DESC_PHONE,
        examples=[EXAMPLE_PHONE],
    ),
]

AddressStr = Annotated[
    str,
    Field(
        min_length=1,
        max_length=255,
        description="Адрес клиента",
        examples=["г. Москва, ул. Пушкина, д. 10, кв. 5"],
    ),
]


class PhoneAddressBase(BaseModel):
    """
    Базовая схема с общими полями
    """

    phone: PhoneStr
    address: AddressStr


class PhoneAddressCreate(PhoneAddressBase):
    """
    Схема создания
    """


class AddressUpdate(BaseModel):
    """
    Схема обновления
    """

    address: AddressStr


class PhoneAddressResponse(PhoneAddressBase):
    """
    Схема ответа
    """
