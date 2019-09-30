import datetime
from enum import Enum
from django.db import models
from django.utils import timezone
from  sanergy_leave.utils import ChoiceEnum
from users.models import *


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

    class Meta:
        Abstract=True

    # leave categories and their statuses

class EmpLeaveRequestChoices(ChoiceEnum):
    Personal_Leave = 'Personal'
    Annual_Leave = 'Annual'
    Military_Leave = 'Military'
    Pregnancy_Disability_Leave = 'Expectant'
    Pending_Status = 'Pending'
    Approved_Status = 'Approved'
    Declined_Status = 'Declined'
    Cancelled_Status = 'Cancelled'

    class Meta:
        Abstract=True



# citrus_fans = Profile.objects.filter(
#     favourite_fruit__in=[Fruit.orange, Fruit.lemon, Fruit.lime])

class Leave(models.Model):
    empLeave_req_id= models.AutoField(primary_key=True)
    emp_id=models.ForeignKey(Profile, on_delete=models.CASCADE,default=0)
    emp_fullname=models.CharField(max_length=60)
    Leave_Type = models.CharField(max_length=300)
    Begin_Date = models.DateField(help_text='Leave begin date')
    End_Date = models.DateField(help_text='Leave end date')
    Requested_Days = models.PositiveIntegerField(default=0,help_text='Total no of requested leave days')
    Comments = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return '%s %s %s' % (self.empLeave_req_id, self.emp_id, self.emp_fullname)



    @classmethod
    def print_all(cls):
        leave = Leave.objects.all()
        return leave