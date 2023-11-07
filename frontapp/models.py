from django.db import models

# Create your models here.
class userlogindb(models.Model):
    EMAIL = models.EmailField(max_length=100, null=True, blank=True)
    USERNAME = models.CharField(max_length=100, null=True, blank=True)
    PASSWORD = models.CharField(max_length=100, null=True, blank=True)
    CONFIRMPASSWORD = models.CharField(max_length=100, null=True, blank=True)
