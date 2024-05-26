from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # LOGIN
    path("register/", views.register, name="register"),
    # path("login/", auth_views.LoginView.as_view(next_page="course_list"), name="login"),
    path("login/", views.login_view, name="login"),
    # path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login', http_method_names = ['get', 'post', 'options']), name='logout'),
    path('logout/', views.logout, name='logout'),
   
# RESET password
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

   
    # path("password_reset/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_reset_done"),
    # path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done")
]