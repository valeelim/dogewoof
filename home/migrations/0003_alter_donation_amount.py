# Generated by Django 4.1.2 on 2022-10-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.PositiveBigIntegerField(),
        ),
    ]
