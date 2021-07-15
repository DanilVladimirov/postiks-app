from rest_framework import serializers
from postsapp.models import Post, Comments


class PostSerializer(serializers.ModelSerializer):
    amount_of_upvotes = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        extra_kwargs = {"publication": {"required": False}}
