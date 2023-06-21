from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db import async_session
from app.models.block import Block


class BlockchainRepository:

    def __init__(self):
        self.session: AsyncSession = async_session()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session is not None:
            try:
                await self.session.close()
            except Exception as e:
                raise e

    async def get_block_by_id(self, block_id: int):
        pass

    async def get_block_by_hash(self, block_hash: str) -> Block | None:
        query = (
            select(Block).
            where(Block.hash == block_hash).
            options(selectinload(Block.transactions))
        )
        result = await self.session.execute(query)
        block = result.scalars().one_or_none()
        return block

    async def get_blockchain(self) -> List[Block]:
        query = (
            select(Block).
            options(selectinload(Block.transactions)).
            order_by(Block.id.desc())
        )
        result = await self.session.execute(query)
        blockchain = result.scalars().all()
        return blockchain
