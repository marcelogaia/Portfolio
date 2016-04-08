from __future__ import unicode_literals
from portfolio import settings
from django_thumbs.db.models import ImageWithThumbsField
from django.db import models

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class User(models.Model):
    name            = models.CharField(max_length=30)
    address         = models.CharField(max_length=50, blank=True,null=True)
    country         = models.CharField(max_length=50)
    state_province  = models.CharField(max_length=30, verbose_name="State / Province")
    city            = models.CharField(max_length=60)
    email           = models.EmailField()
    phone_number    = models.CharField(max_length=12, verbose_name="Phone no.", blank=True,null=True)
    linkedin        = models.URLField(blank=True,null=True)
    github          = models.URLField(blank=True,null=True)
    website         = models.URLField(blank=True,null=True)
    
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
    country         = models.CharField(max_length=50)
    state_province  = models.CharField(max_length=30, verbose_name="State / Province")
    city            = models.CharField(max_length=60)
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

class Management(models.Model):
    title       = models.CharField(max_length=30)
    text        = models.TextField()
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title           = models.CharField(max_length=30)
    experience      = models.ForeignKey(Experience, on_delete=models.CASCADE, null=True, blank=True)
    description     = models.TextField()
    featured_image  = models.ImageField(upload_to='project-pictures')
    date            = models.DateField()
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Project.objects.get(id=self.id)
            if this.featured_image != self.featured_image:
                this.featured_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Project, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Project)
def Project_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.featured_image.delete(False)
    
    
class Project_image(models.Model):
    project     = models.ForeignKey(Project, on_delete=models.CASCADE)
    image       = ImageWithThumbsField(upload_to='project-pictures', sizes=((125,125),(200,200)))
    #image       = models.ImageField(upload_to='project-pictures')
    comment     = models.CharField(max_length=60, blank=True)
    
    def __str__(self):
        return self.comment
    
    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Project_image.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Project_image, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Project_image)
def Project_image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
    
    
class Reference(models.Model):
    resume       = models.ForeignKey(Resume, on_delete=models.CASCADE)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=60,blank=True)
    
    
    

    