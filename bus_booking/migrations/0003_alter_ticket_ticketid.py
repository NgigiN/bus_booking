# Generated by Django 5.0.6 on 2024-05-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0002_alter_ticket_ticketid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticketID',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]