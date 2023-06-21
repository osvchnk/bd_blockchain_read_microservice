from datetime import datetime
from typing import List

from pydantic import BaseModel


class TransactionSchema(BaseModel):
    hash: str

    class Config:
        orm_mode = True


class BlockOutSchema(BaseModel):
    date: datetime
    prev_hash: str
    hash: str
    admin_sign: str

    transactions: List[TransactionSchema]

    class Config:
        orm_mode = True
