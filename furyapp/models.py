from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField

# Create your models here.


class investors(models.Model):
    name = models.CharField(null=True,blank=True,max_length=40)
    investor_contact_no = models.BigIntegerField(null=True,blank=True)
    investor_email = models.CharField(primary_key=True, max_length=100)

class startup_data(models.Model):
    company_name = models.CharField(primary_key=True,max_length=50)
    sector = models.CharField(null=True,blank=True,max_length=30)
    founder = models.CharField(null=True,blank=True,max_length=50)
    contact_no = models.BigIntegerField(null=True,blank=True)
    email = models.CharField(null=True,blank=True,max_length=50)
    team = models.CharField(null=True,blank=True,max_length=50)
    website = models.CharField(null=True,blank=True,max_length=50)

class startup_post(models.Model):
    media_files = models.FileField(upload_to='mediafiles',null=True,blank=True)
    description = models.CharField(null=True,blank=True,max_length=300)
    title = models.CharField(null=True,blank=True,max_length=50)
    like = models.IntegerField(default=0,null=True,blank=True)

class startup_user(models.Model):
    name = models.CharField(null=True,blank=True,max_length=50)
    contact_no = models.BigIntegerField(null=True,blank=True)
    email = models.CharField(primary_key=True,max_length=50)
    
