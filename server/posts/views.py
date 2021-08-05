from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class Posts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(data=posts, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)

    def post(self, request):
        post = Post.objects.create(
            title=request.data.get('title')
        )
        post.save()
        return Response(status=200)
