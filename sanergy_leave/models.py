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

class Role(models.Model):

  MANAGER = 'MANAGER'
  EMPLOYEE = 'EMPLOYEE'

  ROLES = (
    (EMPLOYEE, '0. EMPLOYEE'),
    (MANAGER, '1. MANAGER'),
    )

  role = models.CharField(max_length=30,choices=ROLES, null=True)
  def __str__(self):
    return self.role

class LeaveType(models.Model):
  LEAVE_CHOICES = (
    ('EXPECTANCY', 'EXPECTANCY'),
    ('ANNUAL_LEAVE', 'ANNUAL_LEAVE'),
    ('MILITARY_LEAVE', 'MILITARY_LEAVE'),
    ('EDUCATION_LEAVE', 'EDUCATION_LEAVE'),
    )
  Leave_Types = models.CharField(max_length=20, choices=LEAVE_CHOICES, default='annual')

  def __str__(self):
    return self.Leave_Types

class LeaveStatus(models.Model):
  Approved = 0
  Pending = 1
  Declined = 2
  Statuses=(
    (Approved,'Approved'),
    (Pending, 'Pending'),
    (Declined, 'Declined'),
  )

class Department(models.Model):
    department_name = models.CharField(max_length=30, default = 'Service')
                                       
    def __str__(self):
        return f'{self.department_name} Department'

    @classmethod
    def get_department(cls):
        all_departments=cls.objects.all()
        return all_departments

class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    Leave_Type = models.ForeignKey(LeaveType,on_delete=models.CASCADE)
    leave_issuer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_issuer', null=True)
    Begin_Date = models.DateField(help_text='Leave begin date')
    End_Date = models.DateField(help_text='Leave end date')
    Requested_Days = models.PositiveIntegerField(default=5,help_text='Total no of requested leave days')
    Comments = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '%s %s' % (self.leave_id, self.leave_issuer)

    @classmethod
    def print_all(cls):
        leave = Leave.objects.all()
        return leave

    @classmethod
    def get_all_leaves(cls):
        all_leaves=cls.objects.all()
        return all_leaves

    @classmethod
    def get_single_user_notice(cls,owner):
        user_leaves=cls.objects.filter(user=owner).all()
        return user_leaves

class Notice(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # recipient=models.ForeignKey()
    topic = models.CharField(max_length=100, default="Emergency Notice", null=False, blank=False)
    message = models.TextField(null=False, blank=False)

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

