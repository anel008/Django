from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=50)
    dep_description = models.TextField()
