from rest_framework.serializers import ModelSerializer
from .models import Student


class StudentSerializer(ModelSerializer):
    """Student Serializer for the Student Models"""

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("balance",)
