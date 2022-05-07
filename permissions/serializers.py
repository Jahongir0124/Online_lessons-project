from rest_framework import serializers
from teachers.models import *

class PermissionsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

