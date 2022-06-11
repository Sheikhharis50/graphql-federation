import typing
import strawberry


@strawberry.type
class ShopType:
    id: strawberry.ID
    name: str
    description: str
    products: typing.List["ProductType"]


@strawberry.federation.type(extend=True, keys=["id"])
class ProductType:
    id: strawberry.ID = strawberry.federation.field(external=True)
