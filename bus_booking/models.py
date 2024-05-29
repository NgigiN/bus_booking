"""Basic models for the bus application"""
from django.db import models, transaction
from django.utils import timezone
from django.core.exceptions import ValidationError


class Student(models.Model):
    """Model for student data if required"""
    adm_no = models.CharField(max_length=7, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Bus(models.Model):
    """Model for every bus in school"""
    number_plate = models.CharField(max_length=8, primary_key=True)
    seats = models.IntegerField(default=0)
    available = models.BooleanField(default=False)


class BusSchedule(models.Model):
    """Model for the Bus schedule"""
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)


class Ticket(models.Model):
    """Model for Tickets"""

    ticketID = models.CharField(max_length=10, null=True, blank=True)
    student = models.CharField(max_length=8)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    depature = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        """Ticket validating function"""
        if self.bus.seats <= 0:
            raise ValidationError("No available seats on the bus.")
        with transaction.atomic():
            bus = Bus.objects.select_for_update().get(pk=self.bus.pk)
            if bus.seats <= 0:
                raise ValidationError("No available seats on the bus.")
            bus.seats -= 1
            if bus.seats == 0:
                bus.available = False
            bus.save()
        super().save(*args, **kwargs)
