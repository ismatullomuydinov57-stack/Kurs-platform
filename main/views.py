# main/views.py
from django.shortcuts import render, get_object_or_404
from .models import Course, Student

def index(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        'courses': courses,
        'students': students,
    }
    return render(request, 'main/index.html', context)

def course_students(request, course_id):
    courses = Course.objects.all()
    students = Student.objects.filter(course_id=course_id)
    context = {
        'courses': courses,
        'students': students,
    }
    return render(request, 'main/course_students.html', context)

def student_detail(request, student_id):
    courses = Course.objects.all()
    student = get_object_or_404(Student, id=student_id)
    context = {
        'courses':courses,
        'student': student,
    }
    return render(request, 'main/student_detail.html', context)