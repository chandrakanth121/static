from django.db import models

# Create your models here.
class studentmodel(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()
