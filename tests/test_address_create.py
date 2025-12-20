from unittest.mock import AsyncMock, patch


def test_create_address_success(client):
    payload = {
        "phone": "+7-999-123-45-67",
        "address": "г. Москва, ул. Пушкина, д. 10, кв. 5",
    }

    with patch(
        "app.api.validators.check_phone_duplicate",
        new=AsyncMock(),
    ), patch(
        "app.crud.address.phone_address_crud.create",
        new=AsyncMock(),
    ):
        response = client.post("/phone-address/", json=payload)

    assert response.status_code == 201
    assert response.json() == payload
