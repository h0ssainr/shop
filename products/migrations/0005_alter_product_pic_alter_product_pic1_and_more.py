# Generated by Django 4.0.5 on 2022-07-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_pic_alter_product_pic1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(blank=True, default='None', null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default='None', null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default='None', null=True, upload_to='image'),
        ),
    ]
