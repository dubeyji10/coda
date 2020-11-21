from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Applicant_Profile(models.Model):
    applicant = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='applicant_profile_pics')

    def __str__(self):
        return f'{self.applicant.username} Applicant_Profile'



class Application(models.Model):
    class Score(models.IntegerChoices):
        Male = 1
        Female =2
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(default='90001',max_length=100)
    application_date = models.DateTimeField(default=timezone.now)
    phone=models.CharField(max_length=100,blank=True, null=True)
    country=models.CharField(max_length=100,blank=True, null=True)
    resume=models.FileField(upload_to='resumes/doc/')
    #cover=models.FileField(default=None,upload_to='cover/doc/')

    def __str__(self):
        return f'{self.username} application'

class InteviewUploads(models.Model):
    Id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    ppt=models.FileField(default=None,upload_to='Powerpoints/doc/')
    report=models.FileField(default=None,upload_to='Reports/doc/')
    workflow=models.FileField(default=None,upload_to='Workflows/doc/')
    proc=models.FileField(default=None,upload_to='Procedures/doc/')
    other=models.FileField(default=None,upload_to='Others/doc/')
    Applicant=models.ManyToManyField(Application)

    def __str__(self):
        return f'{self.username} InteviewUploads'

'''
class Uploads(models.Model):
    Id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    interviewppt=models.FileField(upload_to='interviewppt/ppt/')

    tableau=models.FileField(upload_to='interviewtab/tab/')
    alteryx=models.FileField(upload_to='interviewalteryx/alteryx/')
    SQL=models.FileField(upload_to='interviewdb/dba/')
    other=models.FileField(upload_to='interviewother/general/')
    Applicant=models.ManyToManyField(Application)
    
    def __str__(self):
        return f'{self.username} InteviewUploads'
'''

class Rated(models.Model):
    class Score(models.IntegerChoices):
        very_Poor = 1
        Poor =2
        Good = 3
        Very_good = 4
        Excellent = 5
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    topic=models.CharField(max_length=100,default=None)
    rating_date = models.DateTimeField(default=timezone.now)
    punctuality = models.IntegerField(choices=Score.choices)
    communication = models.IntegerField(choices=Score.choices)
    understanding = models.IntegerField(choices=Score.choices)

    def __str__(self):
        return f'{self.id} Rating'

class Employee(models.Model):
    class Score(models.IntegerChoices):
        very_Poor = 1
        Poor =2
        Good = 3
        Very_good = 4
        Excellent = 5
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    topic=models.CharField(max_length=100,default=None)
    employee_date = models.DateTimeField(default=timezone.now)
    punctuality = models.IntegerField(choices=Score.choices)
    communication = models.IntegerField(choices=Score.choices)
    understanding = models.IntegerField(choices=Score.choices)
    rated_by=models.CharField(default="CEO",max_length=100)
    
    def __str__(self):
        return f'{self.id} Employee'

class FirstUpload(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    upload_date = models.DateTimeField(default=timezone.now,null=True,blank=True)
    ppt=models.FileField(upload_to='Powerpoints/doc/')
    report=models.FileField( upload_to='Reports/doc/',null=True,blank=True)
    workflow=models.FileField(upload_to='Workflows/doc/',null=True,blank=True)
    proc=models.FileField(upload_to='Procedures/doc/',null=True,blank=True)
    #other=models.FileField(default="None",upload_to='Others/doc/')
    Applicant=models.ManyToManyField(Application)

    def __str__(self):
        return f'{self.username} upload'
