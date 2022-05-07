from django.contrib.auth.models import User
from django.db import models
from teachers.models import *
# Create your models here.


class Pupil(models.Model):
    pupil = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)


    def __str__(self):
        return self.pupil.username

    class Meta:
        verbose_name = "O'quvchilar ro'yxati"
        verbose_name_plural = "O'quvchilar"
class Buy_lessons(models.Model):
    user = models.ForeignKey(Pupil,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lessons,on_delete=models.CASCADE)
    buy_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson.lesson_name

    class Meta:
        verbose_name = "Xarid qilingan darslar ro'yxati"
        verbose_name_plural = "Xarid qilingan darslar"
class Profile(models.Model):
    pass