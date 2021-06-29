from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('my-blog/', views.my_blog, name='my-blog'),
    path('latest-post/', views.latest_post, name='latest-post'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
  # path('post/<int:pk>/profile/', PostDetailView.as_view(template_name='blog/post_profile.html'), name='post-profile'),
]

