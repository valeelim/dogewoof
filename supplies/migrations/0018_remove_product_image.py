# Generated by Django 4.1.2 on 2022-12-09 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0017_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
