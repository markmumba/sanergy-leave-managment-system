import datetime

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.html import escape, mark_safe
from PIL import Image


class EmploymentTerm(models.Model):
  EMPLOYMENT_TERMS = (
    ('PERMANENT', 'PERMANENT'),
    ('PARTTIME', 'PARTTIME'),
    ('PROBATIONARY', 'PROBATIONARY'),
    )
  Employment_Terms = models.CharField(max_length=20, choices=EMPLOYMENT_TERMS, default='probationary')
  def __str__(self):
    return self.Employment_Terms

class LeaveType(models.Model):
  LEAVE_CHOICES = (
    ('MATERNITY_LEAVE', 'MATERNITY_LEAVE'),
    ('PATERNITY_LEAVE','PATERNITY_LEAVE'),
    ('ANNUAL_LEAVE','ANNUAL_LEAVE'),
    ('COMPASSIONATE_LEAVE','COMPASSIONATE_LEAVE'),
    ('SICK_LEAVE','SICK_LEAVE'),
    ('STUDY_LEAVE', 'STUDY_LEAVE'),
    )
  Leave_Types = models.CharField(max_length=20, choices=LEAVE_CHOICES, default='ANNUAL_LEAVE')

  def __str__(self):
    return self.Leave_Types


class Department(models.Model):
    department_name = models.CharField(max_length=30, default = 'Service')

    class Meta:
        ordering = ('-id',)
                                       
    def __str__(self):
        return f'{self.department_name} Department'

    @classmethod
    def get_departments(cls):
        all_departments = cls.objects.all()
        return all_departments

class Leave(models.Model):

    Approved = 0
    Pending = 1
    Declined = 2
    Statuses = (
    (Approved,'Approved'),
    (Pending, 'Pending'),
    (Declined, 'Declined'),
    )

    leave_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    Leave_Type = models.ForeignKey(LeaveType,on_delete=models.CASCADE)
    leave_issuer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_issuer', null=True)
    Begin_Date = models.DateField(help_text='Leave begin date')
    End_Date = models.DateField(help_text='Leave end date')
    Requested_Days = models.PositiveIntegerField(default=0,help_text='Total no of requested leave days',blank=True,null=True)
    leave_status= models.IntegerField(choices=Statuses,default=1)
    leave_balance = models.PositiveIntegerField(default=0, blank=True, null=True)
    Comments = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ('-leave_id',)

    def __str__(self):
        return '%s %s' % (self.leave_id, self.leave_issuer)

    @classmethod
    def print_all(cls, pk=id):
        leave = Leave.objects.all()
        return leave

    @classmethod
    def get_single_user_notice(cls,owner):
        user_leaves=cls.objects.filter(user=owner).all()
        return user_leaves

class Notice(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, default="Emergency Notice", null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.topic

    @classmethod
    def get_all_notice(cls):
        all_notices=cls.objects.all()
        return all_notices

    @classmethod
    def get_single_user_notice(cls,owner):
        user_notices=cls.objects.filter(owner=owner).all()
        return user_notices

