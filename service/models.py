from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Service(models.Model):
    service_title=models.CharField(max_length=100)
    service_desc=HTMLField()