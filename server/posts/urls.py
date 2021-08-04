from django.urls import path
from . import views


urlpatterns = [
    path('create', views.CreatePost.as_view(), name='create_post'),
    path('all', views.GetPosts.as_view(), name='get_posts'),
]
