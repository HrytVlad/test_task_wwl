from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    probation = models.BooleanField(default=False)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.first_name} - {self.position}'


class Order(models.Model):
    task_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.task_id}) by {self.employee.user.first_name}'
