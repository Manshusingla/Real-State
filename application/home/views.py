from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact as cnts
from .forms import Contact


# Create your views here.
def login(request):
    return render(request,"login.html")
def index(request):
    return render(request,"index.html")


# Create your views here.

# @login_required(login_url='/')
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    form=Contact()
    return render(request,"contact.html",{"form":form})

def services(request):
    return render(request,"services.html")
def company_certification(request):
    return render(request,"company_certification.html")
def login(request):
    return render(request,"login.html")


def user_detail(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    address=request.POST['address']
    phone_number=request.POST['phone_number']
    message=request.POST['message']
    subject=request.POST['subject']
    print(first_name)
    try:
        print(first_name)
        reg=cnts(first_name=first_name,last_name=last_name,email=email,phone=phone_number,message=message,)
        reg.save()
        return redirect("contact") 
        
    except:
        messages.error(request,'plaese fills valid data')
        return redirect("contact")    


def loginuser(request):
    username = request.POST['username']
    password = request.POST['password']
    # print(username)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('home') 
    else:
        messages.error(request,'Try again later')
        return redirect('/') 

def loginout(request):
    logout(request)
    return redirect('login') 