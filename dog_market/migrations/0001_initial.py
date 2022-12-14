# Generated by Django 4.1.2 on 2022-11-02 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DogItem',
            fields=[
                ('item_title', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('breed', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
