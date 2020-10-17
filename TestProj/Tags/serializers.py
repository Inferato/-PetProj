from rest_framework import serializers
from .User import User
from taggit.models import Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class UserTagSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'tags']
