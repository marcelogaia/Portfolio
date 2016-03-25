from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    linkedin = models.URLField()
    github = models.URLField()
    website = models.URLField()

class Resume(models.Model):
    title = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField()
    languages = models.TextField()
    skills = models.TextField()
    
class Experience(models.Model):
    resume_id = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    company_website = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    description = models.TextField()
    
class Education(models.Model):
    title = models.CharField(max_length=30)
    institution = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=30)
    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    description = models.TextField()
    featured_img = models.CharField(max_length=30)
    date = models.DateField()

class Management:
    title = models.CharField(max_length=30)
    text = models.TextField()
    
class Project_images:
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.CharField(max_length=30)
    thumb_url = models.CharField(max_length=30)
    comment = models.CharField(max_length=60)
    