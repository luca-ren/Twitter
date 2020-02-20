from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Tweet, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment_owner = serializers.ReadOnlyField(source='comment_owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'url', 'message', 'comment_owner', 'tweet')


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    tweet_owner = serializers.ReadOnlyField(source='tweet_owner.username')

    class Meta:
        model = Tweet
        fields = ('id', 'url', 'title', 'message', 'tweet_owner', 'comments')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username')