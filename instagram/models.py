from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    bio = HTMLField()
    profile_pic = ImageField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)


    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

class Image(models.Model):
    img = ImageField(manual_crop ='1080x1080')
    img_name = models.CharField(max_length= 30)
    img_caption = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def newsfeed(cls):
        images = cls.objects.all()
        return images

    # @classmethod
    # def search_by_user(cls,search_term):
    #     user = cls.objects.filter(title__icontains=search_term)
    #     return user

