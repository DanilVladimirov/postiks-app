import json
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from postsapp.forms import PostCreateForm
from postsapp.models import Post, Comments
from django.contrib import messages
from django.db.models import Count


class StartPageView(View):
    template_name = 'postsapp/start-page.html'

    def get(self, request, *args, **kwargs):
        context = {}
        posts = Post.objects.annotate(count=Count('users_upvotes')).order_by('-count')
        context.update({'posts': posts})
        return render(request, self.template_name, context)


class CreatePostView(View):
    template_name = 'postsapp/create-post-page.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        context = {}
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.author = request.user
            instance.save()
            messages.success(request, 'Created !')
            return redirect('start-page')
        else:
            messages.error(request, 'Error while creating post, check if all fields are filled')
        return render(request, self.template_name, context)


class UsersPostView(View):
    template_name = 'postsapp/users-post-page.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        posts = request.user.post.order_by('-date')
        context = {'posts': posts}
        return render(request, self.template_name, context)


class PagePostView(View):
    template_name = 'postsapp/post-page.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['pid'])
        context = {'post': post}
        return render(request, self.template_name, context)


class ChangePostView(View):
    template_name = 'postsapp/post-edit-page.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['pid'])
        if request.user == post.author:
            context = {'post': post}
            return render(request, self.template_name, context)
        else:
            messages.error(request, 'Access denied')
            return redirect('start-page')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        context = {}
        post = Post.objects.get(id=self.kwargs['pid'])
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited :)')
            return redirect('users-post-page')
        else:
            context.update({'form': form})
        return render(request, self.template_name, context)


@login_required
def add_post(request):
    if request.POST:
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.author = request.user
            instance.save()

            data_response = {
                'success': True,
                'title': instance.title,
                'link': instance.link,
                'date': instance.date.strftime('%Y-%m-%d %H:%M'),
                'post_id': instance.id,
                'username': instance.author.username,
            }
        else:
            data_response = {'success': False}
        return HttpResponse(json.dumps(data_response, cls=DjangoJSONEncoder), content_type='application/json')


@login_required
def add_comment(request):
    if request.POST:
        post = Post.objects.get(id=request.POST.get('postid'))
        comm = Comments.objects.create(author=request.user,
                                       text=request.POST.get('comment'),
                                       post=post)
        comm.save()
        data_response = {'success': True,
                         'date': comm.date.strftime('%Y-%m-%d %H:%M')}
        return HttpResponse(json.dumps(data_response, cls=DjangoJSONEncoder), content_type='application/json')


@login_required
def del_post(request):
    if request.POST:
        post = Post.objects.get(id=request.POST.get('postid'))
        post.delete()
        data_response = {'success': True}
        return HttpResponse(json.dumps(data_response), content_type='application/json')


@login_required
def vote_post(request):
    if request.POST:
        data_response = {}
        post = Post.objects.get(id=request.POST.get('postid'))
        if request.user in post.users_upvotes.all():
            post.users_upvotes.remove(request.user)
            data_response.update({'success': False})
        else:
            post.users_upvotes.add(request.user)
            data_response.update({'success': True})
        return HttpResponse(json.dumps(data_response), content_type='application/json')
