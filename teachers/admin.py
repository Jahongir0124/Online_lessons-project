from django.contrib import admin
from . import models
from .models import *

admin.site.register(Teacher)
admin.site.register(Lessons)

