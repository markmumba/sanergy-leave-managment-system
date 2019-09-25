from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request, 'sanergytemplates/homepage.html')

def  leavepage(request):
    return render (request,'sanergytemplates/leavepage.html')

