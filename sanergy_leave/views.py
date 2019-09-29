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
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if 'Begin_Date' < 'End_Date':
            delta = 'Begin-Date'-'End_date'
            Requested_days = delta.days

            if form.is_valid():
                leave = form.save(commit=False)
                leave.username = current_user

            return redirect('applyform')

    else:
        form = LeaveForm()

        leaves = Leave.print_all()

        return render(request, 'sanergytemplates/leave_apply.html', {'lform': form, "leavess": leaves})


# def append_to_table (request):
#         current_user=request.user
#         leaves=Leave.print_all()
#         return render(request, 'sanergytemplates/leave_apply.html',{'leavess':leaves})
