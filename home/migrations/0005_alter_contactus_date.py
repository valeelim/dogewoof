# Generated by Django 4.1.2 on 2022-11-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_donation_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateField(default='2022-11-01'),
        ),
    ]