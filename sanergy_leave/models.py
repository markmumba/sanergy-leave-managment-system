import datetime
from django.db import models
from django.utils import timezone
from enumchoicefield import ChoiceEnum, EnumChoiceField

# Create your models here.

class workerChoices(ChoiceEnum):
    Male = 'M'
    Female = 'F'
    # worker level
    Employee = 'Employee'
    Manager = 'Manager'
    HR = 'HR'
    # employment status
    Permanent = 'Permanent'
    Probationary = 'Probationary'
    Limited_term = 'Limited-term'
    Temporary = 'Temporary'

class workerDetails(models.Model):
    First_Name = models.CharField(max_length=14)
    Middle_Name = models.CharField(max_length=14,null=True)
    Last_Name = models.CharField(max_length=14)
    Mobile_Number = models.PositiveIntegerField(default=0)
    Birth_Date = models.DateField()
    Gender = models.CharField(max_length=1, choices=workerDetails.choices())
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    Email_Address = models.EmailField(max_length=70)
    Hire_Date = models.DateField()
    Nationality = models.CharField(max_length=50)
    Worktype = models.CharField(max_length=15, choices=workerDetails.choices())
    IsActive = models.BooleanField(null=True)

    def __str__(self):
        return '%s %s' % ( self.First_Name, self.Last_Name)