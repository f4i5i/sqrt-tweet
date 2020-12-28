from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('pageinfo',PageView, name="PageView"),
    path('postinfo',PostView, name="PostView"),
]