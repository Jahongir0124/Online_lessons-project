from rest_framework import serializers
from rest_framework.exceptions import APIException

from .models import *


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['lesson_name','teacher','description','image']

    def to_representation(self, instance):
        repr = super(LessonSerializer, self).to_representation(instance)
        repr['image'] = '127.0.0.1:8000' + instance.image.url
        return repr


class CreateTeacher(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        if len(password) <= 4:
            raise APIException(detail='password min length should be more than 4 .')
        user = User.objects.create(
           **validated_data
        )
        user.set_password(password)
        user.save()
        teacher = Teacher.objects.create(user=user)
        return 'sdsds'

class Teachersserializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["user"]

class TeacherProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
class TeacherDownloadLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['teacher','lesson_name','image','video_file','description']