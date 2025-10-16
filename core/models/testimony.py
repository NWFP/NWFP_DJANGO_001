from django.db import models
from ckeditor.fields import RichTextField

class Testimony(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=200, null = True, blank=True)
    full_description = RichTextField(max_length=500, null = True, blank=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='testimonies', null=True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='testimonies', null=True, blank=True)
    url = models.URLField(max_length=200, null = True, blank=True)
    youtube_code = models.CharField(max_length=100, null = True, blank=True)
    video_filename = models.CharField(max_length=255, null = True, blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Testimonies"


    def __str__(self):
        return self.title
    
    