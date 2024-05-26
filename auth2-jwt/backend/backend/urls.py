from django.contrib import admin
from django.urls import path, include
from authentification.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for Django admin interface
    path("api/user/register", CreateUserView.as_view(), name="register"),  # URL pattern for user registration view
    path("api/token/", TokenObtainPairView.as_view(), name="token"),  # URL pattern for obtaining JWT token
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh"),  # URL pattern for refreshing JWT token
    path("api-auth/", include("rest_framework.urls")),  # URL patterns for Django REST framework authentication views
    path("api/", include("authentification.urls"))
]
