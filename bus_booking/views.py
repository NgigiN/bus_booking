from rest_framework import generics
from .models import Student, Bus, BusSchedule, Ticket
from .serializers import StudentSerializer, BusSerializer, BusScheduleSerializer, TicketSerializer
from django.db import transaction
from django.db.models import F
from rest_framework.exceptions import ValidationError
import random
import string


class StudentView(generics.ListCreateAPIView):
    """This view create students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """This view gets, updates or deletes for Students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class BusView(generics.ListCreateAPIView):
    """This view create Buses"""
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusDetailView(generics.RetrieveUpdateDestroyAPIView):
    """This view gets, updates or deletes for Buses"""
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusScheduleView(generics.ListCreateAPIView):
    """This view create Bus schedules"""
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer


class BusScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """This view gets, updates or deletes for Bus schedules"""
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer


def generate_ticket_id(adm_no):
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    adm_part = adm_no[-2:]
    return f'T{random_part}{adm_part}'


class TicketView(generics.ListCreateAPIView):
    """This view create Tickets"""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        available_buses = Bus.objects.filter(available=True, seats__gt=0).select_for_update()
        if not available_buses.exists():
            raise ValidationError("No available buses with remaining seats")
        bus = available_buses.first()
        adm_no = serializer.validated_data['student']
        ticket_id = generate_ticket_id(adm_no)

        ticket = serializer.save(ticketID=ticket_id, bus=bus)

        bus.seats -= 1
        if bus.seats == 0:
            bus.available = False
        bus.save()
        return ticket


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """This view gets, updates or deletes for Tickets"""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
