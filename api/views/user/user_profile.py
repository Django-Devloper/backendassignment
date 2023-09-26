from api.models import Post
from api.serializers.user_profile_serializer import UserProfileSerializers
from rest_framework import generics


class UserProfileView(generics.ListAPIView):
    serializer_class = UserProfileSerializers
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(created_by=user)