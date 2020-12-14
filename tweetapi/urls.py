from django.urls import path
from .views import TweetView

urlpatterns = [
    path('tweet',TweetView, name="tweetview"),    
]
