from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from teachers.models import Lessons, Teacher
from teachers.serializer import Teachersserializer
from .serializers import *

class Teachers(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = PermissionsAdminSerializer
    def get(self,request):
        teachers = Teacher.objects.all()
        teacher = []
        serializer = Teachersserializer(teachers,many=True)
        for tea in teachers:
            lesson = Lessons.objects.filter(teacher=tea)
            lessons = []
            for l in lesson:
                lessons.append(l.lesson_name)

            d = {
                'teacher':tea.url,
                'lessons':lessons
            }
            teacher.append(d)
        return Response(teacher)
    @swagger_auto_schema(request_body=PermissionsAdminSerializer)
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        #serializer.is_valid(raise_exception=True)
        teacher = Teacher.objects.filter(user=request.user)
        data = request.data['user']
        print(data)
        if teacher:
            teach = Teacher.objects.get(user=data)
            print(teach.permision)
            teach.permision = True
            teach.save()
            return Response({'Succsess'})
        else:
            return Response({'No Teacher'})

