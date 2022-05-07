from django.contrib.auth.models import User
from django.db import models
class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    permision = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    @property
    def url(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        verbose_name = 'Ustozllar royxati'
        verbose_name_plural = 'Ustozlar'
class Lessons(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='Dars ustozi',help_text='Dars ustozi')
    lesson_name = models.CharField(max_length=400,verbose_name='Dars nomi')
    video_file = models.FileField()
    image = models.ImageField()
    description = models.TextField(verbose_name='Dars haqida qisqacha')
    quentity = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lesson_name


    class Meta:
        verbose_name = 'On-line dars'
        verbose_name_plural = 'On-line darslar'
