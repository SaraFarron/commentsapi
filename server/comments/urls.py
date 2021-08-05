from django.urls import path
from . import views


urlpatterns = [
    path('', views.Comments.as_view(), name='add_comment'),
]
