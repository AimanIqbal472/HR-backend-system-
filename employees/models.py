from django.db import models
from accounts.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.FloatField()

    resume = models.FileField(upload_to="documents/resume/", null=True)
    id_proof = models.FileField(upload_to="documents/id/", null=True)

    def __str__(self):
        return self.user.username
