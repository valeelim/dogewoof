# Generated by Django 4.1.2 on 2022-12-11 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0019_remove_product_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]