# Generated by Django 4.2 on 2023-05-03 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo_codigo', '0001_initial'),
        ('orden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='promo_codigo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promo_codigo.promocodigo'),
        ),
    ]