# Generated by Django 5.0.6 on 2024-06-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0003_alter_ticket_ticketid'),
    ]

    operations = [
        migrations.AddField(
            model_name='busschedule',
            name='stationed',
            field=models.CharField(default='Waiting', max_length=30),
        ),
    ]
