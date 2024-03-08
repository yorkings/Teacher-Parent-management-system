from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  *

class TeacherRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    tsc_no = forms.CharField(max_length=20)  
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'tsc_no', 'email', 'password1', 'password2']

class AdminRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Set the user as a staff member
        user.is_superuser = True  # Set the user as a superuser
        if commit:
            user.save()
        return user

class ParentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = CustomUser  # Corrected from 'models' to 'model'
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )

class EventForm(forms.ModelForm):
     class Meta:
         model=events
         fields='__all__'   