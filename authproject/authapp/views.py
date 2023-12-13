from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render(request, 'home.html')

def signpage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
         # check if the password length is at least 8 characters
        if len(pass1) < 8 or len(pass2) < 8:
            messages.warning(request, "Password Must Be At Least 8 Characters")
            return render(request, 'signup.html')

        # check if the password fields match
        if pass1 != pass2:
            messages.warning(request, "Password Did Not Match!")
            return render(request, 'signup.html')

        # check if the username already exists
        if User.objects.filter(username=uname).exists():
            messages.warning(request, "Username Already Exists!")
            return render(request, 'signup.html')

        # check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email Already Exists!")
            return render(request, 'signup.html')

        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request,f"Welcome {uname}! Account Created Successfully!")
            return redirect('login')
            
        
    return render(request, 'signup.html')

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        en = authenticate(request,username=username,password=pass1)
        if en is not None:
            login(request,en)
            return redirect('home')
    
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')



    
