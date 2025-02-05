import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_account():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/accounts", json={"holder_name": "Juan Pérez", "balance": 1000.0})
    assert response.status_code == 200
    assert "account_id" in response.json()

@pytest.mark.asyncio
async def test_get_accounts():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/accounts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_update_balance():
    # Primero creamos una cuenta
    async with AsyncClient(app=app, base_url="http://test") as client:
        create_response = await client.post("/accounts", json={"holder_name": "Carlos López", "balance": 500.0})
        account_id = create_response.json()["account_id"]

        # Luego actualizamos el saldo
        update_response = await client.patch(f"/accounts/{account_id}", json={"balance": 200.0})

    assert update_response.status_code == 200
    assert isinstance(update_response.json(), float)  # Debería devolver el saldo actualizado
