from pyexpat import model
from django.db import models

# Create your models here.
class Additem(models.Model):
    plno=models.CharField(max_length=120)
    relatedplno=models.CharField(max_length=120)
    unifiedplno=models.CharField(max_length=120)
    desc=models.CharField(max_length=500)
    aac=models.CharField(max_length=120)
    specno=models.CharField(max_length=500)
    gw=models.CharField(max_length=500)
    date=models.DateField()

#to change the name field of the additem's database
    def __str__(self):
        return self.plno
    
