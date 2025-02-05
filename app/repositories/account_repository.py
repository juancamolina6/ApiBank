from app.db.mongodb import accounts_collection
from typing import Optional

class AccountRepository:
    async def create_account(self, account_data: dict) -> str:
        result = await accounts_collection.insert_one(account_data)
        # Se podría retornar el account_id ya que lo generamos en el servicio
        return account_data["account_id"]

    async def update_balance(self, account_id: str, amount: float) -> Optional[float]:
        # Ahora buscamos por "account_id" en lugar de usar ObjectId
        updated_account = await accounts_collection.find_one_and_update(
            {"account_id": account_id},
            {"$inc": {"balance": amount}},
            return_document=True
        )
        return updated_account["balance"] if updated_account else None

    async def get_all_accounts(self) -> list:
        accounts = []
        async for account in accounts_collection.find():
            # Si no existe account_id, lo asignamos usando el _id convertido a string
            if "account_id" not in account:
                account["account_id"] = str(account["_id"])
            # Opcionalmente, eliminar _id si no es necesario en la respuesta
            account.pop("_id", None)
            accounts.append(account)
        return accounts
        
    async def get_account_by_id(self, account_id: str):
        return await accounts_collection.find_one({"account_id": account_id})



