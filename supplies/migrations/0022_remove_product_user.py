# Generated by Django 4.1.2 on 2022-12-11 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0021_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]