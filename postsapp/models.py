from django.contrib.auth.models import User
from django.db import models
import datetime


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=200,
                             default='no-title')
    link = models.URLField(default='')
    date = models.DateTimeField(default=datetime.datetime.now)
    users_upvotes = models.ManyToManyField(User,
                                           related_name='votes',
                                           blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='post',
                               null=True)

    def __str__(self):
        return self.title

    def amount_of_upvotes(self):
        return self.users_upvotes.count()


class Comments(models.Model):
    text = models.TextField(default='no-text')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='u_comments',
                               null=True)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comment')
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.text[:10]}...'
