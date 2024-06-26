# Generated by Django 4.2 on 2024-06-25 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_rename_name_skill_skill_name_alter_project_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 53, 18, 738494, tzinfo=datetime.timezone.utc), verbose_name='Date Time published'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 53, 18, 739493, tzinfo=datetime.timezone.utc), verbose_name='Время, когда заяка была отправлена'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='status_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 53, 18, 739493, tzinfo=datetime.timezone.utc), verbose_name='Время, когда статус заявки был изменен'),
        ),
        migrations.AlterField(
            model_name='projectnotice',
            name='pub_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 12, 53, 18, 741067, tzinfo=datetime.timezone.utc)),
        ),
    ]
