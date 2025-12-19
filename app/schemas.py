from pydantic import BaseModel, Field

DESC_PHONE = "Номер телефона клиента"
EXAMPLE_PHONE = "+7-999-123-45-67"

DESC_ADDRESS = "Адрес клиента"
EXAMPLE_ADDRESS = "г. Москва, ул. Пушкина, д. 10, кв. 5"


class PhoneAddressBase(BaseModel):
    """
    Базовая схема с общими полями
    """

    phone: str = Field(
        json_schema_extra={
            "description": DESC_PHONE,
            "example": EXAMPLE_PHONE,
        },
    )
    address: str = Field(
        json_schema_extra={
            "description": DESC_ADDRESS,
            "example": EXAMPLE_ADDRESS,
        },
    )


class PhoneAddressCreate(PhoneAddressBase):
    """
    Схема создания
    """


class AddressUpdate(BaseModel):
    """
    Схема обновления
    """

    address: str = Field(
        ...,
        json_schema_extra={
            "description": DESC_ADDRESS,
            "example": EXAMPLE_ADDRESS,
        },
    )


class PhoneAddressResponse(PhoneAddressBase):
    """
    Схема ответа
    """
