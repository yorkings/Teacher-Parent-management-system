from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role='teacher'
            user.save()
              # Replace 'home' with the desired URL after registration
            return redirect("admin_dashboard")
    else:
        form = TeacherRegistrationForm()
    return render(request, 'admindashboard/teacher_register.html', {'form': form})


@login_required
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role='admin'
            user.save()  # Replace 'home' with the desired URL after registration
            return redirect("admin_dashboard")
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_registration.html', {'form': form})


@login_required
def parent_register(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role='parent'
            user.save()
            login(request, user)
            return redirect('admin_dashboard')  # Replace 'home' with the desired URL after registration
    else:
        form = ParentRegistrationForm()
    return render(request, 'admindashboard/parent_registration.htm', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')  # Replace with your admin dashboard URL
                elif user.role == 'teacher':
                    return redirect('teacher_dashboard')  # Replace with your teacher dashboard URL
                elif user.role == 'parent':
                    return redirect('parent_dashboard')  # Replace with your parent dashboard URL
                else:
                    return redirect('home')  # Replace with your default dashboard URL
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')    
def admin_dashboard(request):
    return render(request,'admindashboard/admin_dashboard.html')

def events(request):
    if request.method=="POST":
        event=EventForm(request.POST)
        if event.is_valid():
            event.save()
            return redirect('admin_dashboard')
    else:
       event=EventForm()
    return render(request,'admindashboard/event.html',{'form':event})             
    
