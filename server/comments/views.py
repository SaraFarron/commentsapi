from rest_framework.views import APIView
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


class Comments(APIView):
    def get(self, request):
        post_id = request.data.get('post')
        comment_id = request.data.get('comment')
        try:
            post = Post.objects.get(id=post_id)
            comments = Comment.objects.filter(post=post)

        except ObjectDoesNotExist:
            try:
                comments = Comment.objects.get(id=comment_id).child_comments
            except ObjectDoesNotExist:
                return Response(
                    {'error': f'не существует комментария {comment_id}'},
                    status=404)

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
            try:
                parent_comment = Comment.objects.get(id=comment_id)

            except ObjectDoesNotExist:
                return Response(
                    {'error': f'не существует комментария {comment_id}'},
                    status=404)
            comment = Comment.objects.create(
                text=request.data.get('text'),
                post=None
            )
            comment.save()
            parent_comment.child_comments.add(comment)
            parent_comment.save()
            return Response(status=200)

        except ValueError:
            return Response(
                {'error': f'не существует статьи {post_id} или комментария {comment_id}'},
                status=404)

        except IntegrityError:
            return Response(
                {'error': 'укажите text в теле запроса'},
                status=400)
