import strawberry
from .services import ProductService

product_service = ProductService()


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

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        # here we could fetch the book from the database
        # or even from an API
        product = product_service.get_by_id(id)
        return ProductType(
            id=id,
            name=product.name,
            description=product.description,
            category=product.category,
        )
