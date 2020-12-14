from django.db import models

# Create your models here.

class Tweets (models.Model):
    tweet_id = models.IntegerField()
    tweet_time = models.TextField()
    tweet_text = models.TextField()

    def __str__(self):
        return self.tweet_text