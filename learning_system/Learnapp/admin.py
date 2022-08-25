from django.contrib import admin
from .models import Course, Student, Support
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    model = Course

class StudentAdmin(admin.ModelAdmin):
    model = Student
    
    def save_model(self, requset, obj, form, change):
        if getattr(obj, "user", None) is None:
            obj.user = requset.user
        return super().save_model(requset, obj, form, change)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj is not None and obj.user == request.user:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        elif obj is not None and obj.user == request.user:
            return True
        else:
            return False

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Support)