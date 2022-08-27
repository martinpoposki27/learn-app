from dataclasses import fields
from urllib import request
from django import forms
from .models import Student, Support
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ChangeStudentForm(UserCreationForm):

    # def __init__(self, *args, **kwargs):
    #     super(ChangeStudentForm, self).__init__(*args, **kwargs)
    #     for field in self.visible_fields():
    #         field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Student
        fields = ['name', 'surname']

class SupportForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Support
        student = Student
        fields = ['subject', 'message']

