from django.shortcuts import render,redirect

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')
    
    
def  leavepage(request):
    return render (request,'leavepage.html')

    