# Generated by Django 4.2 on 2024-05-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProfile', '0002_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status_id',
            field=models.CharField(choices=[('student', 'Студент'), ('teacher', 'Преподаватель'), ('company', 'Компания')], help_text='Введите статус', max_length=30, verbose_name='Status Name'),
        ),
    ]
