from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class ShopProduct(models.Model):
    id = models.IntegerField(
        primary_key=True,
        blank=False,
        null=False,
    )
    shop = models.ForeignKey(
        verbose_name="Shop",
        to="app_shop.Shop",
        on_delete=models.CASCADE,
        related_name="products",
        db_column="shop_id",
        blank=False,
        null=False,
    )

    def __str__(self):
        return str(self.id)
