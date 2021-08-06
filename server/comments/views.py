from rest_framework.views import APIView
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class Comments(APIView):
    def get(self, request):
        post_id = request.data.get('post')
        try:
            post = Post.objects.get(id=post_id)
        except ObjectDoesNotExist:
            return Response(
                {'error': f'не существует статьи {post_id}'},
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
        post_id = request.data.get('post')
        comment_id = request.data.get('comment')
        try:
            post = Post.objects.get(id=post_id)
            comment = Comment.objects.create(
                text=request.data.get('text'),
                post=post)
            comment.save()
            return Response(status=200)
        except ObjectDoesNotExist:
            parent_comment = Comment.objects.get(id=comment_id)
            post = Post.objects.get(id=parent_comment.post.id)
            comment = Comment.objects.create(
                text=request.data.get('text'),
                post=post
            )
            comment.save()
            parent_comment.child_comments.add(comment)
            parent_comment.save()
            return Response(status=200)
        except ValueError:
            return Response(
                {'error': f'не существует статьи/комментария {post_id}/{comment_id}'},
                status=404)
