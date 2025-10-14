from django.contrib import admin
from core.models.student import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','organisation','project_title')