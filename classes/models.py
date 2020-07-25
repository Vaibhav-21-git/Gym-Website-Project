from django.db import models
from datetime import datetime
from coaches.models import Coach
from django.db.models.signals import post_save

class Class(models.Model):
    class Time(models.TextChoices):
            time_1 = '10:00-14:00', "10:00-14:00"
            time_2 = '14:00-16:00', "14:00-16:00"
            time_3 = '16:00-18:00', "16:00-18:00"
            time_4  = '18:00-20:00', "18:00-20:00"
            time_5 = '20:00-22:00', "20:00-22:00"
            closed = 'تعطیل', "تعطیل"

    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    workout_type = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='classes/presence_classes/%Y/%m/%d')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    is_published = models.BooleanField(default=True)
    sunday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="یکشنبه")
    monday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="دوشنبه")
    tuesday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="سه شنبه")
    wednesday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="چهارشنبه")
    thursday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="پنجشنبه")
    friday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="جمعه")
    saturday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="شنبه")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "کلاس های حضوری"


class PrivateOnlineClass(models.Model):

    class Time(models.TextChoices):
            time_1 = '10:00-14:00', "10:00-14:00"
            time_2 = '14:00-16:00', "14:00-16:00"
            time_3 = '16:00-18:00', "16:00-18:00"
            time_4  = '18:00-20:00', "18:00-20:00"
            time_5 = '20:00-22:00', "20:00-22:00"
            closed = 'افلاین', "افلاین"

    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    workout_type = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='classes/private_online_classes/%Y/%m/%d')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    is_published = models.BooleanField(default=True)
    sunday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="یکشنبه")
    monday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="دوشنبه")
    tuesday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="سه شنبه")
    wednesday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="چهارشنبه")
    thursday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="پنجشنبه")
    friday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="جمعه")
    saturday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="شنبه")

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "کلاس های انلاین خصوصی"


class PublicOnlineClass(models.Model):

    class Time(models.TextChoices):
            time_1 = '10:00-14:00', "10:00-14:00"
            time_2 = '14:00-16:00', "14:00-16:00"
            time_3 = '16:00-18:00', "16:00-18:00"
            time_4  = '18:00-20:00', "18:00-20:00"
            time_5 = '20:00-22:00', "20:00-22:00"
            closed = 'افلاین', "افلاین"

    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    workout_type = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='classes/public_online_classes/%Y/%m/%d')
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    sunday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="یکشنبه")
    monday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="دوشنبه")
    tuesday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="سه شنبه")
    wednesday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="چهارشنبه")
    thursday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="پنجشنبه")
    friday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="جمعه")
    saturday = models.CharField(max_length=100,choices=Time.choices, default=Time.closed,verbose_name="شنبه")

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "کلاس های انلاین عمومی"


    
def set_presence_classes(sender, instance, created, *args, **kwrags):
    qs = Coach.objects.filter(id=instance.coach.id)
    if str(instance.title) not in qs[0].classes:
            presence_classes = str(instance.title) + "\n" + qs[0].classes
            qs.update(classes = presence_classes)
post_save.connect(set_presence_classes,sender=Class)     


def set_private_online_classes(sender, instance, created, *args, **kwrags):
    qs = Coach.objects.filter(id=instance.coach.id)
    if str(instance.title) not in qs[0].classes:
            presence_classes = str(instance.title) + "\n" + qs[0].classes
            qs.update(classes = presence_classes)
post_save.connect(set_private_online_classes,sender=PrivateOnlineClass)  


def set_public_online_classes(sender, instance, created, *args, **kwrags):
    qs = Coach.objects.filter(id=instance.coach.id)
    if str(instance.title) not in qs[0].classes:

            presence_classes = str(instance.title) + "\n" + qs[0].classes
            qs.update(classes = presence_classes)
post_save.connect(set_public_online_classes,sender=PublicOnlineClass)  