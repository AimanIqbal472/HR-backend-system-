from django.db import models
from employees.models import Employee

class Leave(models.Model):
    LEAVE_TYPE = (
        ('SICK', 'Sick'),
        ('CASUAL', 'Casual'),
        ('EARNED', 'Earned'),
    )

    STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
