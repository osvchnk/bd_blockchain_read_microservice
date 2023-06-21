from fastapi import APIRouter

from app.services.BlockchainService import BlockchainService


router = APIRouter(
    prefix="/block",
    tags=["block"]
)


@router.get("")
async def get_blockchain():
    return await BlockchainService().get_blockchain()


@router.get("/{block_hash}")
async def get_block_by_hash(block_hash: str):
    return await BlockchainService().get_block_by_hash(block_hash)
