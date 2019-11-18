from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Profile(models.Model):
    bio = models.TextField()
    profile_pic = ImageField( blank = True)
