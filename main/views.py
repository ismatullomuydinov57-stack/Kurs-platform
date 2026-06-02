# main/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student
from .forms import CourseForm, StudentForm

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


def course_create(request:HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CourseForm(data=request.POST)
            if form.is_valid():
                course = form.save()
                return redirect('index')
        else:
           form = CourseForm()
    context = {
        'form': form
    }
    return render(request, 'main/course_create.html', context)



def student_create(request:HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StudentForm(data=request.POST)
            if form.is_valid():
                student = form.save()
                return redirect('student_detail', student_id=student.pk)
        else:
           form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'main/student_create.html', context)

def course_update(request:HttpRequest, course_id:int):
    course=Course.objects.get(pk=course_id)
    if request.method=='POST':
        form=CourseForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('index')
    form=CourseForm(instance=course)
    context={
        'course':course,
        'form':form
    }
    return render(request, 'main/course_update.html', context)

def student_update(request:HttpRequest, student_id:int):
    student=Student.objects.get(pk=student_id)
    if request.method=='POST':
        form=StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    form=StudentForm(instance=student)
    context={
        'student':student,
        'form':form
    }
    return render(request, 'main/student_update.html', context)
