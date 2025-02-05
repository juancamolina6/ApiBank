import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from bson import ObjectId
from pydantic.config import ConfigDict


class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)


from pydantic import BaseModel, Field

class AccountCreate(BaseModel):
    account_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Identificador único de la cuenta")
    holder_name: str = Field(..., min_length=3, max_length=100, description="Nombre del titular de la cuenta")
    balance: float = Field(0.0, ge=0.0, description="Saldo inicial, no puede ser negativo")

class AccountUpdate(BaseModel):
    balance: float = Field(..., description="Cantidad a agregar o restar", gt=-1000000, lt=1000000)  # Limitar rango


class AccountResponse(BaseModel):
    account_id: str
    holder_name: str
    balance: float
    created_at: datetime

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )