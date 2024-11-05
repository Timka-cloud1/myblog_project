from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostForm

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.published.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'



# @login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            # post.author = request.user  # Устанавливаем автора как текущего пользователя
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})