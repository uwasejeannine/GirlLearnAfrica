from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('mentor_list/', views.mentor_list, name='mentor_list'),
    path('student_list/', views.student_list, name='student_list'),
    path('course_list/', views.course_list, name='course_list'),
    path('event_list/', views.event_list, name='event_list'),
    path('feedback/', views.feedback, name='feedback'),
    path('add_course/', views.add_course, name='add_course'),
    path('register_student/',views.register_student, name='register_student'),
    path('register_mentor/', views.register_mentor, name='register_mentor'),
    path('add_event/', views.add_event, name='add_event'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('course/<str:course_name>/', views.course_details, name='course_details'),

]


