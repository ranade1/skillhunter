# Generated by Django 3.0.7 on 2020-06-18 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0002_auto_20200616_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'ordering': ['-created_date'], 'verbose_name_plural': 'Searches'},
        ),
    ]
