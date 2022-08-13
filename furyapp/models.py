from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField

# Create your models here.


class investors(models.Model):
    name = models.CharField(null=True,blank=True,max_length=40)
    investor_contact_no = models.BigIntegerField(null=True,blank=True)
    investor_email = models.CharField(primary_key=True, max_length=100)
    #view which startup has highest funding
    money = models.BigIntegerField(null=True,blank = True)

    def __unicode__(self):
        return self.investor_email


class startup_data(models.Model):
    company_name = models.CharField(primary_key=True,max_length=50)
    sector = models.CharField(null=True,blank=True,max_length=30)
    founder = models.CharField(null=True,blank=True,max_length=50)
    contact_no = models.BigIntegerField(null=True,blank=True)
    email = models.CharField(null=True,blank=True,max_length=50)
    team = models.CharField(null=True,blank=True,max_length=50)
    website = models.CharField(null=True,blank=True,max_length=50)
    funds = models.BigIntegerField(null=True,blank = True)
    #total funding they raised

    def __unicode__(self):
        return self.company_name

class startup_post(models.Model):
    media_files = models.FileField(upload_to='mediafiles',null=True,blank=True)
    description = models.CharField(null=True,blank=True,max_length=300)
    title = models.CharField(null=True,blank=True,max_length=50)
    like = models.IntegerField(default=0,null=True,blank=True)

class startup_user(models.Model):
    name = models.CharField(null=True,blank=True,max_length=50)
    contact_no = models.BigIntegerField(null=True,blank=True)
    email = models.CharField(primary_key=True,max_length=50)

    def __unicode__(self):
        return self.email
    
class tasks(models.Model):
    task_name = models.CharField(null=True,blank=True,max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status =models.BooleanField(default = False)
    companny = models.ForeignKey(startup_data, on_delete=models.CASCADE)
