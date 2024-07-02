from django.urls import path

from .views import IsStudentRegisteredApiView

urlpatterns = [
    path(
        "is-registered/<str:admno>/",
        IsStudentRegisteredApiView.as_view(),
    ),
]
