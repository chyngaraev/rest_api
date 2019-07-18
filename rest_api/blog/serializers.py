from rest_framework import serializers
from .models import Post, PostComments


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user_name', 'title', 'content', 'image', 'created_at', 'updated_at')
        model = Post

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','user', 'post', 'content_comment','image_comment','create_at','update_at')
        model = PostComments