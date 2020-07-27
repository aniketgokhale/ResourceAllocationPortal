from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=250)
    department = models.CharField(max_length=50)
    year = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    registrationId = models.CharField(max_length=50)
    rollNo = models.CharField(max_length=100)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.registrationId
