import strawberry

from app_product.schema import (
    AppProductQuery,
)


class Query(
    AppProductQuery,
):
    pass


schema = strawberry.federation.Schema(query=Query)
