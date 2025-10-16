from django.db import models

class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    ref_type = models.CharField(max_length=20)
    ref_type_id = models.IntegerField()
    authors = models.CharField(max_length=255)
    pub_year = models.IntegerField()
    title = models.CharField(max_length=255)
    journal = models.CharField(max_length=255, blank=True)
    volume = models.IntegerField(blank=True, null=True)
    issue = models.CharField(blank=True, null=True)
    pages = models.CharField(max_length=50, blank=True)
    abstract = models.TextField(blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    doi = models.URLField(blank=True)
    image = models.URLField(blank=True)
    issue_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Publications"

    def __str__(self):
        return f"{self.title} ({self.get_ref_type_display()}, {self.pub_year})"