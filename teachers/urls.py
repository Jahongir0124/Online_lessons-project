from django.urls import path
from .  import views
urlpatterns = [
    path('',views.ShowLessons.as_view(),name='homepage'),
    path('techerSignUp',views.TeacherCreate.as_view(),name='teacherCreate'),
    path('teacherProfile',views.TeacherProfile.as_view(),name='teacherProfile'),
    path('teacherDownloadLesson',views.TeacherDownloadLesson.as_view(),name='teacherDownloadLesson'),
]