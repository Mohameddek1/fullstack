from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def register(request):
    # If the request method is POST, it means the user submitted the registration form
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        # Bind the POST data to the form
        if form.is_valid():
            # If the form data is valid, save the user and redirect to the login page
            user = form.save()
            return redirect("login")
        # If the form data is not valid, it will be re-rendered with validation errors
    else:
        # If the request method is not POST (i.e., GET), show an empty registration form
        form = CustomUserCreationForm()

    # Render the registration page with the form
    return render(request, "registration/register.html", {"form": form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('/course')
        else:
            # Handle invalid login credentials
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'registration/login.html')
    


# RESET PASSWORD
