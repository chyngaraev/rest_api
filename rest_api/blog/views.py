from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from blog.forms import SignUpForm
from .models import Post, PostComments
from .serializers import PostSerializers, CommentSerializer
from .permissions import IsCommentOwner, IsPostOwner
from rest_framework.authentication import TokenAuthentication
from .pagination import ListPagination


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')
    else:
        form = SignUpForm
        return render(request, 'signup.html', {'form':form})

def mainUrl(request):
    return render(request, 'main.html', {})


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializers


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user_name', 'title')
    search_fields = ('user_name', 'post', 'content_comment')


class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsPostOwner,)


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsPostOwner,)


class PostCommentListView(generics.ListAPIView):
    pagination_class = ListPagination
    queryset = PostComments.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user', 'content_comment')
    search_fields = ('user', 'post_comments', 'content')


class PostCommentDetailView(generics.RetrieveUpdateAPIView):
    queryset = PostComments.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCommentOwner,)


class PostCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer


class PostCommentDeleteView(generics.DestroyAPIView):
    queryset = PostComments.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCommentOwner,)