from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from sanergy import urls as sanergy_leave_urls
from sanergy_leave import views as sanergy_leave_views

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm

# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    if request.user.is_superuser==True:
         return render(request, 'users/profiles.html', context)
    elif request.user.is_staff == True:
        return render(request, 'users/staffprofile.html', context)
    else:
         return render(request, 'users/profile.html', context)
