from django.shortcuts import render
from django.http import HttpResponse
import requests
from .apicalls import *
import django_rq

# Create your views here.
def PageView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(page_info)
    return HttpResponse("Simple Page Name and Fan Count APi Call..........")

def PostView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(post_info)
    return HttpResponse("Posts Data Fetching..........")