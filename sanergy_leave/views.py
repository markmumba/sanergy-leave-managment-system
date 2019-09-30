from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from users.models import Profile

from .forms import LeaveForm

# Create your views here.


def homepage(request):
    return render(request, 'sanergytemplates/homepage.html')


def apply_leave(request):
    current_user = request.user
    if current_user.is_superuser == True:
        return redirect(request, 'admintemplates/hr.html')
    elif current_user.profile.is_staff == True:
        return redirect(request, 'admintemplates/manager.html')
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

def admin(request):
    return render(request, 'admin/adminsite.html')
    