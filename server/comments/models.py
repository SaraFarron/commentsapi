from django.db import models
from posts.models import Post


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    child_comments = models.ManyToManyField('Comment')

    def __str__(self):
        return f'comment under {self.post}'
