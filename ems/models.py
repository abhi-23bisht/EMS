from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=50,primary_key=True)
    contact = models.CharField(max_length=10)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'