# Generated by Django 4.2 on 2024-06-26 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeed', '0025_alter_newsarticle_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 26, 15, 56, 53, 936388, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]