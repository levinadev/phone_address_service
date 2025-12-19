from fastapi import APIRouter, status

from app.api.validators import check_phone_duplicate, check_phone_exists
from app.crud.address import phone_address_crud
from app.schemas.address import (
    AddressUpdate,
    PhoneAddressCreate,
    PhoneAddressResponse,
)

router = APIRouter()


@router.get(
    "/{phone}",
    response_model=PhoneAddressResponse,
    status_code=status.HTTP_200_OK,
)
async def get_address(phone: str):
    await check_phone_exists(phone)
    address = await phone_address_crud.get(phone)
    return PhoneAddressResponse(phone=phone, address=address)


@router.post(
    "/",
    response_model=PhoneAddressResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_address(data: PhoneAddressCreate):
    await check_phone_duplicate(data.phone)
    await phone_address_crud.create(phone=data.phone, address=data.address)
    return PhoneAddressResponse(phone=data.phone, address=data.address)


@router.put(
    "/{phone}",
    response_model=PhoneAddressResponse,
    status_code=status.HTTP_200_OK,
)
async def update_address(phone: str, data: AddressUpdate):
    await check_phone_exists(phone)
    await phone_address_crud.update(phone=phone, address=data.address)
    return PhoneAddressResponse(phone=phone, address=data.address)


@router.delete(
    "/{phone}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_address(phone: str):
    await check_phone_exists(phone)
    await phone_address_crud.delete(phone)
