from django.db import models

# Create your models here.

class Image(models.Model):
    images = models.ImageField(upload_to = 'image/')
    title = models.CharField()
    description = models.TextField()
   
class Student(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    education_level = models.CharField()
    student_email = models.EmailField()

class Freelancer(models.Model):
    freelancer_names = models.CharField()
    project_name = models.CharField()
    freelancer_email = models.EmailField()

class Enterprise(models.Model):
   enterprise_ founder = models.CharField()
    enterprise_name = models.CharField()
    enterprise_location = models.CharField()
    entrprise_email = models.EmailField()
      
class Business(models.Model):
    business_founder = models.CharField()
    business_name = models.CharField()
    business_location = models.CharField()
    business_email = models.EmailField()

class Academic(models.Model):
    academic_name = models.CharField()
    academic_location = models.CharField()
    academic_email = models.EmailField() 

class Government(models.Model):
    academic_name = models.CharField()
    academic_location = models.CharField()
    academic_email = models.EmailField()