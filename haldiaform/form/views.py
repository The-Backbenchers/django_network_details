from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views import generic 
# Create your views here.
class RoomList(generic.ListView):
    # return HttpResponse("Hello World")
    queryset = Room.objects.order_by('-created_on')
    
    template_name = 'base.html'

class RoomDetail(generic.DetailView):
    model = Room
    template_name = 'room_detail.html'

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

def network_reg(request):
    return render(request,'network_reg.html')
def owner_reg(request):
    return render(request,'owner_reg.html')