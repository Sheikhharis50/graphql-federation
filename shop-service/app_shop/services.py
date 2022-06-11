from typing import Optional
from django.db import models
from .models import Shop


class ShopService:
    model = Shop
    related_many_fields = ("products",)
    ordering = ("id",)

    def get_all(self, page: int, size: int) -> models.QuerySet[Shop]:
        start = (page - 1) * size
        end = page * size
        return (
            self.model.objects.prefetch_related(*self.related_many_fields)
            .order_by(*self.ordering)
            .all()[start:end]
        )

    def get_by_id(self, id: int) -> Optional[Shop]:
        try:
            return self.model.objects.prefetch_related(*self.related_many_fields).get(
                pk=id
            )
        except self.model.DoesNotExist:
            return None
