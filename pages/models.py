from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

    
class CarouselBanner(models.Model):
     image = models.ImageField(upload_to='banners/carousel_banners/%Y/%m/%d')
     small_title = models.CharField(max_length=100, blank=True)
     normal_title_1 = models.CharField(max_length=100, blank=True)
     normal_title_2 = models.CharField(max_length=100, blank=True)
     normal_title_3 = models.CharField(max_length=100, blank=True)
     highlighted_title_1 = models.CharField(max_length=100, blank=True)
     highlighted_title_2 = models.CharField(max_length=100, blank=True)   
     highlighted_title_3 = models.CharField(max_length=100, blank=True)

     def __str__(self):
        return str(self.id)
     class Meta:
        verbose_name_plural = "بنر های خانه"  


class Banner(models.Model):

    class Pages(models.TextChoices):
            page_1 = 'presence_class', "کلاس های حضوری"
            page_2 = 'online_private_class', "کلاس های انلاین خصوصی"
            page_3 = 'online_public_class', "کلاس های انلاین عمومی"
            page_4  = 'beginner_workouts', "تمرینات سطح مبتدی"
            page_5 = 'intermediate_workouts', "تمرینات سطح متوسط"
            page_6 = 'advanced_workouts', "تمرینات سطح پیشرفته"
            page_7 = 'our_team', "تیم ما"
            page_8 = 'gallery', "گالری"
            page_9 = 'contact_us', "ارتباط با ما"
            page_10 = 'profile', "پروفایل کاربری"
            page_11 = 'online_private_class_details', "جزئیات کلاس انلاین خصوصی"
            page_12 = 'online_public_class_details',"جزئیات کلاس انلاین عمومی"
            page_13 = 'presence_class_details',"جزئیات کلاس حضوری"
            
    
    image = models.ImageField(upload_to='banners/pages_banners/%Y/%m/%d')
    title = models.CharField(max_length=100)
    page = models.CharField(max_length=100,choices=Pages.choices,unique=True)
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = "بنر ها"     


class Honors(models.Model):
    image = models.ImageField(upload_to='honors/%Y/%m/%d')
    description = models.TextField()
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "افتخارت باشگاه"     

