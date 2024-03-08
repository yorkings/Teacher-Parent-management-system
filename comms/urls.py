from django.urls import path
from .views import *

urlpatterns = [
    path('teacher/register/', teacher_register, name='teacher_register'),
    path('dashboard-admin/register/', admin_register, name='admin_register'),
    path('parent/register/', parent_register, name='parent_register'),
    path("dashboard/ad-dash/",admin_dashboard,name='admin_dashboard'),
    path('Dashboard/event',events,name='event'),
    path('',login_user,name='login'),
    path('',login_user,name='logout')
]


    