from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import requests
from .apicalls import *
from .tasks import *
import django_rq
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.schemas import AutoSchema
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .filters import *
from .forms import FbProfileForm
from .models import *
from .serializers import PageSerializer, PostSerializer, CommentSerializer


# Create your views here.

def PageView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(pageData)
    return HttpResponse("Simple Page Name and Fan Count APi Call..........")

def PostView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(postData)
    return HttpResponse("Posts Data Fetching..........")

def CommentView(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(CommData)
    return HttpResponse("Comments Data Fetching..........")


class PageCollection(GenericAPIView):
    serializer_class = PageSerializer
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            items = Page.objects.all()
            page_serializer = PageSerializer(items, many=True)
            return JsonResponse(page_serializer.data, safe=False)
    
    def post(self, request):
        page_serializer = PageSerializer(data=request.data)
        if page_serializer.is_valid():
            page_serializer.save()
            return Response(page_serializer.data, status=status.HTTP_201_CREATED)
        return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PageDetail(GenericAPIView):
    serializer_class = PageSerializer
   
    def delete(self,request, pk):
        item = Page.objects.get(id=pk)
        item.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item = Page.objects.get(id=pk)
        page_serializer = PageSerializer(item, data=request.data)
        if page_serializer.is_valid():
            page_serializer.save()
            return Response(page_serializer.data)
        return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsCollection(GenericAPIView):
    serializer_class = PostSerializer
    def get(self, request):

        """ List all Post, or Create a New Post """
        if request.method == 'GET':
            items = Posts.objects.all()
            print(items)
            post_serializer = PostSerializer(items, many=True)
            return Response(post_serializer.data)
    
    def post(self, request):
        """ 
        To Create New Post
        ---
        """
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsDetail(GenericAPIView):
    serializer_class = PostSerializer

    def delete(self,request, pk):
        item = Posts.objects.filter(page_fid=pk)
        item.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item = Posts.objects.filter(id=pk)
        serializer = PostSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentCollection(GenericAPIView):
    serializer_class = CommentSerializer
    filter_fields = ('comment_id','posts_fid')

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


class CommentDetail(GenericAPIView):
    serializer_class = CommentSerializer

    def delete(self,request, pk):
        item = Comments.objects.filter(id=pk)
        item.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item = Comments.objects.filter(id=pk)
        serializer = CommentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
def CommentFillter(request):
    print(request.user)
    userid = FbProfile.objects.get(user=request.user)
    page = Page.objects.get(fbU_fid=userid.id)
    print(userid)
    print(page.page_id)
    comments = Comments.objects.filter(page_fid=page)

    myFilter = CommentFilter(request.GET, queryset=comments)
    comments = myFilter.qs
    context = {'myFilter': myFilter, 'comments':comments}
    return render (request, 'fbapi/comments.html', context)

@login_required
def FbProfileView(request):
    if request.method == 'POST':
        form = FbProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FbProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'fbapi/pageConnecting.html', context)

@login_required
def PageSelectView(request):
    info = FbProfile.objects.get(user=request.user)
    uid = info.FbuserId
    utok = info.Fbusertoken

    data = PageLink(uid,utok)
    print(data['data'])
    context = {
        'data': data['data'],
    }
    return render (request, 'fbapi/PageSelect.html', context)


# class PageApiView(LoginRequiredMixin, generics.ListAPIView):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer

# class PostsApiView(LoginRequiredMixin, generics.ListAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer

# class CommentsApiView(LoginRequiredMixin, generics.ListAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSerializer