
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_contactus_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date',

            field=models.DateField(default='2022-12-04'),

        ),
    ]
