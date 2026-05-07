from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status



@api_view()
def PostList(request):
    posts = Post.objects.filter(status=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view()
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)