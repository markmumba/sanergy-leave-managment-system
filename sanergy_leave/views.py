from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django.urls import reverse, reverse_lazy

from users.models import Profile
import datetime
from .forms import AddEmployeeForm, LeaveForm
from .models import Leave
from .email import  *

# Create your views here.

def homepage(request):
    todays_date = datetime.datetime.now()
    return render(request, 'sanergytemplates/homepage.html',{'todays_date':todays_date})

def full_calendar(request):
    return render(request, 'sanergytemplates/calendar.html')

@login_required(login_url="/login/")
def employee_list(request):
    all_users = User.objects.all()
  
    return render (request, 'admin/employee_list.html', {'all_users':all_users})


@login_required
def addEmployee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            
            name=form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1') 
            form.save()

            welcome_email(name,email, password)

            messages.success(request,'Employee added succesfully')
            return redirect('managersite')

    else:

        form=AddEmployeeForm()

    return render(request, 'admin/add_employee.html', {'form': form})

@login_required
def apply_leave(request):
        
    current_user = request.user

    if current_user.is_superuser == True:
        return redirect(managersite)

        # return render(request, 'admin/hr.html')
    elif current_user.is_staff==True:
        return redirect(managersite)

    else:

        requested_days = 0
        if request.method == 'POST':
            form = LeaveForm(request.POST, request.FILES)
            if form.is_valid():
                leave = form.save(commit=False)
                leave.user = current_user
                leave.emp_id=current_user.id
                leave.save()
                
                return redirect('apply_leave')

        else:
            
            form = LeaveForm()

   
    return render(request, 'sanergytemplates/leave_apply.html', {"lform": form, 'requested_days': requested_days})


def table (request):
    leaves = Leave.print_all()
    return render(request, 'sanergytemplates/table.html',{ "leavess": leaves})

@login_required
def managersite(request):
    employees=Profile.objects.filter(is_employee=True).all()
    leaves = Leave.print_all()
    return render(request, 'admin/manager.html',{'employees':employees , "leavess": leaves})


@login_required
def accept_leave(request,pk):
 
    leave=Leave.objects.get(pk=pk)
    leave.leave_status=Leave.Approved

    name=leave.user.username
    email =leave.user.email
    date = leave.Begin_Date
    date2 = leave.End_Date
    leave.save()
    status_approval_email(name,email,date,date2)
    messages.success(request,'Leave Approval notification sent')

    return redirect('managersite')


@login_required
def decline_leave(request,pk):
    leave=Leave.objects.get(pk=pk)
    leave.leave_status=Leave.Declined

    name=leave.user.username
    email =leave.user.email
    leave.save()
    status_declined_email(name,email)
    messages.success(request,'Leave Decline notification sent')

    return redirect('managersite')

