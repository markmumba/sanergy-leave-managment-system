import datetime
from enum import Enum
from django.db import models
from django.utils import timezone
from sanergy_leave utils import ChoiceEnum
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

    # leave categories and their statuses

class EmpLeaveRequestChoices(ChoiceEnum):
    Personal_Leave = 'Personal'
    Annual_Leave = 'Annual'
    Military_Leave = 'Military'
    Pregnancy_Disability_Leave = 'Expectancy'
    Pending_Status = 'Pending'
    Approved_Status = 'Approved'
    Declined_Status = 'Declined'
    Cancelled_Status = 'Cancelled'

    #worker details and selections

class workerDetails(models.Model):
    First_Name = models.CharField(max_length=14)
    Middle_Name = models.CharField(max_length=14,null=True)
    Last_Name = models.CharField(max_length=14)
    Mobile_Number = models.PositiveIntegerField(default=0)
    Birth_Date = models.DateField()
    Gender = EnumChoiceField(workerChoices)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    Email_Address = models.EmailField(max_length=70)
    Hire_Date = models.DateField()
    Worktype = EnumChoiceField(workerChoices, default = workerChoices.Employee)
    IsActive = models.BooleanField(null=True)

    def __str__(self):
        return '%s %s' % ( self.First_Name, self.Last_Name)












# from enumchoicefield import ChoiceEnum, EnumChoiceField

# class Fruit(ChoiceEnum):
#     apple = "Apple"
#     banana = "Banana"
#     lemon = "Lemon"
#     lime = "Lime"
#     orange = "Orange"

# class Profile(models.Model):
#     name = models.CharField(max_length=100)
#     favourite_fruit = EnumChoiceField(Fruit, default=Fruit.banana)


# apple_lovers = Profile.objects.filter(favourite_fruit=Fruit.apple)
# banana_haters = Profile.objects.exclude(favourite_fruit=Fruit.banana)

# citrus_fans = Profile.objects.filter(
#     favourite_fruit__in=[Fruit.orange, Fruit.lemon, Fruit.lime])
