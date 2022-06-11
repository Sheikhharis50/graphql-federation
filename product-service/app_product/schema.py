import typing
import strawberry

from .types import (
    CategoryType,
    ProductType,
)
from .services import (
    CategoryService,
    ProductService,
)

category_service = CategoryService()
product_service = ProductService()


@strawberry.type
class AppProductQuery:
    @strawberry.field
    def all_categories() -> typing.List[CategoryType]:
        return category_service.get_all()

    @strawberry.field
    def all_products() -> typing.List[ProductType]:
        return product_service.get_all()
