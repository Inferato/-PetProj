from django.http import Http404
from rest_framework import permissions
from .permisisons import IsOwnerOrReadOnly, IsCompanyAdmin
from rest_framework import generics
from .User import User
from taggit.models import Tag
from .serializers import UserSerializer, TagsSerializer, UserTagSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsCompanyAdmin]


class Tags(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsCompanyAdmin]


class TagsList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class UserTag(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

