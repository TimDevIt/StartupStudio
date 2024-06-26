# Generated by Django 4.0.1 on 2022-05-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectentry',
            name='status',
            field=models.CharField(blank=True, choices=[('pen', 'Pending'), ('acc', 'Accepted'), ('den', 'Denied')], default='p', help_text='Current entry status', max_length=3),
        ),
        migrations.AlterField(
            model_name='teamentry',
            name='status',
            field=models.CharField(blank=True, choices=[('pen', 'Pending'), ('acc', 'Accepted'), ('den', 'Denied')], default='p', help_text='Current entry status', max_length=3),
        ),
    ]
