from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Tweet, Comment
from .serializers import TweetSerializer, UserSerializer, CommentSerializer
from django.contrib.auth.models import User

# Create your views here.


class TweetView(viewsets.ModelViewSet):

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(tweet_owner=self.request.user)

class CommentView(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(comment_owner=self.request.user)

class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


