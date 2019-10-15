import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django.urls import reverse, reverse_lazy

from users.models import Profile

from .email import *
from .forms import AddEmployeeForm, LeaveForm
from .models import Leave
from .datecounter import dateDiffInSeconds,daysHoursMinutesSecondsFromSeconds

# Create your views here.

def homepage(request):
    todays_date = datetime.datetime.now()

    return render(request, 'sanergytemplates/homepage.html',{'todays_date':todays_date})


@login_required
def addEmployee(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            
            name=form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1') 
            form.save()
            welcome_email(name,email, password)

            employee=Profile.objects.filter(user__username=name).first()

            employee.department=current_user.profile.department

            employee.save()

            messages.success(request,'Employee added succesfully')
            return redirect('managersite')

    else:

        form=AddEmployeeForm()

    return render(request, 'admins/add_employee.html', {'form': form})



@login_required(login_url="/login/")
def employee_list(request):
    all_users = User.objects.all()
<<<<<<< HEAD
  
    return render (request, 'admins/employee_list.html', all_users)
=======

    return render (request, 'admins/employee_list.html', {'all_users':all_users})
>>>>>>> 171391791e2be0839f4934f1a7b886a64b932429

@login_required
def apply_leave(request):

    current_user = request.user

    if current_user.is_superuser == True:
        return redirect(managersite)

        # return render(request, 'admins/hr.html')
    elif current_user.is_staff==True:
        return redirect(managersite)

    else:

        requested_days = 0
        if request.method == 'POST':
            form = LeaveForm(request.POST, request.FILES)
            if form.is_valid():
                leave = form.save(commit=False)
                leave.user = current_user

                start_date = form.cleaned_data['Begin_Date']
                end_date = form.cleaned_data['End_Date']
               
                requested_days = daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(start_date, end_date))
                leave.Requested_Days=requested_days

                name = current_user.username
                superusers = User.objects.filter(is_superuser=True)

                for user in superusers:
                    leave_request_sent(name,user.email)

                leave.save()

                return redirect('table')

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
    return render(request, 'admins/manager.html',{'employees':employees , "leavess": leaves})


@login_required
def hrsite(request):
    employees=Profile.objects.filter(is_employee=True).all()
    leaves = Leave.print_all()
    return render(request, 'admins/hr.html',{'employees':employees , "leavess": leaves})


@login_required
def single_leave(request,leave_id):
    single_leave = Leave.objects.get(leave_id)
    return render(request, 'admins/single_leave.html',{"single_leave": single_leave})


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

# def individual_leaves(request, user_id):
#     current_user = request.user
#     users_leaves = Leave.objects.filter(user = current_user)
#     return render(request, 'users/profile.html',{"users_leaves": users_leaves})

