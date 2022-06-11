import typing
import strawberry

from .types import (
    ShopType,
)
from .services import (
    ShopService,
)

shop_service = ShopService()


@strawberry.type
class AppShopQuery:
    @strawberry.field
    def all_shops(page: int = 1, size: int = 10) -> typing.List[ShopType]:
        return [
            ShopType(
                id=shop.id,
                name=shop.name,
                description=shop.description,
                products=shop.products.all(),
            )
            for shop in shop_service.get_all(page, size)
        ]

    @strawberry.field
    def shop_by_id(id: int) -> ShopType:
        shop = shop_service.get_by_id(id=id)
        return ShopType(
            id=shop.id,
            name=shop.name,
            description=shop.description,
            products=shop.products.all(),
        )
