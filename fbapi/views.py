from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from .apicalls import *
import django_rq
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import PageSerializer, PostSerializer, CommentSerializer


# Create your views here.

def PageView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(page_info)
    return HttpResponse("Simple Page Name and Fan Count APi Call..........")

def PostView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(post_info)
    return HttpResponse("Posts Data Fetching..........")

def CommentView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(comment_info)
    return HttpResponse("Comments Data Fetching..........")


class PageCollection(APIView):

    def get(self, request):
        items = Page.objects.all()
        serializer = PageSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Pageserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PageDetail(APIView):

    def delete(self,request, pk):
        item = Page.objects.all(id=pk)
        item.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item = Page.objects.all(id=pk)
        serializer = PageSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsCollection(APIView):

    def get(self, request):
        items = Posts.objects.all()
        serializer = PostSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsDetail(APIView):

    def delete(self,request, pk):
        item = Posts.objects.all(id=pk)
        item.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item = Posts.objects.all(id=pk)
        serializer = PostSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentCollection(APIView):

    def get(self, request):
        items = Comments.objects.all()
        serializer = CommentSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def delete(self,request, pk):
        item = Comments.objects.all(id=pk)
        item.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item = Comments.objects.all(id=pk)
        serializer = commentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class PageApiView(LoginRequiredMixin, generics.ListAPIView):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer

# class PostsApiView(LoginRequiredMixin, generics.ListAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer

# class CommentsApiView(LoginRequiredMixin, generics.ListAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSerializer