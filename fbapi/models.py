from django.db import models

# Create your models here.

class Page(models.Model):
    page_id = models.IntegerField()
    page_name = models.TextField()
    page_fans= models.IntegerField()
    page_url = models.URLField()
    page_about = models.TextField()

    def __str__(self):
        return self.page_name

class Posts(models.Model):
    page_fid = models.ForeignKey(Page, related_name="pagefid",on_delete=models.PROTECT)
    post_id= models.CharField(max_length=1000,null=True)
    post_photo = models.URLField()
    post_message = models.TextField()
    post_permalink= models.URLField()
    post_likes_count= models.IntegerField()
    post_shares_count = models.IntegerField()
    post_reaction = models.IntegerField()
    post_time = models.TextField()

    def __str__(self):
        return self.post_id


class Comments(models.Model):
    comment_id= models.CharField(max_length=1000,null=True)
    comment_from = models.CharField(max_length=1000,null=True)
    posts_fid = models.ForeignKey(Posts, related_name="postsfid",on_delete=models.PROTECT)
    comment_message = models.TextField()
    comment_likes_count= models.IntegerField()
    comment_time = models.TextField()
    can_like = models.BooleanField()
    can_remove = models.BooleanField()
    comment_count = models.IntegerField()
    can_comment = models.BooleanField()
    is_private = models.BooleanField()
    is_hidden = models.BooleanField()
    can_hide = models.BooleanField()

    def __str__(self):
        return self.comment_message

class Replys(models.Model):
    reply_id= models.CharField(max_length=1000,null=True)
    reply_from = models.CharField(max_length=1000,null=True)
    comment_fid = models.ForeignKey(Comments, related_name="commentsfid",on_delete=models.PROTECT)
    reply_message = models.TextField()
    reply_reply= models.TextField()
    reply_likes_count= models.IntegerField()
    reply_reaction = models.IntegerField()
    reply_time = models.TextField()
    can_like = models.BooleanField()
    can_remove = models.BooleanField()
    comment_count = models.IntegerField()
    can_comment = models.BooleanField()
    is_private = models.BooleanField()
    is_hidden = models.BooleanField()
    can_hide = models.BooleanField()

    def __str__(self):
        return self.reply_message
