from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')
    

def  leavepage(request):
    return render (request,'leavepage.html')

    