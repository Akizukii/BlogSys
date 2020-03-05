from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('category/<int:category_id>', views.category, name='category'),
    path('reply/comment/<int:comment_id>', views.reply_comment, name='reply'),
    path('tt/', views.tt, name='tt'),
]