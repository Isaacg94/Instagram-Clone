from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Profile(models.Model):
    bio = models.TextField()
    profile_pic = ImageField( blank = True)

class Image(models.Model):
    img = ImageField( blank = True, manual_crop = '1080x1080')
    img_name = models.CharField(max_length= 30)
    img_caption = models.TextField()
    profile = models.ForeignKey(Profile)
