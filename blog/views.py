from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   # <app>/<model>_<viewType>.html
    context_object_name = 'posts'
    ordering = ['-dat_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/post_profile.html'   # <app>/<model>_<viewType>.html
    context_object_name = 'posts'
    ordering = ['-dat_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


def PostDetail(request, pk):
    post = Post.objects.get(id=pk)
    current_logged_in_user = request.user
    comments_list = Comment.objects.filter(blog=post).order_by('-date_added')
    # comments_list = list(comments_list.values())

    post_num = pk

    if request.method == 'GET':
        form = CommentForm()

    # The below if statement handles multiple forms seperatly
    # the like buttons and comment form
    if request.method == 'POST':

        if 'comment_button' in request.POST:

            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.commentator = current_logged_in_user
                new_comment.blog = post
                new_comment.save()
                return redirect('post-detail', pk=post_num)

    context = {'post': post, 'comments_list': comments_list, 'form': form}

    return render(request, 'blog/post_detail.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        messages.success(self.request, "Post Created Successfully")
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_message = 'List successfully saved!!!!'

    def form_valid(self, form):
        messages.success(self.request, "Post Updated Successfully")
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required()
def my_blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/myblogs.html', context)


@login_required()
def latest_post(request):
    posts = Post.objects.filter().order_by('-dat_posted')[0:]
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.commentator:
            return True

        return False


