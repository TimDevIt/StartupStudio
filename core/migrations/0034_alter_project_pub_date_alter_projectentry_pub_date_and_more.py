# Generated by Django 4.2 on 2024-06-25 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alter_project_pub_date_alter_projectentry_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 57, 59, 832685, tzinfo=datetime.timezone.utc), verbose_name='Date Time published'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 57, 59, 834680, tzinfo=datetime.timezone.utc), verbose_name='Время, когда заяка была отправлена'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='status_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 57, 59, 834680, tzinfo=datetime.timezone.utc), verbose_name='Время, когда статус заявки был изменен'),
        ),
        migrations.AlterField(
            model_name='projectnotice',
            name='pub_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 57, 59, 835681, tzinfo=datetime.timezone.utc)),
        ),
    ]
