from api.serializers.post_serializer import PostSerializers
from api.models import Post
from rest_framework import generics

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = None
