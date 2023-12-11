from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=2080)
    department=models.CharField(max_length=2080)
    dob=models.DateField()
    designation=models.CharField(max_length=2080)
    salary=models.CharField(max_length=2080)
    address=models.CharField(max_length=2080)
    others=models.TextField()
