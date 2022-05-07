from django.urls import path
from . import views
urlpatterns = [
    path('',views.PupilView.as_view(),name='pupil'),
    path('pupilProfile',views.PupilProfile.as_view(),name='pupilProfile'),
    path('buy_lesson',views.Buy_lessonView.as_view(),name='buy_lesson'),

]