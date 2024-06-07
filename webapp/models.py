from django.db import models

# # Create your models here.
class contactdb(models.Model):
    cname =models.CharField(max_length=100,null=True,blank=True)
    cemail = models.EmailField(max_length=100, null=True, blank=True)
    cphone = models.IntegerField( null=True, blank=True)
    csubject = models.CharField(max_length=100, null=True, blank=True)
    cmessage = models.CharField(max_length=100, null=True, blank=True)

class registerdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Quantity= models.IntegerField(null=True, blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)

