# Generated by Django 4.1.2 on 2022-12-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contactus_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateField(default='2022-12-11'),
        ),
    ]
