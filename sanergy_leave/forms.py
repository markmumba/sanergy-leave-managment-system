from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from .models import Leave, Notice
from users.models import Profile

leave_choices = [
    
    ('annual leave','Annual leave'),
    ('compassion leave','Compassion leave'),
    ('maternity leave','Maternity leave'),
    ('Paternity leave', 'Paternity leave'),
    ('study leave', 'Study leave'),
  ]

class LeaveForm(forms.ModelForm):

    class Meta:
        model= Leave
        widgets = {
           'Begin_Date':forms.DateTimeInput(attrs={ 'class':
               'datetime-input'}),
            'End_Date':forms.DateTimeInput(attrs={ 'class':
               'datetime-input'}),
            'Leave_Type':forms.Select(choices=leave_choices)
        }

        exclude=['empLeave_req_id','emp_id','emp_fullname','user','leave_status','leave_issuer','Requested_Days']


class AddEmployeeForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class ManagerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        if commit:
            user.save()
        return user

