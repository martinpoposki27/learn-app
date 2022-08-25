from django.shortcuts import render
from .models import Course, Student,Support
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, SupportForm, ChangeStudentForm
from http.client import HTTPResponse
from multiprocessing import context
from turtle import title
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def frontpage(request):
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     courses = Course.objects.filter(title__icontains=q)
    # else:
    #     courses = Course.objects.all()
    courses = Course.objects.all()
    student = Student.objects.filter(user = request.user).get()
    context = {
        'courses': courses,
        'student': student
    }
    return render(request, 'system/frontpage.html', context=context)

def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    student = Student.objects.filter(user = request.user).get()
    student.last_course = course
    if student.progress < 100:
        student.progress = student.progress + 5
    student.save()
    return render(request, 'system/course_detail.html', {'course': course})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        first_course = Course.objects.first()
        if form.is_valid():
            u = form.save()
            user = form.cleaned_data.get('username')
            Student.objects.create(
                user=u,
                last_course=first_course
            )
            messages.success(request, "Account was created for " + user)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            messages.info(request, "Username or Password is incorrect!")
            return render(request, 'accounts/login.html')
    context = {}
    return render(request, 'accounts/login.html', context)

def levelpage(request):
    thisstudent = Student.objects.filter(user = request.user).get()
    students = Student.objects.exclude(user=request.user).all()
    context = {
        'thisstudent': thisstudent,
        'students': students
    }
    return render(request, 'system/levelpage.html', context=context)

def profilepage(request):
    student = Student.objects.filter(user = request.user).get()

    # if request.method == 'POST':
    #     form = ChangeStudentForm(request.POST)

    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         profile.profile = profile
    #         profile.student = request.user
    #         profile.save()
                
    #         return redirect('profilepage')
    # else:
    #     form = ChangeStudentForm()

    context = {
        'student': student,
        # 'form': form
    }
    return render(request, 'accounts/profilepage.html', context=context)

def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)

        if form.is_valid():
            support = form.save(commit=False)
            support.support = support
            support.student = request.user
            support.save()
            
            return redirect('frontpage')
    else:
        form = SupportForm()

    return render(request, 'system/support.html', {'form': form})