# Generated by Django 3.0.8 on 2020-07-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0010_auto_20200624_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='query',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='search',
            name='user_agent',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='url',
            field=models.URLField(max_length=255, unique=True),
        ),
    ]