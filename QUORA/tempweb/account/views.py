from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already registered")
            return redirect('register')
        elif password1 != password2:
            messages.info(request, "Passwords do not match")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            messages.success(request, "User created successfully")
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')
