# Generated by Django 4.2.7 on 2024-06-17 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 6, 17, 6, 40, tzinfo=datetime.timezone.utc)),
        ),
    ]
