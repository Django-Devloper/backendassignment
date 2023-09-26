from api.serializers.post_serializer import PostSerializers
from api.models import Post
from rest_framework import generics

class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
