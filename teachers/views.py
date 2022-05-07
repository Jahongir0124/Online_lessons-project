from django.contrib.auth import authenticate
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from . models import *
from .serializer import *
from rest_framework.permissions import *
import json


class ShowLessons(APIView):
    teachers = Teacher.objects.all()
    a = []
    for i in teachers:
        a.append(i)
    def get(self,request):
        snippets = Lessons.objects.all()
        serializer = LessonSerializer(snippets, many=True)
        return Response(serializer.data)


class TeacherCreate(APIView):
    serializer_class =  CreateTeacher

    @swagger_auto_schema(request_body=CreateTeacher)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        return Response({
            "user created Sucsess"

        })



class TeacherProfile(APIView):
    serializer_class = TeacherProfile
    permission_classes = [IsAuthenticated]
    def get(self,request):
        teacher = Teacher.objects.filter(user=request.user)
        if teacher:
            teach = Teacher.objects.get(user=request.user)
            b_lesson = Lessons.objects.filter(teacher=teach)
            a = []
            for i in b_lesson:
                a.append(i.lesson_name)
            return Response({'lesson': a})
        else:
            return Response({'No logged'})



class TeacherDownloadLesson(APIView):
    serializer_class = TeacherDownloadLessonSerializer
    @swagger_auto_schema(request_body=TeacherDownloadLessonSerializer)
    def post(self, request):
        teacher = Teacher.objects.filter(user=request.user)
        serializer = self.serializer_class(data=request.data)
        print(request.FILES)
        serializer.is_valid(raise_exception=True)
        if teacher:
            teach = Teacher.objects.get(user=request.user)
            if teach.permision:
                print(serializer.data)
                creat = Lessons.objects.create(
                    teacher_id=serializer.data['teacher'],
                    lesson_name=serializer.data['lesson_name'],
                    image=request.FILES['image'],
                    video_file=request.FILES['video_file'],
                    description=serializer.data['description']
                )
                return Response({'Success'})
            else:
                return Response({'Failed'})
        else:
            return Response('No logged')