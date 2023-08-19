from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("username or password is incorrect!!")
    
    return render(request, "users/login.html")

def register_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("your passowrd and confirm password are not same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")

    return render(request, "users/registeration.html")

def profile_page(request):
    return render(request, "users/profile.html")


