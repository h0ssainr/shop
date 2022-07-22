# Generated by Django 4.0.5 on 2022-07-20 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, default='null', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand'),
        ),
    ]