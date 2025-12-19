from fastapi import APIRouter, status

from app.api.validators import check_phone_duplicate, check_phone_exists
from app.crud.address import PhoneAddressCRUD
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
    address = await PhoneAddressCRUD.get(phone)
    return {"phone": phone, "address": address}


@router.post(
    "/",
    response_model=PhoneAddressResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_address(data: PhoneAddressCreate):
    await check_phone_duplicate(data.phone)
    await PhoneAddressCRUD.create(phone=data.phone, address=data.address)
    return {"phone": data.phone, "address": data.address}


@router.put(
    "/{phone}",
    response_model=PhoneAddressResponse,
    status_code=status.HTTP_200_OK,
)
async def update_address(phone: str, data: AddressUpdate):
    await check_phone_exists(phone)
    await PhoneAddressCRUD.update(phone=phone, address=data.address)
    return {"phone": phone, "address": data.address}


@router.delete(
    "/{phone}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_address(phone: str):
    await check_phone_exists(phone)
    await PhoneAddressCRUD.delete(phone)
