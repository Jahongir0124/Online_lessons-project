from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.permissions import *


class PupilView(APIView):
    def get(self,request):
        return Response({'salom':'brat'})

    serializer_class = PupilSerializer

    @swagger_auto_schema(request_body=PupilSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        return Response({
            "pupil created Sucsess"

        })

class PupilProfile(APIView):
    serializer_class = PupilProfileSeriializer
    @swagger_auto_schema(request_body=PupilProfileSeriializer)
    def post(self,request):
        username = request.data['username']
        pas = request.data['password']
        user = authenticate(username=username,password=pas)
        try:
            pupils = Pupil.objects.get(pupil=user)
            if pupils:
                b_lesson = Buy_lessons.objects.filter(user=pupils)
                a = []
                for i in b_lesson:
                    a.append(i.lesson.lesson_name)

                return Response({'lesson':a})
            else:
                return Response(request.data)
        except Exception as e:
            pass

class Buy_lessonView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Buy_LessonSerializer
    @swagger_auto_schema(request_body=Buy_LessonSerializer)
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        lesson = Lessons.objects.get(pk=serializer.data['lesson'])
        print(type(serializer.data['lesson']))
        order = Buy_lessons.objects.create(
            user_id=serializer.data['user'],
            lesson_id=serializer.data['lesson']
        )
        lesson.quentity+=1
        lesson.save()
        return Response({'Ordered Succesful'})



