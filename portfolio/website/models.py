from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name            = models.CharField(max_length=30)
    address         = models.CharField(max_length=50)
    city            = models.CharField(max_length=60)
    state_province  = models.CharField(max_length=30, verbose_name="State / Province")
    country         = models.CharField(max_length=50)
    email           = models.EmailField()
    phone_number    = models.CharField(max_length=12, verbose_name="Phone no.")
    linkedin        = models.URLField()
    github          = models.URLField()
    website         = models.URLField()
    
    def __str__(self):
        return self.name + " (" + str (self.id) + ")"
    
class Language(models.Model):
    name        = models.CharField(max_length=30)
    code        = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name        = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Resume(models.Model):
    title       = models.CharField(max_length=30)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    summary     = models.TextField()
    language    = models.ManyToManyField(Language)
    skill       = models.ManyToManyField(Skill)
    
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    resume          = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title           = models.CharField(max_length=30)
    company_name    = models.CharField(max_length=30)
    company_website = models.URLField()
    start_date      = models.DateField()
    end_date        = models.DateField()
    city            = models.CharField(max_length=60)
    state_province  = models.CharField(max_length=30, verbose_name="State / Province")
    country         = models.CharField(max_length=50)
    description     = models.TextField()
    
    def __str__(self):
        return self.title + "-" + self.company_name
    
class Education(models.Model):
    resume      = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title       = models.CharField(max_length=30)
    institution = models.CharField(max_length=30)
    start_date  = models.DateField()
    end_date    = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return self.title + "-" + self.institution

class Project(models.Model):
    title           = models.CharField(max_length=30)
    experience      = models.ForeignKey(Experience, on_delete=models.CASCADE)
    description     = models.TextField()
    featured_image  = models.CharField(max_length=30)
    date            = models.DateField()
    
    def __str__(self):
        return self.title

class Management(models.Model):
    title       = models.CharField(max_length=30)
    text        = models.TextField()
    
    def __str__(self):
        return self.title
    
class Project_image(models.Model):
    project     = models.ForeignKey(Project, on_delete=models.CASCADE)
    url         = models.CharField(max_length=30)
    thumb_url   = models.CharField(max_length=30, verbose_name="Thumbnail URL")
    comment     = models.CharField(max_length=60)
    
    def __str__(self):
        return self.comment
    
class Reference(models.Model):
    resume       = models.ForeignKey(Resume, on_delete=models.CASCADE)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=60,blank=True)