from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=30,default="")
    Phone=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=50,default="")
    Services=models.CharField(max_length=20, default="")
    