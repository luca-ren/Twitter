from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Tweet, Comment, CommentLike, TweetLike
from django.contrib.auth.models import User


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment_owner = serializers.ReadOnlyField(source='comment_owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'url', 'message', 'comment_owner', 'tweet', 'comments_liked_by')


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    tweet_owner = serializers.ReadOnlyField(source='tweet_owner.username')

    class Meta:
        model = Tweet
        fields = ('id', 'url', 'title', 'message', 'tweet_owner', 'comments', 'tweets_liked_by')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'tweet_owner', 'comment_owner', 'comment_like_owner', 'tweet_like_owner')


class CommentLikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CommentLike
        fields = ('id', 'url', 'comment_like_owner', 'comment')


class TweetLikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TweetLike
        fields = ('id', 'url', 'tweet_like_owner', 'tweet')