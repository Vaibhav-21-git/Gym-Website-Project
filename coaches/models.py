from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Coach(models.Model):
    name = models.CharField(max_length=200)
    account = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    photo = models.ImageField(upload_to='coaches/%Y/%m/%d')
    live_stream_link = models.URLField(blank=True, null=True)
    classes = models.CharField(max_length=1000,blank=True)   
    info_1 = models.CharField(max_length=200,blank=True)
    info_2 = models.CharField(max_length=200,blank=True)
    info_3 = models.CharField(max_length=200,blank=True)
    info_4 = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[ MaxValueValidator(45), MinValueValidator(25)])
    height = models.IntegerField(validators=[ MaxValueValidator(230), MinValueValidator(160)])
    weight = models.DecimalField(decimal_places=2,max_digits=6,null=True)
    hire_date = models.DateField(default=datetime.now,blank=False)
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "مربیان"





