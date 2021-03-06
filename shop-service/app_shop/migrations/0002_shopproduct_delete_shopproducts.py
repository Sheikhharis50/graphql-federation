# Generated by Django 4.0.5 on 2022-06-11 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('shop', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app_shop.shop', verbose_name='Shop')),
            ],
        ),
        migrations.DeleteModel(
            name='ShopProducts',
        ),
    ]
