from django.shortcuts import render, redirect,get_object_or_404
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
    
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace 'student_list' with the URL for listing students
    else:
        form = StudentForm()

    return render(request, 'create_student.html', {'form': form})

def update_student(request, student_id):
    instance = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace 'student_list' with the URL for listing students
    else:
        form = StudentForm(instance=instance)

    return render(request, 'update_student.html', {'form': form, 'student': instance})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Similar views for Subject, Result, and Attendance

# Subject views
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Replace 'subject_list' with the URL for listing subjects
    else:
        form = SubjectForm()

    return render(request, 'create_subject.html', {'form': form})

def update_subject(request, subject_id):
    instance = get_object_or_404(Subject, id=subject_id)
    
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Replace 'subject_list' with the URL for listing subjects
    else:
        form = SubjectForm(instance=instance)

    return render(request, 'update_subject.html', {'form': form, 'subject': instance})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

# Result views
def create_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result_list')  # Replace 'result_list' with the URL for listing results
    else:
        form = ResultForm()

    return render(request, 'create_result.html', {'form': form})

def update_result(request, result_id):
    instance = get_object_or_404(Result, id=result_id)
    
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('result_list')  # Replace 'result_list' with the URL for listing results
    else:
        form = ResultForm(instance=instance)

    return render(request, 'update_result.html', {'form': form, 'result': instance})

def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_list.html', {'results': results})

# Attendance views
def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Replace 'attendance_list' with the URL for listing attendance
    else:
        form = AttendanceForm()

    return render(request, 'create_attendance.html', {'form': form})

def update_attendance(request, attendance_id):
    instance = get_object_or_404(Attendance, id=attendance_id)
    
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Replace 'attendance_list' with the URL for listing attendance
    else:
        form = AttendanceForm(instance=instance)

    return render(request, 'update_attendance.html', {'form': form, 'attendance': instance})

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance_records': attendance_records})
