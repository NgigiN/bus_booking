"""Serializers for the models of the bus_application"""
from datetime import timezone
from rest_framework import serializers
from .models import Student, Bus, BusSchedule, Ticket


class StudentSerializer(serializers.ModelSerializer):
    """Student Serializer for the Student Models"""
    class Meta:
        model = Student
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    """Bus Serializer for the Bus Models"""
    class Meta:
        model = Bus
        fields = "__all__"


class BusScheduleSerializer(serializers.ModelSerializer):
    """Bus Scehdule Serializer for the Bus Scehdule Models"""
    class Meta:
        model = BusSchedule
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    """Ticket Serializer for the Ticket Models"""
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ('ticketID',)
