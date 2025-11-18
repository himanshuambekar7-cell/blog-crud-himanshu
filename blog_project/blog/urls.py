from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('posts/', views.post_list, name='post_list'),  # all posts
    path('posts/create/', views.post_create, name='post_create'),  # create new post
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),  # edit post
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),  # delete post
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # view single post
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
