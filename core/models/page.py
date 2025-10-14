from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from utils.model import Model

class Page(Model, ActivatorModel,TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description= models.TextField(blank=True)
    status = models.CharField(max_length=50)
    timestamps = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Page name"

    def __str__(self):
        return f"Page {self.page_number} of {self.publication.title}"