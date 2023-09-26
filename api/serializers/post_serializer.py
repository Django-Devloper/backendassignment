from api.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['first_name', 'last_name']

class PostSerializers(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['user','title','content']
