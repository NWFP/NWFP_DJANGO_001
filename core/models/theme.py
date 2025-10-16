from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    
    class Meta:
        verbose_name_plural = "Themes"

    def __str__(self):
        return self.name