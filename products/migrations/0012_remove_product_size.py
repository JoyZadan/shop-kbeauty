# Generated by Django 3.2 on 2022-11-23 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_rename_sale_price_product_original_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
