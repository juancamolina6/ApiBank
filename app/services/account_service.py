from datetime import datetime
from app.repositories.account_repository import AccountRepository
from app.models.account_model import AccountCreate, AccountResponse
from fastapi import HTTPException



class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    async def create_account(self, account_data: AccountCreate) -> str:
        # Verificar si el ID ya existe
        existing_account = await self.repository.get_account_by_id(account_data.account_id)
        if existing_account:
            raise HTTPException(status_code=400, detail="El account_id ya existe, debe ser único")
        account_dict = account_data.dict()
        account_dict.update({
            
            "balance": account_dict.pop("balance", 0.0),
            "created_at": datetime.now(),  # Asegurar que se crea este campo
            })
        return await self.repository.create_account(account_dict)

    async def update_balance(self, account_id: str, balance: float) -> float:
        if balance == 0:
            raise HTTPException(status_code=400, detail="El monto no puede ser cero")
        
        result = await self.repository.update_balance(account_id, balance)
        
        if not result:
            raise HTTPException(status_code=404, detail="Cuenta no encontrada")
        
        return result


    async def get_all_accounts(self) -> list[AccountResponse]:
        accounts = await self.repository.get_all_accounts()
        return [AccountResponse(**account) for account in accounts]