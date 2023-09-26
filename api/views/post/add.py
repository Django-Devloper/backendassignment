from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers.post_serializer import PostSerializers
from api.models import Post

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializers

    def perform_create(self, serializer):
        user = self.request.user.id
        serializer.save(
            created_by_id=user
        )
