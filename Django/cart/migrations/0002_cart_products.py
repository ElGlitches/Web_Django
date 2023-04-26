# Generated by Django 4.2 on 2023-04-26 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='cart.CartProduct', to='products.product'),
        ),
    ]