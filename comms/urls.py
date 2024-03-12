from django.urls import path
from .views import *

from django.urls import path
from .views import *

urlpatterns = [
    path('teacher/register/', teacher_register, name='teacher_register'),
    path('dashboard-admin/register/', admin_register, name='admin_register'),
    path('parent/register/', parent_register, name='parent_register'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/parent/', parent_dashboard, name='parent_dashboard'),
    path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'),
    #events
    path('dashboard/event/',create_events, name='event'),
    path('dashboard/event/delete/<int:id>',delete_even, name='delete_event'),
    path('dashboard/event/edit/<int:id>',edit_events, name='edit_event'),
    path('dashboard/event/list/',event_list, name='list_event'),
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # Student-related URLs
    path('create/student/', create_student, name='create_student'),
    path('update/student/<int:student_id>/', update_student, name='update_student'),
    path('delete/student/<int:id>/', delete_student, name='delete_student'),

    path('student/list/', student_list, name='student_list'),

    # Subject-related URLs
    path('create/subject/', create_subject, name='create_subject'),
    path('update/subject/<int:subject_id>/', update_subject, name='update_subject'),
    path('subject/list/', subject_list, name='subject_list'),

    # Result-related URLs
    path('create/result/', create_result, name='create_result'),
    path('update/result/<int:result_id>/', update_result, name='update_result'),
    path('result/list/', result_list, name='result_list'),

    # Attendance-related URLs
    path('create/attendance/', create_attendance, name='create_attendance'),
    path('update/attendance/<int:attendance_id>/', update_attendance, name='update_attendance'),
    path('delete/attendance/<int:attendance_id>/', update_attendance, name='update_attendance'),
    path('attendance/list/', attendance_list, name='attendance_list'),
]



    