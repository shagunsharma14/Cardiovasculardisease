from django.db import models

# Create your models here.

class users(models.Model):
    name=models.CharField(max_length=50)
    pnum=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class udetails(models.Model):
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    height=models.CharField(max_length=10)
    weight=models.CharField(max_length=10)
    systolic=models.CharField(max_length=10)
    diastolic=models.CharField(max_length=10)
    cholestrol=models.CharField(max_length=10)
    glucose=models.CharField(max_length=10)
    smoking=models.CharField(max_length=10)
    alchohol=models.CharField(max_length=10)
    active=models.CharField(max_length=10)
