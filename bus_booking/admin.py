from django.contrib import admin
from .models import Student, Ticket, Bus, BusSchedule

admin.site.register(Student)
admin.site.register(Ticket)
admin.site.register(Bus)
admin.site.register(BusSchedule)
