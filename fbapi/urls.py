from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('pageinfo',PageView, name="PageView"),
    path('postinfo',PostView, name="PostView"),
    path('commentsinfo',CommentView, name="CommentView"),
    path('page/',PageCollection.as_view()),
    path('page/<int:pk>',PageDetail.as_view()),
    path('posts/',PostsCollection.as_view()),
    path('posts/<int:pk>',PostsDetail.as_view()),
    path('comment/',CommentCollection.as_view()),
    path('comment/<int:pk>',CommentDetail.as_view()),
]