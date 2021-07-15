from django.urls import path
from api.views import (PostsView,
                       PostCreate,
                       PostDetails,
                       api_overview,
                       CommentsOfPost,
                       AddComment,
                       CommentDetails)

urlpatterns = [
    path('', api_overview, name='api_overview'),
    path('post_create/', PostCreate.as_view(), name='post-create'),
    path('posts_all/', PostsView.as_view(), name='posts-all'),
    path('post/<int:pid>/', PostDetails.as_view(), name='post-details'),
    path('post/<int:pid>/comments/', CommentsOfPost.as_view(), name='comments-post'),
    path('add_comment/', AddComment.as_view(), name='comment-add'),
    path('comment/<int:cid>/', CommentDetails.as_view(), name='comment-details')
]
