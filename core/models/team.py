from django.db import models
from django.utils import timezone
from utils.model import IdModel
#from django_extensions.db.models import ActivatorModel
from ckeditor.fields import RichTextField

class Team(IdModel):
    name = models.CharField(max_length=255)
    team_type = models.CharField(max_length=20,
                             choices=[('Work Package','Work Package'),
                                      ('Technical','Technical'),
                                      ('Statistical Support','Statistical Support'),
                                      ('KEC', 'KEC')], blank=True)                       
    work_package = models.CharField(max_length=255,
                            choices=[('Farm and Design','Farm and Design'),
                                     ('Soils','Soils'),
                                     ('Biodiversity','Biodiversity'),
                                     ('Water','Water'),
                                     ('Gases','Gases'),
                                     ('Remote Sensing','Remote Sensing'),
                                     ('Data','Data'),
                                     ('Data Systems','Data Systems')], blank=True)
    skillset = models.TextField(max_length=200, blank=True)
    image = models.URLField(blank=True)
    staff_link = models.URLField(blank=True)
    activation_date = models.DateField(default=timezone.now) # Activation date
    deactivation_date = models.DateField(null=True, blank=True) # Deactivation date
    #biography = RichTextField(max_length=1000,blank=True)
    
    class Meta:
        verbose_name_plural = "Team Members"
