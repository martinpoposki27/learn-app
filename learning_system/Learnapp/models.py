from email import message
from sys import maxsize
from django.db import models

# Create your models here.

from email.policy import default
from pickle import TRUE
from tkinter import CASCADE
from turtle import title
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    topic = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(default="/")
    description = models.TextField(max_length=100, null=True, blank=True)
    textcontent = models.TextField(null=True, blank=True)
    videoUrl = models.URLField(null=True, blank=True)

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_img = models.ImageField(default="profile_imgs/lank-profile.png", upload_to="profile_imgs/")
    progress = models.IntegerField(default=0)
    last_course = models.ForeignKey(Course, null = True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Support(models.Model):
    subject = models.CharField(max_length=255)
    student = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    message = models.TextField()
    
    def __str__(self):
        return self.subject + " - " + str(self.student)



