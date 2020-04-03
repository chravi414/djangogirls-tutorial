from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts', views.post_list, name='post_list'),
    path('posts/<int:id>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_new, name='post_new'),
    path('posts/edit/<int:id>', views.post_edit, name='post_edit')
]
