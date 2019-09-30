from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from sanergy import urls as sanergy_leave_urls
from sanergy_leave import views as sanergy_leave_views

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm

# Create your views here.

# def register(request):
#     '''
#     view function for registration
#     '''
#     if request.method=='POST':
#         form=UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             useremail=form.cleaned_data.get('email')
#             userphonenumber=form.cleaned_data.get('phone_number')
#             createdAgent=User.objects.filter(email=useremail).first()
#             createdAgent.profile.is_staff=True
#             createdAgent.profile.is_employee=False
#             createdAgent.profile.phone_number=userphonenumber
#             createdAgent.save()
#             messages.success(request,f'Account for {username} created!')
#             return redirect('login')
#         else:
#             form=UserRegisterForm()
#             return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('index')
        else:
            u_form=UserUpdateForm(instance=request.user)
            p_form=ProfileUpdateForm(instance=request.user.profile)
            context={
                'u_form': u_form,
                'p_form': p_form
                }
        return render(request, 'users/profile.html', context)
