from .models import *
from django import forms

class LeaveForm(forms.ModelForm):
    class Meta :
        model=Leave
        exclude=['empLeave_req_id','emp_id']
        