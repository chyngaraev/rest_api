from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),

    path('<int:pk>/delete/', PostDelete.as_view(), name= 'post_delete'),

    path('', PostList.as_view(), name = 'post_detail'),

    path('<int:pk>/', PostDetail.as_view(), name = 'post_detail'),

    path('comment/', PostCommentListView.as_view(), name='comment_list'),

    path('comment/<int:pk>/', PostCommentDetailView.as_view(), name = 'comment_detail'),

    path('comment/create/', PostCommentCreateView.as_view(), name = 'comment_create'),

    path('comment/<int:pk>/delete', PostCommentDeleteView.as_view(), name = 'comment_delete'),



# path('create/', PostCreate.as_view(), name='post_create'),



]