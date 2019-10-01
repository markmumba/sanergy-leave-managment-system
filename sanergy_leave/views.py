from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext

from users.models import Profile

from .forms import AddEmployeeForm, LeaveForm
from .models import Leave

# Create your views here.


def homepage(request):
    return render(request, 'sanergytemplates/homepage.html')

@login_required
def apply_leave(request):
    
    current_user = request.user
    if current_user.is_superuser == True:
        return render(request, 'admin/hr.html')
    elif current_user.profile.is_staff == True:
        return render(request, 'admin/manager.html')
    else:
        requested_days = 0
        if request.method == 'POST':
            form = LeaveForm(request.POST, request.FILES)
            if form.is_valid():
                start_date = form.cleaned_data['Begin_Date']
                end_date = form.cleaned_data['End_Date']
                delta = end_date-start_date
                requested_days = delta.days
                leave = form.save(commit=False)
                leave.username = current_user
                leave.emp_id=current_user.id
                leave.save()

                return redirect('applyform')

            else:
                form = LeaveForm()

                leaves = Leave.print_all()

                return render(request, 'sanergytemplates/leave_apply.html', {"lform": form, "leavess": leaves, 'requested_days': requested_days})

@login_required
def admin(request):
    return render(request, 'admin/manager.html')

@login_required
def adminsite(request):
    return render(request, 'admin/manager.html')
    '''
    view function for creating manager,
    '''
    
@login_required
def addEmployee(request):
    if request.method=='POST':
        form=AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            useremail=form.cleaned_data.get('email')
            createdEmployee=User.objects.filter(email=useremail).first()
            createdEmployee.profile.is_staff=False
            createdEmployee.profile.is_employee=True
            createdEmployee.save()
            messages.success(request,f'Account for {username} created!')
            return redirect('login')
        else:
            form=AddEmployeeForm()
            return render(request, 'admin/add_employee.html', {'form': form})

# getting user profile forr the loged in User

def user_profile(request):
    """Displays information unique to the logged-in user."""

    user = authenticate(username='superuserusername', password='sueruserpassword')
    login(request, user)

    return render(request, 'user/profile.html',
           context_instance=RequestContext(request))
