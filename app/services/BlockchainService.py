from app.repositories.BlockchainRepository import BlockchainRepository
from app.schemas.block import BlockOutSchema


class BlockchainService:

    def __init__(self):
        self.repository: BlockchainRepository = BlockchainRepository()

    async def get_blockchain(self):
        async with self.repository as repo:
            result = await repo.get_blockchain()
        blockchain = []
        for block in result:
            blockchain.append(BlockOutSchema.from_orm(block))
        return blockchain

    async def get_block_by_hash(self, hash) -> BlockOutSchema | None:
        async with self.repository as repo:
            result = await repo.get_block_by_hash(hash)
        if result:
            return BlockOutSchema.from_orm(result)
        return result
