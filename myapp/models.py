from django.db import models

# Create your models here.
class category_db(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="profile", null=True,blank=True)

class productdb(models.Model):
    Category = models.CharField(max_length=50,null=True,blank=True)
    Product = models.CharField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Brand = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="profile", null=True,blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=50, null=True,blank=True)
    Email = models.EmailField(max_length=50, null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=50, null=True,blank=True)


class checkoutdb(models.Model):
    Firstname = models.CharField(max_length=100, null=True,blank=True)
    Lastname = models.CharField(max_length=100, null=True,blank=True)
    Emailid = models.EmailField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Address = models.CharField(max_length=100, null=True,blank=True)
    Country = models.CharField(max_length=50,null=True,blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
