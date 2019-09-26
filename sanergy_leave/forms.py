from .models import *
from django import forms

class LeaveForm(forms.ModelForm):
    class Meta :
        model=Leave
        widgets = {
            'Begin_Date':forms.DateInput(attrs={'class':'datepicker'}),
        }
        exclude=['empLeave_req_id','emp_id','emp_fullname']
        