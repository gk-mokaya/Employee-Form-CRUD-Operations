from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    employee_name = models.CharField(max_length=30)
    employee_email = models.EmailField(unique=True)
    employee_contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.employee_name