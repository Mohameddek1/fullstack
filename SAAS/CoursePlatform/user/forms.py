from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    # Define email field with EmailInput widget and add 'form-control' class
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    
    # Define username field with TextInput widget and add 'form-control' class
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    
    # Define password1 field with PasswordInput widget and add 'form-control' class
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    
    # Define password2 field with PasswordInput widget and add 'form-control' class
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        # Set the model to User and fields to include username, email, password1, and password2
        model = User
        fields = ("username", "email", "password1", "password2")





# forms.py
# from django import forms
# from django.contrib.auth.models import User

# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("Username is already taken.")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email is already registered.")
#         return email

#     def save(self):
#         # Create a new user object
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'],
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password']
#         )
#         return user