from django.db import models
from django.utils import timezone
from django_extensions.db.models import ActivatorModel
from utils.model import IdModel



class Page(IdModel):
    template_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20,choices=[('Draft','Draft'),('Published','Published')],default='Draft')
    landing_page = models.CharField(max_length=10,choices=[('Yes','Yes'),('No','No')],default='No')
    description = models.TextField(max_length = 200, blank=True)
    activation_date = models.DateField(default=timezone.now) # Activation date
    deactivation_date = models.DateField(null=True, blank=True) # Deactivation date
    
    class Meta:
        verbose_name_plural = "Pages"

    # def __str__(self):
    #     return self.name + " - " + self.title + " - " + self.status