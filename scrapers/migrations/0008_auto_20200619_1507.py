# Generated by Django 3.0.7 on 2020-06-19 15:07

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0007_auto_20200618_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 15, 7, 55, 76814, tzinfo=utc)),
        ),
    ]
