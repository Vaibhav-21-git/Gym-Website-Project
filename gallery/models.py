from django.db import models


class Gallery(models.Model): 
    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    display_filter_id = models.IntegerField(default=1)
    def __str__(self):
        if not self.title:
            return str("تصویر شماره " + str(self.id))
        else:
            return self.title 

    class Meta:
        verbose_name_plural = "تصاویر"


