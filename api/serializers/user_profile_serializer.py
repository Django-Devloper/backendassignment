from rest_framework import serializers
from api.serializers.user_serializer import UserSerializer
from api.models import Post


class UserProfileSerializers(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    class Meta:
        model=Post
        fields=["created_by","title","content"]
