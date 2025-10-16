from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Data Type"
    
    def __str__(self):
        return self.name
    
    