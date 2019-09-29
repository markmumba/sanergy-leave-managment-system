from .models import *
from django import forms

leave_choices = [
    
    ('annual leave','Annual leave'),
    ('compassion leave','Compassion leave'),
    ('maternity leave','Maternity leave'),
    ('Paternity leave', 'Paternity leave'),
    ('study leave', 'Study leave'),
]

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        widgets = {
           'Begin_Date':forms.DateTimeInput(attrs={ 'class':
               'datetime-input'}),
            'End_Date':forms.DateTimeInput(attrs={ 'class':
               'datetime-input'}),
            'Leave_Type':forms.Select(choices=leave_choices)
        }

        exclude=['empLeave_req_id','emp_id','emp_fullname']
        
