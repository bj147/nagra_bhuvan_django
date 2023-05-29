from django.db import models

class student(models.Model):
    name=models.TextField(max_length=30)
    clgname=models.CharField(max_length=100)
    
    cgpa=models.IntegerField()
    dob=models.DateField()
    branch=models.TextField() 
    

# Create your models here.
