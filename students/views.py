import os
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.mixins import Response
from .serializers import StudentSerializer
import requests as http

from .models import Student


class IsStudentRegisteredApiView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        """Checks if the user is regisred if not register them"""
        admno: str = kwargs["admno"]

        querset = Student.objects.filter(admission_number=admno)

        if querset:
            return Response(
                {"registered": True},
                status=HTTP_200_OK,
            )

        # Ask for data from verisafe
        result = http.get(f"{os.getenv("VERISAFE_BASE")}/students/find/admno/{admno}")

        if result.status_code == HTTP_200_OK:
            serializer = StudentSerializer(data=result.json())

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"registered": True},
                    status=HTTP_200_OK,
                )
            else:
                raise Exception("Invalid data from verisafe")
                # return Response(
                #     {"registered": False},
                #     status=HTTP_500_INTERNAL_SERVER_ERROR,
                # )
        else:
            return Response(
                {
                    "registered": False,
                    "error": "I sense something sinister ~ Count Douku",
                },
                status=HTTP_400_BAD_REQUEST,
            )
