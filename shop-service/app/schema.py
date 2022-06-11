import typing
import strawberry

from app_shop.types import (
    ShopType,
    ProductType,
)
from app_shop.schema import (
    AppShopQuery,
)


class Query(
    AppShopQuery,
):
    _service: typing.Optional[str]


schema = strawberry.federation.Schema(query=Query, types=[ShopType, ProductType])
