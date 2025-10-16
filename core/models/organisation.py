from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    Ror = models.CharField(max_length=100, null=True, blank=True) # Research Organization Registry ID
    
    
    class Meta:
        verbose_name_plural = "Organisations"

    def __str__(self):
        return self.name
    
    