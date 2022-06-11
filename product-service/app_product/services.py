import typing
from .models import Category, Product


class ProductService:
    model = Product
    related_fields = ("category",)
    related_many_fields = ()

    def get_queryset(self):
        return (
            self.model.objects.select_related(*self.related_fields)
            .prefetch_related(*self.related_many_fields)
            .order_by("id")
        )

    def get_all(self):
        return self.get_queryset().all()

    def get_by_id(self, id: int):
        try:
            return self.get_queryset().get(id=id)
        except self.model.DoesNotExist:
            return None

    def get_by_ids(self, ids: typing.List[int]):
        return self.get_queryset().filter(id__in=ids)

    def get_by_category(self, category_id: str):
        return self.get_queryset().filter(category_id=category_id).all()


class CategoryService:
    model = Category
    related_many_fields = ("products",)

    def get_all(self):
        return self.model.objects.prefetch_related(*self.related_many_fields).all()

    def get_by_id(self, id: int):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return None
