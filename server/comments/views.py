from rest_framework.views import APIView
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class Comments(APIView):
    def get(self, request):
        title = request.data.get('title')
        try:
            post = Post.objects.get(title=title)
        except ValueError:
            return Response(
                {'error': f'не существует статьи {title}'},
                status=404)
        try:
            comments = Comment.objects.filter(post=post)
        except ObjectDoesNotExist:
            return Response({}, status=200)
        serializer = CommentSerializer(data=comments, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)

    def post(self, request):
        title = request.data.get('title')
        try:
            post = Post.objects.get(title=title)
        except ValueError:
            return Response(
                {'error': f'не существует статьи {title}'},
                status=404)
        if post in Post.objects.all():
            comment = Comment.objects.create(
                text=request.data.get('text'),
                post=post)
            comment.save()
            return Response(status=200)
        else:
            return Response(
                {'error': fr'не существует статьи "{request.data.get("title")}"'},
                status=404)
