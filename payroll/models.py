from django.db import models
from employees.models import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    basic = models.FloatField()
    hra = models.FloatField()
    da = models.FloatField()
    tax = models.FloatField()
    net_salary = models.FloatField()

    def save(self, *args, **kwargs):
        self.tax = 0.1 * (self.basic + self.hra + self.da)
        self.net_salary = (self.basic + self.hra + self.da) - self.tax
        super().save(*args, **kwargs)
