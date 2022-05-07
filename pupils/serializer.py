from django.contrib.auth.models import User
from rest_framework import serializers

from pupils.models import *


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    def create(self, validated_data):
        password = validated_data['password']
        user = User.objects.create(
            **validated_data
        )
        user.set_password(password)
        user.save()
        pupil = Pupil.objects.create(pupil=user)
        return ''

class PupilProfileSeriializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class Buy_LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy_lessons
        fields = '__all__'