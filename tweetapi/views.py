from django.shortcuts import render
from django.http import HttpResponse
import requests
from .apicalls import *
import django_rq
# Create your views here.

def TweetView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(tweet_call)
    return render(request, 'tweetapi/tweet.html',{'title':'Tweets'})
    