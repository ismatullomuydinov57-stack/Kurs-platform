# main/urls.py
from django.urls import path
from . views import index, course_students, student_detail, course_create, student_create, course_update, student_update

urlpatterns = [
    path('', index, name='index'),
    path('course/<int:course_id>/students/', course_students, name='course_students'),
    path('student/<int:student_id>/',student_detail, name='student_detail'),
    path('course_create/', course_create, name='course_create'),
    path('course_update/<int:course_id>/', course_update, name='course_update'),
    path('student_update/<int:student_id>/', student_update, name='student_update'),
    path('student_create/', student_create, name='student_create'),

]

