# Generated by Django 4.1.2 on 2022-11-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogitem',
            name='contact',
            field=models.CharField(default='NULL', max_length=32),
        ),
    ]
