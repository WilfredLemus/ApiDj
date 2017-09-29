from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Video


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

class VideoSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)
  class Meta:
    model = Video
    fields = ('id', 'title', 'description', 'user')