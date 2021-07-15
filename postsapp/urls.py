from django.urls import path
from postsapp.views import (StartPageView,
                            CreatePostView,
                            add_post,
                            add_comment,
                            del_post,
                            UsersPostView,
                            ChangePostView,
                            PagePostView,
                            vote_post,)

urlpatterns = [
    path('', StartPageView.as_view(), name='start-page'),
    path('add_post/', add_post, name='add-post'),
    path('add_comment/', add_comment, name='add-comment'),
    path('create_post/', CreatePostView.as_view(), name='create-post-page'),
    path('del_post/', del_post, name='del-post'),
    path('my_posts/', UsersPostView.as_view(), name='users-post-page'),
    path('edit_post/<int:pid>/', ChangePostView.as_view(), name='edit-post-page'),
    path('post/<int:pid>/', PagePostView.as_view(), name='post-page'),
    path('vote_post/', vote_post, name='vote-post')
]
