from .models import Category, Product


class ProductService:
    model = Product
    related_fields = ("category",)

    def get_all(self):
        return self.model.objects.select_related(*self.related_fields).all()

    def get_by_id(self, id: int):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return None

    def get_by_category(self, category_id: str):
        return (
            self.model.objects.select_related(*self.related_fields)
            .filter(category_id=category_id)
            .all()
        )


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
