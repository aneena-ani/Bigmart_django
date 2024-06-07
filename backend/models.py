from django.db import models

# Create your models here.
class catedb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="category image",null=True,blank=True)
    description =models.CharField(max_length=1000,null=True,blank=True)

class prodb(models.Model):
    catname = models.CharField(max_length=100,null=True,blank=True)
    proname = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=1000,null=tuple,blank=True)
    pimage = models.ImageField(upload_to="category image", null=True)
    price = models.IntegerField(null=True,blank=True)


