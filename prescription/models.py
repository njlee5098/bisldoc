from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)