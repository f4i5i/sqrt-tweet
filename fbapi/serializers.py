from rest_framework import serializers
from .models import *

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

