from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
# Create your views here.
def Home(request):
    # return HttpResponse("Hello World")
    return render(request,'base.html')
def signup(request):
    # return HttpResponse("Hello World")
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
        else:
            messages.error(request, f'There is some problem') 
    else:
        form=NewUserForm()

    context={'form':form}
    return render(request,'signup.html',context)

def signin(request):
    # return HttpResponse("Hello World")
    return render(request,'signin.html')