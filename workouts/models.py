from django.db import models
from datetime import datetime


class Workouts(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     rule = models.CharField(max_length=20)
     image = models.ImageField(upload_to='workout/workouts/%Y/%m/%d')

     def __str__(self):
        return self.title
    
     class Meta:
        verbose_name_plural = "تمرینات"



class Workout_List(models.Model):
    class Grade(models.TextChoices):
            grade1  = 'مبتدی', "مبتدی"
            grade2 = 'متوسط', "متوسط"
            grade3 = 'پیشرفته', "پیشرفته"

    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=200,choices=Grade.choices)
    image = models.ImageField(upload_to='workout/workout_list/%Y/%m/%d')
    selected_workouts = models.ManyToManyField(Workouts,blank=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "فهرست تمرینات"



    
        