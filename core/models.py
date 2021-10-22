# from functools import _Descriptorp
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Poster(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True,upload_to='poster')

    def __str__(self):
        return self.title

# class Poster(models.Model):
#     id=models.CharField(max_length=255,null=True,blank=True)
#     first_name_and_second_name=models.TextField(null=True,blank=True)
#     age=models.CharField(null=True,blank=True)
#     gender=models.CharField(null=False)

#     def __str__(self):
#         return self.first_name_and_second_name