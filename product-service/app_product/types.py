import strawberry

# from strawberry.dataloader import DataLoader
# from typing import Any, List
from .services import ProductService

product_service = ProductService()


# async def load_products(keys: List[int]) -> List[Any]:
#     return product_service.get_by_ids(keys)


# loader = DataLoader(load_fn=load_products)


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
    # async def resolve_reference(cls, id: strawberry.ID):
    def resolve_reference(cls, id: strawberry.ID):
        """
        FIXME: we need to resolve N+1 problem here
        """
        product = product_service.get_by_id(id=id)
        # product = await loader.load(id)
        return ProductType(
            id=id,
            name=product.name,
            description=product.description,
            category=product.category,
        )
