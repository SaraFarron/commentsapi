from rest_framework.views import APIView
from posts.models import Post
from .models import Comment
from rest_framework.response import Response


class GetComments(APIView):
    def get(self, request):
        if request.post in Post.objects.all():
            comments = Comment.objects.get(post=request.post)
            # serializer
            return Response(status=200)
        else:
            return Response({'error': f'не существует статьи "{request.post}"'}, status=404)


class AddComment(APIView):
    def post(self, request):
        if request.post in Post.objects.all():
            comment = Comment.objects.create(
                text=request.text,
                post=request.post
            )
            comment.save()
            return Response(status=200)
        else:
            return Response({'error': f'не существует статьи "{request.post}"'}, status=404)
