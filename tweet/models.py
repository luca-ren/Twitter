from django.db import models

# Create your models here.


class Tweet(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    tweet_owner = models.ForeignKey('auth.User', related_name='tweet_owner', on_delete=models.CASCADE)
    #comments = models.ForeignKey(Comment, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.CharField(max_length=250)
    comment_owner = models.ForeignKey('auth.User', related_name='comment_owner', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.message