from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null = True, blank=True)
    organisation = models.CharField(max_length = 255, null = True, blank=True)
    course_name = models.CharField(max_length=255, null = True, blank=True)
    project_title = models.CharField(max_length=255, null = True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    
    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name