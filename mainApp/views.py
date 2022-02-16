from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.contrib import messages
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        nid = request.POST.get('nid')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        schedule = request.POST.get('schedule')

        userData = userForm(
            name = name,
            phone =phone,
            email = email,
            nid = nid,
            address = address,
            gender = gender,
            pass1 = pass1,
            pass2 = pass2,
            schedule = schedule
        )
        userData.save()
        messages.success(request,'register successfully')
        return redirect('home')

    return render(request,'index.html')

def userlogin(request):

    return render(request,'login.html')

#def userRegister(request):
