from django.db import models

# Create your models here.

class Registerdb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class cartdb(models.Model):

    Username = models.CharField(max_length=100,null=True,blank=True)
    Product = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)

