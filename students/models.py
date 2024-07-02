from django.db import models

# Create your models here.


class Student(models.Model):
    """The student model data"""

    admission_number = models.CharField(
        max_length=7,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
