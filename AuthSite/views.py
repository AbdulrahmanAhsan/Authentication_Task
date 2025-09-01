from django.shortcuts import render, redirect
from django.db.models import Q, F
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import User_Profile

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request, user):
    return render(request, 'dashboard.html', {'user': user})

    
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User_Profile.objects.filter(Q(user__username=username) | Q(user__email=username.lower())).exists():
            return render(request, 'login.html', {'error': "User does not exist"})
        
        if User_Profile.objects.filter(user__email=username.lower()).exists():
            temp_user = User_Profile.objects.get(user__email=username.lower())
            username = temp_user.user.username

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            return dashboard(request, user)
        
    return render(request, 'login.html') 

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get("username")
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        pfp = request.FILES.get('pfp')

        email = email.lower()

        if password != confirm_password:
            return render(request, 'signup.html', {'error': "Passwords do not match"})

        if User_Profile.objects.filter(Q(user__username=username)).exists():
            return render(request, 'signup.html', {'error': "Username Already Exists"})
        
        if User_Profile.objects.filter(Q(user__email=email)).exists():
            return render(request, 'signup.html', {'error': "Email Already Exists"})
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        user_profile = User_Profile.objects.create(user=user ,pfp=pfp)
        user_profile.save()
        return redirect('/authsite/login/')

    return render(request, 'signup.html')