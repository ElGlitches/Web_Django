# Generated by Django 4.2 on 2023-04-26 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]