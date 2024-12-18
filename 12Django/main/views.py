from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.


def index(request):
    # return HttpResponse("Hello DJANGO")
    return render(request, 'main1.html', )


def student(r, id):
    student = Students.objects.get(id=id)
    return render(r, 'student.html', context={'student': student})


def students(r):
    students = Students.objects.all()
    return render(r, 'students.html', context={'students': students})

def course(r, id):
    course = Course.objects.get(id=id)
    return render(r, 'course.html', context={'course': course})


def courses(r):
    courses = Course.objects.all()
    return render(r, 'courses.html', context={'courses': courses})
