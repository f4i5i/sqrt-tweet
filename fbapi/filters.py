import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CommentFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "comment_time", lookup_expr='gte')
    end_date = DateFilter(field_name = "comment_time", lookup_expr='lte')

    class Meta():
        model = Comments
        fields = '__all__'
        exclude = ['comment_id','comment_from','can_like','can_like','can_remove','is_private','is_hidden','can_hide',
                    'is_spam','remaning','completed','can_comment','comment_count','comment_likes_count','comment_time','page_fid', 'posts_fid','comment_message']
        