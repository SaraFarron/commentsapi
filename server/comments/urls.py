from django.urls import path
from . import views


urlpatterns = [
    path('add', views.AddComment.as_view(), name='add_comment'),
    path('all', views.GetComments.as_view(), name='get_comments'),
]
