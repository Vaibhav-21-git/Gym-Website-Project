from django.db import models
from classes.models import Class

class Gallery(models.Model): 

    Filter_CHOICES =[
    ("buffet", "بوفه"), 
    ("gym", "محیط باشگاه"), 
    ]
    classes = Class.objects.all()
    for i in classes:
        Filter_CHOICES.append((str(i.title), str(i.title)),)

    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    display_filter_id = models.CharField(choices=Filter_CHOICES, max_length=200)
    def __str__(self):
        if not self.title:
            return str("تصویر شماره " + str(self.id))
        else:
            return self.title 

    class Meta:
        verbose_name_plural = "تصاویر"


