# Generated by Django 4.2 on 2024-04-18 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeed', '0014_alter_newsarticle_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 18, 11, 9, 54, 216224, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]