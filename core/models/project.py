from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=255)
    goal = models.CharField(max_length=200, null= True, blank=True)
    description = RichTextField(max_length=500, null= True, blank=True)
    #student = models.ManyToManyField('Student', related_name='projects', blank=True)
    data = models.ManyToManyField('Data', related_name = 'projects', blank=True)
    tag = models.ManyToManyField('Tag', related_name = 'projects', blank=True)
    theme = models.ManyToManyField('Theme', related_name = 'projects', blank=True)
    additional_data = RichTextField(null = True, blank=True)
    
    class Meta:
        verbose_name_plural = "Projects"


    def __str__(self):
        return self.title