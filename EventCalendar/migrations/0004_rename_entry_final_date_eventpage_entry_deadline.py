# Generated by Django 4.0.1 on 2022-03-07 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0003_eventpage_entry_final_date_eventpage_event_organiser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventpage',
            old_name='entry_final_date',
            new_name='entry_deadline',
        ),
    ]