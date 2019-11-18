from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Profile(models.Model):
    bio = models.TextField()
    profile_pic = ImageField( blank = True)

class Image(models.Model):
    img = models.ImageField(upload_to='feed/')
    img_name = models.CharField(max_length= 30)
    img_caption = models.TextField()
    profile = models.ForeignKey(Profile)
