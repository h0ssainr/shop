# Generated by Django 4.0.5 on 2022-07-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
