from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name = 'list'),
]
