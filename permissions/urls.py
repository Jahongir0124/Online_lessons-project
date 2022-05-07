from django.urls import path
from . import views
urlpatterns = [
    path('teachers',views.Teachers.as_view(),name='teachers'),
]