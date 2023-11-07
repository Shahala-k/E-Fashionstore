from django.db import models

# Create your models here.
class adminregdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    MOBILE = models.IntegerField(null=True, blank=True)
    USERNAME = models.CharField(max_length=50, null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile")
class categorydb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    DISCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile")


class productdb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    PRIZE = models.IntegerField(null=True, blank=True)
    QUANTITY = models.CharField(max_length=100, null=True, blank=True)
    DISCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile")
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    EMAIL = models.EmailField(max_length=100, null=True, blank=True)
    MESSAGE = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    PRIZE = models.IntegerField(null=True, blank=True)
    TPRIZE = models.IntegerField(null=True, blank=True)
    QUANTITY = models.IntegerField(null=True, blank=True)

class userdetails(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    ADDRESS = models.CharField(max_length=100,null=True, blank=True)
    STATE = models.CharField(max_length=50,null=True, blank=True)
    EMAIL=models.CharField(max_length=50, null=True, blank=True)
    PRODUCT=models.CharField(max_length=50, null=True, blank=True)
    PRIZE=models.CharField(max_length=50, null=True, blank=True)