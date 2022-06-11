import strawberry


@strawberry.type
class CategoryType:
    id: strawberry.ID
    name: str


@strawberry.federation.type(keys=["id"])
class ProductType:
    id: strawberry.ID
    name: str
    description: str
    category: CategoryType
