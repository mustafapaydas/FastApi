import asyncio

from fastapi import APIRouter

from logic.shop_logic import get_shops, generate_shop, update_shop, delete_shop
from models.model import ShopSchema

shop_router = APIRouter(
    prefix="/shop",
    tags=["shop"],
    responses={404: {"description": "Not found"}},
)

@shop_router.get("/shops")
async def read_items():
    return get_shops()
@shop_router.post("generate/shop")
async def generate_sop(shop:ShopSchema):
    try:
        asyncio.run(generate_shop(shop))
        return "201 Generated"
    except Exception as e:
        return e


@shop_router.put("update/shop")
async def update_shop(shop:ShopSchema):
    asyncio.run(update_shop(shop))
    try:
        asyncio.run(update_shop(shop))
        return "200 Updated"
    except Exception as e:
        return e

@shop_router.delete("/shop/delete/{item_id}")
async def delete_shop(shop_id: int):
    try:
        asyncio.run(delete_shop(shop_id))
        return "200 Deleted"
    except Exception as e:
        return e