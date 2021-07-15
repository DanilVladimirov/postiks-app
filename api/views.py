from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from postsapp.models import Post, Comments
from django.http import Http404
from api.serializers import PostSerializer, CommentsSerializer
from rest_framework import status


@api_view(["GET"])
def api_overview(request, format=None):
    api_urls = {
        "Delete, Update and Get the post": "/post/< id >/",
        "Create post": reverse("post-create", request=request, format=format),
        "View all posts": reverse("posts-all", request=request, format=format),
        "Comments of post": "/post/< id >/comments/",
        "Create comment": reverse("comment-add", request=request, format=format),
        "Delete, Update and Get the comment": "comment/< id >/",
    }

    return Response(api_urls)


class CommentsOfPost(APIView):
    def get(self, request, pid):
        post = Post.objects.get(id=pid)
        comments = post.comment.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)


class AddComment(APIView):
    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetails(APIView):
    def get_object(self, cid):
        try:
            return Comments.objects.get(id=cid)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, cid, format=None):
        comment = self.get_object(cid)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, cid, format=None):
        comment = self.get_object(cid)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cid, format=None):
        comment = self.get_object(cid)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCreate(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetails(APIView):
    def get_object(self, pid):
        try:
            return Post.objects.get(id=pid)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pid, format=None):
        post = self.get_object(pid)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pid, format=None):
        post = self.get_object(pid)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pid, format=None):
        post = self.get_object(pid)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
