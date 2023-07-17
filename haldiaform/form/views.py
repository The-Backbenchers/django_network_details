from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    # return HttpResponse("Hello World")
    return render(request,'base.html')
def signup(request):
    # return HttpResponse("Hello World")
    return render(request,'signup.html')
def signin(request):
    return render(request,'signin.html')