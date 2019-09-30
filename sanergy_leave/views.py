from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from datetime import date
# Create your views here.


def homepage(request):
    return render(request, 'sanergytemplates/homepage.html')


def apply_leave(request):
    current_user = request.user
    requested_days = 0
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            start_date = form.cleaned_data['Begin_Date']
            end_date = form.cleaned_data['End_Date']
            requested_days = delta.days
            delta = end_date-start_date
          
            leave = form.save(commit=False)
            leave.username = current_user

            return redirect('applyform')

    else:
        form = LeaveForm()

        leaves = Leave.print_all()

        return render(request, 'sanergytemplates/leave_apply.html', {'lform': form, "leavess": leaves, 'requested_days': requested_days})


# def append_to_table (request):
#         current_user=request.user
#         leaves=Leave.print_all()
#         return render(request, 'sanergytemplates/leave_apply.html',{'leavess':leaves})
