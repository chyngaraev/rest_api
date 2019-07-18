from rest_framework.permissions import BasePermission
from .models import Post, PostComments

class IsPostOwner(BasePermission):
    def has_permission(self, request, view):
        post = Post.objects.get(pk=view.kwargs['pk'])
        if 'pk' not in view.kwargs:
            return False
        if post.user_name == request.user:
            return True

class IsCommentOwner(BasePermission):
    def has_permission(self, request, view):
        comment = PostComments.objects.get(pk=view.kwargs['pk'])
        if 'pk' not in view.kwargs:
            return False
        if comment.user == request.user:
            return True