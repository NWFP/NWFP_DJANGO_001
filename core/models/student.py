from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    organisation = models.CharField(max_length = 255)
    project_title = models.CharField(max_length=255)
    

    class Meta:
        verbose_name_plural = "Students"
