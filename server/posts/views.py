from rest_framework.views import APIView
from .models import Post
from rest_framework.response import Response


class CreatePost(APIView):
    def post(self, request):
        post = Post.objects.create(
            title=request.title
        )
        post.save()
        return Response(status=200)


class GetPosts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        # serializer
        return Response(status=200)
