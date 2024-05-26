from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

# Create your views here.

@require_POST
def login_view(request):
    # Parse request body to obtain username and password
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    
    # Check if username or password is missing
    if username is None or password is None:
        return JsonResponse({"detail":"Please provide username and password"})
    
    # Authenticate user with provided credentials
    user = authenticate(username=username, password=password)
    
    # Check if authentication failed
    if user is None:
        return JsonResponse({"detail":"invalid credentials"}, status=400)

    # Log in user if authentication is successful
    login(request, user)
    return JsonResponse({"details": "Successfully logged in!"})

    

def logout_view(request):
    # Check if user is authenticated
    if not request.user.is_authenticated:
        return JsonResponse({"detail":"You are not logged in!"}, status=400)
    
    # Log out user
    logout(request)
    return JsonResponse({"detail":"Successfully logged out!"})


@ensure_csrf_cookie
def session_view(request):
    # Check if user is authenticated
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})
    
    # Return JSON response indicating user authentication
    return JsonResponse({"isAuthenticated": True})

        
def whoami_view(request):
    # Check if user is authenticated
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})
    
    # Return JSON response with username if user is authenticated
    return JsonResponse({"username": request.user.username})













