# Generated by Django 4.1.2 on 2022-12-11 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_contactus_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
