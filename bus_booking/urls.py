from django.urls import path
from .views import StudentView, StudentDetailView, BusView, BusDetailView, BusScheduleView, BusScheduleDetailView, TicketView, TicketDetailView

urlpatterns = [
    path("student/", StudentView.as_view(), name="student_list"),
    path("student/<pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("bus/", BusView.as_view(), name="bus_list"),
    path("bus/<pk>/", BusDetailView.as_view(), name="bus_detail"),
    path("bus_schedule/", BusScheduleView.as_view(), name="bus_schedule_list"),
    path("bus_schedule/<pk>/", BusScheduleDetailView.as_view(), name="bus_schedule_detail"),
    path("ticket/", TicketView.as_view(), name="ticket_list"),
    path("ticket/<pk>/", TicketDetailView.as_view(), name="ticket_detail"),
]
