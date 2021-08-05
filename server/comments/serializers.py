from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Comment


class CommentSerializer(ModelSerializer):
    post = StringRelatedField()

    class Meta:
        model = Comment
        fields = ['text', 'post']
