from django.db import models

# Create your models here.
class FileList(models.Model):
    Filename=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    Createdby=models.CharField(max_length=100)
    Assignedto=models.CharField(max_length=100)

    def __str__(self):
        return self.Filename


