from fastapi import APIRouter, Depends, HTTPException
from app.services.account_service import AccountService
from app.repositories.account_repository import AccountRepository
from app.models.account_model import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter(prefix="/accounts", tags=["accounts"])

def get_service() -> AccountService:
    return AccountService(AccountRepository())

@router.post("/", response_model=str)
async def create_account(
    account_data: AccountCreate,
    service: AccountService = Depends(get_service)
):
    return await service.create_account(account_data)

@router.patch("/{account_id}", response_model=float)
async def update_balance(
    account_id: str,
    update_data: AccountUpdate,
    service: AccountService = Depends(get_service)
):
    try:
        return await service.update_balance(account_id, update_data.amount)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[AccountResponse])
async def list_accounts(service: AccountService = Depends(get_service)):
    return await service.get_all_accounts()