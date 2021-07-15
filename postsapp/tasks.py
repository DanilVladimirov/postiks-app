from celery import shared_task
from postsapp.models import Post


@shared_task(name="clear_upvotes")
def clear_upvotes():
    for post in Post.objects.all():
        post.users_upvotes.clear()
    return 'upvotes cleared !'
